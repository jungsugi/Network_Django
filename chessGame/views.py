from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserInfo, RoomInfo

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

	#return HttpResponse("게임중ㅎㅎ")
	return render(request, 'chessGame/chess.html')
