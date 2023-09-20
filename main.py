from gtts import gTTS

txtWord = 'van'

txt = 'สะกดคำว่า {} ... ... คือ'.format(txtWord)

for t in txtWord:
	txt += " "
	txt += " ...  ...  "
	txt += t


print(txt)

# tts = gTTS(text=txt, lang='th')

# tts.save('demo.mp3')