def calculate_agla_risk(age, gender, total_cholesterol, hdl, ldl, smoker, systolic_bp):
    """
    Berechnet das 5-Jahres-Herzinfarktrisiko basierend auf dem AGLA-Score.
    
    :param age: Alter des Patienten (Jahre)
    :param gender: Geschlecht ('m' für männlich, 'w' für weiblich)
    :param total_cholesterol: Gesamtcholesterinwert (mmol/L)
    :param hdl: HDL-Cholesterinwert (mmol/L)
    :param ldl: LDL-Cholesterinwert (mmol/L)
    :param smoker: Raucherstatus (True für Raucher, False für Nichtraucher)
    :param systolic_bp: Systolischer Blutdruck (mmHg)
    :return: Geschätztes Risiko für einen Herzinfarkt in den nächsten 5 Jahren (%)
    """
    
    # Basis-Risiko abhängig von Alter und Geschlecht
    base_risk = 0.5 if gender == 'w' else 1.0
    base_risk *= (age / 50)  # Risiko steigt mit dem Alter
    
    # Cholesterin-Faktoren
    cholesterol_factor = (total_cholesterol - 5) * 1.2  # Annahme: Referenzwert 5 mmol/L
    hdl_factor = (1.5 - hdl) * 1.5  # Schutzfaktor von HDL
    ldl_factor = (ldl - 3) * 1.3  # Risiko steigt mit erhöhtem LDL
    
    # Rauchen erhöht das Risiko erheblich
    smoking_factor = 2.0 if smoker else 1.0
    
    # Blutdruck-Faktor
    bp_factor = (systolic_bp - 120) * 0.05  # Ab 120 mmHg steigt das Risiko
    
    # Gesamt-Risiko berechnen
    risk = base_risk + cholesterol_factor - hdl_factor + ldl_factor + bp_factor
    risk *= smoking_factor
    
    # Minimum und Maximum begrenzen
    risk = max(0, min(risk, 30))  # Begrenzung auf 30% Risiko
    
    return round(risk, 2)

# Beispiel:
print(calculate_agla_risk(age=55, gender='m', total_cholesterol=6.2, hdl=1.3, ldl=4.1, smoker=True, systolic_bp=140))
