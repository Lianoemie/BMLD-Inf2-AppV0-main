import streamlit as st
import pandas as pd

st.title("Kalorienrechner")

st.write("Diese App wurde entwickelt, um den täglichen Kalorienverbrauch zu berechnen. Die Berechnung basiert auf dem Grundumsatz (BMR) und dem Gesamtumsatz (TDEE).")

# Überprüfe, ob die Berechnungsseite aufgerufen werden soll
if 'berechnen' not in st.session_state:
    st.session_state.berechnen = False

# Wenn der Benutzer auf den Button klickt, zur Berechnungsseite wechseln
if st.button('Zur Berechnung'):
    st.session_state.berechnen = True
    st.experimental_rerun()

# Wenn der Benutzer auf der Berechnungsseite ist
if st.session_state.berechnen:
    # Berechnungsseite (Kalorienrechner)
    st.write("Berechnen Sie Ihre täglichen Kalorien!")

"""
Diese App wurde von folgenden Personen entwickelt:
- Lia Müller (muellli6@students.zhaw.ch)
- Selina Rüdisüli (ruedisel@students.zhaw.ch)

""" 

