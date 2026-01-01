import queue
import sounddevice as sd
from vosk import Model,KaldiRecognizer
import pyttsx3
import json
import datetime

model = Model("/Users/trishsagar/Desktop/New Folder With Items/AI Classes/AI33:VoiceAssistant/vosk-model-en-us-0.22-lgraph")
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()

def callback(indata, frames, time, status):
    if status:
        print(status)
    else:
        audio_queue.put(bytes(indata))
def process_query(query):
    query=query.lower()
    if 'time' in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The Current time is {now}."
    elif 'date' in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        response = f"Today's Date is {today}."
    else:
        response = "I am sorry I could not understand that."
    return response

def main():
    with sd.RawInputStream(samplerate=16000,blocksize=800,dtype="int16",channels=1,callback=callback):
        print("Listening.... speak into your microphone")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text=json.loads(result)["text"]
                if text.strip()!="":
                    print("you said: ", text)
                    response = process_query(text)
                    print("Assistant: ", response)
                    tts_engine.say(response)
                    tts_engine.runAndWait()
if __name__ == "__main__":
    main()


