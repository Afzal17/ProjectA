# |IMPORT STATEMENTS|
import psycopg2
import random
import datetime as date
import requests
from tkinter import *

# We beginnen met een database connectie
database_connection = psycopg2.connect(
    host="localhost",
    database="projecta_2023",
    user="postgres",
    password="open"
)

# Functie
def laat_bericht_zien():
    # We gebruiken de cursor method om gebruik te maken van SQL statements
    cur = database_connection.cursor()

    # We gebruiken de execute method om de laatste 5 berichten te pakken
    cur.execute("SELECT reizigernaam, berichtbeschrijving, stationnaam, beoordelingsdatum FROM  bericht ORDER BY beoordelingsdatum DESC LIMIT 5")

    # We vangen de SQL statement uit de execute door middel van de fetchall() method + in een variable (5 laatste berichten)
    de_vijf_laatste_berichten = cur.fetchall()

    # Hieronder kan optioneel een print statement gebruikt te worden om de inhoud te controleren!

    # Voor de weather API key heb ik gebruik gemaakt van een YouTube video & een account gemaakt op de weather api website

    # We gaan een random station kiezen uit de stations.txt
    return de_vijf_laatste_berichten

# Random station generator
with open('../module1/stations.txt') as station_file:
    station_lijst = station_file.readlines()
    random_station = station_lijst[random.randint(0, len(station_lijst)-1)]

# We gaan een connectie maken met de WEATHER API (hiervoor heb ik de documentatie gebruikt
def get_weather_info(random_station):
    resource_uri = 'https://api.openweathermap.org/data/2.5/weather?&appid=18aefc4f90493ec89c486d1b5993584f&units=metric&lang=nl'
    parameters = {'q':  random_station +',nl'}
    response = requests.get(resource_uri, parameters)
    response_data = response.json()

    weer_omschrijving = response_data['weather'][0]['description']
    temperatuur = str(round(response_data['main']['temp'], 1)) + '°C'

    weer = [weer_omschrijving, temperatuur]

    return weer

# Alle berichten in een variabel zetten
cur = database_connection.cursor()
variable_1 = laat_bericht_zien()
station1 = variable_1[0][2]
station2 = variable_1[1][2]
station3 = variable_1[2][2]
station4 = variable_1[3][2]
station5 = variable_1[4][2]

# We pakken de kolom uit het stationnaam dat we opgeven
query = "SELECT * FROM station_service WHERE station_service = %s"
data = (station1,)
cur.execute(query, data)
station1_data = cur.fetchall()
print(station1_data[0])

data = (station2,)
cur.execute(query, data)
station2_data = cur.fetchall()

data = (station3,)
cur.execute(query, data)
station3_data = cur.fetchall()

data = (station4,)
cur.execute(query, data)
station4_data = cur.fetchall()

data = (station5,)
cur.execute(query, data)
station5_data = cur.fetchall()


# We gaan Tkinter runnen
root = Tk()
root.title('Welkom op het mooie scherm')
root.geometry('1200x700')

label = Label(master=root,
              text='Welkom bij de NS',
              background='Yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold'),
              width=1200,
              height=700,)


button = Button(master=root,
                text=f"{variable_1[0]}, \n ,{variable_1[1]}, \n ,{variable_1[2]}, \n ,{variable_1[3]}, \n ,{variable_1[4]}")
button.pack(pady=10)


weather = Label(master=root,
              text=f"Het weer in {random_station}: {get_weather_info(random_station)}")

button = Button(master=root,
              text=f"{station1_data[0][0]} NL, OV-Bike = {station1_data[0][2]}, Elevator = {station1_data[0][3]}, Toilet = {station1_data[0][4]}, Park & Ride= {station1_data[0][5]} ")

button.pack()

button = Button(master=root,
              text=f"{station2_data[0][0]} NL, OV-Bike = {station2_data[0][2]}, Elevator = {station2_data[0][3]}, Toilet = {station2_data[0][4]}, Park & Ride= {station2_data[0][5]} ")

button.pack()

button = Button(master=root,
              text=f"{station3_data[0][0]} NL, OV-Bike = {station3_data[0][2]}, Elevator = {station3_data[0][3]}, Toilet = {station3_data[0][4]}, Park & Ride= {station3_data[0][5]} ")

button.pack()

button = Button(master=root,
              text=f"{station4_data[0][0]} NL, OV-Bike = {station4_data[0][2]}, Elevator = {station4_data[0][3]}, Toilet = {station4_data[0][4]}, Park & Ride= {station4_data[0][5]} ")

button.pack()

button = Button(master=root,
              text=f"{station5_data[0][0]} NL, OV-Bike = {station5_data[0][2]}, Elevator = {station5_data[0][3]}, Toilet = {station5_data[0][4]}, Park & Ride= {station5_data[0][5]} ")

button.pack()

button.pack(pady=10)

weather.pack()
label.pack()
root.mainloop()










