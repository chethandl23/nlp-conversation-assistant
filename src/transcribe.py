import whisper
import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build (1)\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build\bin"

def transcribe_audio(audio_path, model_size="base"):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    print(f"Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)

    print(f"Transcribing: {audio_path}")
    result = model.transcribe(audio_path)

    return result["text"]
