from transformers import pipeline

# Carga del modelo de resumen
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_cv(text):
    # Limita a 1024 tokens (máximo que soporta el modelo)
    if len(text) > 1024:
        text = text[:1024]

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
