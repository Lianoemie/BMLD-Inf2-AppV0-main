import streamlit as st

# Titel der App
st.title('Kalorienrechner')

# Geschlechtsauswahl mit Radio-Button
geschlecht = st.radio("Wählen Sie Ihr Geschlecht:", ('Männlich', 'Weiblich'))

# Eingabefelder für Alter, Gewicht und Größe
alter = st.number_input('Alter (in Jahren)', min_value=0, max_value=120, value=25, step=1)
gewicht = st.number_input('Gewicht (in kg)', min_value=30, max_value=200, value=70, step=1)
groesse = st.number_input('Größe (in cm)', min_value=100, max_value=250, value=170, step=1)

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
if geschlecht:
    # Nur berechnen, wenn Alter, Gewicht und Größe eingegeben wurden
    if alter > 0 and gewicht > 0 and groesse > 0:
        # Button zum Berechnen
        if st.button('Berechnen'):
            bmr = berechne_bmr(gewicht, groesse, alter, geschlecht=geschlecht)

            # TDEE (Gesamtumsatz) basierend auf Aktivitätsniveau
            tdee = berechne_tdee(bmr, aktivitaet)

            # Zeige den Gesamtumsatz (TDEE) an
            st.write(f"Der geschätzte Kalorienverbrauch pro Tag beträgt: {tdee:.2f} kcal")
    else:
        st.warning("Bitte stellen Sie sicher, dass Sie alle Eingabefelder korrekt ausgefüllt haben.")
