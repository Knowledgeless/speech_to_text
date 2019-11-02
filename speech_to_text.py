import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
	print('Listening...')
	audio = r.listen(source)

	text = r.recognize_google(audio)
	if text == 'open Chrome' or text == 'Google search' or text =='let me search on Google':
		webbrowser.open('http://www.google.com/')
	print('You said: {}'.format(text))
	
