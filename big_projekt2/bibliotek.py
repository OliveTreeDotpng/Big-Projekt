from datetime import datetime
from Bok import Bok

class Bibliotek:
    def __init__(self) -> None:
        self.inventory = [] # Skapar en tom inventarielista för att lagra böcker i biblioteket
     
    def låna(self):
        titel = input ("Ange titeln på boken du vill låna: ")
        
        for bok in self.inventory:
            if bok.titel.lower() == titel.lower(): # Kontrollera om boken finns i inventory
                if bok.utlånad == True:  # Om boken redan har status True så betyder det att den redan är utlånad.
                    print (f"{bok.titel} är redan utlånad")
                    return

                bok.utlånad = True # Här ändrar vi status till True att den är utlånad, eftersom vi vet att den inte var utlånad tidigare
                print (f"{bok.titel} är nu utlånad")
                with open ("log.txt", "a", encoding="utf-8") as fil:
                    now = datetime.now() .strftime("%Y-%m-%d %H:%M")
                    fil.write(f"Du har lånat {bok.titel} {now}\n")
                return         
               
        print (f"Hittade ingen bok med titeln '{titel}' i biblioteket.")

    def lämna_tillbaks(self):

        utlånade_böcker = False # Flagga för att kontrollera om några böcker är utlånade

        for böcker in self.inventory:
            if böcker.utlånad:
                print (böcker)
                utlånade_böcker = True # Om en bok är utlånad, ändra flaggan till True

        if utlånade_böcker == False: # Inga böcker är utlånade, informera användaren
            print ("Inga böcker är utlånade för tillfället.")
            return

        while True: # While loop ifall användaren gör en typo

            val = input ("Ange bok som ska lämnas tillbaks: ") .lower()
            for böcker in self.inventory:

                if böcker.titel.lower() == val.lower(): # Kontrollera om bokens titel matchar användarens inmatning
                    if böcker.utlånad == False: # Kontrollerar status
                        print (f"{böcker.titel} är inte utlånad.")
                        return

                    böcker.utlånad = False
                    print (f"{böcker.titel} är nu returnerad.")
                    return
                    
            print (f"Hittade ingen bok med titeln '{val}'. Försök igen.")  

    def lägg_till_bok(self):
        # Fråga användaren om titel, författare och kategori
        titel = input("Ange bokens titel: ")
        författare = input ("Ange bokens författare: ")
        kategori = input ("Ange kategorin för boken: ")
        
        ny_bok = Bok(titel, författare, kategori)

        # Lägg till den nya boken till inventarielistan
        self.inventory.append(ny_bok)

        print (f"Boken {titel} av {författare} har beställts")

    def visa_böcker_per_kategori(self):
            print("[1] Skräck\n[2] Fantasy\n[3] Romantik\n[4] Sci-Fi")
            val = input ("Välj en kategori: ")
            
            # För varje bok i bibliotekets boklista (self.inventory) som matchar vald kategori, skriv ut boken.
            if val == "1": 
                print ()
                for bok in self.inventory:  
                    if bok.kategori == "Skräck":
                        print(bok)

            elif val == "2": 
                print ()
                for bok in self.inventory:
                    if bok.kategori == "Fantasy":
                        print (bok)

            elif val == "3": 
                print ()
                for bok in self.inventory:
                    if bok.kategori == "Romantik":
                        print (bok)
                        
            elif val == "4": 
                print ()
                for bok in self.inventory:
                    if bok.kategori == "Sci-Fi":
                        print (bok)
            else: 
                print ("Där blev något fel, ange en siffra som motsvarar det du vill göra.")


    def visa_alla_böcker(self):
        print ()
        index = 0
        for böcker in self.inventory:
            index += 1
            print (index, böcker) # Använd __str__-metoden i Bok för snygg utskrift
        print ()

    def ta__bort_böcker(self, vald):
        self.inventory.pop(vald-1) # tar bort 1 för att matcha index
        


