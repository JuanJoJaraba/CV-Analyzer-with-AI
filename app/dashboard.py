import streamlit as st
from resume_parser import extract_text_from_file
from analyzer import analyze_cv
import os
import matplotlib.pyplot as plt
import pandas as pd
from summarizer import summarize_cv
from matcher import match_cv_to_job
from recommender import generar_recomendaciones

st.set_page_config(page_title="CV Analyzer", layout="centered")

st.title("📄 Analizador Inteligente de CVs")
st.write("Sube un CV en formato **PDF** o **DOCX** para analizarlo automáticamente usando IA.")

uploaded_file = st.file_uploader("Selecciona un archivo", type=["pdf", "docx"])

if uploaded_file is not None:
    # Guarda el archivo temporalmente
    file_path = os.path.join("app/data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Extrae el texto
    text = extract_text_from_file(file_path)
    # Resumen con IA
    st.subheader("🧠 Resumen automático del CV")

    with st.spinner("Generando resumen con IA..."):
        resumen = summarize_cv(text)
        st.success("Resumen generado:")
        st.write(resumen)
    # Mostrar texto si se desea
    with st.expander("🔍 Ver texto extraído"):
        st.write(text)
        
    st.subheader("🧪 Comparar CV con una Vacante")

    job_desc = st.text_area("Pega aquí la descripción de la vacante:")

    if job_desc:
        with st.spinner("Analizando coincidencia..."):
            match_score = match_cv_to_job(text, job_desc)
            st.success(f"🔗 Nivel de coincidencia: {match_score}%")

            if match_score > 75:
                st.write("✅ Alta compatibilidad para esta vacante.")
            elif match_score > 50:
                st.write("🟡 Compatibilidad media.")
            else:
                st.write("🔴 Poca coincidencia con la vacante.")
                
    st.subheader("💡 Recomendaciones para mejorar el CV")

    if st.button("Generar recomendaciones con IA"):
        with st.spinner("Generando recomendaciones..."):
            recomendaciones = generar_recomendaciones(text)
            st.markdown(recomendaciones)

    # Analiza el contenido
    st.subheader("📊 Resultados del análisis")
    results = analyze_cv(text)
    for k, v in results.items():
        st.write(f"**{k}:** {', '.join(v) if isinstance(v, list) else v}")

    # Gráfico de tecnologías
    tecnologias = results.get("Tecnologías", [])

    if tecnologias and tecnologias != ["No detectadas"]:
        st.subheader("📈 Tecnologías detectadas")

        fig, ax = plt.subplots()
        ax.bar(tecnologias, [1]*len(tecnologias), color="skyblue")
        ax.set_ylabel("Recuento")
        ax.set_title("Tecnologías encontradas en el CV")
        plt.xticks(rotation=45, ha='right')  # 🔄 Rota las etiquetas para que no se sobrepongan
        st.pyplot(fig)

    # Guardar en CSV
    csv_path = "app/data/cv_data.csv"

    new_data = {
        "Archivo": uploaded_file.name,
        "Nombre": results["Nombre"],
        "Email": results["Email"],
        "Teléfono": results["Teléfono"],
        "Tecnologías": ", ".join(tecnologias) if tecnologias else ""
    }

    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:
        df = pd.DataFrame([new_data])

    df.to_csv(csv_path, index=False)
    st.success("✅ Análisis guardado en CSV.")

    # Mostrar historial
    st.subheader("📁 Historial de CVs analizados")
    st.dataframe(df)

    # Limpia el archivo temporal si deseas (opcional)
    # os.remove(file_path)
