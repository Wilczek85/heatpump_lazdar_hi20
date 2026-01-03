# Lazar HI20 Heat Pump – Home Assistant Integration

## Opis
Pełna integracja Home Assistant (2025) dla pompy ciepła **Lazar HI20** poprzez oficjalne API chmurowe hkslazar.net.

## Funkcje
- Config Flow (UI)
- Sensory temperatur (×0.1°C)
- Switch ON/OFF
- Select trybu pracy (CO / Chłodzenie / CWU)
- Climate entity
- Obsługa energii (Energy Dashboard)
- Gotowe do HACS

## COP
COP liczony uproszczoną metodą: energia wyjściowa / energia elektryczna.
Brak danych przepływu → przyjęto nominalne parametry producenta.

## Instalacja
1. Dodaj repozytorium do HACS
2. Zainstaluj „Lazar HI20 Heat Pump”
3. Restart HA
4. Dodaj integrację z UI

## Release
v2026.1.1