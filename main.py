from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
from tqdm import tqdm
from pathlib import Path

current_path = str(Path(__file__).parent.resolve())

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



sentences = ["ภาษาอังกฤษวันละคำ วันนี้ขอเสนอคำว่า ", txtWord, txtWord, "สามารถสะกดได้ดังนี้"]

sound = AudioSegment.from_file(str(Path(current_path, "joyful-jingle.mp3")), format='mp3')

for i, sen in enumerate(sentences):
	pronunThai(sen)
	
	filename = "demo.mp3{}".format(i)
	sound = AudioSegment.from_file(str(Path(current_path, filename)), format='mp3')
	
	sound += sound




sound.export(r'C:\Users\saich\Documents\EngPrac\exported.mp3', format='mp3')

