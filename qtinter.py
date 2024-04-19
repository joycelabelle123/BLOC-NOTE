
from tkinter import TK 
from tkinter import filedialog,messagebox
root=tk()
root.title("bloc note")
root.geometry("11OOx600+150+200")
root.resizable(false,false)


var_filename=StringVar()
label_area=label(root,text="nom du fichier",font=("times new roman",15))
label_area.place(x=50,y=100)
 
txt_area=Text(root,font=("times new roman",15),db=15,relief=RIDGE)
txt_area.place(x=50,y=20, width=130,height=260)


mainloop()
# Code calculatrice
