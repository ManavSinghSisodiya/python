# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = "....... Rrajat please take my lund in your mouth"
# input_text = input(a 'type here what you want to listen---')

# Setting the language
language = "hi"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, tld="co.in", slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the file
os.system("start demo.mp3")