# Stappenplan Module 2 Moderator Input/Goedkeuring & Afkeuring Station Zuil
# 1. In module 1 hebben we de input ontvangen van de reiziger en weggeschreven naar de database
# 2. We maken een database connectie om vervolgens een SQL statement uit te voeren zodat we
#    kunnen checken of alle berichten zichtbaar gemaakt kunnen worden (dit is een test)
# 3. We gebruiken de fetchall() method om de SQL resultaten op te vangen
# 4. We vragen de moderator om de volgend gegevens: (Moderatornummer + Moderatornaam + Moderator-email)
# 5. Als we de input ontvangen hebben pushen wij deze ook gelijk door naar de database
# 6. Voor het pushen heb ik een variable aangemaakt met een SQL statement, dit komt gelijk in de Moderator tabel
# 7. We maken een for loop waarin de moderator het uitgeprinte bericht kan goedkeuren of afkeuren (zie code beneden)
# 8. We geven ook automatisch de datum + tijdstip mee van de beoordeling
# 9. Op het einde van de loop inserten we met een SQl statement alle input en vullen we de data van het bericht aan
# 10. Einde stappenplan!

# |IMPORT STATEMENTS|
from datetime import datetime
import psycopg2

# Hier maken we een database connectie om alle berichten van de reiziger uit de database te halen
con = psycopg2.connect(
    host="localhost",
    database="projecta_2023",
    user="postgres",
    password="open"
)

# Hier maken we een connectie om SQL statements te runnen
cur = con.cursor()

# Hier maken we een SQL statement waar de oudste bericht wordt geselecteerd
cur.execute("SELECT * FROM bericht WHERE beoordeling IS NULL ORDER BY berichtdatum ASC")

tabellen = cur.fetchall()

# Hier vragen we de Moderator om zijn gegevens in te voeren
moderator_nummer = input("mod wat is je bsn: ")
moderator_naam = input("mod wat is je naam: ")
moderator_email = input("mod wat is je email:")

# Hier maken we een variable aan met een SQL statement om de ingevoerde input
# van de moderator in de moderator tabel in te voeren met middel van placeholders
moderator_push = "INSERT INTO moderator(moderatornummer, moderatornaam, email ) VALUES (%s, %s, %s)"
moderator_insert = (moderator_nummer, moderator_naam, moderator_email)
cur.execute(moderator_push, moderator_insert)
con.commit()

# We gaan vervolgens een for loop maken waar we elke bericht printen waar de beoordeling value
# nog op 0 staat (Bericht ID, Reizigernaam, Berichtdatum, Berichtbeschrijving, Stationnaam)
for tabel in tabellen:
    print("Bericht ID: ",tabel[0])
    print("Reizigernaam: ",tabel[1])
    print("Berichtdatum: ",tabel[2])
    print("Berichtbeschrijving: ",tabel[3])
    print("Stationaam: ",tabel[6])
    print("\n")

    # Hier vragen we de moderator of hij het bericht wil goedkeuren of afkeuren
    # Goedkeuren = J (Ja) -> j
    # Afkeuren = N (Nee) -> n
    bericht_goed_fout = input("Moderator wil je dit bericht goedkeuren ja(j) of nee(n)?: ")

    # Hier geven we de actuele datum en tijdstip mee van de beoordeling die door de moderator is uitgevoerd
    actuele_tijd_beoordeling_moderator = datetime.now()
    actuele_datum_moderator = datetime.strftime(actuele_tijd_beoordeling_moderator, "%d-%m-%y")
    actuele_tijdstip_moderator = datetime.strftime(actuele_tijd_beoordeling_moderator, "%H:%M:%S")
    moderator_samenvoeging = actuele_datum_moderator + ' ' + actuele_tijdstip_moderator

    # Hier naderen we het einde van de loop we zorgen ervoor dat met elke loop de beoordeling wordt
    # ge-update met een ja of nee in de database
    update_database = "UPDATE bericht SET moderatornummer = %s, beoordeling = %s, beoordelingsdatum = %s WHERE bericht = %s"
    update_second = (moderator_nummer, bericht_goed_fout, moderator_samenvoeging, tabel[0])
    cur.execute(update_database, update_second)
    con.commit()

# DB: Connectie met de database wordt afgesloten!
con.close()






















