# Description du programme :
# Programme qui permet de calculer la position des planètes du système solaire à une date donnée.

# Importer les modules nécessaires
# Le module requests permet de faire des requêtes à un site internet (API)
import requests

print("Bienvenue dans votre calculateur de position de planètes !")
# Demander à l'utilisateur de choisir une date pour laquelle calculer les positions des planètes
date = input("Entrez une date (format: YYYY-MM-DD): ")
# date = "2025-02-27"

# Appeler le site internet IMCCE pour obtenir les données de toutes les planètes de la liste à la date choisie
liste_planetes = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"] # Nom des planètes en anglais (OBLIGATOIRE)
lien = "https://ssp.imcce.fr/webservices/miriade/api/ephemph.php"

print(f"\nVoici les résultats pour la date du {date}:\n")
for planete in liste_planetes:
    parametres = {
        "-name": f"p:{planete}", # La planete
        "-ep": date, # La date que nous avons choisie
        "-mime": "json", # Le format de la réponse (OBLIGATOIRE COMME CA)
        "-output": "--coord(ec)", # Le format des coordonées (OBLIGATOIRE COMME CA) : ec = écliptique
        "-observer": "@0"  # BARYCENTRE DU SYSTEME SOLAIRE
    }
    reponse = requests.request("GET", lien, params=parametres)
    data = reponse.json()
    longitude = data.get("data", [{}])[0].get("Longitude", "Erreur")

    if longitude == "Erreur":
        print(f"- {planete} : Erreur")
    else:
        print(f"- {planete} : {longitude[2:4]}°")

print("\n\nMerci d'avoir utilisé notre calculateur de position de planètes !")
