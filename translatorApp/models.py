from django.db import models

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    audio = models.FileField(upload_to='audios/', blank=True,null=True )
    srt_file = models.FileField(upload_to='subtitles/', blank=True, null=True)  # Field for the .srt file path

