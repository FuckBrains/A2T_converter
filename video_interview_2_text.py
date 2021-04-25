"""This module contains a video interview specific speech-to-text-converter for large video files"""

import wave
import math
import contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip


banner = r'''

  __ 	   __    _______   __________
  \ \	  / /   |_____  | |___2021___|   
   \ \	 / /	 _____| |     |  |
    \ \_/ /	    |  _____|     |  |
     \	 /	    |  |____      |  |
      \_/ideo   |_______|     |__|ext

     [A Sven Eschlbeck Production]

- - - - - - - - - - - - - - - - - - - - - - 
- - - - - - - - - - - - - - - - - - - - - -

Hello! Welcome to VIDEO2TEXT.
Enter 'q' to quit any time.

- - - - - - - - - - - - - - - - - - - - - - 
- - - - - - - - - - - - - - - - - - - - - -

'''

print(banner)


# Specifying video and audio file
transcribed_audio_file_name = 'transcribed_speech.wav'
zoom_video_file_name = 'zoom_0.mp4'