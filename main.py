import tkinter as tkr
from tkinter import simpledialog
import FUNCIONESS as fun
from FUNCIONESS import mayoria_de_edad2, mayoria_de_edad

base= tkr.Tk()
base.title("djfngdher")

nombre= simpledialog.askstring("nombre","digite su nombre:")
edad= simpledialog.askinteger("edad","digite su edad:")
usar_label=tkr.Label(base,text=mayoria_de_edad(nom=ed),font=)
usar_label=tkr.Label(base,text=RR,font)
usar_label.pack(pady)
base.mainloop()