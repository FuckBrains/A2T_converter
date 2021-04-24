"""This module contains a microphone audio to text converter"""

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Welcome message and information
print("###########################################################")
print("...........................................................")
print("...........................................................")
print("...........................................................")
print("############## Mic2T by Sven Eschlbeck 2021 ###############")
print("...........................................................")
print("...........................................................")
print("...........................................................")
print("###########################################################")
print("Hello! Welcome to Microphone2Text.")
print("Enter 'q' to quit any time.")
print("-----------------------------------------------------")


while True:
	# Asking for the language of the given speech
	lang = input("Please specify your language.\nPress '1' for French.\nPress '2' for German.\nPress '3' for Italian.\nPress '4' for Russian.\nLeave blank for default (English).\n")
	if lang == '1':
		language = 'fr-Fr'
	if lang == '2':
		language = 'de-De'
	if lang == '3':
		language = 'it-It'
	if lang == '4':
		language == 'ru-Ru'
	if lang == '':
		language = 'en-Us'
	if lang == 'q':
		break

	# Asking for the duration of the planned recording
	length = input("\nHow long do you plan to speak?\nDefine a time span, press '1' for 30 seconds.\nPress '2' for 60 seconds.\nPress '3' for 90 seconds.\nPress '4' for 120 seconds.\nPress '5' for 300 seconds.\nLeave blank for default (10 seconds).\n")
	if length == '1':
		duration = 30
	if length == '2':
		duration = 60
	if length == '3':
		duration = 90
	if length == '4':
		duration = 120
	if length == '5':
		duration = 300
	if length == '':
		duration = 10
	if length == 'q':
		break


	# Initializing the recognizer
	r = sr.Recognizer()

	# Defining microphone as input source
	with sr.Microphone() as source:
		# Users starts speaking
		print("\nSpeak now!")
		print("-----------------------------------------------------")
		# Read the audio data from the default microphone
		audio_data = r.record(source, duration = duration)
		# Printing wait statement
		print("Recognizing voice...")
		# Convert speech to text
		text = r.recognize_google(audio_data, language = language)
		# Print text
		print("-----------------------------------------------------")
		print(f"Record:\n{text}")
		print("-----------------------------------------------------")

	question_save = input("Do you want to save the transcription to a text file? [y/n]")
	if question_save == 'y':
		# Ask for the destination folder where the text should be stored
		destination_folder = input("Please specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
		# Ask for the file name
		file_name = input("Please specify the desired file name.\n")

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{text}")

		print("-----------------------------------------------------")
		print("Your text file is created...\nGo to the folder you specified to access it.")
		print("-----------------------------------------------------")

	if question_save == 'n':
		pass
	if question_save == 'q':
		break

	question_more = input("Do you wish to record another speech? [y/n]")
	if question_more == 'y':
		print("-----------------------------------------------------")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
