"""This module contains a YouTube specific videospeech-to-text-converter for large audio and video files"""

import speech_recognition as sr
import moviepy.editor as mp
import os
from pytube import YouTube
from pydub import AudioSegment
from pydub.silence import split_on_silence


banner = r'''



		__   __  _______
		\ \_/ / |__   __|
		 \   /     | |
		  |_|      |_|
		                     #####
		                        ##
		                     #####
		                     ##
		                     #####
		                      	       _______
		                     	      |__   __|
		                                 | |
		                                 |_|	
         [Sven Eschlbeck] [2021]


##############################################################################
##############################################################################

Hello! Welcome to 'YouTube2Audio'.

Enter 'q' to quit any time.

##############################################################################
##############################################################################
'''

print(banner)


prompt = r"""
Please specify the language of the submitted YouTube video.

Press '1' for French.			Press '2' for German.			Press '3' for Italian.
Press '4' for Russian.			Press '5' for Dutch.			Press '6' for Mandarin (Han Yu).
Press '7' for Spanish.  		Press '8' for Turkish.  		Press '9' for Swedish.
Press '10' for Portuguese.		Press '11' for Japanese.  		Press '12' for Korean.
Press '13' for Polish. 			Press '14' for Czech.  			Press '15' for Finnish.
Press '16' for Hebrew. 			Press '17' for Hungarian.		Press '18' for Indonesian.
Press '19' for Malaysian.		Press '20' for Norwegian.		Press '21' for Romanian.
Press '22' for Serbian.   		Press '23' for Slovak.   		Press '24' for Afrikaans.

Leave blank for default (English).
"""


while True:
	# Asking the user for specific url
	url = input("\nPlease specify the full url to the YouTube video.\nYour entry should look like this: 'https://www.youtube.com/...' but without quotes.\n")
	if url == 'q':
		break

	print("\n------------------------------------------------------------------------------")
	lang = input(prompt)

	if lang == '1':
		language = 'fr-FR'
	if lang == '2':
		language = 'de-DE'
	if lang == '3':
		language = 'it-IT'
	if lang == '4':
		language == 'ru-RU'
	if lang == '5':
		language = 'nl-NL'
	if lang == '6':
		language = 'zh-CN'
	if lang == '7':
		language = 'es-ES'
	if lang == '8':
		language = 'tr'
	if lang == '9':
		language = 'sv-SE'
	if lang == '10':
		language = 'pt-PT'
	if lang == '11':
		language = 'ja'
	if lang == '12':
		language = 'ko'
	if lang == '13':
		language = 'pl'
	if lang == '14':
		language = 'cz'
	if lang == '15':
		language = 'fi'
	if lang == '16':
		language = 'he'
	if lang == '17':
		language = 'hu'
	if lang == '18':
		language = 'id'
	if lang == '19':
		language = 'ms-MY'
	if lang == '20':
		language = 'no-NO'
	if lang == '21':
		language = 'ro-RO'
	if lang == '22':
		language = 'sr-SP'
	if lang == '23':
		language = 'sk'
	if lang == '24':
		language = 'af'
	if lang == '':
		language = 'en-US'
	if lang == 'q':
		break


	# Downloading the video with the highest possible quality and naming it video_file
	yt = YouTube(url).streams.first().download('youtube', filename='video_file')

	# Defining storage of clip
	clip = mp.VideoFileClip(r'youtube/video_file.mp4')
	# Creating an audio file (wav) from the video file (mp4)
	clip.audio.write_audiofile(r'youtube/video_file.wav')

	# Creating a speech recognition object/ Initializing the recognizer
	r = sr.Recognizer()

	# Defining the path to the youtube video and audio files directory
	path = 'youtube/video_file.wav'

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
	print("\n------------------------------------------------------------------------------\n")
	print("Transcribing audio batchwise...\nThis may take a moment.")
	print("\n------------------------------------------------------------------------------\n")
	print("Creating directory 'audio_batches' to store audio chunks...")
	print("\n------------------------------------------------------------------------------\n")
	print("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\nFull text:\n\n", get_large_audio_transcription(path))
	print("\n------------------------------------------------------------------------------\n")


	question_save = input("Do you want to save the transcription to a text file? [y/n]\nNote: If you choose 'n' the files will be overwritten with the next download.\n")
	if question_save == 'y':
		# Ask for the destination folder where the text should be stored
		destination_folder = input("\nPlease specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
		# Ask for the file name
		file_name = input("\nPlease specify the desired file name.\nYour entry should look like this: 'example_file.txt' but without quotes.\n")

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{whole_text}")

		print("\n------------------------------------------------------------------------------\n")
		print("Your text file is created...\nGo to the folder you specified to access it.")
		print("\n------------------------------------------------------------------------------\n")

	if question_save == 'n':
		pass
	if question_save == 'q':
		break


	# Asking user if he/she wishes to continue
	question_more = input("Do you wish to convert another file? [y/n]\n")
	if question_more == 'y':
		print("\n------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
