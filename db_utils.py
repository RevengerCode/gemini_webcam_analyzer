import mysql.connector

# 🔧 Configurazione DB (modifica con i tuoi dati)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Unigio01=',
    'database': 'multimodal_llm'
}

# Crea la tabella se non esiste
def init_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Descrizioni (
            id INT AUTO_INCREMENT PRIMARY KEY,
            caption TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Salva una descrizione nel DB
def salva_descrizione(caption, timestamp):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Descrizioni (caption, timestamp)
        VALUES (%s, %s)
    """, (caption, timestamp))
    conn.commit()
    cursor.close()
    conn.close()

def get_ultime_descrizioni(n=10):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT caption, timestamp FROM Descrizioni ORDER BY id DESC LIMIT %s", (n,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"caption": r[0], "timestamp": r[1].strftime("%Y-%m-%d %H:%M:%S")} for r in rows]
