import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Simulador de Laboratorio", layout="wide")

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

# Botón para comenzar
if st.session_state.step == 0:
    if st.sidebar.button("Iniciar Configuración", key="btn_inicio"):
        st.session_state.step = 1
        st.rerun()  # 🔄 Re-render inmediato

# Sección 1: Capacidad de Tubos
elif st.session_state.step == 1:
    st.sidebar.subheader("1. Capacidad de Tubos")
    capacidad = st.sidebar.selectbox("Seleccione", ["0,2 ml", "0,5 ml", "1 ml", "1.5 ml", "2 ml"])

    if st.sidebar.button("Siguiente", key="btn_step1"):
        avanzar_siguiente(2, "Capacidad de Tubos", capacidad)

# Sección 2: Número de tubos por rotor
elif st.session_state.step == 2:
    st.sidebar.subheader("2. Número de tubos por rotor")
    cantidad_tubos = st.sidebar.number_input("Ingrese cantidad", min_value=1, step=1)

    if st.sidebar.button("Siguiente", key="btn_step2"):
        avanzar_siguiente(3, "Número de Tubos", cantidad_tubos)

# Sección 3: Revoluciones por minuto (RPM)
elif st.session_state.step == 3:
    st.sidebar.subheader("3. Revoluciones por minuto (RPM)")
    velocidad = st.sidebar.slider("Seleccione RPM", min_value=3000, max_value=6000, step=500)

    if st.sidebar.button("Finalizar", key="btn_step3"):
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






'''
Será un asistente que funcionaras como motor de recomendación para COBISA, una empresa que se dedica a la distribución de equipo médico.  Dentro de tu base de conocimiento tienes varios documentos pdf. El usuario te dirá como entrada: Capacidad de Tubos,
Número de Tubos,
Revoluciones por minuto,
Tipo Rotor,
Tipo de vaso,
Tipo de Tapa,
Tipo de inserto,
Refrigeracion. Y debes buscar en los documentos pdf y recomendar el número de parte de cada centrífuga y los accesorios seleccionados. Debes retornar el número de referencia o número de parte de la centrifuga seleccionada y cada configuración o accesorio solicitado. Debes buscar el número de recipiente y de adaptador que se ajuste a la solicitud del usuario. Filtros: No mostrar opciones que no calcen al 100% con la solicitud Que tipos de rotores posee las centrífugas. Que tipos de rotores, tamaño de tubos, volumen de cada tubo y cantidad de tubos posee todos los modelos de centrifuga pequeñas, de mesa y de piso de Hettich.
Que especialidad tiene cada centrífuga Hettich. Quiero todos los modelos de centrífugas. Que tipos de centrífugas tiene Hettich. Que cantidad de tubos por rotor y volumen de tubos existen en las centrífugas de Hettich. Analiza los diferentes volúmenes de tubos compatibles con cada centrífuga. Analiza los diferentes rotores compatibles con cada centrífuga de Hettich. Analiza la velocidad máxima y el RCF de cada centrífuga.



el formato de salida debe ser el siguiente:


{
  "Capacidad de Tubos": {
    "descripcion": capacidad elegida y retorna las dimensiones del tubo que se ajuste a lo requerido,
    "codigo": retornar el codigo o numero de referencia de los tubos que funcionen
  },
  "Número de Tubos": {
    "descripcion": cantidad de tubos elegidos por el usuario,
    "codigo": retornar el codigo o numero de referencia de los tubos que funcionen
  },
  "Tipo de Rotor": {
    "descripcion": tipo de rotor elegido por el usuario,
    "codigo": retornar el codigo o numero de referencia del rotor que funcione
  },
  "Tipo de Vaso": {
    "descripcion": tipo de vaso elegido
    "codigo": retornar el codigo o numero de referencia del vaso que funcione
  },
  "Tipo de Tapa": {
    "descripcion": tipo de tapa elegido
    "codigo": retornar el codigo o numero de referencia de la tapa que funcione
  },
  "Tipo de Inserto": {
    "descripcion": tipo de inserto elegido,
    "codigo": retornar el codigo o numero de referencia del iserto que funcione
  },
  "Modelo de Centrifuga": {
    "descripcion": Analiza las variables y retorna el nombre de la centrifuga que mas se adapte (SOLO EL NOMBRE DEL MODELO, ejemplo EBA 200, EBA 280),
    "codigo": retornar el codigo o numero de referencia de la centrifuga que funcione
  }
}

en caso de que no coincida algo agregar "no encontrado" en el campo del json.
Devuelve como resultado el json solamente, no agregues ningun texto adicional

'''