"""This module contains a text-to-speech converter"""

from gtts import gTTS
from playsound import playsound
import os


banner = r'''

	##### ##### # # #####   ##### ####
	  #   ##     #    #       #   #  #
	  #   ##### # #   #       #   ####

	##### ###### ###### ###### ###### #     #
	#     #    # #      #      #      #     #
	##### ###### ###### ###### #      #######
	    # #      #      #      #      #     #
	##### #      ###### ###### ###### #     #


		[Sven Eschlbeck] [2021]


###################################################################
###################################################################

Hello! Welcome to 'TEXT2SPEECH'.

Enter 'q' to quit any time.

###################################################################
###################################################################

'''

print(banner)


prompt = r"""
Please specify the language of the aimed output speech.

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

	print("------------------------------------------------------------------------------")
	lang = input(prompt)

	if lang == '1':
		language = 'fr'
	if lang == '2':
		language = 'de'
	if lang == '3':
		language = 'it'
	if lang == '4':
		language == 'ru'
	if lang == '5':
		language = 'nl'
	if lang == '6':
		language = 'zh-CN'
	if lang == '7':
		language = 'es'
	if lang == '8':
		language = 'tr'
	if lang == '9':
		language = 'sv'
	if lang == '10':
		language = 'pt'
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
		language = 'en'
	if lang == 'q':
		break


	# Asking if user wants to load text from a file or type into command line
	print("\n------------------------------------------------------------------------------\n")
	input_type = input("Do you want to read text from a file or type it into this terminal window?\nType 'file' for option 1 and 'type' for option 2.\n")

	if input_type == 'file':
		# Ask for the destination folder where the speech should be stored
		origin_path = input("\nPlease specify the full path to the folder including the file name.\nYour entry should look like this: 'C:/User/.../example.txt' but without quotes.\n")
		# Loading text file
		filename = origin_path
		with open(filename, 'r') as f:
			text_input = f.read()
		# Aborting if a 'q' is given
		if origin_path == 'q':
			break

	if input_type == 'type':
		# Asking user to specify the text he/she wishes to convert into speech
		print("\n------------------------------------------------------------------------------\n")
		text_input = input("Please type in the text you wish to convert to speech.\nYour entry should look like this: 'I would like to convert this text!' but without quotes.\n")
		# Aborting if a 'q' is given
		if text_input == 'q':
			break

	# Aborting if a 'q' is given
	if input_type == 'q':
		break


	# Asking user for the wanted audio speed
	print("\n------------------------------------------------------------------------------\n")
	speed = input("Would you like the speech to be read fast or slowly by the computer voice? [f/s]\n")

	if speed == 's':
		tempo = True # Slow

	if speed == 'f':
		tempo = False # Fast

	# Aborting if a 'q' is given
	if speed == 'q':
		break


	# Passing the text and language to the engine
	# slow=True/False tells the module that the converted audio should have a slow/high speed
	myobj = gTTS(text = text_input, lang = language, slow = tempo)


	# Temporarily saving audio file
	myobj.save('temp_speeches/temp_audio.wav')


	print("\n------------------------------------------------------------------------------\n")
	question_play = input("Do you wish to play the computer generated audio speech? [y/n]\n")

	if question_play == 'y':
		os.system(' start temp_speeches/temp_audio.wav')

	if question_play == 'n':
		continue

	# Aborting if a 'q' is given
	if question_play == 'q':
		break


	print("\n------------------------------------------------------------------------------\n")
	question_save = input("Do you want to save the computer generated speech to an audio file? [y/n]\n")

	if question_save == 'y':
		# Ask for the destination folder where the speech should be stored
		destination_folder = input("\nPlease specify the full path to the desired destination folder.\nYour entry should look like this: 'C:/User/...' but without quotes.\n")
		# Aborting if a 'q' is given
		if destination_folder == 'q':
			break

		# Ask for the file name
		file_name = input("\nPlease specify the desired file name with ending (.wav).\nYour entry should look like this: 'example_file.wav' but without quotes.\n")

		# Aborting if a 'q' is given
		if file_name == 'q':
			break

		# Creating individual user path from destination folder and file name
		user_path = f"{destination_folder}/{file_name}"
		# Save audio file
		myobj.save(f"{user_path}")

		print("\n------------------------------------------------------------------------------\n")
		print("Your audio file is created...\nGo to the folder you specified to access it.")
		print("\n------------------------------------------------------------------------------\n")

	if question_save == 'n':
		pass

	# Aborting if a 'q' is given
	if question_save == 'q':
		break


	# Asking user if he/she wishes to continue
	question_more = input("\nDo you wish to convert another text? [y/n]\n")

	if question_more == 'y':
		print("\n------------------------------------------------------------------------------\n")
		continue

	if question_more == 'n':
		break

	# Aborting if a 'q' is given
	if question_more == 'q':
		break
