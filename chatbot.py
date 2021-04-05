import pyglet
import speech_recognition as sr


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

            song = pyglet.media.load('audio.mp3')
            song.play()
            pyglet.app.run()

        if text.lower() == "prueba chat":
            song = pyglet.media.load('file.mp3')
            song.play()
            pyglet.app.run()

        if text.lower() == "semillero":
            song = pyglet.media.load('test.mp3')
            song.play()
            pyglet.app.run()

    except :
        print("No entiendo err: {}")





