from celery import shared_task
from .services import extract_audio_from_video
from .models import Video
from .services import transcribe_to_srt
import logging
import os
from django.conf import settings

logger = logging.getLogger(__name__)

@shared_task
def extract_audio_task(video_id):
    try:
        video_instance = Video.objects.get(id=video_id)
        audio_file_path = extract_audio_from_video(video_instance.video.path)
        logger.info(f'Audio file path: {audio_file_path}')  # Log the path for debugging
        video_instance.audio.name = audio_file_path
        video_instance.save(update_fields=['audio'])
    except Video.DoesNotExist:
        logger.error(f'Video with id {video_id} does not exist')
    except Exception as e:
        logger.error(f'Unexpected error: {e}')




@shared_task
def transcribe_video_to_srt_task(video_id):
    try:
        video_instance = Video.objects.get(id=video_id)
        audio_file_path = os.path.join(settings.MEDIA_ROOT, extract_audio_from_video(video_instance.video.path))

        # Call the transcribe function from services
        transcription_text = transcribe_to_srt(audio_file_path)

        #logger.info(f"Texte traduit: {transcription_text}") This was just to test
        # Save transcription text to the database
        #video_instance.transcription_text = transcription_text
        #video_instance.save()

        # Save transcription as an SRT file
        srt_filename = f"{video_instance.pk}.srt"
        srt_file_path = os.path.join(settings.MEDIA_ROOT, 'subtitles', srt_filename)
        os.makedirs(os.path.dirname(srt_file_path), exist_ok=True)
        with open(srt_file_path, 'w') as srt_file:
            srt_file.write(transcription_text)

        # Update the srt_file field in the Video model
        video_instance.srt_file.name = os.path.join('subtitles', srt_filename)
        video_instance.save(update_fields=['srt_file'])

        logger.info(f"Transcription completed for video ID: {video_id}")

    except Video.DoesNotExist:
        logger.error(f"Video with id {video_id} does not exist")
    except Exception as e:
        logger.error(f"Unexpected error in transcribe_video_to_srt_task: {e}")
