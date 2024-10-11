from Bibliotek import Bibliotek
from Bok import Bok
import sys

def huvudprogram():
    while True:
        print ("\n[1] Se alla våra böcker\n[2] Visa böcker per kategori\n[3] Låna en bok\n[4] Lämna tillbaks bok\n[5] Beställ bok till vårat bibliotek\n[6] Ta bort bok\n[7] Lämna biblioteket\n")

        val = input ("")
        if val == "1":
            mitt_bibliotek.visa_alla_böcker()
        elif val == "2":
            mitt_bibliotek.visa_böcker_per_kategori()
        elif val == "3":
            mitt_bibliotek.låna()
        elif val == "4":
            mitt_bibliotek.lämna_tillbaks()
        elif val == "5":
            mitt_bibliotek.lägg_till_bok()
        elif val == "6":
            mitt_bibliotek.visa_alla_böcker()
            while True:
                try:
                    vald = int (input ("Ange en siffra: "))
                    mitt_bibliotek.ta__bort_böcker(vald)
                    break
                except ValueError:
                    print ("Ogiltigt val, ange en siffra mellan 1 och 12")
                    
            
        elif val == "7":
            print ("Hej då välkommen åter!")
            sys.exit()
        else:
            print ("Där blev något fel, ange en siffra som motsvarar det du vill göra.")

# Skapa ett objekt av klassen Bibliotek för att lagra och hantera böcker
mitt_bibliotek = Bibliotek()

# Lägger till böcker i inventarielistan
mitt_bibliotek.inventory.append(Bok("IT", "Stephen Hawking", "Skräck"))
mitt_bibliotek.inventory.append(Bok("Dracula", "Bram Stoker", "Skräck"))
mitt_bibliotek.inventory.append(Bok("Frankenstein", "Mary Shelley", "Skräck" ))

mitt_bibliotek.inventory.append(Bok("Cold Days", "Jim Butcher", "Fantasy"))
mitt_bibliotek.inventory.append(Bok("Lord Of The Rings", "J.R.R Tolkien", "Fantasy" ))
mitt_bibliotek.inventory.append(Bok("Mistborn", "Brandon Sanderson", "Fantasy"))

mitt_bibliotek.inventory.append(Bok("The Fault In Our Stars", "John Green", "Romantik"))
mitt_bibliotek.inventory.append(Bok("Det är så logiskt, alla fattar utom du", "Lisa Bjärbo", "Romantik"))
mitt_bibliotek.inventory.append(Bok("Syskonkärlek", "Katarina von Bredow", "Romantik"))

mitt_bibliotek.inventory.append(Bok("Mickey 7", "Edward Ashton", "Sci-Fi"))
mitt_bibliotek.inventory.append(Bok("We are Legion (We are Bob)", "Dennis E. Taylor", "Sci-Fi"))
mitt_bibliotek.inventory.append(Bok("Forging Zero", "Sara King", "Sci-Fi"))

huvudprogram()