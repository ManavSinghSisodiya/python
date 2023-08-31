# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = "poooooooooohhhhhhhh,,,,lo aur uska cake bana lo aur उसे भी खा लो ..poooooooooooohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
# input_text = input('type here what you want to listen---')

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, tld="co.in", slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the file
os.system("start demo.mp3")