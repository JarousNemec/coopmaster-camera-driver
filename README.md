# coopmaster-camera-driver
- komunikator mezi IP camerou a obraz zpracovavajici aplikaci (dog alarm, chicken watch guard)

## funkcionalita
- nese si informaci o konfiguraci jednotlivych IP kamerach aktuálně je zde pevně zahardcoděne používání dvou kamer 1. pro dog alarm a 2. pro chicken watch guard 
- vystavuje REST API pro ziskani aktualniho obrazu z chicken kamery a kamery v ohrade 
- vraci obrazek ve FULL HD rozliseni
- pro každý call se načte nový obrázek z kamery

## technologie
- python
- rtsp - real-time streaming protocol
- knihovny
  - **Flask**: Lehký webový framework pro rychlý vývoj webových aplikací.
  - **colorama**: Manipulace s barvami v textovém výstupu na terminálu.
  - **waitress**: Rychlý WSGI server pro produkční nasazení webových aplikací.
  - **python-dotenv**: Načítání konfigurace z `.env` souborů.
  - **requests**: Jednoduché HTTP požadavky (GET, POST, atd.).

## hardware
- IP camera Hilook by Hikvision IPC-B180HA-LU
