class Bok:
    def __init__(self, titel, författare, kategori ) -> None:
        self.titel = titel
        self.författare = författare
        self.kategori = kategori

        self.utlånad = False # Alla böcker som blir skapade får automatiskt statusen "inte utlånad"

    # Lägg till en __str__-metod för att definiera hur boken ska presenteras
    def __str__(self) -> str:
        return f"{self.titel} av {self.författare} (Kategori: {self.kategori})"