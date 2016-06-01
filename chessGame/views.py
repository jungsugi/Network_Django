from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserInfo, RoomInfo, ChessBoard

# Create your views here.
def index(request):
	return render(request, 'chessGame/index.html')


def main(request):
	#str=request.POST['title']
	str = request.POST.get('title', False)

	room=RoomInfo.objects.all()
	context={'rooms':room}
	#user=UserInfo(name=request.POST['title'])
	#user.save

	UserInfo.objects.create(name=str)

	return render(request, 'chessGame/main.html', context)
	#return HttpResponse(user.name)

def make(request):

	return render(request, 'chessGame/make.html')
	#return HttpResponse("방만들기")

def ing(request):
	str=request.POST['roomname']

	RoomInfo.objects.create(name=request.POST['roomname'])

	#room=RoomInfo(name=request.POST['roomname'])
	#방이름 같지않게 예외처리 필요
	room=RoomInfo.objects.filter(name=str)
	#room=RoomInfo.objects.get(poll_id=poll.id, candidate_id=selection)

	#room.save
	#return HttpResponse(room.id)
	return HttpResponseRedirect("/room/{}/".format(room[0].id))

def room(request, room_id):
	room=RoomInfo.objects.filter(id=room_id)
	context={'room':room[0]}
	return render(request, 'chessGame/room.html',context)
	#return HttpResponse("방 안")
def chess(request, room_id):
	"""
	a=검은 폰
	b=검은 룩
	c=검은 나이트
	d=검은 비숍
	e=검은 퀸
	f=검은 킹

	g=하얀 폰
	h=하얀 룩
	i=하얀 나이트
	j=하얀 비숍
	k=하얀 퀸
	l=하얀 킹

	x=빈칸
	"""
	board=[['b','c','d','e','f','d','c','b'],
			['a','a','a','a','a','a','a','a'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['g','g','g','g','g','g','g','g'],
			['h','i','j','k','l','j','i','h']]

	chess=ChessBoard.objects.filter(room_number=room_id)
	str=request.POST.get('move', False)
	if(chess and str):
		str=request.POST.get('move', False)

		ptr=chess[0].board

		a=0
		a=int(a)
		for i in range(0,8):
			for u in range(0,8):
				k=ptr[a]
				q=board[i][u]
				board[i][u]=k
				a+=1
		""""		

		board=[['b','c','d','e','f','d','c','b'],
				['a','a','a','a','a','a','a','a'],
				['x','x','x','x','x','x','x','x'],
				['x','x','x','x','x','x','x','x'],
				['x','x','x','x','x','x','x','x'],
				['x','x','x','x','x','x','x','x'],
				['g','g','g','g','g','g','g','g'],
				['h','i','j','k','l','j','i','h']]
		"""		
		board[int(str[2])][int(str[3])]=board[int(str[0])][int(str[1])]
		board[int(str[0])][int(str[1])]='x'

		b=""
		for i in board:
			for j in i:
				b=b+j

		chess[0].board=b
		chess[0].save()

		context={'board':board,'str':str}
		#return HttpResponse(ptr)	
		return render(request, 'chessGame/chess.html',context)
	else:
		board=[['b','c','d','e','f','d','c','b'],
				['a','a','a','a','a','a','a','a'],
				['x','x','x','x','x','x','x','x'],
				['x','x','x','x','x','x','x','x'],
				['x','x','x','x','x','x','x','x'],
				['x','x','x','x','x','x','x','x'],
				['g','g','g','g','g','g','g','g'],
				['h','i','j','k','l','j','i','h']]

		b=""
		for i in board:
			for j in i:
				b=b+j

		ChessBoard.objects.create(board=b, room_number=room_id)
		context={'board':board}
		#return HttpResponse(b)
		return render(request, 'chessGame/chess.html',context)
