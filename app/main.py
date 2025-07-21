from resume_parser import extract_text_from_file
from analyzer import analyze_cv
from summarizer import summarize_cv


ruta = "app/data/ejemplo_cv.pdf"
texto = extract_text_from_file(ruta)

print("\n--- Análisis de CV ---\n")
analisis = analyze_cv(texto)
for clave, valor in analisis.items():
    print(f"{clave}: {valor}")
