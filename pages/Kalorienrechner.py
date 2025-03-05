import streamlit as st

# Titel der App
st.title('Kalorienrechner')

# Eingabefelder für Alter, Gewicht und Größe
alter = st.number_input('Alter (in Jahren)', min_value=0, max_value=120, value=25, step=1)
gewicht = st.number_input('Gewicht (in kg)', min_value=30, max_value=200, value=70, step=1)
groesse = st.number_input('Größe (in cm)', min_value=100, max_value=250, value=170, step=1)

# Zeige die eingegebenen Werte
st.write(f"Alter: {alter} Jahre")
st.write(f"Gewicht: {gewicht} kg")
st.write(f"Größe: {groesse} cm")




