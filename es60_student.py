import json

def aggiungi_studente(path=NOME_FILE):
    nome: str(input("Inserisci il nome dello studente: ")).strip()
    voto_str: float(input("Inserisci il voto dello studente (0-10): "))

    if not nome:
        print("Errore il nome non può essere vuoto")
        return

    if voto < 0 or voto > 10:
        print("Errore il voto deve essere positivo.")
        return

    try:
        voto = float(voto_str)
    except ValueError:
        print("Errore voto deve essere un numero.")
        return

    studente = {"nome": nome, "voto": voto}
    studenti.append(studente)
    print(f"Aggiunto: {nome} con voto {voto}")

def salva_studenti(path=NOME_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(studenti, f, ensure_ascii=False, indent=4)

def Visualizza_lista(studenti):
    if not studenti:
        print("Nessuno studente.")
        return
    for i in range(len(studenti)):
        s = studenti[i]
        print(f"{i}. {s['nome']} - Voto: {s['voto']}")

def mostra_dettagli(studenti, indice):
    if indice < 0 or indice >= len(studenti):
        print("Indice non valido.")
        return
    s = studenti[indice]
    print(f"Nome: {s['nome']}")
    print(f"Voto: {s['voto']}")


def cancella_studente(studenti):
    mostra_lista(studenti)
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
    mostra_lista(studenti)  
    indice_str = input("Indice da cancellare: ")

    try: 
        indice = int(indice_str)
    except ValueError:
        print("Errore indice non valido.")
        return

    if indice < 0 or indice >= len(studenti):
        print("Errore indice non valido.")
        return

    voto_str: float(input("Nuovo voto (0-10): "))
    
    try:
        voto = float(voto_str)
    except ValueError:
        print("Errore voto deve essere un numero.")
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
        if min_voto <= s['voto']  <= max_voto:
            risultati.append(s)

    if not risultati:
        print("Nessuno studentein questo range.")
        return

    print(f"Trovato {len(risultati)} risultato:")
    for s in risultati:
        print(f"  {s['nome']} - Voto: {s['voto']}")


def main():
    
    NOME_FILE = "stundenti.json"
    
    try: 
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError,IOError):
        return []

    print("\n=== GESTIONE STUDENTI ===")
    print("1. Aggiungi studente")
    print("2. Visualizza lista")
    print("3. Visualizza dettaglio (per indice)")
    print("4. Aggiorna voto")
    print("5. Cancella studente")
    print("6. Ricerca per nome")
    print("7. Filtra per voto")
    print("8. Esci")

    scelta: int(input("Scelta: "))
    if scelta == "1":
        aggiungi_studente = aggiungi_studente(path=NOME_FILE)
    elif scelta == "2":
        Visualizza_lista = Visualizza_lista(studenti)
    elif scelta == "3":
        Visualizza_dettaglio = mostra_dettagli()

    