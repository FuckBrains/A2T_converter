"""This module contains a speech-to-text-converter for small to medium sized audio files"""

import speech_recognition as sr

# Specifying the audio file that the text will be transcribed from
filename = 'C:/Users/sven-/src/A2T_converter/audio_files/example.wav'

# Initializing the recognizer
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile(filename) as source:
	# Listen for the data (loading audio into memory)
	audio_data = r.record(source)
	# Recognize speech and convert to text
	# Command uploads file to Google Cloud, using their A.I. to convert it and returns the text transcription
	text = r.recognize_google(audio_data)
	# Print text
	print(text)