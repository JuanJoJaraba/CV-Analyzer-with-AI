from sentence_transformers import SentenceTransformer, util

# Modelo para embeddings semánticos
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

def match_cv_to_job(cv_text, job_description):
    # Convertir ambos textos a embeddings
    embeddings = model.encode([cv_text, job_description], convert_to_tensor=True)

    # Calcular la similitud coseno
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()

    # Convertir a porcentaje
    return round(similarity * 100, 2)
