#https://www.geeksforgeeks.org/convert-text-speech-python/

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = """Появилось видео с места ДТП, произошедшего в понедельник утром на трассе Калининград-Черняховск.
Судя по ролику, опубликованному в Сообществе автомобилистов Калининградской области,
в аварии приняли участие не два автомобиля, как сообщалось ранее, а гораздо большее их количество."""
  
# Language in which you want to convert
language = 'ru'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)


# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("audio.mp3")
  
# Playing the converted file
#os.system("mpg321 welcome.mp3")
os.system("audio.mp3")

