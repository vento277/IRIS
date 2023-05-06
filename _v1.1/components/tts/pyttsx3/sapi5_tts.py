import pyttsx3

def tts(text):
    print(text)

    # convert text -> speech
    converter = pyttsx3.init('sapi5') # initialize 

    voices = converter.getProperty('voices')
    newVoiceRate = 175
    converter.setProperty('rate', newVoiceRate)
    converter.setProperty('voice', voices[1].id)
    converter.say(text) # say the given parameter
    converter.runAndWait() # wait untill all texts are said