from studente import Studente
studenti = []

def mostra_menu():
    print("\n--- MENU ---")
    print("1. Aggiungi studente")
    print("2. Aggiungi voto a studente")
    print("3. Stampa schede")
    print("4. Mostra lo studente migliore")
    print("5. Esci")

while True:
    mostra_menu()
    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input(">Nome: ")
        cognome = input(">Cognome: ")
        data_di_nascita = int(input(">Data di nascita: "))
        nuovo = Studente(nome, cognome, data_di_nascita)
        studenti.append(nuovo)
        print("Studente aggiunto con successo!")

    elif scelta == "2":
        if not studenti:
            print("Non ci sono studenti registrati.")
            continue

        for i,s in enumerate(studenti):
            print(f"{i}. {s.name} {s.cognome}")
        index = int(input("Scegli lo studente(numero): "))
        voto = float(input(">Voto: "))
        studenti[index].aggiungi_voto(voto)
        print("Voto aggiunto con successo!")


    elif scelta == "3":

        if not studenti:
            print("Nessuno studente registrato.")
            continue

        print("\n--- SCHEDE STUDENTI ---")
        for studente in studenti:
            studente.scheda()

    elif scelta == "4":

        migliore = None
        media_massima = -1

        if not studenti:
            print("Nessuno studente registrato.")
            continue

        for s in studenti:
            media = s.media() if s.voti else 0
            if media > media_massima:
                media_massima = media
                migliore = s

        if migliore:
            print(f"\nLo studente con la media più alta è {migliore.name} {migliore.cognome} con media {media_massima}")
        else:
            print("Nessuno studente ha voti registrati.")


    elif scelta == "5":
        print("Uscita dal programma.")
        break