from django.db import models

# Create your models here.
class UserInfo(models.Model):
	name=models.CharField(max_length=10)

class RoomInfo(models.Model):
	name=models.CharField(max_length=15)

class ChessBoard(models.Model):
	board=models.TextField()
	room_number=models.IntegerField(default=0)


