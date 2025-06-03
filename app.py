from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join("data", "bakery.db")

def get_prodotti():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT nome, descrizione, prezzo, immagine FROM prodotti")
    prodotti = cur.fetchall()
    conn.close()
    return prodotti

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prodotti")
def prodotti():
    items = get_prodotti()
    return render_template("prodotti.html", prodotti=items)

if __name__ == "__main__":
    app.run(debug=True)

