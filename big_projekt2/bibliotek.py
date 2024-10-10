import sys

class Bok:
    def __init__(self, titel, författare, kategori ) -> None:
        self.titel = titel
        self.författare = författare
        self.kategori = kategori

        self.utlånad = False # Alla böcker som blir skapade får automatiskt statusen "inte utlånad"

    # Lägg till en __str__-metod för att definiera hur boken ska presenteras
    def __str__(self) -> str:
        return f"{self.titel} av {self.författare} (Kategori: {self.kategori})"

class Bibliotek:
    def __init__(self) -> None:
        self.inventory = [] # Skapar en tom inventarielista för att lagra böcker i biblioteket
     
    def låna(self):
        titel = input ("Ange titeln på boken du vill låna: ")
        
        for bok in self.inventory:
            if bok.titel.lower() == titel.lower(): # Kontrollera om boken finns i inventory
                if bok.utlånad == True:  # Om boken redan har status True så betyder det att den redan är utlånad.
                    print (f"{bok.titel} är redan utlånad")
                    return # Avsluta metoden

                bok.utlånad = True # Här ändrar vi status till True att den är utlånad, eftersom vi vet att den inte var utlånad tidigare
                print (f"{bok.titel} är nu utlånad")
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

    def ta_bort_bok(self):
        pass

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
        for böcker in self.inventory:
            print (böcker) # Använd __str__-metoden i Bok för snygg utskrift
        print ()

def huvudprogram():
    while True:
        print ("\n[1] Se alla våra böcker\n[2] Visa böcker per kategori\n[3] Låna en bok\n[4] Lämna tillbaks bok\n[5] Beställ bok till vårat bibliotek\n[6] Lämna biblioteket\n")

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

# Printar alla böcker
#mitt_bibliotek.visa_alla_böcker()



huvudprogram()

