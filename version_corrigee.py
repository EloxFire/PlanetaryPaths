# Description: Programme qui permet de calculer la position des planètes du système solaire à une date donnée.

# Importer les modules nécessaires
# Le module requests permet de faire des requetes à un site internet (API)
import requests


# Demander à l'utilisateur l'action à faire : "Choisir une planète unique" ou "Calculer pour toutes les planètes"
print("Bienvenue dans votre calculateur de position de planètes !")
choix_utilisateur = input("Tapez 1 pour choisir une planète unique, ou 2 pour calculer pour toutes les planètes: ")


# if permet de vérifier si une condition est vraie
# if (si en français) le choix de l'utilisateur est égal à "1" : alors on exécute le code qui suit
# else (sinon en français) : on exécute un autre code
if choix_utilisateur == "1":

    # Demander à l'utilisateur de choisir une planète parmi la liste de planètes
    print("Liste des planètes disponibles: Mercure, Venus, Mars, Jupiter, Saturne, Uranus, Neptune")
    planete = input("Choisissez une planète: ")
    print(f"Vous avez choisi la planète {planete}")

    # Demander à l'utilisateur de choisir une date
    date = input("Entrez une date (format: YYYY-MM-DD): ")

    # Appeler le site internet IMCCE pour obtenir les données de la planète à la date choisie
    lien = "https://ssp.imcce.fr/webservices/miriade/api/ephemph.php"
    parametres = {
        "-name": f"p:{planete}", # La planète que nous avons sélectionée
        "-ep": date.strftime("%Y-%m-%d"), # La date que nous avons choisie
        "-mime": "json", # Le format de la réponse (OBLIGATOIRE COMME CA)
        "-output": "--coord(ec)", # Le format des coordonées (OBLIGATOIRE COMME CA) : ec = écliptique
        "-observer": "@0"  # BARYCENTRE DU SYSTEME SOLAIRE
    }
    reponse = requests.request("GET", lien, params=parametres)
    data = reponse.json()
    print(data)
elif choix_utilisateur == "2":
    print("Calcul pour toutes les planètes...")
else:
    print(f"Une erreur est survenue... Votre choix ({choix_utilisateur}) n'est pas reconnu.")