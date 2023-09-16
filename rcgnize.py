import speech_recognition as sr
recognizer = sr.Recognizer()
microphone = sr.Microphone()


def recognize_user(*args: tuple):
    with microphone:
        data = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=0.5)

        try:
            print('speak: ')
            audio = recognizer.listen(microphone, 5, 30)

        except sr.WaitTimeoutError:
            print('Check your micro and speak')
            return ' '
        try:
            print('Recognizing... ')
            data = recognizer.recognize_google(audio, language='ru').lower()

        except sr.UnknownValueError:
            print('Check your internet connection')

        return data
