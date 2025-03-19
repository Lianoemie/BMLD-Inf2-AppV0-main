import streamlit as st

from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

# CSS, um andere Stile zu ändern
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #1e2a8a; /* Dunkleres Blau für den Button */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# Titel der App
st.title('Kalorienrechner')

# Geschlechtsauswahl mit Radio-Button
geschlecht = st.radio("Wählen Sie Ihr Geschlecht:", ('Männlich', 'Weiblich'))

# Eingabefelder für Alter, Gewicht und Größe mit Standardwert None (Zwang zur Eingabe)
alter = st.number_input('Alter (in Jahren)', min_value=1, max_value=120, value=None, step=1)
gewicht = st.number_input('Gewicht (in kg)', min_value=9, max_value=200, value=None, step=1)
groesse = st.number_input('Größe (in cm)', min_value=80, max_value=250, value=None, step=1)

# Auswahl des Aktivitätsniveaus
aktivitaet = st.radio(
    'Wählen Sie Ihr Aktivitätsniveau aus:',
    ('Vorwiegend sitzend (Bürojob, Studium)', 'Vorwiegend stehend (Verkauf, Handwerk)', 'Vorwiegend laufend (Handwerker, Sportler)')
)

# BMR-Berechnung (Männer und Frauen)
def berechne_bmr(gewicht, groesse, alter, geschlecht='Männlich'):
    if geschlecht == 'Männlich':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:  # weiblich
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)
    return bmr

# Aktivitätsfaktor je nach Auswahl
def berechne_tdee(bmr, aktivitaet):
    if aktivitaet == 'Vorwiegend sitzend (Bürojob, Studium)':
        aktivitaetsfaktor = 1.2
    elif aktivitaet == 'Vorwiegend stehend (Verkauf, Handwerk)':
        aktivitaetsfaktor = 1.55
    else:  # Vorwiegend laufend (Handwerker, Sportler)
        aktivitaetsfaktor = 1.9
    return bmr * aktivitaetsfaktor

# Berechnung des BMR (Grundumsatz), falls Geschlecht ausgewählt
if st.button('Berechnen'):
    # Überprüfen, ob alle Eingabefelder ausgefüllt wurden (nicht None oder 0)
    if alter and gewicht and groesse:
        bmr = berechne_bmr(gewicht, groesse, alter, geschlecht=geschlecht)

        # TDEE (Gesamtumsatz) basierend auf Aktivitätsniveau
        tdee = berechne_tdee(bmr, aktivitaet)

        # Zeige den Gesamtumsatz (TDEE) an
        st.write(f"Der geschätzte Kalorienverbrauch pro Tag beträgt: {tdee:.2f} kcal")
    else:
        st.warning("Bitte stellen Sie sicher, dass Sie alle Eingabefelder korrekt ausgefüllt haben.")
