# A2T_converter

Welcome to A2T, the easily usable tool to transcribe audio information into text files. Did you ever hear an audiobook or watch a YouTube video and wished to be able to have a transcript of the spoken word? If the answer is yes, then this project might be helpful.

## Converter types

- YouTube -> convert YouTube videos by just typing in a specific url
- videos -> convert any locally stored video file (e.g. Zoom call recording, Twitter video, Facebook video, TikTok video, etc.)
- short audio files -> convert WhatsApp voice messages, short audio news and more
- long audio files -> convert audio books, poems, stories, political speeches and more
- self recorded speeches -> convert microphone input into text
- text to speech -> Validate the other programs

## Text-to-speech

With 'text_2_speech' you can convert text into computer generated speeches. This can be helpful if you have no audio file available and want to create your own. Also, this program can be used to validate the other scripts' accuracy when transcribing.  
Just create an audio file with 'text_2_speech' and use that file to transcribe its audio into text. Ideally, the generated text should be equal to the text you provided for 'text_2_speech'.

## Languages
  
Note that the software is only applicable to audio data in supported languages. Transcribing data of unsopported languages with this API can cause wrong and unintentional transcriptions.  

Currently supported languages include:  
- English  
- French
- German
- Italian
- Russian
- Dutch
- Mandarin (Han Yu)
- Spanish
- Turkish
- Swedish
- Portuguese
- Japanese
- Korean
- Polish
- Czech
- Finnish
- Hebrew
- Hungarian
- Indonesian
- Malaysian
- Norwegian
- Romanian
- Serbian
- Slovak
- Afrikaans

## Type handling

The audio converters 'multi_lang_audio_2_text_sm' and 'multi_lang_audio_2_text_la' currently need '.wav' files as a prerequesite. Necessary proprocessings and typecastings can be done here: https://online-audio-converter.com/  
The YouTube-to-Text converter 'youtube_2_text' can process any input without the necessity of typecasting, the video transcriber can handle all common video formats.

## Controls

The program is very intuitive. Just follow the command line instructions and you'll be fine.  
To quit the program at any time, press <kbd>Q</kbd> whenever a question is asked or click on the red 'X' in the upper right cmd window corner.  
If asked a question, reply by either pressing <kbd>Y</kbd> for 'yes', <kbd>N</kbd> for 'no', or <kbd>Q</kbd> to quit the program.  
To confirm the given answer, press <kbd>&#9166;</kbd>.  

## Hardware & Software Requirements

This program can be run without much computing power. It can be executed on any modern device using Microsoft's Windows operating system. Other OS may work but are not specifically supported.  
A2T is written in python and currently only available in the form of multiple python modules. Therefore, you need to download python in order to execute the program files (.py files). The required storage capacity depends on the user's behavior. It can range from a few MB when only transcribing small audio files to multiple GB when downloading and converting large video files.  
After downloading and storing this repository, open a python terminal window, navigate to the repository directory and type e.g. 'multi_lang_audio_2_text_la.py'. As soon as you hit <kbd>&#9166;</kbd>, the program will start.

## Code Documentation

The documentation for this project can be found under 'docs/build/html/index.html'. Navigate to the file on your local machine and open it in a web browser.

## Resources & Links

https://www.python.org/ (Python)  
https://www.anaconda.com/ (Anaconda)  
https://pytube.io/en/latest/ (Pytube)  
https://github.com/jiaaro/pydub (Pydub)  
https://pypi.org/project/SpeechRecognition/ (SpeechRecognition)  
https://cloud.google.com/speech-to-text (Google Cloud Speech-to-Text API)  
https://www.sphinx-doc.org/en/master/# (Sphinx)  
https://readthedocs.org/ (Read the Docs)  

## Contact

You have questions about the project or want to report a bug or feedback in general?  
Contact me via sven.eschlbeck@t-online.de
