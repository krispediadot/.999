from django.db import models

# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=10)
	introduction = models.TextField()
	area = models.CharField(max_length=15)
	party_number = models.IntegerField(default=1)


class Post(models.Model):
	title = models.CharField(max_length=100)
	photo = models.ImageField(blank=True)


class Video(models.Model):
	name = models.CharField(max_length=500)
	videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return self.name + ": " + str(self.videofile)

class Ratio(models.Model):
	title = models.CharField(max_length=500)
	timeline = models.CharField(max_length=500)
	ratio = models.CharField(max_length=500)
	total_ratio = models.CharField(max_length=500)

	time_dict = models.CharField(max_length=1500)

	def __str__(self):
		return self.title
