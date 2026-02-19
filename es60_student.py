import json
import os

NOME_FILE = "stundenti.json"

def load_studenti(path=NOME_FILE):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []


def aggiungi_studente(path=NOME_FILE) -> tuble[bool, str, dict | None]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            studenti = json.load(f)
    except FileNotFoundError:
        studenti = [] 

    nome = input("Inserisci il nome dello studente: ").strip()
    voto_str = input("Inserisci il voto dello studente (0-10): ")

    if not nome:
        print("Errore: il nome non può essere vuoto")
        return

    try:
        voto = float(voto_str)
    except ValueError:
        print("Errore: il voto deve essere un numero.")
        return

    if voto < 0 or voto > 10:
        print("Errore: il voto deve essere tra 0 e 10.")
        return

    studente = {"nome": nome, "voto": voto}

    studenti.append(studente)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(studenti, f, indent=4, ensure_ascii=False)

    print(f"Aggiunto: {nome} con voto {voto}")


def salva_studenti(path=NOME_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(studenti, f, ensure_ascii=False, indent=4)

def visualizza_lista(studenti):
    if not studenti:
        print("Nessuno studente.")
        return
    for i in range(len(studenti)):
        s = studenti[i]
        print(f"{i}. {s['nome']} - Voto: {s['voto']}")

def mostra_dettagli(studenti, indice) -> tuble[bool, str, dict | None]:
    if indice < 0 or indice >= len(studenti):
        print("Indice non valido.")
        return
    s = studenti[indice]
    print(f"Nome: {s['nome']}")
    print(f"Voto: {s['voto']}")


def cancella_studente(studenti):
    visualizza_lista(studenti)
    indice_str = input("Indice da cancellare: ")

    try: 
        indice = int(indice_str)
    except ValueError:
        print("Errore indice non valido.")
        return
    
    nome = studenti[indice]["nome"]
    studenti.pop(indice)
    print(f"Cancellato: {nome}")


def aggiorna_studente(studenti):
    visualizza_lista(studenti)  
    indice_str = input("Indice da cancellare: ")

    try: 
        indice = int(indice_str)
    except ValueError:
        print("Errore indice non valido.")
        return

    if indice < 0 or indice >= len(studenti):
        print("Errore indice non valido.")
        return
    
    voto_str = input("Nuovo voto (0-10): ")
    try:
        voto = float(voto_str)
    except ValueError:
        print("Errore: voto deve essere un numero.")
        return
    
    if voto < 0 or voto > 10:
        print("Errore il voto deve essere positivo.")
        return

    studenti[indice]["voto"] = voto
    print(f"Aggiornato: {studenti[indice]['nome']} con voto {voto}")

def ricerca_per_nome(studenti):
    termine_di_ricerca = input("Termine di ricerca: ").strip().lower()
    if not termine_di_ricerca:
        print("Errore il termine non può essere vuoto.")
        return
    
    risultati = []
    for i in studenti:
        nome_in_minuscolo = i["nome"].lower()
        if termine_di_ricerca in nome_in_minuscolo:
            risultati.append(i)
    
    if not risultati:
        print("Nessuno studente trovato.")
        return
    
    print(f"Trovato {len(risultati)} risultato:")
    for i in risultati:
        print(f"{i['nome']} - Voto: {i['voto']}")

def filtra_per_voto(studenti):
    min_str = input("Voto minimo (0-10): ")
    try:
        min_voto = float(min_str)
    except ValueError:
        print("Errore numero non valido.")
        return

    max_str = input("Voto massimo (0-10): ")
    try:
        max_voto = float(max_str)
    except ValueError:
        print("Errore numero non valido.")
        return

    if min_voto < 0 or min_voto > 10 or max_voto < 0 or max_voto > 10:
        print("Errore i voti devono essere tra 0 e 10.")
        return

    if min_voto > max_voto:
        print("Errore il voto minimo non può essere maggiore del voto massimo.")
        return

    risultati = []
    for i in studenti:
        if min_voto <= i['voto']  <= max_voto:
            risultati.append(i)

    if not risultati:
        print("Nessuno studente.")
        return

    print(f"Trovato {len(risultati)} risultato:")
    for s in risultati:
        print(f"  {s['nome']} - Voto: {s['voto']}")

def statistiche(studenti):
    numero_studenti = print(f"Numero di studenti: {len(studenti)}")
    voto_max = max(studenti(voto_max))
    voto_min = min(studenti(voto_min))
    
    print(f"nome: {studenti(nome)}, voto: {max(studenti(voto))}") 
    print(f"nome: {studenti(nome)}, voto: {min(studenti(voto))}")



def main():

    studenti = load_studenti()

    while True:
        print("\n=== GESTIONE STUDENTI ===")
        print("1. Aggiungi studente")
        print("2. Visualizza lista")
        print("3. Visualizza dettaglio (per indice)")
        print("4. Aggiorna voto")
        print("5. Cancella studente")
        print("6. Ricerca per nome")
        print("7. Filtra per voto")
        print("8. Statistiche")
        print("9. Esci")

        scelta = input("\nScelta (1-9): ").strip()
    
        if scelta == "1":
            Aggiungi_studente = aggiungi_studente(path=NOME_FILE)
        elif scelta == "2":
            Visualizza_lista = visualizza_lista(studenti)
        elif scelta == "3":
            visualizza_lista(studenti)
            indice_str = input("Indice: ")
            try:
                indice = int(indice_str)
                mostra_dettagli(studenti, indice)
            except ValueError:
                print("Errore l'indice deve essere un numero.")
        elif scelta == "4":
            Aggiorna_voto = aggiorna_studente(studenti)
        elif scelta == "5":
            Cancella_studente = cancella_studente(studenti)
        elif scelta == "6": 
            Ricerca_per_nome = ricerca_per_nome(studenti)
        elif scelta == "7":
            Filtra_per_voto = filtra_per_voto(studenti)
        elif scelta == "8":
            Statistiche = statistiche(studenti)
        elif scelta == "9":
            print("Arrivederci")
            break
        else:
            print("Scelta non valida insescisci un dumero da 1 a 8.")

main()