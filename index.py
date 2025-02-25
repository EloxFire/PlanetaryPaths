import tkinter as tk
from tkinter import messagebox, font
from tkcalendar import DateEntry
import requests

def valider_date():
    selected_date = cal.get_date()
    selected_planet = planet_var.get()
    if selected_date and selected_planet:
        display_data(message="Chargement...")
        url = "https://ssp.imcce.fr/webservices/miriade/api/ephemph.php"
        querystring = {
            "-name": f"p:{selected_planet}",
            "-ep": selected_date.strftime("%Y-%m-%d"),
            "-mime": "json",
            "-observer": "@0"  # BARYCENTRE DU SYSTEME SOLAIRE
        }

        print(f"Appel à l'API: {url}")

        try:
            response = requests.request("GET", url, params=querystring)
            if response.status_code == 200:
                data = response.json()
                display_data(data=data)
            else:
                display_data(message=f"Une erreur est survenue : {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erreur", f"Erreur de requête: {e}")
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une date et une planète.")

def display_data(data=None, message=None):
    if result_text:  # Vérifiez si result_text est défini
        print("Affichage des données dans result_text")
        result_text.delete(1.0, tk.END)  # Effacer le contenu précédent

        if message:
            result_text.insert(tk.END, f"{message}\n")
        elif data:
            sso_name = data.get("sso", {}).get("name", "N/A")
            sso_type = data.get("sso", {}).get("type", "N/A")
            v_mag = round(data.get("data", [{}])[0].get("V Mag", "N/A"), 1)

            result_text.insert(tk.END, f"Nom: {sso_name}\n")
            result_text.insert(tk.END, f"Type: {sso_type}\n")
            result_text.insert(tk.END, f"Magnitude apparente: {v_mag}\n")
        else:
            result_text.insert(tk.END, "Aucune donnée à afficher.\n")
    else:
        print("Erreur : result_text n'est pas défini")

def changer_planete_selectionnee():
    selected_planet = planet_var.get()
    if selected_planet:
        print(f"Planète sélectionnée: {selected_planet}")
    else:
        print("Aucune planète sélectionnée")

# Créer la fenêtre principale
root = tk.Tk()
root.title("PlanetaryPaths - Un projet Astroshare")
root.geometry("600x500")
root.configure(bg="#000000")

# Définir une police personnalisée
custom_font = font.Font(size=14)  # Taille de la police

# Ajouter un sélecteur de date
cal = DateEntry(root, width=12, background='#ffffff', foreground='#000000', borderwidth=0, font=custom_font)
cal.grid(row=1, column=0, columnspan=2, pady=20)

# Ajouter un groupe de boutons radio pour sélectionner une planète
planet_var = tk.StringVar(value="")
planets = ["Mercure", "Vénus", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"]
planets_values = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

radio_frame = tk.Frame(root, bg="#000000")
radio_frame.grid(row=2, column=0, padx=20, pady=5, sticky="n")

for i, planet in enumerate(planets):
    rb = tk.Radiobutton(
        radio_frame,
        text=planet,
        height=1,
        width=8,
        anchor="w",
        variable=planet_var,
        value=planets_values[i],
        bg="#2E2E2E",
        fg="#FFFFFF",
        highlightthickness=0,
        borderwidth=0,
        relief="flat",
        selectcolor="#2E2E2E",
        command=changer_planete_selectionnee,
        font=custom_font  # Appliquer la police personnalisée
    )
    rb.pack(anchor=tk.W, pady=5)

# Ajouter un widget Text pour afficher les résultats
result_text = tk.Text(root, bg="#2E2E2E", fg="#FFFFFF", relief="flat")
result_text.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

# Ajouter un bouton valider
valider_button = tk.Button(
    root,
    text="Valider",
    command=valider_date,
    bg="white",
    fg="black",
    relief="flat",
    bd=0,
    highlightthickness=0,
    font=custom_font  # Appliquer la police personnalisée
)
valider_button.grid(row=3, column=0, columnspan=2, pady=20)

# Configurer la grille pour que la colonne de droite s'étende
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)

# Lancer la boucle principale
root.mainloop()
