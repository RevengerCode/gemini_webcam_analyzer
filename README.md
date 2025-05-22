# 🎥 Gemini Webcam Analyzer

Questa web app, sviluppata con Flask, consente di monitorare in tempo reale ciò che accade davanti a una webcam locale. Ogni 5 secondi oppure ogni volta che si clicca sul pulsante di cattura, il sistema cattura un'immagine e la invia a Gemini 2.0 Flash. Il modello analizza l'immagine e restituisce una breve descrizione testuale del comportamento osservato.

Tutte le descrizioni generate vengono poi salvate automaticamente in un database MySQL, insieme al relativo timestamp, permettendo così la costruzione di uno storico consultabile e utilizzabile per analisi successive.


## 🚀 Funzionalità

- ✅ Streaming live della webcam su browser (via MJPEG)
- ✅ Descrizione automatica delle immagini in tempo reale con Google Gemini
- ✅ Salvataggio delle descrizioni in un database **MySQL**
- ✅ Interfaccia web semplice e responsiva con HTML/CSS/JavaScript
- ✅ Visualizzazione dello **storico** delle descrizioni archiviate

---

## 🧠 Tecnologie utilizzate

| Componente         | Ruolo                                               |
|--------------------|-----------------------------------------------------|
| Flask              | Web framework leggero                               |
| OpenCV (`cv2`)     | Acquisizione immagini dalla webcam                  |
| google-generativeai|  Interazione con il modello Gemini 2.0 di Google    |
| MySQL              | Database relazionale per lo storico delle descrizioni |
| python-dotenv      | Gestione sicura delle chiavi API (`.env`)           |

---

## 🛠 Installazione

1. Clona il repository:

```bash
git clone https://github.com/TUO_USERNAME/gemini_webcam_analyzer.git
cd gemini_webcam_analyzer
```

2.Crea un ambiente virtuale
```bash
python -m venv .venv
source .venv/bin/activate  # su Linux/macOS
.venv\\Scripts\\activate   # su Windows
```

3.Installa le dipendenze:

```bash
pip install -r requirements.txt
```

4.Crea un file .env con la tua chiave API Gemini:
```bash
API_KEY=la_tua_api_key_google
```

5. Avvia l'app e vai in localhost
```bash
python app.py
```
