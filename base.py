import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Charger la base de données
file_path = "Base.xlsx"  # Remplacez par le chemin vers votre fichier
df = pd.read_excel(file_path)

# Liste des colonnes à tester
variables = [
    "Echanges commerciaux",
    "PIB-Nigeria",
    "PIB-Cameroun",
    "Population-Nigeria",
    "Population-Cameroun"
]

# Fonction pour effectuer le test de Dickey-Fuller Augmenté
def adf_test(series, variable_name):
    result = adfuller(series, autolag='AIC')
    print(f"Résultats du test ADF pour {variable_name}:")
    print(f"  - Statistique ADF : {result[0]}")
    print(f"  - P-valeur : {result[1]}")
    print(f"  - Nombre de retards : {result[2]}")
    print(f"  - Nombre d'observations utilisées : {result[3]}")
    for key, value in result[4].items():
        print(f"  - Valeur critique {key} : {value}")
    if result[1] < 0.05:
        print("  ==> La série est stationnaire (H0 rejetée).\n")
    else:
        print("  ==> La série n'est PAS stationnaire (H0 non rejetée).\n")

# Appliquer le test de stationnarité sur les variables
for var in variables:
    if var in df.columns:
        adf_test(df[var].dropna(), var)
    else:
        print(f"La variable {var} n'existe pas dans la base de données.")
