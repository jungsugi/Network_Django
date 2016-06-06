from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
ready=0;
user1=""
# Create your views here.
def index(request):
   return render(request, 'chessGame/index.html')


def index_ing(request):
	str = request.POST.get('title', False)
	UserInfo.objects.create(name=str)

	user = UserInfo.objects.get(name=str)
	request.session['user_id']=request.POST['title']
	user.one_or_two = 2
	user.save()
	#return HttpResponseRedirect("/main")
	return HttpResponseRedirect("/main/{}/".format(user.id))

def main(request,myname):
   room = RoomInfo.objects.all()

   me=UserInfo.objects.get(id=myname)  
   context={'rooms':room, 'me':me }

   return render(request, 'chessGame/main.html', context)
   #return HttpResponse(k.name)

def make(request,myname):

	me=UserInfo.objects.get(id=myname)
	context={'me':me}
	return render(request, 'chessGame/make.html', context)
   #return HttpResponse("방만들기")

def make_ing(request, myname):

   user = UserInfo.objects.get(name=request.session['user_id'])
   user.one_or_two = 1

   str = request.POST.get('roomname', False)
   RoomInfo.objects.create(name=str)
   room = RoomInfo.objects.get(name=str)
   room.user1 = user.name
   room.save()

   context = {'roominform' : room , 'room_no' : room.id }
   
   #return render (request, 'chessGame/room.html' , context)
   return HttpResponseRedirect("/room/{}/{}".format(room.id, myname))
   
def room(request, room_id,myname):

	#user = UserInfo.objects.get(name=request.session['user_id'])
	me=UserInfo.objects.get(id=myname)
	room = RoomInfo.objects.get(id=int(room_id))
	if(room.full == 0):
		room.user1=me.name
		room.full = 1
		room.save()
		context={'room': room,'me':me}
		return render(request, 'chessGame/room.html',context)
	elif(room.full == 1 and room.user1!=me.name):
		room.user2 = me.name
		room.full = 2 
		room.save()
		context={'room' : room, 'me':me }
		return render(request, 'chessGame/room.html',context)
	elif(room.user1!=me.name and room.user2!=me.name and room.full==2):
		
		return HttpResponseRedirect("/main/{}/".format(myname))
	else:
		
		context={'room' : room,'me':me }
		return render(request, 'chessGame/room.html',context)

def room_to_chess(requset, room_id, myname):
	me=UserInfo.objects.get(id=myname)
	room=RoomInfo.objects.get(id=room_id)

	if room.user1=='none' or room.user2=='none':
		return HttpResponseRedirect("/room/{}/{}".format(room.id, myname))

	global ok_1
	global ok_2
	ok_1=0
	ok_2=0
	while 1:
		if room.user1==me.name:
			ok_1=1
			#return HttpResponse("ok_1")
		if room.user2==me.name:
			ok_2=1
			#return HttpResponse("ok_2")
		if ok_1 == 1 and ok_2 == 1:
			#return HttpResponse("ok_go!!")
			return HttpResponseRedirect("/room/{}/chess/{}".format(room.id, myname))
		

	#return HttpResponse("방 안")
def chess(request, room_id, myname):
	global ready
	
	me = UserInfo.objects.get(id=myname)
	room = RoomInfo.objects.get(id=int(room_id))

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

	if(chess):
		#str=request.POST.get('move', False)
		ptr=chess[0].board
		a=0
		a=int(a)
		for i in range(0,8):
			for u in range(0,8):
				board[i][u]=ptr[a]
				a+=1

		context={'board':board,'str':str,'room':room,'me':me}
		#return HttpResponse(ptr)	
		return render(request, 'chessGame/chess.html',context)

	else:
		b=""
		for i in board:
			for j in i:
				b=b+j
		ChessBoard.objects.create(board=b, room_number=room_id)
		context={'board':board,'room':room,'me':me}
		#return HttpResponse(b)
		return render(request, 'chessGame/chess.html',context)

def chess_ing(request, room_id, myname):
	me = UserInfo.objects.get(id=myname)
	str=request.POST.get('move', False)
	#str예외처리 필요

	board=[['b','c','d','e','f','d','c','b'],
			['a','a','a','a','a','a','a','a'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['g','g','g','g','g','g','g','g'],
			['h','i','j','k','l','j','i','h']]

	Chess=ChessBoard.objects.filter(room_number=room_id)
	chess=Chess[0]
	ptr=chess.board

	a=0
	#a=int(a)
	for i in range(0,8):
		for u in range(0,8):
			board[i][u]=ptr[a]
			a+=1

	piece=board[int(str[0])][int(str[1])]
	#piece와 str을 인자로 받아 piece의 str동작이 올바른 동작인지 판별하는 함수 필요
	#동작이 적절하면 아래 실행
		
	board[int(str[2])][int(str[3])]=board[int(str[0])][int(str[1])]
	board[int(str[0])][int(str[1])]='x'

	b=""
	for i in board:
		for j in i:
			b=b+j

	chess.board=b
	chess.save()

	#context={'board':board,'str':str}
	#return HttpResponse(chess.board)	
	#return render(request, 'chessGame/chess.html',context)
	return HttpResponseRedirect("/room/{}/chess/{}".format(room_id, me.id))
