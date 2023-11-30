from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'audio', 'srt_file')

admin.site.register(Video, VideoAdmin)