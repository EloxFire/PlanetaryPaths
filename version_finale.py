# Description du programme :
# Programme qui permet de calculer la position des planètes du système solaire à une date donnée.

# Importer les modules nécessaires
# Le module requests permet de faire des requêtes à un site internet (API)
import requests

print("Bienvenue dans votre calculateur de position de planètes !")
# Demander à l'utilisateur de choisir une date pour laquelle calculer les positions des planètes
date = input("Entrez une date au format année-mois-jour (Exemple: 2025-02-27): ") or "now" # Date choisir par l'utilisateur (maintenant par défaut si laissé vide)

liste_planetes = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"] # Nom des planètes (en anglais OBLIGATOIRE pour le site)
lien = "https://ssp.imcce.fr/webservices/miriade/api/ephemph.php" # Lien du site de calcul des positions de l'IMCCE

print(f"\nVoici les résultats pour la date du {date}:")
for planete in liste_planetes: # le mot-clé 'for' indique une boucle, les instructions à l'intérieur vont se répéter pour chaque nom dans la liste de planètes
    parametres = {
        "-name": f"p:{planete}", # La planete
        "-ep": date, # La date que nous avons choisie
        "-mime": "json", # Le format de la réponse (OBLIGATOIRE COMME CA)
        "-output": "--coord(ec)", # Le format des coordonées (OBLIGATOIRE) : ec = écliptique; eq2000 = équatorial
    }
    # Appeler le site internet IMCCE pour obtenir les données de toutes les planètes de la liste à la date choisie
    # On donne à la fonction requests la méthode GET (obligatoire), le lien du site et les paramètres (nom de la planète, date, format de coordonées)
    reponse = requests.request("GET", lien, params=parametres)
    data = reponse.json()
    longitude = data.get("data", [{}])[0].get("Longitude", "Erreur")

    if longitude == "Erreur":
        print(f"- {planete} : Erreur")
    else:
        print(f"- {planete} : {longitude[2:4]}°")

print("\nMerci d'avoir utilisé notre calculateur de position de planètes !")
