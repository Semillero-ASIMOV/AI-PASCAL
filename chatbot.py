import wave
import alsaaudio
import time

import speech_recognition as sr
import numpy as np

def playAudio(self):
    # open audio file and device
    audio_file = wave.open(self, 'rb')
    audio_device = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NORMAL, 'default')

    # we are hard coding the audio format!
    audio_device.setchannels(2)
    audio_device.setrate(44100)
    audio_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    audio_device.setperiodsize(980)

    # play the audio
    audio_data = audio_file.readframes(980)
    while audio_data:
        audio_device.write(audio_data)
        audio_data = audio_file.readframes(980)

    audio_file.close()


import speech_recognition as sr
import time
from subprocess import call

trigger = "hola pascal"

recognizer = sr.Recognizer()

print("Beginning to listen...")

def listen():
        with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                try:
                    str=recognizer.recognize_google(audio, language='es-ES')
                    return str.lower()
                except sr.UnknownValueError:
                    print("No entiendo bien")
                return ""

def menu():

    ubicacion=np.array(["necesito ubicarme","ayudame a ubicarme","quiero ubicarme","como ubicarme","donde ubicarme","ubicación" ])
    bus = np.array(["necesito el bus","donde es el bus","cuando sale el otro bus","bus"])
    saludos = np.array(["como estas","como vas","que tal tu dia","como estuvo tu dia"])

    text=listen()
    print(text.lower())

    if text == "" :
        return False

    if text.lower() in ubicacion:
        print("Claro Dime donde quieres ir")

        playAudio('audios/file.wav')

        print("AUDIO END")

    if text.lower() in saludos:
        print("Muy Bien Y Tu")

        playAudio('audios/file.wav')

        print("AUDIO END")

    if text.lower() in bus:
        print("A Donde Vas")

        playAudio('audios/t3.wav')
        print("AUDIO END")
    return True



print("Trying to always listen...")
a=1
while a==1:
        str=listen()
        print(str)
        if str == trigger:
            print("ENTRO a Trigger")
            bool = menu()

            if bool:
                a=2

        #time.sleep(0.2)

print("SALE")





