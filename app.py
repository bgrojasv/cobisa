import streamlit as st
from PIL import Image
import requests
import time
import json
import re 


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
    time.sleep(13)  # Pequeña pausa para permitir que el bot responda
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



def contiene_palabra(texto, palabra):
    # Normaliza el texto eliminando caracteres especiales y convirtiendo a minúsculas
    texto_normalizado = re.sub(r'[^a-zA-Z0-9 ]', '', texto).lower()
    palabra_normalizada = palabra.lower()
    return palabra_normalizada in texto_normalizado

# ------------------------------------------ APP ---------------------------------------------------------------------------
# Configuración de la página
st.set_page_config(page_title="Configurador COBISA", layout="wide")

st.title("Configurador de centrifugas inteligente de COBISA")
st.markdown("Seleccione y ajuste los parámetros para encontrar su equipo ideal utilizando Inteligencia Artificial")


st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        background-color: #006477;  /* Mantener el color del sidebar */
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    /* Ajuste para los selectbox, slider, number_input y radio buttons */
    div[data-baseweb="select"] * {
        color: black !important;
    }
    div[data-testid="stNumberInput"] input {
        color: black !important;
    }
    div[data-baseweb="slider"] * {
        color: black !important;
    }
    div[data-testid="stRadio"] * {
        color: black !important;
    }
    /* Estilo para input text con letra en gris */
    div[data-testid="stTextInput"] input {
        color: gray !important;
    }
</style>
    """,
    unsafe_allow_html=True
)

# Inicialización del estado si no existe
if "step" not in st.session_state:
    st.session_state.step = 0
if "config" not in st.session_state:
    st.session_state.config = {}

# Función para avanzar al siguiente paso sin necesidad de doble clic
def avanzar_siguiente(step, key, valor):
    st.session_state.config[key] = valor
    st.session_state.step = step
    st.rerun()  # 🔄 Fuerza un re-render inmediato

# Selección de imagen según la sección actual
if st.session_state.step == 0:
    image_path = "imagenes/main.png"  # Imagen de inicio
elif st.session_state.step == 1:
    image_path = "imagenes/main.png"
elif st.session_state.step == 2:
    image_path = "imagenes/main.png"
elif st.session_state.step == 3:
    image_path = "imagenes/main.png"
elif st.session_state.step == 4:
    image_path = "imagenes/main.png"
elif st.session_state.step == 5:
    image_path = "imagenes/main.png"
elif st.session_state.step == 6:
    image_path = "imagenes/main.png"
elif st.session_state.step == 7:
    image_path = "imagenes/main.png"
elif st.session_state.step == 8:
    image_path = "imagenes/main.png"
elif st.session_state.step == 9:
    image_path = "imagenes/main.png"
elif st.session_state.step == 10:
    image_path = None

# Cargar y mostrar la imagen actual
try:
    image = Image.open(image_path)
    st.image(image, use_container_width=True)
except Exception as e:
    print("No se pudo encontrar la imagen")
    #st.warning(f"No se pudo cargar la imagen: {image_path}")



# Sidebar para configuración
st.sidebar.title("Configuración del Equipo")
st.sidebar.divider()

# Botón para comenzar
if st.session_state.step == 0:
    if st.sidebar.button("Iniciar Configuración", key="btn_inicio",type='primary'):
        st.session_state.step = 1
        st.rerun()  # 🔄 Re-render inmediato

# Sección 1: Capacidad de Tubos
elif st.session_state.step == 1:
    st.sidebar.subheader("1. Volumen de Tubos")

    image_path = "imagenes/tubo.png" 
    tubo = Image.open(image_path)
    st.sidebar.image(tubo, width=20)

    capacidad = st.sidebar.selectbox("Seleccione", ["0,2 ml","0,5 ml","1 ml","1.5 ml","2 ml","3 ml","4 ml","5 ml","6 ml","7 ml","9 ml","10 ml","15 ml","25 ml","50 ml","85 ml","100 ml","250 ml","400 ml","450 ml"])

    if st.sidebar.button("Siguiente", key="btn_step1",type='primary'):
        avanzar_siguiente(2, "Capacidad de Tubos", capacidad)

# Sección 2: Número de tubos por rotor
elif st.session_state.step == 2:
    st.sidebar.subheader("2. Número de tubos por rotor")

    image_path = "imagenes/tubo.png" 
    tubo = Image.open(image_path)
    st.sidebar.image(tubo, width=20)

    cantidad_tubos = st.sidebar.number_input("Ingrese cantidad", min_value=1, step=1)

    if st.sidebar.button("Siguiente", key="btn_step2",type='primary'):
        avanzar_siguiente(3, "Número de Tubos", cantidad_tubos)

# Sección 3: Revoluciones por minuto (RPM)
elif st.session_state.step == 3:
    st.sidebar.subheader("3. Revoluciones por minuto (RPM)")
    velocidad = st.sidebar.slider("Seleccione RPM", min_value=3000, max_value=6000, step=500)

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        avanzar_siguiente(4, "Revoluciones por minuto", velocidad)

# Sección 4: Tipo de rotor
elif st.session_state.step == 4:
    st.sidebar.subheader("4. Tipo de rotor")

    tipo_rotor = st.sidebar.selectbox("Seleccione", ['Ángulo Fijo', 'Oscilante 4 posiciones', 'Oscilante 6 posiciones','Oscilante sin tapa'])

    if tipo_rotor == 'Ángulo Fijo':
        image_path = "imagenes/rotor/angulo_fijo.png" 
        tubo = Image.open(image_path)
        st.sidebar.image(tubo, width=150)
    if tipo_rotor == 'Oscilante 4 posiciones':
        image_path = "imagenes/rotor/oscilante4.png" 
        tubo = Image.open(image_path)
        st.sidebar.image(tubo, width=150)
    if tipo_rotor == 'Oscilante 6 posiciones':
        image_path = "imagenes/rotor/oscilante6.png" 
        tubo = Image.open(image_path)
        st.sidebar.image(tubo, width=150)
    if tipo_rotor == 'Oscilante sin tapa':
        image_path = "imagenes/rotor/oscilantesintapa.png" 
        tubo = Image.open(image_path)
        st.sidebar.image(tubo, width=150)        

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        if tipo_rotor == 'Ángulo Fijo':
            avanzar_siguiente(9, "Tipo Rotor", tipo_rotor)
        else:
            avanzar_siguiente(5, "Tipo Rotor", tipo_rotor)

import streamlit as st

# Sección 5: Vaso
if st.session_state.step == 5:
    st.sidebar.subheader("5. Tipo de vaso")
    tipo_vaso = st.sidebar.radio("Seleccione", ["Vaso sin tapa", "Vaso mayor capacidad", "Vaso con tapa", "Vaso rectangular"])

    if st.sidebar.button("Siguiente", key="btn_step5", type='primary'):
        avanzar_siguiente(6, "Tipo de vaso", tipo_vaso)

# Sección 6: Tapas
elif st.session_state.step == 6:
    st.sidebar.subheader("6. Tipo de tapa")
    tipo_tapa = st.sidebar.selectbox("Seleccione", ['Para vaso pequeño', 'Para vaso mediano', 'Para vaso rectangular'])

    if st.sidebar.button("Siguiente", key="btn_step6", type='primary'):
        avanzar_siguiente(7, "Tipo de Tapa", tipo_tapa)

# Sección 7: Insertos
elif st.session_state.step == 7:
    st.sidebar.subheader("7. Tipo de inserto")
    tipo_inserto = st.sidebar.selectbox("Seleccione", ['Vaso cilíndrico', 'Vaso rectangular', 'Vaso para rotor'])

    if st.sidebar.button("Siguiente", key="btn_step7", type='primary'):
        avanzar_siguiente(8, "Tipo de inserto", tipo_inserto[0])  # Se guarda solo un valor

# Sección 8: Refrigeración
elif st.session_state.step == 8:
    st.sidebar.subheader("8. Refrigeración")
    refrigeracion = st.sidebar.selectbox("Seleccione", ['No', 'Sí'])

    if st.sidebar.button("Siguiente", key="btn_step8", type='primary'):
        avanzar_siguiente(9, "Refrigeración", refrigeracion)


elif st.session_state.step == 9:
    nombre = st.sidebar.text_input("Nombre del solicitante")
    organizacion = st.sidebar.text_input("Nombre de la organizacion")
    telfono = st.sidebar.text_input("Telefono")
    correo = st.sidebar.text_input("correo electrónico")

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        avanzar_siguiente(10, "", "")


# Mensaje final tras completar todas las secciones
if st.session_state.step == 10:
    st.sidebar.success("Configuración completada")

    # Construir el string con la configuración seleccionada
    config_str = ", ".join([f"{key}: {value}" for key, value in st.session_state.config.items()])
    
    # Guardar en una variable
    st.session_state.config_summary = config_str

    st.write(config_str)
    
    # Obtener respuesta del bot
    with st.spinner("Estamos buscando tu centrífuga ideal...", show_time=True):
        respuesta = botpress_interaction(config_str)


    descripcion_modelo_centrifuga = respuesta
    # Mostrar la descripción específica en Streamlit
    #st.subheader("Descripción del Modelo de Centrífuga:")
    st.subheader("La centrifuga que mejor se adapta a tu necesidad es:")
    st.write(descripcion_modelo_centrifuga)

    # Pequenas
    if contiene_palabra(descripcion_modelo_centrifuga, "EBA 200"):
        #st.write("La EBA 200 es una centrífuga práctica y compacta para muestras de pequeño tamaño. Incluye un rotor de ángulo fijo de 8 posiciones para alojar tubos estándar de sangre y orina de hasta 15 ml de capacidad.")
        st.image(Image.open("imagenes/pequenas/eba200.png"), use_container_width=True)
    elif contiene_palabra(descripcion_modelo_centrifuga, "EBA 270"):
        #st.write("La EBA 270 es una centrífuga pequeña con un rotor oscilante que se ha desarrollado específicamente para su uso en entornos clínicos. Puede centrifugar tubos de sangre y tubos de orina de hasta 15 ml de volumen a una velocidad máxima de 4000 RPM / 2254 RCF. Su rotor de 90° es ideal para centrifugar tubos de sangre que contienen un gel separador.")
        st.image(Image.open("imagenes/pequenas/eba270.png"), use_container_width=True)
    elif contiene_palabra(descripcion_modelo_centrifuga, "EBA 280"):
        st.write("EBA 200")
    elif contiene_palabra(descripcion_modelo_centrifuga, "HAEMATOKRIT 200"):
        st.write("HAEMATOKRIT 200")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTINA 380"):
        st.write("ROTINA")
    # Micro
    elif contiene_palabra(descripcion_modelo_centrifuga, "MIKRO 185"):
        st.write("MIKRO 185")
    elif contiene_palabra(descripcion_modelo_centrifuga, "MIKRO 200"):
        st.write("MIKRO 200")
    elif contiene_palabra(descripcion_modelo_centrifuga, "MIKRO 220"):
        st.write("MIKRO 220")
    #Mesa
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTOFIX 46"):
            st.write("ROTOFIX 46")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTANA 460"):
        st.write("ROTANA 460")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTINA 420"):
        st.write("ROTINA 420")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTINA 380"):
        st.write("ROTINA 380")
    elif contiene_palabra(descripcion_modelo_centrifuga, "UNIVERSAL 320"):
        st.write("UNIVERSAL 320")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTOFIX 32"):
        st.write("ROTOFIX 32")
    #PISO
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTANA 460"):
        st.write("ROTANA 460")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTIXA 500"):
        st.write("ROTIXA 500")
    elif contiene_palabra(descripcion_modelo_centrifuga, "HettInfo"):
        st.write("HettInfo")
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTO SILENTA 630"):
        st.write("ROTO SILENTA 630")
    # celulas
    elif contiene_palabra(descripcion_modelo_centrifuga, "ROTOLAVIT"):
        st.write("ROTOLAVIT")
    # Dual
    elif contiene_palabra(descripcion_modelo_centrifuga, "ZentriMix 380"):
        st.write("ZentriMix 380")

st.write("Nuestros asesores se pondrán en contacto contigo muy pronto.")
 