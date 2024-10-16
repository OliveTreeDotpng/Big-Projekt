CREATE TABLE IF NOT EXISTS böcker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,     -- Unikt ID för varje bok
    titel TEXT,                               -- Bokens titel
    författare TEXT,                          -- Bokens författare
    kategori TEXT,                            -- Bokens kategori
    utlånad BOOLEAN                           -- Om den är utlånad eller inte
);

-- Här kan andra tabeller eller annat stå och det kommer läsas in.


-- Exempel

-- Kolumn = id eller titel eller författare osv

-- Rad: 1, "Harry Potter", "J.K. Rowling", "Fantasy", False....varje gång användaren skapar en ny bok som skapas en rad.