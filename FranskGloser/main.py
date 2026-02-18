import random
import os
import sys
import shutil
import difflib

# ──────────────────────────────
# Terminal UI system
# ──────────────────────────────

class UI:
    RESET = "\033[0m"
    BOLD = "\033[1m"

    COLORS = {
        "title": "\033[38;5;81m",
        "text": "\033[38;5;252m",
        "muted": "\033[38;5;244m",
        "definition": "\033[38;5;255m",
        "success": "\033[38;5;82m",
        "error": "\033[38;5;203m",
        "accent": "\033[38;5;214m",
        "bar_fg": "\033[38;5;82m",
        "bar_bg": "\033[38;5;238m",
        "history": "\033[38;5;240m",
    }

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def width():
        return shutil.get_terminal_size((80, 20)).columns

    @staticmethod
    def divider(char="─"):
        print(UI.COLORS["muted"] + char * UI.width() + UI.RESET)

    @staticmethod
    def center(text, color="text", bold=False):
        style = UI.COLORS[color] + (UI.BOLD if bold else "")
        print(style + text.center(UI.width()) + UI.RESET)

    @staticmethod
    def label(text, color="text", bold=False):
        style = UI.COLORS[color] + (UI.BOLD if bold else "")
        print(style + text + UI.RESET)

    @staticmethod
    def input(prompt):
        return input(UI.COLORS["muted"] + prompt + UI.RESET).strip()

    @staticmethod
    def progress(current, total, correct):
        bar_width = 30
        filled = int(bar_width * current / total)
        bar = (
            UI.COLORS["bar_fg"] + "█" * filled +
            UI.COLORS["bar_bg"] + "░" * (bar_width - filled)
        )
        print(f"{bar}{UI.RESET}  {current}/{total}  ✅ {correct}")


# ──────────────────────────────
# Utility functions
# ──────────────────────────────

def similarity(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def list_vocab_files():
    return [f for f in os.listdir() if f.endswith(".txt")]


def menu(title, options):
    while True:
        UI.clear()
        UI.center(title, "title", bold=True)
        UI.divider()

        for i, opt in enumerate(options, start=1):
            UI.label(f"{i}. {opt}")

        UI.divider()
        choice = UI.input("Choix > ")

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]


# ──────────────────────────────
# Vocabulary handling
# ──────────────────────────────

def charger_vocabulaire(fichier):
    vocabulaire = []
    with open(fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            if "|" in ligne:
                parts = [p.strip() for p in ligne.split("|")]
                if len(parts) == 3:
                    vocabulaire.append(tuple(parts))
    return vocabulaire


def afficher_historique(inconnus):
    if not inconnus:
        return
    UI.divider("·")
    UI.label("À revoir :", "history", bold=True)
    for mot, definition, anglais in inconnus[-5:]:
        UI.label(f"- {mot} ({anglais}) : {definition}", "history")
    UI.divider("·")


# ──────────────────────────────
# Learning session
# ──────────────────────────────

def apprendre(vocabulaire, mode):
    random.shuffle(vocabulaire)

    total = len(vocabulaire)
    correct = 0
    inconnus = []

    for i, (fr, definition, en) in enumerate(vocabulaire, start=1):
        UI.clear()
        UI.center("Apprentissage du vocabulaire", "title", bold=True)
        UI.divider()
        UI.progress(i - 1, total, correct)
        afficher_historique(inconnus)
        UI.divider()

        UI.label("Définition :", "muted", bold=True)
        UI.label(definition, "definition")
        UI.divider()

        attendu = fr if mode == "FR" else en
        langue = "Français" if mode == "FR" else "Anglais"

        UI.label(f"Réponse attendue : {langue}", "accent")
        UI.label("Aides : ! première lettre   ? traduction anglaise", "muted")

        while True:
            reponse = UI.input("Réponse > ")

            if reponse == "!":
                UI.label(f"🔤 Première lettre : {attendu[0]}", "accent")
                continue

            if reponse == "?":
                if mode == "FR":
                    UI.label(f"🇬🇧 Anglais : {en}", "accent")
                else:
                    UI.label("ℹ️ Aide indisponible dans ce mode.", "muted")
                continue

            if reponse.lower() == attendu.lower():
                UI.label("✅ Correct !", "success", bold=True)
                correct += 1
                break

            sim = similarity(reponse, attendu)
            if sim >= 0.8:
                UI.label("⚠️ Petite faute détectée.", "accent", bold=True)
                UI.label(f"Mot correct : {attendu}", "definition")
                while True:
                    retry = UI.input("Recopie exactement > ")
                    if retry.lower() == attendu.lower():
                        UI.label("✅ Bien corrigé.", "success")
                        correct += 1
                        break
                    else:
                        UI.label("❌ Pas encore exact.", "error")
                break
            else:
                UI.label(f"❌ Faux — réponse : {attendu}", "error", bold=True)
                while True:
                    retry = UI.input("Recopie exactement > ")
                    if retry.lower() == attendu.lower():
                        UI.label("✅ Bien recopié.", "success")
                        break
                    else:
                        UI.label("❌ Toujours pas exact.", "error")
                inconnus.append((fr, definition, en))
                break

    UI.clear()
    UI.center("🎉 Session terminée !", "success", bold=True)
    UI.progress(total, total, correct)
    return inconnus


# ──────────────────────────────
# Main entry point
# ──────────────────────────────

if __name__ == "__main__":
    fichiers = list_vocab_files()
    if not fichiers:
        UI.label("Aucun fichier .txt trouvé.", "error", bold=True)
        sys.exit(1)

    fichier = menu("Choisis un fichier de vocabulaire", fichiers)
    mode_choisi = menu(
        "Mode d'apprentissage",
        [
            "Définition → Français (par défaut)",
            "Définition → Anglais"
        ]
    )

    mode = "FR" if "Français" in mode_choisi else "EN"
    vocabulaire = charger_vocabulaire(fichier)

    inconnus = apprendre(vocabulaire, mode)

    if inconnus:
        with open("vocabulaire_inconnu.txt", "w", encoding="utf-8") as f:
            for fr, definition, en in inconnus:
                f.write(f"{fr} | {definition} | {en}\n")
