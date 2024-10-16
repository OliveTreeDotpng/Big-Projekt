# SQL lite 3
from bibliotek import Bibliotek
import sys

mitt_bibliotek = Bibliotek()

def huvudprogram():
    while True:
        print ("\n[1] Se alla våra böcker\n[2] Visa böcker per kategori\n[3] Låna en bok\n[4] Lämna tillbaks bok\n[5] Lägg till ny bok i vårat bibliotek\n[6] Ta bort bok\n[7] Lämna biblioteket\n")

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

        elif val == "7":
            print ("Hej då välkommen åter!")
            sys.exit()

        else:
            print ("Där blev något fel, ange en siffra som motsvarar det du vill göra.")

huvudprogram()