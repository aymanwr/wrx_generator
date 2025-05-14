from collections import deque
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pathlib import Path
from .forms import UploadForm, YoutubeForm
from tafrigh import Config, TranscriptType, Writer, farrigh
from tafrigh.recognizers.wit_recognizer import WitRecognizer
import subprocess

def is_wav_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read(4) == b'RIFF'
    except IOError:
        return False

def download_youtube_audio(youtube_url):
    output_path = Path(settings.MEDIA_ROOT) / 'downloads' / '%(id)s.%(ext)s'
    command = ['yt-dlp', '-x', '--audio-format', 'wav', '-o', str(output_path), youtube_url]
    subprocess.run(command, check=True)
    audio_file = next(Path(settings.MEDIA_ROOT).glob('downloads/*.wav'))
    return audio_file

def convert_video_to_audio(video_path):
    audio_output_path = video_path.with_suffix('.wav')
    command = ['ffmpeg', '-i', str(video_path), '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', str(audio_output_path)]
    subprocess.run(command, check=True)
    return audio_output_path

def convert_mp3_to_wav(mp3_path):
    wav_output_path = mp3_path.with_suffix('.wav')
    command = ['ffmpeg', '-i', str(mp3_path), str(wav_output_path)]
    subprocess.run(command, check=True)
    return wav_output_path

def transcribe_file(file_path, language_sign):
    if not is_wav_file(file_path):
        return "Error: File is not in WAV format."

    wit_api_key = settings.LANGUAGE_API_KEYS.get(language_sign.upper())
    if not wit_api_key:
        return f"API key not found for language: {language_sign}"

    config = Config(
        urls_or_paths=[str(file_path)],
        skip_if_output_exist=False,
        playlist_items="",
        verbose=False,
        model_name_or_path="",
        task="",
        language="",
        use_faster_whisper=False,
        beam_size=0,
        ct2_compute_type="",
        wit_client_access_tokens=[wit_api_key],
        max_cutting_duration=5,
        min_words_per_segment=1,
        save_files_before_compact=False,
        save_yt_dlp_responses=False,
        output_sample=0,
        output_formats=[TranscriptType.TXT, TranscriptType.SRT],
        output_dir=str(file_path.parent),
    )

    progress = deque(farrigh(config), maxlen=0)
    return "Transcription completed. Check the output directory for the generated files."

def index(request):
    if request.method == 'POST':
        if 'youtube_url' in request.POST:
            form = YoutubeForm(request.POST)
            if form.is_valid():
                youtube_url = form.cleaned_data['youtube_url']
                language_sign = form.cleaned_data['language_sign']
                audio_file = download_youtube_audio(youtube_url)
                message = transcribe_file(audio_file, language_sign)
                return HttpResponse(message)
        else:
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']
                language_sign = form.cleaned_data['language_sign']
                file_path = Path(settings.MEDIA_ROOT) / file.name

                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                if file_path.suffix.lower() == '.mp3':
                    file_path = convert_mp3_to_wav(file_path)
                elif file_path.suffix.lower() in ['.mp4', '.mkv', '.avi']:
                    file_path = convert_video_to_audio(file_path)

                message = transcribe_file(file_path, language_sign)
                return HttpResponse(message)

    else:
        upload_form = UploadForm()
        youtube_form = YoutubeForm()

    return render(request, 'index.html', {'upload_form': upload_form, 'youtube_form': youtube_form})
