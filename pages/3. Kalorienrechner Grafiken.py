# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

import streamlit as st
import pandas as pd

st.title('Kalorienverbrauch Verlauf')

data_df = st.session_state['data_df']

# Überprüfen, ob das DataFrame leer ist
if data_df.empty:
    st.info('Keine Kalorienverbrauchs-Daten vorhanden. Berechnen Sie Ihren Kalorienverbrauch auf der Startseite.')
    st.stop()

# Konvertiere die 'timestamp' Spalte in datetime, falls noch nicht geschehen
data_df['timestamp'] = pd.to_datetime(data_df['timestamp'])

# Aggregiere auf tägliche Basis, indem wir den Index auf den Tag setzen
data_df['date'] = data_df['timestamp'].dt.date
daily_data = data_df.groupby('date').agg({
    'Gewicht': 'last',  # Nimm das letzte Gewicht des Tages
    'Grösse': 'last',    # Nimm die letzte Grösse des Tages
    'TDEE': 'last'      # Nimm den letzten Kalorienverbrauch des Tages
}).reset_index()

# Gewicht über die Zeit
st.line_chart(data=daily_data.set_index('date')['Gewicht'], use_container_width=True)
st.caption('Gewicht über Zeit (in kg)')

# Grösse über die Zeit
st.line_chart(data=daily_data.set_index('date')['Grösse'], use_container_width=True)
st.caption('Grösse über Zeit (in cm)')

# Kalorienverbrauch über die Zeit
st.line_chart(data=daily_data.set_index('date')['TDEE'], use_container_width=True)
st.caption('Kalorienverbrauch über Zeit (in kcal)')

