# French Vocabulary Game

Et simpelt, men effektivt gloseverktøy som kjører i terminalen.

Det kombinerer enkel psykologi med tilgivende respons for å pugge franske gloser jeg har fra en bok.

---

## ✨ Konsept

Språkprorgammer er ofte repetetive og langsomme.

Dette prosjektet fokuserer på rask læring:
- Du skriver ordene på fransk selv fra starten av
- Når du klarer å skrive ordet riktig, forsvinner det fra videre terping
- Det er raskt og enkelt å få en oversikt over 40-50 ord på 30 min

Målet :
- IKKE å lære ordene utenatt
- IKKE å huske ordene for alltid
- Gjenkjenne mange ord raskt
- Få en oversikt over vokabularet i boka
- Forstå ord godt nok - og lenge nok - til å henge med i handlingen
- Føle mestring

---

## 🧱 Arkitektur

Prosjektet er bygget med en enkel filstrukur:
- main.py henter ord og definisjoner fra tekst-filer, og viser de én for én
- new_vocbulary.py hjelper å lage en liste over ukjente ord (kan brukes fortløpende når man leser)
- .txt filene inneholder ord, oversettelser og definisjoner, gitt av en AI

Dette gjør prosjektet:
- Enkelt å tilføye nye ord
- Enkelt å bruke

---

## 🔌 Skrivefeil-integrasjoner

Biblioteket Difflib blir brukt for å gjenkjenne små skrivefeil, for å ikke demotivere brukeren. To små linjer i koden, men en stor påvirkning på psykologien og motivasjonen.
```
def similarity(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()
```

## 💡 Hva jeg lærte

- Hvordan bruke og utnytte terminalen som et verktøy
- Hvordan hjernen tilegner seg kunnskap basert på mestring og rask respons
- Hvordan integrere buffere for å gjøre interaksjonen mer dynamisk
- Programmeringens potensialet for personlig utvikling

## 🔮 Videre utvikling

- Automatisk formatert og utfylt .txt fil, ved bruk av API
- Forbedret UI, lage en simpel web-applikasjon
