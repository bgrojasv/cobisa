import streamlit as st
import requests
import time

# Función para interactuar con Botpress
def botpress_interaction(message_text: str) -> str:
    webhook_id = "59bb142c-f3ce-4740-987c-2e87218697a3"
    user_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InVzZXJfMDFKUDM1Q1ZDMVdGSjBZWlEwNFYyRVJGRVIiLCJpYXQiOjE3NDE3MTU1NjV9.ySADnd4Qlp9xei5dXBCNM9LNWAWQlD-QX1adG06PWTw"
    base_url = f"https://chat.botpress.cloud/{webhook_id}"
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-user-key": user_key
    }

    # Crear conversación
    conversation_url = f"{base_url}/conversations"
    payload = {"id": "1"}
    response = requests.post(conversation_url, json=payload, headers=headers, verify=False)
    
    if response.status_code != 200:
        return "Error al crear la conversación"

    conversation_id = "1"

    # Enviar mensaje
    message_url = f"{base_url}/messages"
    message_data = {
        "conversationId": conversation_id,
        "payload": {
            "type": "text",
            "text": message_text
        }
    }
    response = requests.post(message_url, headers=headers, json=message_data, verify=False)
    
    if response.status_code != 200:
        return "Error al enviar el mensaje"

    # Leer mensajes
    time.sleep(2)  # Pequeña pausa para permitir que el bot responda
    messages_url = f"{base_url}/conversations/{conversation_id}/messages"
    response = requests.get(messages_url, headers=headers, verify=False)

    if response.status_code != 200:
        return "Error al obtener los mensajes"

    # Verificar la respuesta obtenida
    messages = response.json().get("messages", [])
    print("Mensajes obtenidos:", messages)  # Depuración

    payload_text = "No hay respuesta del bot."

    if messages:
        for msg in messages:
            if "payload" in msg and "text" in msg["payload"]:
                payload_text = msg["payload"]["text"]
                break  # Tomar la primera respuesta válida del bot

    # Borrar conversación
    delete_url = f"{base_url}/conversations/{conversation_id}"
    response = requests.delete(delete_url, headers=headers, verify=False)

    return payload_text  # Retorna la respuesta real del bot

# Configuración de Streamlit
st.set_page_config(page_title="Chat con Botpress", layout="centered")

st.title("🤖 Chat con Botpress")

# Historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial de conversación
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input del usuario
user_input = st.chat_input("Escribe un mensaje...")

if user_input:
    # Mostrar mensaje del usuario en la UI
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Obtener respuesta del bot
    bot_response = botpress_interaction(user_input)

    # Mostrar respuesta del bot en la UI
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
