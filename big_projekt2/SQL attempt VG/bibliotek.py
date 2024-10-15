from datetime import datetime
from bok import Bok
import sqlite3

class Bibliotek:
    def __init__(self) -> None:
        # Skapa anslutning till databasen när objektet skapas
        self.connect = sqlite3.connect("bibliotet.db") # Ansluter till databasen
        self.cursor = self.connect.cursor() # Skapar cursor för att köra SQL kommandon

def låna(self):
        # Be användaren om boktitel och låna ut den om den finns
        titel = input("Ange titeln på boken du vill låna: ")

        # Vi går igenom alla kolumner SQL tabellen "böcker", endast från rader där "titel" matchar ett specifikt värde vi anger. =? är en platshållare för variabeln titel.
            # "AND utlånad = 0" betyder att vi bara vill hämta böcker som inte är utlånade.
        self.cursor.execute("SELECT * FROM böcker WHERE titel = ? AND utlånad = 0", (titel,))

        # bok är en tuple som innehåller bokens data från databasen (ID, titel, författare, kategori, utlånad status).
        bok = self.cursor.fetchone()  # Hämta första matchande bok| fetchone() gör så att vi bara hämtar 1 bok även om det finns fler som matchar.

        if bok:
            # Ändrar boken till status utlånad, bok[0] hämtar bokens id från tabellen. t.ex så skulle bok[1] hämta titel.
            self.cursor.execute("UPDATE böcker SET utlånad = 1 WHERE id = ?", (bok[0],))
            self.connect.commit() # Sparar ändringarna permanent i databsen.
            # Hämta aktuell tid och datum
            nu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Skriver till loggfilen när boken lånas ut
            with open ("log.txt", "a", encoding="utf-8") as fil:
                 fil.write(f"Du har lånat '{bok[1]}' (ID: {bok[0]}) den {nu}\n")
                 
            print(f"Boken {bok[1]} är nu utlånad.") # Printar bok titeln är utlånad
        else:
            print(f"Boken {titel} är antingen utlånad eller finns inte i biblioteket.")

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
        


