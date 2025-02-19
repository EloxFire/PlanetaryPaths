import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import requests

def valider_date():
    selected_date = cal.get_date()
    selected_planet = planet_var.get()
    if selected_date and selected_planet:
        # Remplacez l'URL et les paramètres par ceux que vous souhaitez utiliser
        url = "https://ssp.imcce.fr/webservices/miriade/api/ephemph.php"
        params = {
            "date": selected_date.strftime("%Y-%m-%d"),
            "-name": selected_planet
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                messagebox.showinfo("Succès", "Appel réussi!")
            else:
                messagebox.showerror("Erreur", f"Erreur {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erreur", f"Erreur de requête: {e}")
    else:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une date et une planète.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("PlanetaryPaths - Un projet Astroshare")
root.geometry("500x800")
root.configure(bg="#000000")  # Fond noir

# Charger une image et redimensionner
image_path = "assets/astroshare_logo_white.png"  # Remplacez par le chemin de votre image
image = Image.open(image_path)

# Redimensionner l'image tout en conservant le ratio d'aspect
max_width = 200
width_percent = (max_width / float(image.size[0]))
height_size = int((float(image.size[1]) * float(width_percent)))
image = image.resize((max_width, height_size), Image.LANCZOS)

photo = ImageTk.PhotoImage(image)

# Ajouter l'image à la fenêtre
image_label = tk.Label(root, image=photo, bg="#000000")
image_label.pack(pady=20)

# Ajouter un sélecteur de date
cal = DateEntry(root, width=12, background='#ffffff', foreground='#000000', borderwidth=0)
cal.pack(pady=20)

# Ajouter un groupe de boutons radio pour sélectionner une planète
planet_var = tk.StringVar()
planets = ["Mercure", "Vénus", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"]
planets_values = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for i, planet in enumerate(planets):
    rb = tk.Radiobutton(
        root,
        text=planet,
        variable=planet_var,
        value=planets_values[i],
        bg="#000000",
        fg="white",
        selectcolor="#000000",
    )
    rb.pack(anchor=tk.W, padx=20)

# Ajouter un bouton valider
valider_button = tk.Button(
    root,
    text="Valider",
    command=valider_date,
    bg="white",
    fg="black",
    relief="flat",
    bd=0,
    highlightthickness=0
)
valider_button.pack(pady=20)

# Lancer la boucle principale
root.mainloop()
