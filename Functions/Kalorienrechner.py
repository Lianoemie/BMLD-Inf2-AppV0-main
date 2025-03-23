from utils import helpers

def calculate_calories(Alter, Gewicht, Grösse, Aktivitätsniveau, timezone='Europe/Zurich'):
    """
    Calculate Kalorienverbrauch and return a dictionary with inputs, Kalorienverbrauch, category, and timestamp.

    Args:
        Alter (float): Alter in Jahren.
        Gewicht (float): Gewicht in Kilogramm.
        Grösse (float): Grösse in Zentimeter.
        Aktivitätsniveau (str): Aktivitätsniveau.

    Returns:
        dict: A dictionary containing the inputs, calculated Kalorienverbrauch, category, and timestamp.
    """
    if Grösse <= 0 or Gewicht <= 0 or Alter <= 0:
        raise ValueError("Grösse, Gewicht, and Alter must be greater than 0.")
    
    # Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation
    BMR = 10 * Gewicht + 6.25 * Grösse - 5 * Alter + 5  # Assuming male, for female use -161 instead of +5

    # Adjust BMR based on activity level
    activity_levels = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }

    if Aktivitätsniveau not in activity_levels:
        raise ValueError("Invalid Aktivitätsniveau. Choose from: 'sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'.")

    Kalorienverbrauch = BMR * activity_levels[Aktivitätsniveau]

    result_dict = {
        "timestamp": helpers.ch_now(),
        "Grösse": Grösse,
        "Gewicht": Gewicht,
        "Aktivitätsniveau": Aktivitätsniveau,
        "Alter": Alter,
        "Kalorienverbrauch": Kalorienverbrauch
    } 

    return result_dict
