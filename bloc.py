import tkinter as tk
import tkinter as dialog
root = tk.Tk()
root.title("bloc-note")
root.geometrie("500x500")
#creer une barre de menu
menu_bar = tk.Menu(root)
#ajout d'un menu deroulant a la barre de menu
fichier_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="fichier",menu=fichier_menu)
#ajout des elements du menu
fichier_menu.add_command(label="gin")
root.mainloop()