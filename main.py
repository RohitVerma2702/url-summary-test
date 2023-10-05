import streamlit as st
import llm_tutorial

st.title("Controls Generator")

with st.sidebar:
    risk = st.text_input("Mention risk name...", value="")
    clicked = st.button("Submit")

if clicked:
    response = llm_tutorial.generate_controls(risk)

    st.header(risk)
    controls = response["controls"]
    st.write("Controls to be followed:")
    st.write(controls)
    # for item in controls:
    #     st.write(item)
