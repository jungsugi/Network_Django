from django.contrib import admin
from .models import UserInfo, RoomInfo, ChessBoard
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(RoomInfo)
admin.site.register(ChessBoard)