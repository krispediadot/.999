from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Video
from .forms import VideoForm

import os

# Create your views here.
def index(request):
	return render(request, 'video/index.html')

def showvideo(request):
	lastvideo= Video.objects.last()
	videofile= lastvideo.videofile
	form= VideoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
	context = {'videofile': videofile,
				'form': form
				}
	return render(request, 'video/index.html', context)


def video_list(request):
	video_list = Video.objects.all()
	print(os.getcwd())
	return render(request, 'video/video_list.html', {'video_list': video_list})


def video_new(request):
	form = VideoForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/video')
	elif request.method == 'GET':
		return render(request, 'video/video_new.html', {'form':form})

def video_detail(request, video_id):
	from . import detection_video

	video = Video.objects.get(id=video_id)
	videofile = video.videofile
	form = VideoForm(request.POST or None, request.FILES or None)
	detection_video.learning(videofile)

	context = {'videofile': videofile,
				'form': form,
			   'obj':detection_video.obj_list,
			   'ratio':detection_video.ratio_list,
			   'na':detection_video.na
				}
	print('videofile :', videofile)
	print(detection_video.obj_list)
	print(detection_video.ratio_list)

	return render(request, 'video/video_detail.html', context)




