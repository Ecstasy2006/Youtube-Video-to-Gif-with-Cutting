import os

from moviepy.audio.tools.cuts import find_audio_period
from moviepy.editor import *
from moviepy.video.tools.cuts import find_video_period


os.system("youtube-dl Fn70cJQ3EPY -o Dracula.mkv")  

#importing the video and making the cut from minute 2:44 frame 7 to minute 2:48
clip = (VideoFileClip("./Dracula.mkv", audio=False)
    .subclip((2,44.7),(2,48)))    

#exporting the gif
clip.write_gif('1.gif')
