from utils import helpers

def calculate_calories(Alter, Gewicht, Grösse, Aktivitätsniveau, timezone='Europe/Zurich'):
    """
    Calculate Kalorienverbrauch and return a dictionary with inputs, Kalorienverbrauch, category, and timestamp.

    Args:
        Alter (float): Alter in Jahren.
        Gewicht (float): Gewicht in Kilogramm.
        Grösse (float): Grösse in Zentimeter.
        Aktivitätsniveau (str): Aktivitaetsfaktor

    Returns:
        dict: A dictionary containing the inputs, calculated Kalorienverbrauch, category, and timestamp.
    """
    if Grösse <= 0 or Gewicht <= 0 or Alter <= 0:
        raise ValueError("Grösse, Gewicht, and Alter must be greater than 0.")
    
    # Berechnen der Basal Metabolic Rate (BMR) durch die Mifflin-St Jeor Formel
    BMR = 10 * Gewicht + 6.25 * Grösse - 5 * Alter + 5  # Assuming male, for female use -161 instead of +5

    # Adjust BMR based on activity level (Aktivitätsniveau)
    aktivitaetsfaktor = {
        "Vorwiegend sitzend (Bürojob, Studium)": 1.2,
        "Vorwiegend stehend (Verkauf, Handwerk)": 1.55,
        "Vorwiegend laufend (Handwerker, Sportler)": 1.9
    }

    if Aktivitätsniveau not in aktivitaetsfaktor:
        raise ValueError("Invalid Aktivitätsniveau. Choose from: 'Vorwiegend sitzend (Bürojob, Studium)', 'Vorwiegend stehend (Verkauf, Handwerk)', 'Vorwiegend laufend (Handwerker, Sportler)'.")

    Kalorienverbrauch = BMR * aktivitaetsfaktor[Aktivitätsniveau]

    result_dict = {
        "timestamp": helpers.ch_now(),
        "Grösse": Grösse,
        "Gewicht": Gewicht,
        "Aktivitätsniveau": Aktivitätsniveau,
        "Alter": Alter,
        "Kalorienverbrauch": Kalorienverbrauch
    } 

    return result_dict
