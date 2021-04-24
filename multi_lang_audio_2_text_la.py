"""This module contains a general speech-to-text-converter for large audio files"""

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Welcome message and information
print("###########################################################")
print("...........................................................")
print("...........................................................")
print("...........................................................")
print("############## A2T LA by Sven Eschlbeck 2021 ##############")
print("...........................................................")
print("...........................................................")
print("...........................................................")
print("###########################################################")
print("Hello! Welcome to Audio2Text LA.")
print("Enter 'q' to quit any time.")
print("-----------------------------------------------------")


while True:
	# Asking user to specify the path to the audio file
	path = input("Please specify the full path to your audio file.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
	if path == 'q':
		break
	# Asking for the language of the audio file
	lang = input("\nPlease specify the language of the submitted audio file.\nPress '1' for French.\nPress '2' for German.\nPress '3' for Italian.\nPress '4' for Russian.\nLeave blank for default (English).\n")
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

	# Creating a speech recognition object/ Initializing the recognizer
	r = sr.Recognizer()


	# Splitting the audio file into batches and applying speech recognition to the batches
	def get_large_audio_transcription(path):
		"""Splitting audio file into batches and applying speech recognition to each batch"""
		global whole_text # Necessary to access the variable later
		# Opening audio file using pydub
		sound = AudioSegment.from_wav(path)
		# Splitting audio file where silence is 700 ms or longer
		# min_silence_len is the minimum length of a silence used for a split
		# silence_thresh is the threshold in which anything quieter than this will be considered silence
		# keep_silence is the amount of silence to leave at the beginning and the end of each batch detected in ms
		batches = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence=500)

		# Creating directory to store the audio batches
		if not os.path.isdir('audio_batches'):
			os.mkdir('audio_batches')
		whole_text = ""

		# Process each batch
		for i, audio_batch in enumerate(batches, start=1):
			# Export audio batch and save it in 'audio_files/audio_batches'
			batch_filename = os.path.join('audio_batches', f"batch{i}.wav")
			audio_batch.export(batch_filename, format='wav')
			# Recognize the batch
			with sr.AudioFile(batch_filename) as source:
				audio_listened = r.record(source)
				# Trying to convert to text
				try:
					text = r.recognize_google(audio_listened, language = language)
				except sr.UnknownValueError as e:
					print("Error: ", str(e))
				else:
					text = f"{text.capitalize()}. "
					print(batch_filename, ": ", text)
					whole_text += text

		# Return the text for all batches in one piece
		return whole_text

	# Print text
	print("------------------------------------------------------------------")
	print("Transcribing audio batchwise...\nThis may take a moment.")
	print("------------------------------------------------------------------")
	print("Creating directory 'audio_batches' to store audio chunks...")
	print("------------------------------------------------------------------")
	print("---------------------------------\nFull text:\n", get_large_audio_transcription(path))
	print("------------------------------------------------------------------")


	question_save = input("Do you want to save the transcription to a text file? [y/n]")
	if question_save == 'y':
		# Ask for the destination folder where the text should be stored
		destination_folder = input("Please specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
		# Ask for the file name
		file_name = input("Please specify the desired file name.\nYour entry should look like this: 'example_file.txt' but without quotes.\n")

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{whole_text}")

		print("-----------------------------------------------------")
		print("Your text file is created...\nGo to the folder you specified to access it.")
		print("-----------------------------------------------------")

	if question_save == 'n':
		continue
	if question_save == 'q':
		break


	# Asking user if he/she wishes to continue
	question_more = input("Do you wish to convert another file? [y/n]")
	if question_more == 'y':
		print("------------------------------------------------------------------")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
