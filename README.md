# Youtube-converter: downloader.py Usage Guide

## 1. Installazione della libreria Pytubefix
Per utilizzare lo script `downloader.py`, è necessario installare la libreria [Pytubefix](https://pypi.org/project/pytubefix/). Si consiglia di farlo in un ambiente virtuale dedicato (.venv) per evitare conflitti tra dipendenze.

### Creazione ambiente virtuale e installazione
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Su Windows
pip install pytubefix
```

## 2. Modifica dei percorsi (PATH) nel codice
**Prima di eseguire lo script, assicurati di aver modificato correttamente i percorsi (PATHS) relativi alla cartella `videos` e al file CSV** in base alla struttura delle directory del tuo PC e file system. Verifica che i percorsi impostati nel codice corrispondano alle tue cartelle locali per evitare errori di lettura/scrittura.
Assicurati di modificare questi valori nel codice in base alla posizione reale dei tuoi file e cartelle. Ad esempio, se il file CSV si trova in una cartella diversa, aggiorna `CSV_PATH` con il percorso completo, come:

```python
CSV_PATH = "C:/Users/.../miei_csv/prova_estrazione.csv"
VIDEOS_FOLDER = "C:/Users/.../Youtube-converter/videos"
```

## 3. Cartella di destinazione dei video
Lo script salva i video scaricati nella cartella `videos` all'interno del progetto. Se la cartella non esiste, viene creata automaticamente.

## 4. Formato del file CSV
- Il file CSV deve contenere una sola colonna con header **videoId**.
- Ogni riga può contenere **l'ID di uno short** (oppure **il link completo** di uno short YouTube, ma solo se decommentato il codice) .
- Esempio di CSV:
    ```csv
    videoId
    dQw4w9WgXcQ
    https://www.youtube.com/shorts/abc123xyz
    ```

## 5. Funzionamento dello script
- Se il file CSV (`prova_estrazione.csv`) **non è presente**, lo script permette di crearne uno tramite input da tastiera. Inserisci i link uno alla volta e digita `done` per terminare.
- Se il file CSV **esiste**, lo script legge ogni riga e scarica il video corrispondente:
    - Se la riga contiene solo l'ID, viene costruito il link completo.
    - Se la riga contiene il link, viene usato direttamente.

## 6. Avvio dello script
Esegui lo script con:
```bash
python downloader.py
```
Segui le istruzioni a schermo per inserire i link se necessario.

---
**Nota:** Assicurati di avere i permessi di scrittura nella cartella del progetto e una connessione internet attiva per scaricare i video.