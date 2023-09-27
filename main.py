from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
from tqdm import tqdm


def translate(word):
	trans = Translator()
	meaning = trans.translate(word, src='en',  dest='th').text

	return meaning


def pronunEng(word):
	tss = gTTS(text=word, lang='en')
	
	tss.save('engDemo.mp3')


def pronunThai(word):
	tss = gTTS(text=word, lang='th')
	
	tss.save('thaiDemo.mp3')





# translate the meaning of the word
txtWord = 'door'
translatedWord = translate(txtWord)



sentences = ["ภาษาอังกฤษวันละคำ วันนี้ขอเสนอคำว่า ", txtWord]


pronunThai(sentences[0])
pronunEng(sentences[1])




sound1 = AudioSegment.from_file(r'C:\Users\saich\Documents\EngPrac\engDemo.mp3', format='mp3')
sound2 = AudioSegment.from_file(r'C:\Users\saich\Documents\EngPrac\thaiDemo.mp3', format='mp3')


combined = sound1 + sound2

combined.export(r'C:\Users\saich\Documents\EngPrac\exported.mp3', format='mp3')

