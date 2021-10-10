import os
import moviepy.editor as mp
from .models import Video

def toaudio():
    ultimovideo = Video.objects.last()
    nomevideo = ultimovideo.file.name
    video = os.path.abspath('media/' + nomevideo)
    clip = mp.VideoFileClip(video)
    clip.audio.write_audiofile("audiotodownload.mp3")


