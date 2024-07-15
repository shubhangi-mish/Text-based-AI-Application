import pyaudio
import wave
import requests
import json
import pyttsx3

# Constants
AUDIO_FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Hugging Face API endpoint and token
HF_API_ENDPOINT = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
HF_API_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your actual Hugging Face API token

# Initialize text-to-speech engine
engine = pyttsx3.init()

def recognize_speech(audio_file):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    with open(audio_file, "rb") as f:
        data = f.read()
    response = requests.post(HF_API_ENDPOINT, headers=headers, data=data)
    result = json.loads(response.content.decode("utf-8"))
    return result.get("text", "")

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(filename):
    p = pyaudio.PyAudio()
    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(AUDIO_FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
