# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

st.title('Täglicher Kalorienverbrauch')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Kalorienverbrauchs-Daten vorhanden. Berechnen Sie Ihren täglichen Kalorienverbrauch auf der Startseite.')
    st.stop()

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)