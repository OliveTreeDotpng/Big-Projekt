import tkinter as tk
from bibliotek import Bok, Kategori, skräck, fantasy, romantik, sci_fi

root = tk.Tk()

root.title("Bibliotek")
root.minsize(600,600)

"""Visa kategorier och böcker:

    Skapa en Listbox för att visa dina kategorier.
    När du klickar på en kategori, uppdatera en annan Listbox med böcker som tillhör den kategorin."""

kategori_listbox = tk.Listbox(root, height = 5,
                  width = 8,
                  bg = "grey",
                  activestyle = "dotbox",
                  font = "Helvetica",
                  fg = "black")


kategori_lista = [skräck, fantasy, romantik, sci_fi]
for kategori in kategori_lista:
    kategori_listbox.insert(tk.END, kategori.namn)
    



"""Hantera interaktion:
    Lägg till knappar som "Låna" och "Lämna tillbaka" för att hantera bokens status.
    Visa feedback till användaren med hjälp av messagebox från tkinter."""




# Pack widgets
kategori_listbox.pack()


root.mainloop()