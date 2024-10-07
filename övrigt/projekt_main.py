# Lägg till import daytime i en separat text fil som du sparar i en annan txt fil tid och datum användare lånade boken
# Lägg till användare i en annan text fil som håller koll på vilka böcker de har sparat
# Du kan skapa inloggningsuppgifter för en bibliotikarie
# Clear screen in terminal when you exit a function
# När man väljer meny val så behöver man ej trycka på enter
# Tkinkter för grafisk design
# Classer
# from pynput import keyboard
# Fakturera om till Modulärt

from rensa_terminal import rensa_terminal
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

färg.print ("Välkommen till Nisses bibliotek!", style="bold red\n")

def huvudprogram():
    while True:
        print ("\n[1] Se våra böcker\n[2] Låna en bok\n[3] Lämna tillbaks bok\n[4] Lämna biblioteket\n")

        val = input ("")
        if val == "1":
            kolla_bibliotek()
        elif val == "2":
            låna_bok(bibliotek)
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