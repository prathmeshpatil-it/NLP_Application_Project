from transformers import pipeline

summarizer = pipeline("summarization")
text = "Paste long text here"
summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
print(summary)
