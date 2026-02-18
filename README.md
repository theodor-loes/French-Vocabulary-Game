# French Vocabulary Game

Et simpelt, men effektivt gloseverktøy som kjører i terminalen.

Det kombinerer enkel psykologi med tilgivende respons for å pugge franske gloser.
Koden er ment for å hjelpe å lese fransk litteratur.

---

## ✨ Konsept

Språkprorgammer er ofte repetetive og langsomme.

Dette prosjektet fokuserer på rask læring:
- Du skriver ordene på fransk selv fra starten av
- Når du klarer å skrive ordet riktig, forsvinner det fra videre terping
- Det er raskt og enkelt å legge inn nye gloser fra bøker du leser

Målet :
- IKKE å lære ordene utenatt
- IKKE å huske ordene for alltid
- Gjenkjenne mange ord raskt
- Få en oversikt over vokabularet i boka
- Forstå ord godt nok - og lenge nok - til å henge med i handlingen
- (Derav også å føle på mestring)

---

## 🛠️ Kom i gang (Installer og kjør)

Følg disse stegene for å kjøre spillet lokalt:

### 1️⃣ Klon prosjektet

```bash
git clone https://github.com/theodor-loes/French-Vocabulary-Game.git
cd French-Vocabulary-Game
```

### 2️⃣ Sett opp Python-miljø

Det anbefales å bruke en virtuell Python-miljø for å holde prosjektavhengigheter adskilt:
```bash
# (valgfritt) lag et nytt miljø med venv
python3 -m venv venv

# aktiver miljøet
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```
### 📦 Avhengigheter

Prosjektet krever noen Python-biblioteker for å kjøre korrekt.

Installer avhengigheter

For å sikre at alle nødvendige biblioteker installeres, kjør:
```bash
pip install -r requirements.txt
```
Dette vil lese filen requirements.txt og installere alle listede pakker automatisk.

### ▶️ Kjøre spillet

Etter at du har installert avhengigheter:
```bash
python main.py
```
Dette starter spillet i terminalen.

---

## 🔌 Skrivefeil-integrasjoner

Biblioteket Difflib blir brukt for å gjenkjenne små skrivefeil, for å ikke demotivere brukeren. To små linjer i koden, men en stor påvirkning på psykologien og motivasjonen.
```
def similarity(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()
```

---

## 💡 Hva jeg lærte

- Hvordan bruke og utnytte terminalen som et verktøy
- Hvordan hjernen tilegner seg kunnskap basert på mestring og rask respons
- Hvordan integrere buffere for å gjøre interaksjonen mer dynamisk
- Programmeringens potensialet for personlig utvikling

---

## 🔮 Videre utvikling

- Automatisk formatert og utfylt .txt fil, ved bruk av API
- Forbedret UI, lage en simpel web-applikasjon
