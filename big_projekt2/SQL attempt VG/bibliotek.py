from datetime import datetime
import sqlite3

# Du kommer se platshållare såsom (?) i vissa metoder, detta är för att förhindra SQL-injektion
# Detta hindrar användare från att skicka skadlig kod via inputs.
# Exempel på SQL-injektion: Harry Potter; DROP TABLE böcker; --

class Bibliotek:
    def __init__(self) -> None:
        # Skapa anslutning till databasen när objektet skapas
        self.connect = sqlite3.connect("bibliotek.db") # Ansluter till databasen
        self.cursor = self.connect.cursor() # Skapar cursor OBJEKT för att köra SQL kommandon

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
        titel = input ("Ange titel på boken du vill lämna tillbaks")
        self.cursor.execute("SELECT * FROM böcker WHERE titel = ? AND utlånad =  1", (titel,))

        bok = self.cursor.fetchone()

        if bok:
            # Uppdaterar boken med status ej lånad. "WHERE id" med parametern bok[0] gör så att endast denna bok med ett unikt ID ändrar status och inte flera som råkar ha samma namn.
            self.cursor.execute("UPDATE böcker SET utlånad = 0 WHERE id = ?", (bok[0],))
            self.connect.commit()
            print (f"Boken {bok[1]} har lämnats tillbaks.")
        
        else:
             print (f"Boken {titel} finns inte bland våra lånade böcker.")


    def lägg_till_bok(self):
        # Fråga användaren om titel, författare och kategori
        titel = input("Ange bokens titel: ")
        författare = input ("Ange bokens författare: ")
        kategori = input ("Ange kategorin för boken: ")
        
        # Lägger till nya boken i databastabellen "böcker" med hjälp utav cursor objektet.
        self.cursor.execute("INSERT INTO böcker (titel, författare, kategori, utlånad) VALUES (?, ?, ?, ?)",
                            (titel, författare, kategori, False))
        self.connect.commit() # Sparar ändringarna permanent i databastabellen

        # Informerar användare att boken har lagts till.
        print (f"Boken {titel} av {författare} har lagts till i biblioteket")


    def visa_böcker_per_kategori(self):
            kategori = input ("Ange kategori för böcker du vill se: ").lower()

            # SQLite i Python kräver att vi använder tuples för att skicka parametern till SQL, även om det bara är en, därav kommatecknet.
            self.cursor.execute("SELECT * FROM böcker WHERE kategori = ?", (kategori,))
            
            # Hämtar alla böcker från SQL tabellen som en lista av tuples
            böcker = self.cursor.fetchall() 

            # Om listan "böcker" inte är tom så körs koden i if blocket. Python tolkar en tom lista som FALSE och kör därmed inte if satsen.
            if böcker:
                print (f"Böcker i kategorin '{kategori}':")
                for bok in böcker:
                    print (f"ID: {bok[0]}, Titel: {bok[1]}, Författare: {bok[2]}, Kategori: {bok[3]}, Utlånad: {bok[4]}") # Hämtar varje kolumn från tabellen

            # Om listan böcker är tom så körs else
            else:
                print (f"Vi hittade inga böcker i kategorin '{kategori}'")
            

    def visa_alla_böcker(self):
        
        # Hämtar alla böcker från databasen
        self.cursor.execute("SELECT * FROM böcker")
        
        # Hämtar alla böcker i en tuple 
        skriv_ut_alla_böcker = self.cursor.fetchall()

        # Om listan är tom, printa följande
        if not skriv_ut_alla_böcker:
            print (f"Det finns inga böcker, vårat bibliotek är tomt!")
            return
        
        # printar alla böcker
        for bok in skriv_ut_alla_böcker:
            print (f"ID: {bok[0]}, Titel: {bok[1]}, Författare: {bok[2]}, Kategori: {bok[3]}, Utlånad: {bok[4]}")



    def ta__bort_böcker(self, vald):

        titel = input ("Ange titeln på boken du vill ta bort: ")

        self.cursor.execute("DELETE FROM böcker WHERE titel = ?", (titel,)) # Raderar boken som matchar med parametern i våran tuple.

        self.connect.commit() # Spara ändringar permanent

        print(f"Boken {titel} har tagits bort från biblioteket.")



