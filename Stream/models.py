from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)