from transformers import pipeline
import json
import os

qa_pipline = pipeline("question-answering",model = "distilbert-base-uncased-distilled-squad")
def ask_question(context:str,qa_file_path:str = "outputs/qa_history.json"):
    qa_pairs = []
    if os.path.exists(qa_file_path):
        with open(qa_file_path, "r",encoding="utf-8") as f:
            qa_pairs = json.load(f)
    print("\nAsk a question based on the context:\n")

    while True:
        question = input("Q: ")
        if question.lower() in ["exit","quit"]:
            break
        answer = qa_pipline(question=question,context=context)["answer"]
        print(f"A: {answer}\n")

        qa_pairs.append({"question":question,"answer":answer})
    
    with open(qa_file_path,"w",encoding="utf-8") as f:
        json.dump(qa_pairs,f,indent=4,ensure_ascii = False)