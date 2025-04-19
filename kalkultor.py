import streamlit as st

st.title("Kalkulator BMI")

visina = st.number_input("Vnesi višino (v cm):", 150, 220)
tezina = st.number_input("Vnesi težo (v kg):", 40, 150)

if st.button("Izračunaj"):
    bmi = tezina / ((visina / 100) ** 2)
    st.write(f"Tvoj BMI je: {bmi:.2f}")
