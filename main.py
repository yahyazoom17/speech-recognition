import whisper

model = whisper.load_model("base")

audio_path = "D:/Projects/Speech Recognition/speech-recognition/sample-audio.wav"

result = model.transcribe(audio_path, fp16=False)
print(result["text"])
