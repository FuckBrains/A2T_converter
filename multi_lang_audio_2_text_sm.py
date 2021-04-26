"""This module contains a general speech-to-text-converter for small to medium sized audio files"""

import speech_recognition as sr


banner = r'''


			   #####
			   ##		#####   ########
			   ##		   ##      ##
			   ##   	#####      ##
			 ####		##         ##
			 ####  		#####      ##ext    small/medium

            	  [Sven Eschlbeck] [2021]


##############################################################################
##############################################################################

Hello! Welcome to 'MULTI LANGUAGE AUDIO2TEXT for small audio files'.

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
	# Asking user to specify the path to the audio file
	path = input("Please specify the full path to your audio file (including file name).\nYour entry should look like this: 'C:/User/.../example.wav' but without quotes.\n")
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


	# Initializing the recognizer
	r = sr.Recognizer()

	# Open the audio file
	with sr.AudioFile(path) as source:
		# Listen for the data (loading audio into memory)
		audio_data = r.record(source)
		# Recognize speech and convert to text
		# Command uploads file to Google Cloud, using their A.I. to convert it and returns the text transcription
		text = r.recognize_google(audio_data, language = language)
		# Print text
		print("\n------------------------------------------------------------------------------\n")
		print(f"Output:\n\n{text}")
		print("\n------------------------------------------------------------------------------\n")

	question_save = input("Do you want to save the transcription to a text file? [y/n]\n")
	if question_save == 'y':
		# Ask for the destination folder where the text should be stored
		destination_folder = input("\nPlease specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
		# Aborting if a 'q' is given
		if destination_folder == 'q':
			break

		# Ask for the file name
		file_name = input("\nPlease specify the desired file name.\n")
		# Aborting if a 'q' is given
		if file_name == 'q':
			break

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		with open(user_path, 'w') as f:
			# Write the text into the file
			f.write(f"{text}")

		print("\n------------------------------------------------------------------------------\n")
		print("Your text file is created...\nGo to the folder you specified to access it.")
		print("\n------------------------------------------------------------------------------\n")

	if question_save == 'n':
		pass
	if question_save == 'q':
		break

	question_more = input("\nDo you wish to convert another file? [y/n]\n")
	if question_more == 'y':
		print("\n------------------------------------------------------------------------------\n")
		continue
	if question_more == 'n':
		break
	if question_more == 'q':
		break
