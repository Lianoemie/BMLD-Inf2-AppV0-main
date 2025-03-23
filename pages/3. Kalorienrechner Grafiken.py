# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

import streamlit as st

st.title('Kalorienverbrauch Verlauf')

data_df = st.session_state['data_df']

# Debugging: Verfügbare Spalten anzeigen
st.write("Spalten in data_df:", data_df.columns.tolist())

if data_df.empty:
    st.info('Keine Kalorienverbrauchs-Daten vorhanden. Berechnen Sie Ihren Kalorienverbrauch auf der Startseite.')
    st.stop()

# Gewicht über die Zeit
if 'Gewicht' in data_df.columns:
    st.line_chart(data=data_df.set_index('timestamp')['Gewicht'], use_container_width=True)
    st.caption('Gewicht über Zeit (in kg)')
else:
    st.warning("Spalte 'Gewicht' nicht gefunden.")

# Größe über die Zeit (Korrektur: 'Größe' statt 'Grösse')
if 'Größe' in data_df.columns:
    st.line_chart(data=data_df.set_index('timestamp')['Größe'], use_container_width=True)
    st.caption('Größe über Zeit (in cm)')
else:
    st.warning("Spalte 'Größe' nicht gefunden.")

# Kalorienverbrauch über die Zeit
if 'TDEE' in data_df.columns:
    st.line_chart(data=data_df.set_index('timestamp')['TDEE'], use_container_width=True)
    st.caption('Kalorienverbrauch über Zeit (in kcal)')
else:
    st.warning("Spalte 'TDEE' nicht gefunden.")
