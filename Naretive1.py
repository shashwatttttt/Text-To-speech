import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

text_to_speech('Hello World, I am Naretive AI and I will talk to you ')