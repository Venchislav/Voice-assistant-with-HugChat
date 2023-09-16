# libraries needed
import speech_recognition as sr
from bardapi import Bard
from rcgnize import recognize_user
import subprocess
import pyttsx3
from data import TOKEN

# language model to generate speech from text
# it's on russian (as I did it for myself), but you can set different language
tts = pyttsx3.init()

tts.setProperty('voice', 'ru')

# create Bard lib object
bard = Bard(token=TOKEN)

# init microphone and recognizer
r = sr.Recognizer()
m = sr.Microphone()


if __name__ == '__main__':
    while True:
        # our voice input
        input_ = recognize_user()
        # Here I mean if input is bye program breaks
        if input_.lower() == 'пока':
            break
        else:
            print('connecting Bard: ')
            # say bard's response
            tts.say(bard.get_answer(input_)['content'])
            print(bard.get_answer(input_)['content'])
            tts.runAndWait()
