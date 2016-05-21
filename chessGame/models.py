from django.db import models

# Create your models here.
class UserInfo(models.Model):
	name=models.CharField(max_length=10)

class RoomInfo(models.Model):
	name=models.CharField(max_length=15)