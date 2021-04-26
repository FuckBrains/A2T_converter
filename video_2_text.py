"""This module contains a video specific speech-to-text-converter for large video files"""

import wave
import math
import contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip


banner = r'''

	                        _____
	__   ___    _          |  __ |  _______
	\ \ / (_)__| |___ ___  |_| / / |__   __|
	 \ V /| / _` / -_) _ \    / /     | |
	  \_/ |_\__,_\___\___/   / /___   |_|ext
	                        /______|

		[Sven Eschlbeck] [2021]


###################################################################
###################################################################

Hello! Welcome to 'VIDEO2TEXT'.

Enter 'q' to quit any time.

###################################################################
###################################################################

'''

# Printing banner with welcome message
print(banner)


# Asking for the language of the video file
prompt = """
Please specify the language of the video file.

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
	# Asking user to specify the path to the video file
	path = input("Please specify the full path to your video file (including file name).\nYour entry should look like this: 'C:/User/.../example.mp4' but without quotes.\n")
	if path == 'q':
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

	print("------------------------------------------------------------------------------\n")

	# Specifying video and audio file
	transcribed_audio_file_name = 'videos/transcribed_speech.wav'
	video_file_name = path

	# Convert video to audio
	audioclip = AudioFileClip(video_file_name)
	audioclip.write_audiofile(transcribed_audio_file_name)

	# Getting duration of the audio file
	with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
		frames = f.getnframes() # Number of frames
		rate = f.getframerate() # Rate of frames per second
		duration = frames / float(rate) # Total number of frames divided by the rate = duration

	# Calculation total duration
	print("\n------------------------------------------------------------------------------\n")
	print("Calculating total duration of audio track...\nPlease do not interrupt!")
	total_duration = math.ceil(duration / 60)
	print(f"Done. This file contains {total_duration} minutes of audio material.")

	# Creating instance of speech recognizer
	print("\n------------------------------------------------------------------------------\n")
	print("Initializing speech recognition API...")
	r = sr.Recognizer()

	# Asking for storage path
	print("\n------------------------------------------------------------------------------\n")
	destination_folder = input("Path to local storage is required. Please enter the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
	# Aborting if a 'q' is given
	if destination_folder == 'q':
		break

	# Ask for the file name
	file_name = input("\nPlease specify the desired file name.\nYour entry should look like this: 'example_file.txt' but without quotes.\n")
	# Aborting if a 'q' is given
	if file_name == 'q':
		break

	# Creating individual user path from destination folder and file name
	user_path = f"{destination_folder}/{file_name}"


	# Converting audio to text batchwise
	print("\n------------------------------------------------------------------------------\n")
	print("Converting audio to text batchwise...")
	print("\n------------------------------------------------------------------------------\n")
	for i in range(0, total_duration):
		with sr.AudioFile(transcribed_audio_file_name) as source:
			audio = r.record(source, offset = i*60, duration = 60)
			f = open(user_path, 'w') # Create file or append new data if already existing
			f.write(r.recognize_google(audio, language = language)) # Write into file what the Google API transcribes
			f.write(' ') # Leave spaces between two batches/ sentences
	f.close()
	print(f"Done.\nYou can find the transcription under '{user_path}'.")


	# Asking user if he/she wishes to continue
	question_more = input("Do you wish to transcribe another video? [y/n]\n")
	if question_more == 'y':
		print("\n------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
