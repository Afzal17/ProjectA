# Stappenplan Module 1 Bericht Reiziger Station Zuil
# 1. Vraag om bericht beschrijving van de reiziger
# 2. Vraag om een naam (geen naam is automatisch anoniem)
# 3. Automatiseer dat de datum en tijdstip wordt meegenomen
#    - In python heb je een standaard functie die je kan gebruiken
#    - om de actuele datum en tijdstip te noteren
#    - www.programiz.com/python-programming/datetime/current-datetime staat alle informatie
#    - Hiervoor is het van belang om een import statement te maken
# 4. Als we standaard functies van python gebruiken dan horen wij ook de juiste import te hanteren
# 5. Op het einde schrijven we alle informatie toe naar de database


# Hier staan alle import statements voor de functies die we gebruiken
from datetime import datetime
import random
import psycopg2


# Om te beginnen vragen we de user om input
reizigers_bericht = input("Hallo, schrijf hier uw reiservaring: ")

# Omdat de reiziger ook anoniem een bericht kan maken hebben we
# een if statement nodig mocht het zo zijn als er geen naam gebruikt wordt
# Hier checken we of het bericht minder of gelijk staat aan 140 tekens
# Als het bericht voldoet aan de if statement eisen dan kan de reiziger
# vervolgens zijn naam invoeren

if len(reizigers_bericht) <= 140:
    reizigers_naam = input("Uw naam meneer/mevrouw? ")
    if reizigers_naam == "":
        reizigers_naam = "Anonieme Reiziger"
    # We geven automatisch het actuele datum en tijdstip mee van het bericht
    actuele_datum_tijdstip = datetime.now()

    # We vragen eerst de actuele datum door middel van de library
    # (d = Day | m = Month | y = Year)
    actuele_datum = datetime.strftime(actuele_datum_tijdstip, "%d-%m-%y")

    # Daarna vragen we de actuele tijd door middel van de library
    actuele_tijdstip = datetime.strftime(actuele_datum_tijdstip, "%H:%M:%S")

    # Samenvoeging van Datum & Tijdstip
    samenvoeging = actuele_datum + ' ' + actuele_tijdstip

    # We gaan een random station kiezen hiervoor gebruiken we de random functie
    # en ook deze is afkomstig van de python library
    # Voordat we een station kunnen kiezen maken we variable lijst aan
    station_lijst = []

    # We gaan de (station.txt file inlezen)
    file = open("stations.txt")

    # We gaan loopen door de stations en een random station kiezen
    # s = station (individueel station) | we strippen onnodige characters tijdens het loopen
    for s in file.readlines():
        station_lijst.append(s.strip())

    # Hier kiezen we een random station uit de lijst
    # We maken gebruik van de random functie uit de python library
    # www.w3school.com/python/module_random.asp heb ik mijn informatie vandaan
    # We maken een variable aan om gebruik te maken van de python functie
    automatisch_station_kiezer = random.choice(station_lijst)

    # Nu gaan geloopt hebben en een random station gekozen hebben gaan we alle
    # variablen naar een nieuw CSV/TXT bestand schrijven zodat het daar opgeslagen
    # wordt voor de moderator om in te kunnen zien
    # Hiervoor importeren we CSV van de python library
    # www.pythontutorial.net/python-basics/python-write-csv-file/
    print(automatisch_station_kiezer)

    # DB: Hier maken we een database connectie (boven de code staat de import functie)
    # Informatie: www.canvas.hu.nl/courses/32736/pages/prog11-apis-and-databases
    con = psycopg2.connect(
        host="localhost",
        database="projecta_2023",
        user="postgres",
        password="open")

    #DB: Database cursor om interactie met de database te hebben
    cur = con.cursor()

    # DB: Bericht inserten in de database
    database_query = "INSERT INTO bericht(reizigernaam, berichtdatum, berichtbeschrijving, stationnaam ) VALUES (%s, %s, %s, %s) "
    database_insert = (reizigers_naam, samenvoeging, reizigers_bericht, automatisch_station_kiezer)
    cur.execute(database_query, database_insert)

    # DB: Hier commiten we de queries naar de database
    con.commit()

    # DB: Hier sluiten we de database connectie
    con.close()









