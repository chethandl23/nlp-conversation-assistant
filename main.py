import json
import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build (1)\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build\bin"
from pathlib import Path

from src.transcribe import transcribe_audio
from src.summarize import summarize_text
from src.questions_n_ans import ques_n_ans
audio_path = r"C:\Users\DELL\OneDrive\Documents\nlp-conversation-assistant\data\audio.mp3"

# Call the transcribe function
transcript = transcribe_audio(audio_path)

# Save the transcript to a text file
with open("outputs/transcript.txt", "w", encoding="utf-8") as f:
    f.write(transcript)

print("Transcribed audio saved.")
with open("outputs/transcript.txt","r",encoding="utf-8") as f:
    transcript_text = f.read()

summary = summarize_text(transcript_text)

with open("outputs/summary.txt","w",encoding="utf-8") as f:
    f.write(summary)
print("summary saved..")

with open("outputs/summary.txt","r",encoding = "utf-8") as f:
    context = f.read()

question = input("ask any doubt:")
answer = ques_n_ans(question,context)

qa_json_path = Path("outputs/qa_history.json")
if qa_json_path.exists():
    with open(qa_json_path, "r", encoding="utf-8") as f:
        qa_history = json.load(f)
else:
    qa_history = []

qa_history.append({"question": question, "answer": answer})

with open(qa_json_path, "w", encoding="utf-8") as f:
    json.dump(qa_history, f, ensure_ascii=False, indent=4)

print("question and answer saved ")
