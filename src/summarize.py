from transformers import pipeline
def summarize_text(text:str,model_name: str = "facebook/bart-large-cnn",max_length:int = 130,min_length:int = 30) -> str:
    summarizer = pipeline("summarization",model = model_name)

    if len(text.split()) > 700:
        chunks = [text[i:i+700] for i in range(0, len(text),700)]
        summaries = [summarizer(chunk ,max_length = max_length,min_length = min_length,do_sample = False)[0]["summary_text"] for chunk in chunks]
        return " ".join(summaries)
    else:
        summary = summarizer(text,max_length = max_length,min_length = min_length,do_sample = False)[0]['summary_text']
        return summary