from django.db import models

# Create your models here.
class UserInfo(models.Model):
   name=models.CharField(max_length=10)
   one_or_two = 0
   turn=models.IntegerField(default=0)
   
class RoomInfo(models.Model):
   name=models.CharField(max_length=15)
   full = models.IntegerField(default=0)
   user1 = models.CharField(max_length=15,default='none')
   user2 = models.CharField(max_length=15,default='none')
   turn=models.IntegerField(default=0)
   stay=models.IntegerField(default=0)

class ChessBoard(models.Model):
   board=models.TextField()
   room_number=models.IntegerField(default=0)
   turn=models.IntegerField(default=0)

class RoomMaster(models.Model):
   name=models.CharField(max_length=10)