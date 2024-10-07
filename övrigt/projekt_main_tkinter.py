# Lägg till import daytime i en separat text fil som du sparar i en annan txt fil tid och datum användare lånade boken
# Lägg till användare i en annan text fil som håller koll på vilka böcker de har sparat
# Du kan skapa inloggningsuppgifter för en bibliotikarie
# Clear screen in terminal when you exit a function
# När man väljer meny val så behöver man ej trycka på enter
# Tkinkter för grafisk design
# Gör ditt bibliotek om till Classer
# from pynput import keyboard
# Fakturera om till Modulärt
# 

import tkinter as tk
from rich.console import Console
from datetime import datetime
import sys
from låna_bok import låna_bok
class BokenFinnsEj(Exception):
    pass
class KategorinFinnsEj(Exception):
     pass

now = datetime.now() .strftime("%Y-%m-%d %H:%M")
färg = Console()

bibliotek = {
    "skräck": ["it", "dracula", "alien isolation"],
    "fantasy": ["cold days", "lord of the rings", "mistborn"],
    "romantik": ["twilight", "det är så logiskt, alla fattar förutom du", "syskonkärlek" ],
    "sci-fi": ["mickey 7", "bob", "zero"],
}


def huvudprogram():
    root = tk.Tk()

# Sätter titel på huvudfönstret
    root.title("Bibliotek.exe")

    root.minsize(650,480)

    def button_click_låna():
        låna_bok(bibliotek) # Här kallar jag på låna bok i root fönstret
    
    def button_click_låna():
        låna_bok(bibliotek) # Här kallar jag på låna bok i root fönstret
        

    # Skapa en Label och lägg till den i fönstret
    label = tk.Label(root, text="Vi säger så :)")
    display_input = tk.Entry(root, width=100)
    display_input.pack()

    button = tk.Button(root,
                    text = "Låna bok",
                    command = button_click_låna )

    label.pack()

    button.pack(padx=20, pady=20)
    # Startar huvudloopen
    root.mainloop()



def kolla_bibliotek():
    while True:
        färg.print ("Vi har ett stort urval av genrer, vänligen välj en så ska vi se vilka böcker vi har för den valda kategorin.", style="bold purple")
        for x in bibliotek.keys():
            print (x)
        try:
            kategori = input("\nKategori: ")
            if kategori not in bibliotek:
                raise KategorinFinnsEj (f"\nKategorin {kategori} finns ej i vårat bibliotek, välj en av våra följande kategorier: ")
            
            # Om genren (nykeln) finns i biblioteket (listan) så printar den alla böcker (värden) kopplat till nykeln. 
            elif kategori in bibliotek: 
                print (f"\nHär är våra följande böcker inom {kategori}: {bibliotek[kategori]}")
                
        except KategorinFinnsEj as e:
            print (e)
            for x in bibliotek.keys():
                print (x)
            continue
        
        val = input ("Vill du fortsätta kolla igenom våra kategorier? ja/nej: ") .lower()
        if val == "ja":
            continue
        else:
           break  


            
def lämna_tillbaks():

    inmatning = input ("Mata in katerogi och sedan bok som du vill lämna tillbaks, separerat med mellanslag: ").lower()
    # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
    kategori, bok = inmatning.split(maxsplit=1)
    bibliotek [kategori].append(bok)
    with open ("datetime.txt", "a", encoding="utf-8") as lämna_tillbaks:
        lämna_tillbaks.write(f"Du lämnade tillbaks {bok} {now}\n")
        



huvudprogram()     



"""inmatning = input ("Ange kategori och bok, separerat med mellanslag: ").lower()
            # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
            kategori, bok = inmatning.split (maxsplit=1)"""