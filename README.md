# Lazar HI20 – Home Assistant

Niestandardowa integracja Home Assistant dla pomp ciepła **Lazar HI20**.

## Funkcje
- Temperatury, pompy, grzałki
- CWU i CO jako termostaty
- Krzywa grzewcza z walidacją
- Tryby pracy (Grzanie / Chłodzenie / CWU)
- Energy Dashboard (kWh)
- Dashboard Lovelace

## Instalacja
1. Skopiuj `custom_components/lazar_hi20` do katalogu HA
2. Restart Home Assistant
3. Ustawienia → Integracje → Dodaj → Lazar HI20
4. Podaj login i hasło do hkslazar.net

## Energy Dashboard
Ustaw:
- Źródło energii: `sensor.lazar_hi20_energia`

## Dashboard
Importuj `dashboards/lazar_hi20_dashboard.yaml`
