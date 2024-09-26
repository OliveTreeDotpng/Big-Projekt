# Lägg till import daytime i en separat text fil som du sparar i en annan txt fil tid och datum användare lånade boken
# Lägg till användare i en annan text fil som håller koll på vilka böcker de har sparat
# Du kan skapa inloggningsuppgifter för en bibliotikarie
from rich.console import Console
from datetime import datetime
import sys
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
färg.print ("Vi har ett stort urval av genrer, vänligen välj en så ska vi se vilka böcker vi har för den valda kategorin.", style="bold purple")
for x in bibliotek.keys():
    print (x)

def huvudprogram():
    while True:
        def kolla_bibliotek():
            while True:
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
                    val = input ("\n[1] Lämna biblioteket\n[2] Låna en bok\n")
                    if val == "1":
                        sys.exit() #lämnar programmet helt
                    elif val == "2":
                        break
            
        kolla_bibliotek()

        def låna_bok():
            print ("Vilken bok vill du låna? Ange kategori och sedan namnet på boken, separerat med mellanslag: ")
            
            for kategori, böcker in bibliotek.items():
                färg.print (f"{kategori}", style="bold red")
                for bok in böcker:
                    print (bok)

            try:
                fråga = input ("")
                kategori, bok = fråga.split(maxsplit=1)
                if kategori not in bibliotek:
                    raise KategorinFinnsEj (f"Vi har ej tyvärr kategorin {kategori}, vänligen välj en utav våra hundratals andra kategorier: ")
                
            
            except KategorinFinnsEj as e:
                print (f"\n{e}")                
                for kategori in bibliotek.keys():
                    print (kategori)

                

            if bok in bibliotek[kategori]:
                bibliotek[kategori].remove(bok)
                print (f"Du har nu lånat boken {bok}")

                with open ("datetime.txt", "a", encoding="utf-8") as låna:
                    låna.write(f"Du har lånat {bok} {now}\n")

                print (f"{bibliotek[kategori]}")

            
                
        låna_bok()
        
        def lämna_tillbaks():
            inmatning = input ("Mata in katerogi och sedan bok som du vill lämna tillbaks, separerat med mellanslag: ").lower()
            # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
            kategori, bok = inmatning.split(maxsplit=1)
            bibliotek [kategori].append(bok)
            with open ("datetime.txt", "a", encoding="utf-8") as lämna_tillbaks:
                lämna_tillbaks.write(f"Du lämnade tillbaks {bok} {now}\n")

        lämna_tillbaks()
        
        break
huvudprogram()     



"""inmatning = input ("Ange kategori och bok, separerat med mellanslag: ").lower()
            # Splittar endast på första mellenslaget sen kan man skriva hur många man vill ifall boken har mellanslag
            kategori, bok = inmatning.split (maxsplit=1)"""