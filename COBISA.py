import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Simulador de Laboratorio", layout="wide")

# Sidebar para configuración
st.sidebar.title("Configuración del Equipo")
st.sidebar.divider()
st.sidebar.subheader("1. Capacidad de Tubos")
capacidad = st.sidebar.selectbox("Seleccione", ["0,2 ml","0,5 ml","1 ml","1.5 ml","2 ml","3 ml","4 ml","5 ml","6 ml","7 ml","9 ml","15 ml","25 ml","50 ml","85 ml","100 ml","250 ml","400 ml","450 ml"])
st.sidebar.divider()

st.sidebar.subheader("2. Número de tubos por rotor")
cantidad_tubos = st.sidebar.number_input("", step=1)
st.sidebar.divider()


st.sidebar.subheader("3. Revoluciones por minuto (RPM)")

velocidad = st.sidebar.slider("", min_value=3000, max_value=6000, step=500)
st.sidebar.divider()



tipo_tapon = st.sidebar.radio("Tipo de Tapón", ["Rosca", "Presión", "Sellado"])

# Sección de controles principales
st.title("Configurador Inteligente de COBISA")
st.markdown("Seleccione y ajuste los parámetros para encontrar su equipo ideal")

# Cargar la imagen de referencia
image_path = "imagenes/main.png" 
image = Image.open(image_path)
st.image(image, caption="Interfaz de simulación", use_container_width=True)


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Iniciar Simulación"):
        st.success("Simulación en marcha...")
with col2:
    if st.button("Pausar Simulación"):
        st.warning("Simulación pausada")
with col3:
    if st.button("Detener Simulación"):
        st.error("Simulación detenida")

# Resultados simulados
st.subheader("Datos de la Simulación")
st.write(f"**Capacidad seleccionada:** {capacidad}")
st.write(f"**Velocidad de rotación:** {velocidad} RPM")
st.write(f"**Tipo de tapón:** {tipo_tapon}")

st.progress(velocidad / 15000)  # Barra de progreso en función de la velocidad














































import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Simulador de Laboratorio", layout="wide")

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
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar para configuración
st.sidebar.title("Configuración del Equipo")
st.sidebar.divider()
st.sidebar.subheader("1. Capacidad de Tubos")

image_path = "imagenes/tubo.png" 
tubo = Image.open(image_path)
st.sidebar.image(tubo, width=20)


capacidad = st.sidebar.selectbox("Seleccione", ["0,2 ml","0,5 ml","1 ml","1.5 ml","2 ml","3 ml","4 ml","5 ml","6 ml","7 ml","9 ml","15 ml","25 ml","50 ml","85 ml","100 ml","250 ml","400 ml","450 ml"])
st.sidebar.divider()

st.sidebar.subheader("2. Número de tubos por rotor")
cantidad_tubos = st.sidebar.number_input("", step=1)
st.sidebar.divider()


st.sidebar.subheader("3. Revoluciones por minuto (RPM)")

velocidad = st.sidebar.slider("", min_value=3000, max_value=6000, step=500)
st.sidebar.divider()



tipo_tapon = st.sidebar.radio("Tipo de Tapón", ["Rosca", "Presión", "Sellado"])

# Sección de controles principales
st.title("Configurador de centrifugas inteligente de COBISA")
st.markdown("Seleccione y ajuste los parámetros para encontrar su equipo ideal utilizando Inteligencia Artificial")

# Cargar la imagen de referencia
image_path = "imagenes/main.png" 
image = Image.open(image_path)
st.image(image, caption="Interfaz de simulación", use_container_width=True)



































import streamlit as st
from PIL import Image

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

# Cargar y mostrar la imagen actual
try:
    image = Image.open(image_path)
    st.image(image, use_container_width=True)
except Exception as e:
    st.warning(f"No se pudo cargar la imagen: {image_path}")



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

    capacidad = st.sidebar.selectbox("Seleccione", ["0,2 ml","0,5 ml","1 ml","1.5 ml","2 ml","3 ml","4 ml","5 ml","6 ml","7 ml","9 ml","15 ml","25 ml","50 ml","85 ml","100 ml","250 ml","400 ml","450 ml"])

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
        avanzar_siguiente(4, "Tipo de rotor", velocidad)

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
        avanzar_siguiente(5, "Velocidad (RPM)", tipo_rotor)

# Sección 5: Vaso
elif st.session_state.step == 5:
    st.sidebar.subheader("5. Tipo de vaso")
    tipo_rotor = st.sidebar.selectbox("Seleccione", ["Vaso sin tapa","Vaso mayor capacidad","Vaso con tapa","Vaso rectangular"])

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        avanzar_siguiente(6, "Tapas", tipo_rotor)

# Sección 6: Tapas
elif st.session_state.step == 6:
    st.sidebar.subheader("6. Tipo de tapa")
    tipo_rotor = st.sidebar.selectbox("Seleccione", ['Para vaso pequeño','Para vaso mediano','Para vaso rectangular'])

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        avanzar_siguiente(7, "Tapas", tipo_rotor)


# Sección 7: Tapas
elif st.session_state.step == 7:
    st.sidebar.subheader("7. Tipo de inserto")
    tipo_rotor = st.sidebar.selectbox("Seleccione", ['Si','No'])

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        avanzar_siguiente(8, "Tapas", tipo_rotor)


# Sección 6: Tapas
elif st.session_state.step == 8:
    st.sidebar.subheader("8. Refrigeración")
    tipo_rotor = st.sidebar.selectbox("Seleccione", ['Si','No'])

    if st.sidebar.button("Siguiente", key="btn_step3",type='primary'):
        avanzar_siguiente(9, "Tapas", tipo_rotor)


# Mensaje final tras completar todas las secciones
if st.session_state.step == 9:
    st.sidebar.success("Configuración completada 🎉")




































import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Simulador de Laboratorio", layout="wide")

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
    st.sidebar.subheader("1. Capacidad de Tubos")

    image_path = "imagenes/tubo.png" 
    tubo = Image.open(image_path)
    st.sidebar.image(tubo, width=20)


    capacidad = st.sidebar.selectbox("Seleccione", ["0,2 ml", "0,5 ml", "1 ml", "1.5 ml", "2 ml"])

    if st.sidebar.button("Siguiente", key="btn_step1",type='primary'):
        avanzar_siguiente(2, "Capacidad de Tubos", capacidad)

# Sección 2: Número de tubos por rotor
elif st.session_state.step == 2:
    st.sidebar.subheader("2. Número de tubos por rotor")

    image_path = "imagenes/tubo.png" 
    image = Image.open(image_path)
    st.image(image, use_container_width=True)


    cantidad_tubos = st.sidebar.number_input("Ingrese cantidad", min_value=1, step=1)

    if st.sidebar.button("Siguiente", key="btn_step2",type='primary'):
        avanzar_siguiente(3, "Número de Tubos", cantidad_tubos)

# Sección 3: Revoluciones por minuto (RPM)
elif st.session_state.step == 3:
    st.sidebar.subheader("3. Revoluciones por minuto (RPM)")
    velocidad = st.sidebar.slider("Seleccione RPM", min_value=3000, max_value=6000, step=500)

    if st.sidebar.button("Finalizar", key="btn_step3",type='primary'):
        avanzar_siguiente(4, "Velocidad (RPM)", velocidad)

# Mostrar SOLO la configuración actual en la parte inferior
st.sidebar.divider()
st.sidebar.subheader("Configuración Actual")
ultima_config = list(st.session_state.config.keys())[-1] if st.session_state.config else None
if ultima_config:
    st.sidebar.write(f"**{ultima_config}:** {st.session_state.config[ultima_config]}")

# Mensaje final tras completar todas las secciones
if st.session_state.step == 4:
    st.sidebar.success("Configuración completada 🎉")



# Sección de controles principales
st.title("Configurador de centrifugas inteligente de COBISA")
st.markdown("Seleccione y ajuste los parámetros para encontrar su equipo ideal utilizando Inteligencia Artificial")

# MAIN
image_path = "imagenes/main.png" 
image = Image.open(image_path)
st.image(image, use_container_width=True)
