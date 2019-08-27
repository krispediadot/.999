from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Video, Ratio
from .forms import VideoForm

import os

learning_check = True
# Create your views here.
def index(request):
	return render(request, 'video/index.html')

def showvideo(request):
	lastvideo= Video.objects.last()
	videofile= lastvideo.videofile
	form = VideoForm(request.POST or None, request.FILES or None)
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
	global learning_check

	form = VideoForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			learning_check = False
		return HttpResponseRedirect('/video')
	elif request.method == 'GET':
		return render(request, 'video/video_new.html', {'form':form})

def video_detail(request, video_id):

	from . import detection_video

	video = Video.objects.get(id=video_id)
	videofile = video.videofile
	form = VideoForm(request.POST or None, request.FILES or None)

	print('videofile :', videofile)

	if not learning_check:
		detection_video.learning(videofile)
		ratio_data = Ratio(title = video, timeline = detection_video.obj_sec,
						   ratio = detection_video.count_obj, total_ratio = detection_video.total_obj,
						   time_dict=detection_video.time_dict)
		ratio_data.save()
	elif learning_check:
		pass

	try :
		print(video)
		ratio = Ratio.objects.get(title=str(video))
		print(ratio.timeline, ratio.ratio, ratio.total_ratio)
		context = {'videofile': videofile,
				   'form': form,
				   'ratios': eval(ratio.ratio),
				   'total_obj':eval(ratio.total_ratio),
				   'time_dict':eval(ratio.time_dict),
				   }


	except :
		print("not learned yet")
		context = {'videofile': videofile,
				   'form': form
				   }


	# print('real data :', detection_video.count_obj)

	# count_obj = {'gun': 8.75,
	# 			  'knife': 99.9,
	# 			  'cigarette': 12.3,
	# 			  'boob': 24.5,
	# 			  'alcohol': 22.3}

	# print('test data :', count_obj)

	return render(request, 'video/video_detail.html', context)