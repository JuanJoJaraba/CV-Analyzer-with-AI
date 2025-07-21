from openai import OpenAI
import os

client = OpenAI(api_key="API-KEY")  # pon aquí tu API Key directamente
def generar_recomendaciones(cv_text):
    prompt = (
        f"Lee el siguiente CV y genera 3 recomendaciones para mejorarlo "
        f"en cuanto a claridad, presentación y habilidades técnicas:\n\n{cv_text}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": "Eres un asesor experto en redacción de currículums."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


