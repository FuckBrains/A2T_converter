"""This module contains a general speech-to-text-converter for large audio files"""

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

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

	# Creating a speech recognition object/ Initializing the recognizer
	r = sr.Recognizer()


	# Splitting the audio file into batches and applying speech recognition to the batches
	def get_large_audio_transcription(path):
		"""Splitting audio file into batches and applying speech recognition to each batch"""
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
					text = r.recognize_google(audio_listened)
				except sr.UnknownValueError as e:
					print("Error: ", str(e))
				else:
					text = f"{text.capitalize()}. "
					print(batch_filename, ": ", text)
					whole_text += text

		# Return the text for all batches in one piece
		return whole_text

	# Print text
	print("--------------------------------------------------------")
	print("Transcribing audio batchwise...\nThis may take a moment.")
	print("--------------------------------------------------------")
	print("Creating directory 'audio_batches' to store audio chunks...")
	print("--------------------------------------------------------")
	print("---------------------------------\nFull text:\n", get_large_audio_transcription(path))
	print("--------------------------------------------------------")

	# Asking user if he/she wishes to continue
	question = input("Do you wish to convert another file? [y/n]")
	if question == 'y':
		print("--------------------------------------------------------")
		continue
	if question == 'n':
		break
	if question == 'q':
		break
