import whisper

def transcribe_audio(file_name):
    model = whisper.load_model("medium")
    result = model.transcribe(file_name)
    text = result["text"]
    return text

# make a test of the transcription