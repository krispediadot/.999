from django import forms

from .models import Post
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]
        