import streamlit as st
import pandas as pd

st.title("Kalorienrechner")

st.write("Diese App wurde entwickelt, um den täglichen Kalorienverbrauch zu berechnen. Die Berechnung basiert auf dem Grundumsatz (BMR) und dem Gesamtumsatz (TDEE).")
# Auswahl der Seite
page = st.radio("Wählen Sie eine Seite:", ["Startseite", "Berechnung"])

if page == "Startseite":
    # Startseite mit einem Button, um zur Berechnungsseite zu navigieren
    st.write("Willkommen zum Kalorienrechner!")
    
    if st.button('Zur Berechnung'):
        # Seite wechseln (Durch Neuladen mit einer neuen Auswahl im Radio-Button)
        st.session_state.page = 'Berechnung'
        st.experimental_rerun()

elif page == "Berechnung":
    # Berechnungsseite (Kalorienrechner)
    st.write("Berechnen Sie Ihre täglichen Kalorien!")
"""
Diese App wurde von folgenden Personen entwickelt:
- Lia Müller (muellli6@students.zhaw.ch)
- Selina Rüdisüli (ruedisel@students.zhaw.ch)

""" 

