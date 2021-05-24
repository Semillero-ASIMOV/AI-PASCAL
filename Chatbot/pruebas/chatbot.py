import wave
import alsaaudio
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

#Palabra de Activación
trigger = "hola pascal"

#Inicializa Reconocimiento
recognizer = sr.Recognizer()


print("Beginning to listen...")

def listen():
        #identifica Microfono
        with sr.Microphone() as source:

                #Ajusta Microfono A ruidos
                recognizer.adjust_for_ambient_noise(source)

                #Escucha Mic
                audio = recognizer.listen(source)
                try:
                    #Reconoce audio y cambia a texto
                    str=recognizer.recognize_google(audio, language='es-ES')

                    #Retorna texto en minusculas
                    return str.lower()
                except sr.UnknownValueError:
                    print("No entiendo bien")
                return ""

def menu():
    #Crea coleccion con posibles llamadas a pascal
    ubicacion=np.array(["necesito ubicarme","ayudame a ubicarme","quiero ubicarme","como ubicarme","donde ubicarme","ubicación" ])
    bus = np.array(["necesito el bus","donde es el bus","cuando sale el otro bus","bus"])
    saludos = np.array(["como estas","como vas","que tal tu dia","como estuvo tu dia"])

    #Escucha
    text=listen()
    print(text.lower())

    #Si no escucha bien retorna falso
    if text == "" :
        return False

    #Si escucha algo de las colecciones reproduce un audio, si no esta en las colecciones, pide repetir

    if text.lower() in ubicacion:
        print("Claro Dime donde quieres ir")

        playAudio('audios/file.wav')

        print("AUDIO END")

    elif text.lower() in saludos:
        print("Muy Bien Y Tu")

        playAudio('audios/file.wav')

        print("AUDIO END")

    elif text.lower() in bus:
        print("A Donde Vas")

        playAudio('audios/t3.wav')
        print("AUDIO END")
    else:
        print("Perdon, no te entendi muy bien, puedes repetir")
        playAudio('audios/t2.wav')
        print("AUDIO END")
        return False


    return True



print("Trying to always listen...")

#Inicializa Variable para escuchar todo el tiempo hasta escuchar trigger
a=1

#Recorre un while mientras escucha trigger
while a==1:
        #Llama funcion escuchar
        str=listen()

        print(str)

        #Si escucha "hola pascal" llama funcion menu
        if str == trigger:
            print("ENTRO a Trigger")
            bool = menu()

            if bool:
                #Si todo finaliza bien, hace var a=2 y finaliza proceso
                a=2

        #time.sleep(0.2)

print("SALE")





