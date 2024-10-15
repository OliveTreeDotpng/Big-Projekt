import tkinter as tk
from bibliotek import Bok, Kategori, skräck, fantasy, romantik, sci_fi

root = tk.Tk()

root.title("Bibliotek")
root.minsize(600,600)

"""Visa kategorier och böcker:

    Skapa en Listbox för att visa dina kategorier.
    När du klickar på en kategori, uppdatera en annan Listbox med böcker som tillhör den kategorin."""

# Låda i gui't som visar alla kategorier
kategori_listbox = tk.Listbox(root, height = 5,
                  width = 8,
                  bd=5,
                  bg = "grey",
                  activestyle = "dotbox",
                  font = ("Helvetica",16),
                  fg = "black"
                  )




# Lixbox för att visa böckerna
bok_listbox = tk.Listbox(root, height = 10,
                         width = 40,
                         bd = 5,
                         bg = "yellow",
                         font =("Helvetica", 16),
                         fg = "black")

låna_button = tk.Button(root, text="Låna", command=Bok.låna_bok)

låna_button.pack(side=tk.TOP, pady=5)

# Skapar lista
kategori_lista = [skräck, fantasy, romantik, sci_fi]

# Lägger till kategorierna i min listbox i gui't
for kategori in kategori_lista:
    kategori_listbox.insert(tk.END, kategori.namn)
    
def välj_kategori(event):
    val = event.widget.curselection()
    if val == (1,):
        for bok in fantasy.böcker:
            bok_listbox.insert(tk.END, bok)
            print (bok)
    
kategori_listbox.bind("<<ListboxSelect>>", välj_kategori)


"""Hantera interaktion:
    Lägg till knappar som "Låna" och "Lämna tillbaka" för att hantera bokens status.
    Visa feedback till användaren med hjälp av messagebox från tkinter."""


# Packar widgets
kategori_listbox.pack(side=tk.TOP)

# Packar widgets igen nästa listbox
bok_listbox.pack()

# Krävs för att öppna fönstret
root.mainloop()