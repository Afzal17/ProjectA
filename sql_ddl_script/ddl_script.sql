-- Studentnaam: Afzal Sarfaraaz Mohan
-- Opdrachtnaam: DDL Script Project A Stationszuilen

-- Opdrachtbeschrijving:
-- Het is van belang dat ik een SQL/DDL script schrijf voor project A
-- hierbij is het doel om zo accuraat mogelijk aan de hand van de project eisen
-- een database op te stellen met het bijbehorende script

-- Opdrachteisen:
-- 1. Of het bericht goedgekeurd is of niet goedgekeurd is
-- 2. De datum en tijd van beoordeling
-- 3. De naam van de moderator die het bericht heeft beoordeeld
-- 4. Het email-adres van de moderator

-- Extra Notities:
-- DATE = YYYY-MM-DD
-- TIME = 00:00:00 HOUR MINUTES SECONDS
-- Nummer -> ID (Op de Nederlandse manier geschreven)
-- Database Wachtwoord: open

CREATE TABLE moderator(
    moderatornummer SERIAL NOT NULL,
    moderatornaam VARCHAR(255),
    email VARCHAR(255),
    PRIMARY KEY(moderatornummer)
);

CREATE TABLE bericht(
    bericht SERIAL NOT NULL,
    reizigernaam VARCHAR(255),
    berichtdatum DATE NOT NULL,
    berichtbeschrijving VARCHAR(140),
    beoordeling VARCHAR(1),
    beoordelingsdatum DATE,
    stationnaam VARCHAR(255) NOT NULL,
    moderatornummer INTEGER, -- FOREIGN KEY
    PRIMARY KEY (bericht),
    FOREIGN KEY (moderatornummer) REFERENCES moderator(moderatornummer)
);