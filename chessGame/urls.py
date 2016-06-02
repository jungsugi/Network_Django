from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main/$', views.main),
    url(r'^room/(?P<room_id>\d+)/$', views.room),
    url(r'^make/$', views.make),
    url(r'^make/ing/$', views.ing),
    url(r'^room/(?P<room_id>\d+)/chess/$', views.chess),
    url(r'^room/(?P<room_id>\d+)/chess/ing/$', views.chess_ing),
 ]