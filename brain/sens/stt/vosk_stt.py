from xml.etree.ElementTree import TreeBuilder
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r"")
recognizer = KaldiRecognizer(model, 16000)

def stt():
    mic = pyaudio.PyAudio()
    stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print("User: " + text[14: -3])
            return(text[14: -3])

