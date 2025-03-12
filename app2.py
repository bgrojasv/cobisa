import streamlit as st
from streamlit_image_select import image_select

st.set_page_config(page_title="Configurador COBISA", layout="wide")

# Lista de imágenes (rutas locales)
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


#----------------------------- PRINCIPAL -----------------------------
st.title("Configurador Inteligente COBISA")

# Selector de imagen con ajuste de tamaño
selected_image = image_select(
    label="",
    images=pequenas,
    use_container_width=False  # Asegura que el contenedor ocupe el ancho
)

iframe_code = """
<iframe src="https://cdn.botpress.cloud/webchat/v2.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/03/03/23/20250303230903-GASVKWSC.json"
        width="100%" height="600px" style="border:none;"></iframe>
"""

st.markdown(iframe_code, unsafe_allow_html=True)
