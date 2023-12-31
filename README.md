# Python Examen Opracht

## Inleiding
Dit programma neemt als input statestieken van het weer. Deze data is een csv bestand van www.meteoblue.com voor de stad Basel(zwidserland).
Wanneer deze bron gedownload wordt, moeten de volgende data opgehaald worden 
    - Temperature[2 m elevation corrected]
  - Sunshine duration (minutes)
  - Precipitation amount
  - Pressure [mean sea level]
  - Wind gusts

Voor een goede representatie wordt verwacht dat alle eenheden in het metrische systeem staan.

## OmgevingsVariabelen
Hier dient het path naar de database gezet te worden
````DATABASE_PATH=C:\Users\User\Documenten\School\Python\voorbeeld.db````

## De eerste keer uitvoeren van het programma
Met het volgende commando wordt de database geinitialiseerd en de data ingevult.
``python controller.py init``
Hierna wordt er gevraagd om een bron csv bestand op te geven (momenteel moet deze zich nog in de root van het project bevinden).
In dit project zit een voorbeeld csv bestand inbegrepen op de root van het project, met als naam 'src.csv'.

Eens dat dit script is uitgevoerd is de database gevuld met data en kunnen alle andere scripts uitgevoerd worden op deze database.

## Nieuwe data toevoegen of data updaten
Met het ``python controller.py set_src`` kan de database gevuld worden met extra data uit een csv bestand.

## Data opvragen
``python controller.py data-info``
Geeft de basis info en de eerste twee entries weer van een bepaalde locatie die later opgegeven dient te worden.

``python controller.py rainfall``
Dit commando geeft de regenval weer per week, en vergelijkt deze met het gemiddelde van de maand.

## Data exporteren
De data van één locatie kan geëxporteerd worden dmv het volgende commando:
``python controller.py to_csv``
Vervolgens kan de locatie opgegeven worden, wanneer deze blanco is, is dit 'Basel'. Optioneel kan de data samengevoegd worden met de volgende mogelijkheden:
- D: De data wordt gegroepeerd per dag.
- W: De data wordt gegroepeerd per week.
- M: De data wordt gegroepeerd per maand.
- None of '': De data wordt niet gegroupeerd.

De code is niet volledig verfijnd en 'User proof' gemaakt wegens tijdgebrek, er is op de meeste plaatsen wel een basis validatie.

source: https://www.meteoblue.com/en/weather/archive/export?daterange=2022-01-01%20-%202023-10-31&locations%5B%5D=basel_switzerland_2661604&domain=NEMSGLOBAL&min=2022-01-01&max=2023-10-31&params%5B%5D=&params%5B%5D=temp2m&params%5B%5D=&params%5B%5D=&params%5B%5D=&params%5B%5D=&params%5B%5D=&params%5B%5D=&utc_offset=1&timeResolution=hourly&temperatureunit=CELSIUS&velocityunit=KILOMETER_PER_HOUR&energyunit=watts&lengthunit=metric&degree_day_type=10%3B30&gddBase=10&gddLimit=30