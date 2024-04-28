import tkinter as tk 
from tkinter import filedialog
class blocnotes:
    def __init__(self,root):
        self.root = root
        self.root.title("bloc-notes")
        self.contenu = tk.Texte(root)
        self.contenu.pack()

        menu =tk.Menu(root)
        root.config(menu=menu)
        fichier_menu= tk.Menu(menu)
        menu.add_cascade(label="fichier",menu=fichier_menu)
        fichier_menu.add_commande(label="nouveau", commande=self .creer_nouveau_fichier)
        fichier_menu.add_command(label="Ouvrir", command=self.ouvrir_fichier)
        fichier_menu.add_command(label="Enregistrer", command=self.enregistrer)
        fichier_menu.add_command(label="Enregistrer sous", command=self.enregistrer_sous)
        fichier_menu.add_separator()
        fichier_menu.add_command(label="Quitter", command=root.quit)
def creer_nouveau_fichier(self):
        self.contenu.delete(1.0, tk.END)
        print("Nouveau fichier créé.")

    def ouvrir_fichier(self):
        nom_fichier = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
        if nom_fichier:
            with open(nom_fichier, "r") as fichier:
                contenu = fichier.read()
                self.contenu.delete(1.0, tk.END)
                self.contenu.insert(tk.END, contenu)
                print(f"Fichier '{nom_fichier}' ouvert.")

    def enregistrer(self):
        nom_fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
        if nom_fichier:
            contenu = self.contenu.get(1.0, tk.END)
            with open(nom_fichier, "w") as fichier:
                fichier.write(contenu)
                print(f"Contenu enregistré dans le fichier '{nom_fichier}'.")

    def enregistrer_sous(self):
        nom_fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
        if nom_fichier:
            contenu = self.contenu.get(1.0, tk.END)
            with open(nom_fichier, "w") as fichier:
                fichier.write(contenu)
                print(f"Contenu enregistré dans le nouveau fichier '{nom_fichier}'.")

root = tk.Tk()
bloc_notes = BlocNotes(root)
root.mainloop()
