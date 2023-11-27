from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')

