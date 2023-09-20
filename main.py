from gtts import gTTS
from googletrans import Translator


def translate(word):
	trans = Translator()
	meaning = trans.translate(word, src='en',  dest='th').text

	return meaning

txtWord = 'property'
translateWord = translate(txtWord)


txt = 'สะกดคำว่า {} ... ... คือ'.format(txtWord)

for t in txtWord:
	txt += " "
	txt += " ...  ...  "
	txt += t

txt += " .... ... "

txt += "อ่านว่า ... ... " + txtWord
txt += "... ...  มีความหมายว่า ... ... {}".format(translateWord)

print(txt)

tts = gTTS(text=txt, lang='th')

tts.save('demo.mp3')