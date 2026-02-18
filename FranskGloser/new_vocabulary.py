import pyperclip
import os

# ──────────────────────────────
vocabulaire = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    mot = input("Entrez un nouveau mot de vocabulaire (ou 'q' pour quitter) : ").strip()
    if mot.lower() == 'q' or mot == '':
        break
    if mot.lower() in vocabulaire:
        continue
    vocabulaire.append(mot.lower())
pyperclip.copy("\n".join(vocabulaire))