# Lägg till import daytime i en separat text fil som du sparar i en annan txt fil tid och datum användare lånade boken
# Lägg till användare i en annan text fil som håller koll på vilka böcker de har sparat
# Du kan skapa inloggningsuppgifter för en bibliotikarie
# Clear screen in terminal when you exit a function
# När man väljer meny val så behöver man ej trycka på enter
# Tkinkter för grafisk design
# Classer
from pynput import keyboard
from rich.console import Console
from datetime import datetime
import sys
import os
class BokenFinnsEj(Exception):
    pass
class KategorinFinnsEj(Exception):
     pass

now = datetime.now() .strftime("%Y-%m-%d %H:%M")
färg = Console()

class Category:
    def __init__(self, type) -> None:
        self.type = type

class Book:
    def __init__(self, namn, category) -> None:
        self.namn = namn
        self.lånad = False
        self.category = category

skräck = Category("skräck")
fantasy = Category("fantasy")
romantik = Category("romantik")
sci_fi = Category("sci-fi")

bok_1 = Category("it", skräck)




    



bibliotek = {
    "skräck": ["it", "dracula", "alien isolation"],
    "fantasy": ["cold days", "lord of the rings", "mistborn"],
    "romantik": ["twilight", "det är så logiskt, alla fattar förutom du", "syskonkärlek" ],
    "sci-fi": ["mickey 7", "bob", "zero"],
}

färg.print ("Välkommen till Nisses bibliotek!", style="bold red\n")

def huvudprogram():
    while True:
        print ("\n[1] Se våra böcker\n[2] Låna en bok\n[3] Lämna tillbaks bok\n[4] Lämna biblioteket\n")

        if val == "1":
            kolla_bibliotek()
        elif val == "2":
            låna_bok()
        elif val == "3":
            lämna_tillbaks()
        elif val == "4":
            sys.exit()
        else:
            print ("Där blev något fel, ange en siffra som motsvarar det du vill göra.")



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

def låna_bok():
    print ("\n")
    for kategori, böcker in bibliotek.items():
            färg.print (f"{kategori}", style="bold red")
            for bok in böcker:
                print (bok)
    while True:
        print ("\nVilken bok vill du låna? Ange kategori och sedan namnet på boken, separerat med mellanslag: ")
        
        try:
            fråga = input ("")
            kategori, bok = fråga.split(maxsplit=1)
            
            if kategori not in bibliotek:
                raise KategorinFinnsEj (f"Vi har tyvärr ej kategorin {kategori}. ")
            
            if bok not in bibliotek[kategori]:
                raise BokenFinnsEj (f"Vi har tyvärr ej boken {bok}.")

            if bok in bibliotek[kategori]:
                bibliotek[kategori].remove(bok)
                print (f"Du har nu lånat boken {bok}")

                with open ("datetime.txt", "a", encoding="utf-8") as låna:
                    låna.write(f"Du har lånat {bok} {now}\n")

                print (f"{bibliotek[kategori]}")

        except ValueError:
            färg.print("Var god ange både kategori och bok, separerat med mellanslag.", style="bold yellow")

        except KategorinFinnsEj as e:
            färg.print (f"{e}", style="bold yellow")

        except BokenFinnsEj as e:
            färg.print (f"\n{e}", style="bold yellow")

        val = input ("Vill du låna fler böcker? ja/nej: ") .lower()
        if val == "ja":
            continue
        else:
           rensa_terminalen()
           break
            
def lämna_tillbaks():

    inmatning = input ("Mata in katerogi och sedan bok som du vill lämna tillbaks, separerat med mellanslag: ").lower()
    # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
    kategori, bok = inmatning.split(maxsplit=1)
    bibliotek [kategori].append(bok)
    with open ("datetime.txt", "a", encoding="utf-8") as lämna_tillbaks:
        lämna_tillbaks.write(f"Du lämnade tillbaks {bok} {now}\n")
        
def rensa_terminalen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



huvudprogram()     



"""inmatning = input ("Ange kategori och bok, separerat med mellanslag: ").lower()
            # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
            kategori, bok = inmatning.split (maxsplit=1)"""