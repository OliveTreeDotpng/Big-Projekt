class Bok:
    def __init__(self, titel, författare) -> None:
        self.titel = titel
        self.författare = författare
        self.lånad_status = False
    
    def __str__(self) -> str:
        return f"{self.titel} av {self.författare}"

class Kategori:
    def __init__(self, namn) -> None:
        self.namn = namn 
        self.böcker = []  # En tom lista som kommer att hålla Bok-objekt, #Gjort med hjälp av AI

    def lägg_till_bok(self, bok): #Gjort med hjälp av AI
        self.böcker.append(bok)   

       
    
    def visa_böcker(self): #Gjort med hjälp av AI
        if not self.böcker:
            print (f"Boken finns ej i kategorin {self.namn}.")              
        else:
            for bok in self.böcker:
                print (bok)

class Bibliotek: 
    



    
# Skapa kategorier
skräck = Kategori("Skräck")
fantasy = Kategori("Fantasy")
romantik = Kategori("Romantik")
sci_fi = Kategori("Sci-Fi")


# Skapa böcker
skräck1 = Bok("IT", "Stephen Hawking")
skräck2 = Bok("Dracula", "Bram Stoker")
skräck3 = Bok("Frankenstein", "Mary Shelley" )

fantasy1 = Bok("Cold Days", "Jim Butcher")
fantasy2 = Bok("Lord Of The Rings", "J.R.R Tolkien" )
fantasy3 = Bok("Mistborn", "Brandon Sanderson")

romantik1 = Bok("The Fault In Our Stars", "John Green")
romantik2 = Bok("Det är så logiskt, alla fattar utom du", "Lisa Bjärbo")
romantik3 = Bok("Syskonkärlek", "Katarina von Bredow")

scifi_1 = Bok("Mickey 7", "Edward Ashton")
scifi_2 = Bok("We are Legion (We are Bob)", "Dennis E. Taylor")
scifi_3 = Bok("Forging Zero", "Sara King")


# Lägg till böcker i respektive kategorier
skräck.lägg_till_bok(skräck1)
skräck.lägg_till_bok(skräck2)
skräck.lägg_till_bok(skräck3)

fantasy.lägg_till_bok(fantasy1)
fantasy.lägg_till_bok(fantasy2)
fantasy.lägg_till_bok(fantasy3)

romantik.lägg_till_bok(romantik1)
romantik.lägg_till_bok(romantik2)
romantik.lägg_till_bok(romantik3)

sci_fi.lägg_till_bok(scifi_1)
sci_fi.lägg_till_bok(scifi_2)
sci_fi.lägg_till_bok(scifi_3)

bib = Bibliotek(skräck, fantasy, romantik)

#skräck.visa_böcker()