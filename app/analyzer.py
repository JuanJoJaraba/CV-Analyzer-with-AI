import re
import spacy

# Carga modelo inglés pequeño
nlp = spacy.load("en_core_web_sm")

# Lista de tecnologías comunes que podrías ampliar
TECH_KEYWORDS = [
    "JavaScript", "Node.js", "React", "Python", "Django", "Flask", "SQL", "MongoDB",
    "AWS", "Docker", "Kubernetes", "Git", "HTML", "CSS", "TypeScript", "PostgreSQL"
]

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else "No encontrado"

def extract_phone(text):
    match = re.search(r"(\+?\d{1,3})?[-.\s]?\(?\d{3,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}", text)
    return match.group(0) if match else "No encontrado"

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "No encontrado"

def extract_technologies(text):
    found = []
    for tech in TECH_KEYWORDS:
        if tech.lower() in text.lower():
            found.append(tech)
    return list(set(found)) if found else ["No detectadas"]

def analyze_cv(text):
    return {
        "Nombre": extract_name(text),
        "Email": extract_email(text),
        "Teléfono": extract_phone(text),
        "Tecnologías": extract_technologies(text)
    }
