# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === Kalorienverbrauch Grafik ===
import streamlit as st

st.title('Kalorienverbrauch Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Kalorienverbrauchs-Daten vorhanden. Berechnen Sie Ihren Kalorienverbrauch auf der Startseite.')
    st.stop()

# Gewicht über die Zeit
st.line_chart(data=data_df.set_index('timestamp')['Gewicht in (kg)'], 
                use_container_width=True)
st.caption('Gewicht über Zeit (in kg)')

# Grösse über die Zeit 
st.line_chart(data=data_df.set_index('timestamp')['Grösse in (cm)'],
                use_container_width=True)
st.caption('Grösse über Zeit (in cm)')

# Kaloerienverbrauch über die Zeit
st.line_chart(data=data_df.set_index('timestamp')['TDEE'],
                use_container_width=True)
st.caption('Kalorienverbrauch über Zeit (in kcal)')
