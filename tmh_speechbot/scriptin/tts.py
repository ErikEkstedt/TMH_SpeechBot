import torch
import soundfile as sf
import uuid
import subprocess

def synthesize_speech(text):
    file_path = "speech/" + text +str(uuid.uuid4()) + ".mp3"
    subprocess.call(["tts", "--text", text, "--out_path", file_path])
    print(file_path)
    return file_path

# synthesize_speech("Shivam Mehta is amazing")