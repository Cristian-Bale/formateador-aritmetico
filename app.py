
import streamlit as st
from arithmetic_arranger import arithmetic_arranger 


st.set_page_config(page_title="Formateador Aritmético", page_icon="🔢")

st.title("🔢 Formateador Aritmético")

st.write("Bienvenido al formateador de problemas aritméticos. Ingresá sumas o restas, una por línea.")


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