import streamlit as st

st.title("Chatbot de Botpress en Streamlit")

iframe_code = """
<iframe src="https://cdn.botpress.cloud/webchat/v2.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/03/03/23/20250303230903-GASVKWSC.json"
        width="100%" height="600px" style="border:none;"></iframe>
"""

st.markdown(iframe_code, unsafe_allow_html=True)


# ///----------------------------------------------


import streamlit as st
import time
import requests
from streamlit_image_select import image_select

# ----------------------------- CONFIGURACIÓN -----------------------------

st.set_page_config(page_title="Configurador COBISA", layout="wide")

# Reemplaza con los valores de tu Botpress
BOT_ID = "58eab088-c1f5-4641-b842-e93929559b92"  # Encuéntralo en Botpress
API_KEY = "bp_pat_kf0s507mwZNLEg6pg5OXntn1lfMg7wPolt25"  # Reemplázalo con la API Key obtenida
API_URL = f"https://bots.botpress.cloud/v1/bots/58eab088-c1f5-4641-b842-e93929559b92/events"

# ----------------------------- LISTA DE IMÁGENES -----------------------------

celulas = [
    "imagenes/celulas/rotolavitll.png",
    "imagenes/celulas/zentrimix380R.png"
]

micro = [
    "imagenes/micro/micro185.png",
    "imagenes/micro/mikro200.png",
    "imagenes/micro/mikro200r.png",
    "imagenes/micro/mikro220.png",
    "imagenes/micro/mikro220r.png",
]

piso = [
    "imagenes/piso/rotana460rf.png",
    "imagenes/piso/rotixa500rs.png",
    "imagenes/piso/rotona460rc.png",
    "imagenes/piso/rotosilenta630rs.png"
]

pequenas = [
    "imagenes/pequenas/eba270.png",
    "imagenes/pequenas/eba200_200S.png",
    "imagenes/pequenas/eba200md.png",
    "imagenes/pequenas/eba280_280s.png",
    "imagenes/pequenas/haematokrit200.png"
]

angular = [
    "imagenes/angular/rotina380.png",
    "imagenes/angular/rotina380r.png",
    "imagenes/angular/rotina420.png",
    "imagenes/angular/rotina420r.png",
    "imagenes/angular/rotofix32a.png",
    "imagenes/angular/rotofix32amd.png",
    "imagenes/angular/universal320.png",
    "imagenes/angular/universal320r.png"
]

# ----------------------------- INTERFAZ -----------------------------

st.title("Configurador Inteligente COBISA")

# Selector de imagen con ajuste de tamaño
selected_image = image_select(
    label="",
    images=pequenas,
    use_container_width=False
)

# Espacio para mostrar el estado de la conversación
status_placeholder = st.empty()



iframe_code = """
<iframe src="https://cdn.botpress.cloud/webchat/v2.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/03/03/23/20250303230903-GASVKWSC.json"
        width="100%" height="600px" style="border:none;"></iframe>
"""

st.markdown(iframe_code, unsafe_allow_html=True)


# ----------------------------- FUNCIÓN PARA OBTENER MENSAJES -----------------------------

def get_botpress_messages():
    """Consulta la API de Botpress y devuelve los mensajes del chat."""
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        messages = response.json()
        return [msg["payload"]["text"] for msg in messages if "payload" in msg and "text" in msg["payload"]]
    else:
        st.error(f"Error al obtener mensajes: {response.status_code}")
        return []

# ----------------------------- MONITOREO DEL CHATBOT -----------------------------

while True:
    messages = get_botpress_messages()

    if any("EBA 280" in msg for msg in messages):
        status_placeholder.warning("⚠️ Se detectó 'EBA 280' en la conversación.")
        break  # Detiene la verificación
    else:
        status_placeholder.info("⏳ Escuchando mensajes del chatbot...")

    time.sleep(5)  # Consulta cada 5 segundos
