from flask import Flask, render_template, jsonify, Response
from dotenv import load_dotenv
from datetime import datetime
from google import genai
from google.genai import types
from db_utils import init_db, salva_descrizione, get_ultime_descrizioni
import cv2
import os
import atexit

app = Flask(__name__)

# ==== INIZIALIZZAZIONE ====
load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)
init_db()

# ==== WEBCAM GLOBALE ====
video_capture = cv2.VideoCapture(0)

@atexit.register
def cleanup():
    """Chiude correttamente la webcam alla chiusura dell'app"""
    if video_capture.isOpened():
        video_capture.release()

# ==== ROUTE VIDEO STREAM ====
def genera_frame():
    """Genera stream MJPEG continuo dalla webcam"""
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route("/video_feed")
def video_feed():
    """Endpoint MJPEG per lo streaming webcam"""
    return Response(genera_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# ==== ROUTE FLASK ====
@app.route("/")
def index():
    """Pagina principale"""
    return render_template("index.html")

@app.route("/descrizione", methods=["GET"])
def descrizione():
    """Cattura immagine, invia a Gemini, restituisce descrizione"""
    ret, frame = video_capture.read()
    if not ret:
        return jsonify({"error": "Webcam non disponibile"}), 500

    success, image_bytes = cv2.imencode('.jpg', frame)
    if not success:
        return jsonify({"error": "Errore immagine"}), 500

    image_bytes = image_bytes.tobytes()

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
            "Descrivi cosa sta accadendo in questa immagine in meno di 50 caratteri. Solo la descrizione, senza spiegazioni."
        ]
    )

    caption = response.text.strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    salva_descrizione(caption, timestamp)

    return jsonify({"caption": caption, "timestamp": timestamp})

@app.route("/storico")
def storico():
    """Restituisce le ultime descrizioni dal database"""
    return jsonify(get_ultime_descrizioni())

# ==== AVVIO SERVER ====
if __name__ == "__main__":
    app.run(debug=True)
