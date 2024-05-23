import pyttsx3 as tts;

engine = tts.init(driverName = "sapi5")

def saySomething(message):
    engine.say(message)
    engine.runAndWait()
