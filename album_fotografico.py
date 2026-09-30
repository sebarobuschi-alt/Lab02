from csv import reader
import operator
from operator import truediv


def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    album = {}
    in_file_path = file_path
    try:
        # L'uso di 'with' è consigliato perché chiude il file in automatico
        with open(file = in_file_path, mode = 'r') as infile:
            csvreader = reader(infile)
            next(csvreader, None)

            for row in csvreader:

                if not row:
                    continue

                codice = row[0]
                titolo = row[1]
                autore = row[2]
                mese = row[3]
                anno = row[4]

                caratteristiche_foto = [codice, titolo, autore, mese]


                if anno not in album:

                    album[anno] = [caratteristiche_foto]
                else:

                    album[anno].append(caratteristiche_foto)


        for anno, foto in sorted(album.items()):
            print(f'{anno}: {foto}')
        return album

    except FileNotFoundError:
        print('File non trovato')






def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    if


def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    lista_codici = []
    for anno in album:
        lista_foto = album[anno]
        for i in range(len(lista_foto)):
            caratteristiche_foto =  lista_foto[i]
            codice_foto = caratteristiche_foto[0]
            if codice== codice_foto:

               trovato = True
               break
            else:
                trovato = False

        if trovato:
            risultato = f"{','.join(caratteristiche_foto)},{anno}"
            break

        else:
            risultato = None
    return risultato
def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    titoli = []
    anno_str = str(anno)
    if anno_str  in album:
        lista_foto = album[anno_str]
        for i in range(len(lista_foto)):
            caratteristiche_foto = lista_foto[i]
            titolo = caratteristiche_foto[1]
            titoli.append(titolo)
        titoli_ordinati = sorted(titoli)

    else:
        titoli = None
    return titoli_ordinati



def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)

                if album is not None:
                    break
            print(album)

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
