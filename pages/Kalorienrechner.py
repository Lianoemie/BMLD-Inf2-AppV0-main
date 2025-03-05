import streamlit as st

# Titel der App
st.title('Kalorienrechner')

# Eingabefeld für Geschlecht
geschlecht = st.radio(
    'Wählen Sie Ihr Geschlecht:',
    ('Männlich', 'Weiblich')
)

# Eingabefelder für Alter, Gewicht und Größe
alter = st.number_input('Alter (in Jahren)', min_value=0, max_value=120, value=25, step=1)
gewicht = st.number_input('Gewicht (in kg)', min_value=30, max_value=200, value=70, step=1)
groesse = st.number_input('Größe (in cm)', min_value=100, max_value=250, value=170, step=1)

# Auswahl des Aktivitätsniveaus
aktivitaet = st.radio(
    'Wählen Sie Ihr Aktivitätsniveau aus:',
    ('Sitzend', 'Stehend', 'Laufend')
)

# BMR-Berechnung (Männer und Frauen)
def berechne_bmr(gewicht, groesse, alter, geschlecht='männlich'):
    if geschlecht == 'Männlich':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:  # weiblich
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)
    return bmr

# Aktivitätsfaktor je nach Auswahl
def berechne_tdee(bmr, aktivitaet):
    if aktivitaet == 'Sitzend':
        aktivitaetsfaktor = 1.2
    elif aktivitaet == 'Stehend':
        aktivitaetsfaktor = 1.55
    else:  # Laufend
        aktivitaetsfaktor = 1.9
    return bmr * aktivitaetsfaktor

# Berechnung des BMR (Grundumsatz)
bmr = berechne_bmr(gewicht, groesse, alter, geschlecht=geschlecht)

# TDEE (Gesamtumsatz) basierend auf Aktivitätsniveau
tdee = berechne_tdee(bmr, aktivitaet)

# Zeige die Eingabewerte
st.write(f"Geschlecht: {geschlecht}")
st.write(f"Alter: {alter} Jahre")
st.write(f"Gewicht: {gewicht} kg")
st.write(f"Größe: {groesse} cm")
st.write(f"Aktivitätsniveau: {aktivitaet}")

# Zeige den Gesamtumsatz (TDEE) an
st.write(f"Der geschätzte Kalorienverbrauch pro Tag beträgt: {tdee:.2f} kcal")
