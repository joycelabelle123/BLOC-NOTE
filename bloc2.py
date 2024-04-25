import tkinter as tk 
from tkinter import filedialog
class blocnotes:
    def __init__(self,root):
        self.root = root
        self.root.title("bloc-notes")
        self.text_area =tk.Text(root)
        self.text_area.pack(side="bottom",fill="both", expand=True)
#creer un nouveau fichier
        self.new_fille_button = tk.Button(root, text="Nouveau Fichier",command=self.new_file,bg="blue")
        self.new_fille_button.pack()
#ouvrir un fichier existant 
        self.open_file_button = tk.Button(root, text="Ouvrir un Fichier", command=self.open_file ,bg="red")

        self.open_file_button.pack(padx=10,pady=10)

        #enregistrement 
        self .save_button =tk.Button(root, text="enregistrer", command=self.save_file,bg="yellow")
        self.save_button.pack()
        #enregistre sous 
        self.save_as_button = tk.Button(root, text="enregistre sous",command=self.save_as_file,bg="green")
        self.save_as_button.pack() 
        #quitter la fenetre 
        self.quit_button = tk.Button(root,text="Quitter",command=root.quit)
        self.quit_button.pack()
    def new_file(self):
        self.text_area.delete(1.0,tk.END)
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichier texte", "*.txt")])
        if file_path:
            with open(file_path,"r") as file:
                content = file.read()
                self.text_area.delete(1.0,tk.END)
                self.text_area.insert(tk.END,content)
    def save_file(self):
        file_path= filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("fichiers text","*.txt")])
        if file_path:
            content= self.text_area.get(1.0,tk.END)
            with open(file_path, "w") as file:
                file.write(content)
    def save_as_file(self):
        self.save_file()
if __name__== "__main__":
      root =tk .Tk()
      app =blocnotes(root)
      root.mainloop()
