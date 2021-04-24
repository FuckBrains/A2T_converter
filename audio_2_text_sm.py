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

		print("-------------------------------------------")
		print("Your text file is created...\nGo to the folder you specified to access it.")
		print("-------------------------------------------")

	if question_save == 'n':
		continue
	if question_save == 'q':
		break

	question_more = input("Do you wish to convert another file? [y/n]")
	if question_more == 'y':
		print("-------------------------------------------")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
