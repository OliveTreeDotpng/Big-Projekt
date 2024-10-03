from rich.console import Console
from datetime import datetime
import rensa_terminal

class BokenFinnsEj(Exception):
    pass
class KategorinFinnsEj(Exception):
     pass

now = datetime.now() .strftime("%Y-%m-%d %H:%M")
färg = Console()

def låna_bok(bibliotek):
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
           rensa_terminal()
           break

