from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from chessGame.model.rule import *

# Create your views here.
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def index(request):
   return render(request, 'chessGame/index.html')

def log_out(request,myname):

	me=me=UserInfo.objects.get(id=myname)
	me.delete()

	return HttpResponseRedirect("/")

def out(request, room_id, myname):
	me=UserInfo.objects.get(id=myname)
	room=RoomInfo.objects.get(id=int(room_id))

	if room.turn==0:
		if room.user2 =='none':
			room.user1 = 'none'
			room.full = 5
			room.save()
			context ={"me":me, "room":room}

			return render(request, 'chessGame/out.html',context)
				#return render(request, 'chessGame/room.html',context)

		elif room.user2 != 'none':
			if(me.name == room.user1):
				room.user1 = room.user2
				room.user2='none'
				room.full = 1
				room.save()
				
				context ={"me":me, "room":room}
				return render(request, 'chessGame/out.html',context)	
					#return render(request, 'chessGame/room.html',context)

			elif(me.name == room.user2):
				room.user2 = 'none'
				room.full = 1
				room.save()
					# context ={"me":me, "room":room}
					# return render(request, 'chessGame/out.html',context)
					#return render(request, 'chessGame/room.html',context)
				context ={"me":me, "room":room}
				return render(request, 'chessGame/out.html',context)

	elif room.turn==1:
		#room.turn==0 게임 시작안함
		#room.turn==1 게임 사작
		#room.turn==2 user1 이 이김
		#room.turn==3 user2 이 이김

		if me.name==room.user1:#user1이 기권했을 경우
			room.turn=3
			room.stay=1
			room.save()
			return HttpResponseRedirect("/room/{}/chess/{}".format(room_id, myname))

		if me.name==room.user2:#user2이 기권했을 경우
			room.turn=2
			room.stay=1
			room.save()
			return HttpResponseRedirect("/room/{}/chess/{}".format(room_id, myname))


def index_ing(request):
	str = request.POST.get('title', False)
	num2ptr=str.rstrip()
	num1ptr=str.strip()
	num3ptr=str.lstrip()
	ptr=UserInfo.objects.filter(name=str)
	if(str==""):
		cout="이름에 공백이 있으면 안됩니다"
		context={'cout':cout, 'a':0}
		return render(request,'chessGame/errorname.html',context)
	elif (num1ptr != num2ptr or num1ptr !=num3ptr):
		cout="이름에 공백이 있으면 안됩니다"
		context={'cout':cout, 'a':0}
		return render(request,'chessGame/errorname.html',context)
	elif(ptr):
		cout='이미 있는 이름입니다'
		context={'cout':cout, 'a':0}
		return render(request,'chessGame/errorname.html',context)
	else:
		UserInfo.objects.create(name=str)
		user = UserInfo.objects.get(name=str)
		#request.session['user_id']=request.POST['title']
		#ser.one_or_two = 2
		#user.save()
		return HttpResponseRedirect("/main/{}/".format(user.id))

   
def main(request,myname):
	room = RoomInfo.objects.filter(full=1 or 0)
	me=UserInfo.objects.get(id=myname)
	context={'rooms':room, 'me':me }

	d_room=RoomInfo.objects.filter(turn=2)
	if d_room:
		for i in d_room:
			i.delete()

	d_room=RoomInfo.objects.filter(turn=3)
	if d_room:
		for i in d_room:
			i.delete()

	d_room=RoomInfo.objects.filter(full=5)
	if d_room:
		for i in d_room:
			i.delete()


	return render(request, 'chessGame/main.html', context)

def make(request,myname):

	me=UserInfo.objects.get(id=myname)
	context={'me':me}
	return render(request, 'chessGame/make.html', context)

def make_ing(request, myname):

   #user = UserInfo.objects.get(name=request.session['user_id'])
   #user.one_or_two = 1
	str = request.POST.get('roomname', False)
	me=UserInfo.objects.get(id=myname)

	room_all=RoomInfo.objects.all()
	for i in room_all:
		if i.name==str:
			cout='이미 있는 방 제목 입니다.'
			context={'cout':cout,'a':1,'me':me }
			return render(request,'chessGame/errorname.html',context)

	RoomInfo.objects.create(name=str)
	room = RoomInfo.objects.get(name=str)
	room.mypiece=0
	room.user1 = me.name
	room.save()
	context = {'roominform' : room , 'room_no' : room.id }

	return HttpResponseRedirect("/room/{}/{}".format(room.id, myname))
   
def room(request, room_id,myname):

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
			
		if room.user2==me.name:
			ok_2=1
			
		if ok_1 == 1 and ok_2 == 1:

			return HttpResponseRedirect("/room/{}/chess/{}".format(room.id, myname))
		
def chess_stay(request, room_id, myname):
	me=UserInfo.objects.get(id=myname)
	room=RoomInfo.objects.get(id=room_id)
	room.stay=0
	room.save()
	while 1:
		room=RoomInfo.objects.get(id=room_id)
		#if room.turn==2 or 3:
			#return HttpResponseRedirect("/room/{}/chess/{}".format(room_id, myname))
		if room.stay==1:
			room.stay=0
			room.save()
			me.turn=2
			me.save()
			return HttpResponseRedirect("/room/{}/chess/{}".format(room_id, myname))

def chess(request, room_id, myname):
	global ready
	me = UserInfo.objects.get(id=myname)
	room = RoomInfo.objects.get(id=int(room_id))
	if room.turn==0:
		room.turn=1
		room.save()

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

	if not chess:

		b=""
		for i in board:
			for j in i:
				b=b+j
		ChessBoard.objects.create(board=b, room_number=room_id)
		chess=ChessBoard.objects.filter(room_number=room_id)

	ptr=chess[0].board
	a=0
	a=int(a)
	for i in range(0,8):
		for u in range(0,8):
			board[i][u]=ptr[a]
			a+=1

	context={'board':board,'room':room,'me':me}

	if room.turn==2:#user1이 이김
		if me.name==room.user1:
			return render(request, 'chessGame/chess_win.html',context)
		elif me.name==room.user2:
			return render(request, 'chessGame/chess_lose.html',context)
	if room.turn==3:#user2이 이김
		if me.name==room.user2:
			return render(request, 'chessGame/chess_win.html',context)
		elif me.name==room.user1:
			return render(request, 'chessGame/chess_lose.html',context)

	if me.turn==1:
		#room.stay=1
		#room.save()

		#me.turn=0
		#me.save()
		#stay=1
		return render(request, 'chessGame/chess_stay.html',context)

	elif me.turn==2:
		#me.turn=0
		#me.save()
		
		return render(request, 'chessGame/chess.html',context)

	elif room.turn==1:
		if me.name==room.user1:
			return render(request, 'chessGame/chess.html',context)
		elif me.name==room.user2:
			return render(request, 'chessGame/chess_stay.html',context)

def chess_ing(request, room_id, myname):
	room = RoomInfo.objects.get(id=room_id)
	me = UserInfo.objects.get(id=myname)
	str=request.POST.get('move', False)

	board=[['b','c','d','e','f','d','c','b'],
			['a','a','a','a','a','a','a','a'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['x','x','x','x','x','x','x','x'],
			['g','g','g','g','g','g','g','g'],
			['h','i','j','k','l','j','i','h']]


	for i in range(4):
		if(len(str) !=4):
			chess=ChessBoard.objects.filter(room_number=room_id)
			cout='자릿수가 틀림'
			room = RoomInfo.objects.get(id=int(room_id))
			if(chess):
				ptr=chess[0].board
				a=0
				a=int(a)
				for i in range(0,8):
					for u in range(0,8):
						board[i][u]=ptr[a]
						a+=1
				context={'board':board,'room':room,'me':me,'cout':cout}
				return render(request, 'chessGame/chess.html',context)
		elif(isNumber(str[i])==False):
			chess=ChessBoard.objects.filter(room_number=room_id)
			cout='입력 범위를 넘어갔습니다.'
			room = RoomInfo.objects.get(id=int(room_id))
			if(chess):
				ptr=chess[0].board
				a=0
				a=int(a)
				for i in range(0,8):
					for u in range(0,8):
						board[i][u]=ptr[a]
						a+=1
				context={'board':board,'room':room,'me':me,'cout':cout}
				return render(request, 'chessGame/chess.html',context)
		elif(int(str[i])<=7 and int(str[i])>=0 and isNumber(str[i])==True):
			cout='문제없음'
		
		else:
			chess=ChessBoard.objects.filter(room_number=room_id)
			cout='입력 범위를 넘어갔습니다.'
			room = RoomInfo.objects.get(id=int(room_id))
			if(chess):
				ptr=chess[0].board
				a=0
				a=int(a)
				for i in range(0,8):
					for u in range(0,8):
						board[i][u]=ptr[a]
						a+=1
				context={'board':board,'room':room,'me':me,'cout':cout}
				return render(request, 'chessGame/chess.html',context)


	temp_board=board
	room.mypiece +=1
	my=temp_board[int(str[0])][int(str[1])]
	if(room.mypiece==1):
		if(my=='g'or my=='h'or my=='i'or my=='j' or my=='k' or my=='l'):
			cout='good'
		else:
			room.mypiece=0
			chess=ChessBoard.objects.filter(room_number=room_id)
			cout='나의 말이 아닙니다.'
			room = RoomInfo.objects.get(id=int(room_id))
			if(chess):
				ptr=chess[0].board
				a=0
				a=int(a)
				for i in range(0,8):
					for u in range(0,8):
						board[i][u]=ptr[a]
						a+=1
				context={'board':board,'room':room,'me':me,'cout':cout}
				return render(request, 'chessGame/chess.html',context)
	elif(room.mypiece==2):
		if(my=='a' or my=='b' or my=='c' or my=='d'or my=='e' or my =='f'):
			room.mypiece=0
			cout='good'
		else:
			room.mypiece=1
			chess=ChessBoard.objects.filter(room_number=room_id)
			cout='나의 말이 아닙니다.'
			room = RoomInfo.objects.get(id=int(room_id))
			if(chess):
				ptr=chess[0].board
				a=0
				a=int(a)
				for i in range(0,8):
					for u in range(0,8):
						board[i][u]=ptr[a]
						a+=1
				context={'board':board,'room':room,'me':me,'cout':cout}
				return render(request, 'chessGame/chess.html',context)


	temp=ChessBoard.objects.filter(room_number=room_id)
	#temp_board=board
	ptr=temp[0].board
	a=0
	a=int(a)
	for i in range(0,8):
		for u in range(0,8):
			temp_board[i][u]=ptr[a]
			a+=1
	if(Rule(temp_board,str)==False):
		chess=ChessBoard.objects.filter(room_number=room_id)
		cout='둘 수 없는 곳 입니다. 다시 두세요'
		room = RoomInfo.objects.get(id=int(room_id))
		ptr=chess[0].board
		a=0
		a=int(a)
		for i in range(0,8):
			for u in range(0,8):
				board[i][u]=ptr[a]
				a+=1
				context={'board':board,'room':room,'me':me,'cout':cout}
				return render(request, 'chessGame/chess.html',context)


	Chess=ChessBoard.objects.filter(room_number=room_id)
	chess=Chess[0]
	ptr=chess.board

	a=0
	for i in range(0,8):
		for u in range(0,8):
			board[i][u]=ptr[a]
			a+=1

	piece=board[int(str[0])][int(str[1])]
	
	board[int(str[2])][int(str[3])]=board[int(str[0])][int(str[1])]
	board[int(str[0])][int(str[1])]='x'

	b=""
	for i in board:
		for j in i:
			b=b+j

	chess.board=b
	chess.save()

	me.turn=1
	me.save()

	room.stay=1
	room.save()

	a=0
	for i in range(0,1000000):
		a+=1

	return HttpResponseRedirect("/room/{}/chess/{}".format(room_id, me.id))

def win(request,room_id,myname):

	room=RoomInfo.objects.get(id=room_id)
	me=UserInfo.objects.get(id=myname)

	me.turn=0
	me.save()

	chess=ChessBoard.objects.filter(room_number=room.id)
	if chess:
		for i in chess:
			chess.delete()

	context={'room':room, 'me':me}
	return render(request, 'chessGame/win.html',context)

def lose(request,room_id,myname):

	room=RoomInfo.objects.get(id=room_id)
	me=UserInfo.objects.get(id=myname)

	me.turn=0
	me.save()

	#hess=ChessBoard.objects.filter(room_number=room.id)
	#if chess:
	#	for i in chess:
			#chess.delete()

	context={'room':room, 'me':me}
	return render(request, 'chessGame/lose.html',context)

def game(request, room_id, myname):
	me = UserInfo.objects.get(id=myname)
	room = RoomInfo.objects.get(id=int(room_id))

	context={"me":me,"room":room}

	return render(request,'chessGame/game.html',context)
