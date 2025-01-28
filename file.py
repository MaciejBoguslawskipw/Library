import os
import time

class DirectoryMonitor:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.znane_pliki = set(os.listdir(sciezka))
    def monitoruj(self):
        while True:
            aktualne_pliki = set(os.listdir(self.sciezka))
            nowe_pliki = aktualne_pliki - self.znane_pliki
            if nowe_pliki:
                print("Wykryto nowe pliki:", nowe_pliki)
                self.znane_pliki = aktualne_pliki
            time.sleep(2)

class TodoApp:
    def __init__(self):
        self.zadania = []
    def dodaj_zadanie(self, tytul, priorytet):
        self.zadania.append({"tytul": tytul, "priorytet": priorytet, "ukonczone": False})
        with open("todo.log", "a", encoding="utf-8") as f:
            f.write(f"Dodano zadanie: {tytul}, priorytet: {priorytet}\n")
    def oznacz_ukonczone(self, tytul):
        for z in self.zadania:
            if z["tytul"] == tytul:
                z["ukonczone"] = True
                with open("todo.log", "a", encoding="utf-8") as f:
                    f.write(f"Oznaczono jako ukończone: {tytul}\n")
    def pokaz_zadania(self, tylko_ukonczone=None):
        posortowane = sorted(self.zadania, key=lambda x: ["wysoki","średni","niski"].index(x["priorytet"]))
        for z in posortowane:
            if (tylko_ukonczone is None) or (z["ukonczone"] == tylko_ukonczone):
                print(f"{z['tytul']} | Priorytet: {z['priorytet']} | Ukończone: {z['ukonczone']}")
