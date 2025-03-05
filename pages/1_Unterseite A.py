import streamlit as st

st.title("Unterseite A")

st.write("Diese Seite ist eine Unterseite der Startseite.")

def berechne_kalorienbedarf(gewicht, groesse, alter, geschlecht, aktivitaetsniveau):
    # Harris-Benedict-Formel zur Berechnung des Grundumsatzes (BMR)
    if geschlecht.lower() == "m":
        grundumsatz = 66.47 + (13.75 * gewicht) + (5.003 * groesse) - (6.755 * alter)
    else:
        grundumsatz = 655.1 + (9.563 * gewicht) + (1.850 * groesse) - (4.676 * alter)
    
    # Aktivitätsfaktoren
    aktivitaetsfaktoren = {
        "1": 1.2,   # Vorwiegend sitzende oder liegende Tätigkeiten
        "2": 1.4,   # Fast ausschliesslich sitzend, wenig Freizeitaktivitäten
        "3": 1.6,   # Überwiegend sitzend, mit zusätzlichen stehenden/gehenden Tätigkeiten
        "4": 1.9,   # Überwiegend stehende/gehende Tätigkeit
        "5": 2.4    # Körperlich anstrengende berufliche Tätigkeit
    }
    
    gesamtbedarf = grundumsatz * aktivitaetsfaktoren.get(aktivitaetsniveau, 1.2)
    
    return grundumsatz, gesamtbedarf

# Benutzereingaben
geschlecht = input("Geben Sie Ihr Geschlecht ein (m/w): ")
gewicht = float(input("Geben Sie Ihr Gewicht in kg ein: "))
groesse = float(input("Geben Sie Ihre Größe in cm ein: "))
alter = int(input("Geben Sie Ihr Alter in Jahren ein: "))

print("\nWählen Sie Ihr Aktivitätsniveau:")
print("1: Vorwiegend sitzende oder liegende Tätigkeiten")
print("2: Fast ausschliesslich sitzend, wenig Freizeitaktivitäten")
print("3: Überwiegend sitzend, mit zusätzlichen stehenden/gehenden Tätigkeiten")
print("4: Überwiegend stehende/gehende Tätigkeit")
print("5: Körperlich anstrengende berufliche Tätigkeit")

aktivitaetsniveau = input("Geben Sie die Zahl des Aktivitätsniveaus ein: ")

# Berechnung des Kalorienbedarfs
grundumsatz, gesamtbedarf = berechne_kalorienbedarf(gewicht, groesse, alter, geschlecht, aktivitaetsniveau)

# Ausgabe der Ergebnisse
print(f"\nIhr Grundumsatz beträgt: {grundumsatz:.2f} kcal pro Tag")
print(f"Ihr Gesamtenergiebedarf beträgt: {gesamtbedarf:.2f} kcal pro Tag")