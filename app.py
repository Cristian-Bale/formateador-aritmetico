
import streamlit as st
from arithmetic_arranger import arithmetic_arranger 


st.set_page_config(page_title="¡Organizador de Operaciones Matemáticas!", page_icon="🔢")

st.title("🔢 ¡Organizador de Operaciones Matemáticas!")

st.write("""
¡Hola! Esta es una pequeña herramienta que creé para ayudarte a **organizar y ver de forma clara sumas y restas**.

Simplemente ingresa una o varias operaciones (una por línea) en el cuadro de abajo, por ejemplo:
`32 + 698`
`123 - 45`

Luego, haz clic en "Formatear Problemas" y verás cómo los números se alinean perfectamente, ¡como en una hoja de cálculo! También puedes elegir ver las respuestas.
Reglas: Máximo 4 Dígitos""")


problems_example = "32 + 698\n3801 - 2\n45 + 43\n123 + 49"
problems_input = st.text_area("Ingresa los problemas aritméticos (uno por línea):", problems_example, height=180)


col1, col2 = st.columns(2)

with col1:
    show_answers = st.checkbox("Mostrar respuestas")

with col2:
    process_button = st.button("Formatear Problemas")

if process_button: 
    problems_list = [p.strip() for p in problems_input.split('\n') if p.strip()]

    if not problems_list:
        st.warning("Por favor, ingresa al menos un problema para formatear.")
    else:
        result = arithmetic_arranger(problems_list, show_answers) 

        if result.startswith('Error'):
            st.error(f"**¡Error al procesar!**\n\n{result}") 
        else:
            st.success("¡Problemas formateados correctamente!") 
            st.code(result, language='text') 

st.markdown("---")
st.write("Proyecto realizado para FreeCodeCamp - Desarrollado por Cristian Duran.")