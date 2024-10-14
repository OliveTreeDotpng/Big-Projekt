import sqlite3

# Skapa en anslutning till databasen (detta skapar en ny fil som heter "bibliotek.db" om den inte finns)
connection = sqlite3.connect("bibliotek.db")

# Med detta objekt kan vi skicka SQL-frågor (kommandon) till databasen. Det är cursor som faktiskt exekverar våra SQL-satser.
cursor = connection.cursor()

# Öppna SQL-filen 'setup_tables.sql', som innehåller SQL-koden för att skapa tabellerna.
with open("create_table.sql", "r") as sql_fil:
    sql_script = sql_fil.read() # Läser hela innehållet från SQL filen och sprarar det i variabeln "sql script" 

# Kör SQL-koden som vi läste in från "create_table.sql"
# "executescript()" används för att köra SQL kommandon, plural, om det finns fler i filen.
cursor.executescript(sql_script)

# Vi sparar aka commitar ändringarna till databasen
connection.commit()

# Stänger anslutningen till databasen. Detta frigör resurser och säkerställer att inga fler ändringar görs.
connection.close()

print ("Databasen och tabellerna är skapade.")