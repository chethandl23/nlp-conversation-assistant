import json
import os
from fastapi import FastAPI, UploadFile, File,Form
from fastapi.responses import JSONResponse
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build (1)\ffmpeg-2025-07-21-git-8cdb47e47a-essentials_build\bin"
from pathlib import Path
import shutil
from src.transcribe import transcribe_audio
from src.summarize import summarize_text
from src.questions_n_ans import ask_question
app = FastAPI()
audio_save_path = "data\audio.mp3"
transcript_path = "outputs/transcript.txt"
summary_path = "outputs/summary.txt"
QA_path = "outputs/qa_history.json"

#endpoint 1 : transcrbe audio
@app.post("/transcribe")
async def transcribe_endpoint(file: UploadFile = File(...)):
    with open(audio_save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    

# Call the transcribe function
    transcript = transcribe_audio(audio_save_path)

# Save the transcript to a text file
    with open("outputs/transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)
    return {"transcript": transcript}

@app.post("/summarize")
async def summarize_endpoint():
    if not os.path.exists(transcript_path):
        return JSONResponse(status_code=404, content={"message": "Transcript file not found."})
    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = f.read()
    summary = summarize_text(transcript_text)

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)
    
    return {"summary": summary}


#endpoint 3 : question and answer
@app.post("/ask_question")
async def ask_question_endpoint(question: str = Form(...)):
    if not os.path.exists(transcript_path):
        return JSONResponse(status_code=404, content={"message": "Transcript file not found."})
    with open(summary_path, "r", encoding="utf-8") as f:
        summary_text = f.read()
    answer = ask_question(summary_text, question)
    
    qa_entry = {
        "question": question,
        "answer": answer
    }

    if os.path.exists(QA_path):
        with open(QA_path, "r", encoding="utf-8") as f:
            qa_history = json.load(f)
    else:
        qa_history = []

    qa_history.append(qa_entry)

    with open(QA_path, "w", encoding="utf-8") as f:
        json.dump(qa_history, f, indent=4)

    return {"answer": answer}