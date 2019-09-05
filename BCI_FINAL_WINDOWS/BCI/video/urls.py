from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'video'

urlpatterns = [
	# url(r'^', views.showvideo),
	url(r'^$', views.video_list, name='list'),
	url(r'^new$', views.video_new, name='new'),
    # url(r'', views.video_new, name='new'),
	url(r'(?P<video_id>\d+)/$', views.video_detail, name='detail'),
	# url(r'^popup$', views.popup),
]
