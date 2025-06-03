from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from waitress import serve
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necessario per flash messages
DB_PATH = os.path.join("data", "bakery.db")

def get_prodotti():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT id, nome, descrizione FROM prodotti")
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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        nome = request.form["nome"]
        cognome = request.form["cognome"]
        password = request.form["password"]
        email = request.form["email"]
        telefono = request.form["telefono"]

        # Cifra la password prima di salvarla
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO utente (username, nome, cognome, password, email, telefono) VALUES (?, ?, ?, ?, ?, ?)",
                (username, nome, cognome, hashed_password, email, telefono)
            )
            conn.commit()
            flash("Registrazione completata! Ora puoi accedere.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username o email già esistenti.", "danger")
        finally:
            conn.close()
    return render_template("register.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)