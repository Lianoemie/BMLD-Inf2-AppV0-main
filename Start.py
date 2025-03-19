import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Kalorienrechner")

st.write("Der Kalorienrechner ist eine benutzerfreundliche Webanwendung, die es Nutzern ermöglicht, ihren täglichen Kalorienverbrauch basierend auf individuellen Daten zu berechnen. Der Nutzer gibt sein Alter, Gewicht, Größe und Geschlecht an und wählt sein Aktivitätsniveau aus (z. B. sitzend, stehend oder laufend). Mithilfe einer Formel zur Berechnung des Grundumsatzes (BMR) und einem Aktivitätsfaktor wird der Gesamtenergieverbrauch (TDEE) ermittelt, der den Kalorienbedarf pro Tag anzeigt. ")

"""
Diese App wurde von folgenden Personen entwickelt:
- Lia Müller (muellli6@students.zhaw.ch)
- Selina Rüdisüli (ruedisel@students.zhaw.ch)

""" 

