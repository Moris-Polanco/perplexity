import streamlit as st
import requests
import openai
import os

# Accedemos a la clave de API de OpenAI a través de una variable de entorno
openai.api_key = os.environ.get("OPENAI_API_KEY")

def obtener_respuesta(pregunta):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Este chatbot responde preguntas sobre la legislación guatemalteca. Pregunta: {pregunta}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return "Lo siento, no pude obtener una respuesta."

st.title("Chatbot de Legislación Guatemalteca")
st.write("Escribe tu pregunta sobre la legislación guatemalteca y el chatbot intentará responderla.")
pregunta_usuario = st.text_input("Escribe tu pregunta aquí:")

if st.button("Enviar pregunta"):
    if pregunta_usuario:
        respuesta_chatbot = obtener_respuesta(pregunta_usuario)
        st.write(f"Respuesta del chatbot: {respuesta_chatbot}")
    else:
        st.warning("Por favor, ingresa una pregunta antes de presionar el botón.")
