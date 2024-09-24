# Lägg till import daytime i en separat text fil som du sparar i en annan txt fil tid och datum användare lånade boken
# Lägg till användare i en annan text fil som håller koll på vilka böcker de har sparat
# Du kan skapa inloggningsuppgifter för en bibliotikarie
from rich.console import Console
from datetime import datetime
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
}

färg.print ("Välkommen till Nisses bibliotek!", style="bold red\n")
färg.print ("Vi har ett stort urval av genrer, vänligen välj en så ska vi se vilka böcker vi har för den valda kategorin.", style="bold purple")
for x in bibliotek.keys():
    print (x)

def huvudprogram():
    while True:
        def kolla_bibliotek():
            while True:
                try:
                    kategori = input("Kategori: ")
                    if kategori not in bibliotek:
                        raise KategorinFinnsEj (f"Kategorin {kategori} finns ej i vårat bibliotek, välj en av våra följande kategorier: ")
                        
                    
                    elif kategori in bibliotek:
                        print (f"\nHär är våra följande böcker inom {kategori}: {bibliotek[kategori]}")

                except KategorinFinnsEj as e:
                    print ("\n")
                    print (e)
                    for x in bibliotek.keys():
                        print (x)
                    
                
                val = input ("Vill du fortsätta kolla igenom våra kategorier? ja/nej: ") .lower()
                if val == "ja":
                    continue
                else:
                    break
            
        kolla_bibliotek()

        def låna_bok():
            with open ("datetime.txt", "a+") as låna:
                i = låna.write(f"Du lånade boken {now}\n")
            
        låna_bok()
        
        
        break
huvudprogram()     


"""inmatning = input ("Ange kategori och bok, separerat med mellanslag: ").lower()
            # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
            kategori, bok = inmatning.split (maxsplit=1)"""