# 🧠 CV Analyzer with AI

Este proyecto es una herramienta inteligente desarrollada con Python y Streamlit que permite analizar hojas de vida (CVs) automáticamente usando inteligencia artificial.


---

## 🚀 ¿Qué hace?

🔍 **Funciones principales:**

- 📄 **Lectura de CVs** en formato PDF o DOCX  
- ✍️ **Generación de resumen automático** del contenido del CV con IA  
- 📊 **Comparación de CV con una vacante** para calcular nivel de coincidencia  
- 📈 **Análisis de campos clave:** nombre, email, teléfono, experiencia, skills  
- 🧠 **Recomendaciones automáticas** para mejorar el perfil

---

## 🧰 Tecnologías usadas

- Python 3.11  
- [Streamlit](https://streamlit.io/) (interfaz)  
- [OpenAI API](https://platform.openai.com/) (análisis y recomendaciones)  
- `PyPDF2`, `python-docx` (lectura de archivos)  
- `re`, `spacy` (procesamiento de texto)  
- `pandas` (registro histórico)

---

## ⚙️ Cómo usar

1. **Clona el repositorio:**

```bash
git clone https://github.com/JuanJoJaraba/CV-Analyzer-with-AI.git
cd CV-Analyzer-with-AI

2. Instala las dependencias:
pip install -r requirements.txt

3. Crea un archivo .env con tu clave de OpenAI:
env
OPENAI_API_KEY=sk-...

4. Ejecuta la app:
streamlit run app/dashboard.py

<img width="1037" height="862" alt="image" src="https://github.com/user-attachments/assets/69cfab85-d842-4b9c-91ee-00802935c665" />
