# 🎥 Gemini Webcam Analyzer

Web app Flask per il monitoraggio in tempo reale tramite webcam con generazione automatica di descrizioni grazie al modello multimodale **Gemini 2.0 Flash** di Google.

---

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

4.Crea un file .env con la tua chiave API Gemini

5. Avvia l'app
