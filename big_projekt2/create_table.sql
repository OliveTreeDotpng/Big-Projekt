CREATE TABLE IF NOT EXISTS böcker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,     -- Unikt ID för varje bok
    titel TEXT,                               -- Bokens titel
    författare TEXT,                          -- Bokens författare
    kategori TEXT,                            -- Bokens kategori
    utlånad BOOLEAN                           -- Om den är utlånad eller inte
);

-- Här kan andra tabeller eller annat stå och det kommer läsas in.