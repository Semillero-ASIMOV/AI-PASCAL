import wave
import speech_recognition as sr
import alsaaudio


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

# Class for blinking the leds

#def escucharPascal(self):

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo...")

    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:

        text = r.recognize_google(audio, language='es-ES')

        print("Dijiste: {}".format(text.lower()))

        if text.lower() == "hola pascal":
            print("En que te puedo Ayudar")

            playAudio('file.wav')

            print("AUDIO END")

        if text.lower() == "prueba chat":
            playAudio('audio.wav')

            print("AUDIO END")

        if text.lower() == "semillero":
            playAudio('file.wav')

            print("AUDIO END")

    except :
        print("No entiendo")






