"""This module contains a general speech-to-text-converter for small to medium sized audio files"""

import speech_recognition as sr

# Welcome message and information
print("########################################################")
print("############## A2T by Sven Eschlbeck 2021 ##############")
print("########################################################")
print("Hello! Welcome to A2T.")
print("Enter 'q' to quit any time.")


while True:
	# Asking user to specify the pyth to the audio file
	path = input("Please specify the full path to your audio file.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
	if path == 'q':
		break

	# Initializing the recognizer
	r = sr.Recognizer()

	# Open the audio file
	with sr.AudioFile(path) as source:
		# Listen for the data (loading audio into memory)
		audio_data = r.record(source)
		# Recognize speech and convert to text
		# Command uploads file to Google Cloud, using their A.I. to convert it and returns the text transcription
		text = r.recognize_google(audio_data)
		# Print text
		print("-------------------------------------------")
		print(f"Output:\n{text}")
		print("-------------------------------------------")

	question = input("Do you wish to convert another file? [y/n]")
	if question == 'y':
		print("-------------------------------------------")
		continue
	if question == 'n':
		break
	if question == 'q':
		break
