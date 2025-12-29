import queue
import sounddevice as sd
from vosk import Model,KaldiRecognizer
import pyttsx3
import json
import datetime
import random
model = Model("/Users/trishsagar/Desktop/New Folder With Items/AI Classes/AI33:VoiceAssistant/vosk-model-en-us-0.22-lgraph/conf/model.conf")
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
        today = datetime.datetime.today().strf("%B %d, %Y")
        response = f"Today's Date is {today}."
    else:
        print("I am sorry I could not understand that.")
    return response


