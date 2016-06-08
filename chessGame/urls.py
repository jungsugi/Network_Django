from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ing/$', views.index_ing),

    url(r'^main/(?P<myname>\d+)/$', views.main),
    url(r'^room/(?P<room_id>\d+)/(?P<myname>\d+)/$', views.room),
    url(r'^room/(?P<room_id>\d+)/(?P<myname>\d+)/out/$',views.out),
    url(r'^make/(?P<myname>\d+)/$', views.make),
    url(r'^log_out/(?P<myname>\d+)/$', views.log_out),
    url(r'^make/ing/(?P<myname>\d+)/$', views.make_ing),
    url(r'^room/(?P<room_id>\d+)/chess/(?P<myname>\d+)/$', views.chess),
    url(r'^room/(?P<room_id>\d+)/room_to_chess/(?P<myname>\d+)/$', views.room_to_chess),
    url(r'^room/(?P<room_id>\d+)/chess/ing/(?P<myname>\d+)/$', views.chess_ing),
    url(r'^room/(?P<room_id>\d+)/chess/stay/(?P<myname>\d+)/$', views.chess_stay),
    url(r'^room/(?P<room_id>\d+)/chess/win/(?P<myname>\d+)/$', views.win),
    url(r'^room/(?P<room_id>\d+)/chess/lose/(?P<myname>\d+)/$', views.lose),
    url(r'^room/(?P<room_id>\d+)/chess/(?P<myname>\d+)/game/$', views.game),

 ]