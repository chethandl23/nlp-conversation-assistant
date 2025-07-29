from transformers import pipeline


def ques_n_ans(question :str,context:str,model_name:str = "google/flan-t5-base") -> str:
    qa_pipeline = pipeline("text2text-generation",model = model_name)
    prompt = f"Context:{context}\nQuestion:{question}\nAnswer:"

    response =qa_pipeline(prompt,max_length =150,do_sample = False)[0]["generated_text"]
    return response.strip()