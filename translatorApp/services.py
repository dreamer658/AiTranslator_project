from moviepy.editor import VideoFileClip
import whisper
from whisper.utils import get_writer
from django.conf import settings
import os
import logging

logger = logging.getLogger(__name__)

def extract_audio_from_video(video_path):
    try:
        # Ensure the 'audios' directory exists within 'media'
        audios_dir = os.path.join(settings.MEDIA_ROOT, 'audios')
        if not os.path.exists(audios_dir):
            os.makedirs(audios_dir)
        
        # Create the audio filename and path
        audio_filename = os.path.basename(video_path).rsplit('.', 1)[0] + '.mp3'
        audio_path = os.path.join(audios_dir, audio_filename)

        # Extract audio using MoviePy
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()

        # Log the success and path of the audio file
        logger.info(f'Audio extracted successfully. Audio path: {audio_path}')

        # Return the relative path for use in the Django model
        relative_audio_path = os.path.relpath(audio_path, settings.MEDIA_ROOT)
        return relative_audio_path

    except Exception as e:
        # Log any error during the process
        logger.error(f'Error extracting audio: {e}')
        raise e

def transcribe_to_srt(audio_file_path):
    try:
        # Load Whisper model
        model = whisper.load_model("base")

        # Transcribe the audio
        result = model.transcribe(audio_file_path)
        
        # Return the transcription text
        return result["text"]
        
    except Exception as e:
        logger.error(f"Error in transcribing audio: {e}")
        raise
