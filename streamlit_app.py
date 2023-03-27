import streamlit as st
import requests
import openai
import os

# Accedemos a la clave de API de OpenAI a través de una variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

def obtener_respuesta(pregunta):
    url = 'https://api.perplexity.ai/v1/dialogue'

    headers = {
        'Authorization': f'Bearer {clave_api}',
        'Content-Type': 'application/json',
    }

    data = {
        'input': {
            'text': pregunta,
            'domain': 'es',  # Establecer el dominio del lenguaje en español
        },
        'context': {
            'knowledge': [
                {
                    'text': 'Este chatbot responde preguntas sobre la legislación guatemalteca.',
                }
            ]
        }
    }

    respuesta = requests.post(url, json=data, headers=headers)

    if respuesta.status_code == 200:
        return respuesta.json()['output']['text']
    else:
        return "Lo siento, no pude obtener una respuesta."

st.title("Chatbot de Legislación Guatemalteca")
st.write("Escribe tu pregunta sobre la legislación guatemaltealteca y el chatbot intentará responderla.")

pregunta_usuario = st.text_input("Escribe tu pregunta aquí:")

if st.button("Enviar pregunta"):
    if pregunta_usuario:
        respuesta_chatbot = obtener_respuesta(pregunta_usuario)
    st.write(f"Respuesta del chatbot: {respuesta_chatbot}")
    else:
        st.warning("Por favor, ingresa una pregunta antes de presionar el botón.") 
