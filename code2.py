import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
root.title("bloc-note groupe 4")

def function():
 
    def Ouvrir():
        block = filedialog.askopenfilename()
        text_editor.insert(0., open(block, "r").read())
 
    def sauvegarder():
        block = filedialog.asksaveasfilename()
        open(block, "w").write(text_editor.get(0., tk.END))
    
    def sauvegarder_sous():
        if not block:
            sauvegarder()
        else:
            open(block, "w").write(text_editor.get(0., tk.END))
    
    def calculatrice():
        calculette = tk.Toplevel(root)
        calculette.title("Calculatrice")

        valeur = tk.Entry(calculette, font=("time new roman", 30))
        valeur.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 1, 4)
        ]
        for (text, row, col, *span) in buttons:
            button = ttk.Button(calculette, text=text)
            button.grid(row=row, column=col, columnspan=span[-1] if span else 1, sticky="nsew")
            button.bind("<Button-1>", lambda event, txt=text: valeur.insert(tk.END, txt))
 
    menuBar = tk.Menu(root)
    option = tk.Menu(menuBar)
 
    option.add_command(label="Nouveau fichier", command=function)
    option.add_command(label="Ouvrir un fichier", command=Ouvrir)
    option.add_command(label="Enregistrer sous", command=sauvegarder)
    option.add_command(label="Enregistrer", command=sauvegarder_sous)
    option.add_command(label="calculatrice", command=calculatrice)
    option.add_command(label="quitter")
    menuBar.add_cascade(label="fichiers", menu=option)
    root.config(menu=menuBar)
 
    text_editor = tk.Text(root, height=500, width=500)
    text_editor.pack()
 
 
    text_editor.bind("<Control-s>", sauvegarder_sous)
 
    root.mainloop()
function()