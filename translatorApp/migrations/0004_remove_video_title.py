# Generated by Django 4.2.7 on 2023-11-28 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translatorApp', '0003_video_srt_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]
