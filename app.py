from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os
from waitress import serve
from werkzeug.security import generate_password_hash, check_password_hash
import re

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

@app.before_request
def require_login():
    allowed_routes = ['login', 'register', 'static']
    if request.endpoint not in allowed_routes and 'user_id' not in session:
        return redirect(url_for('login'))

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/prodotti")
def prodotti():
    items = get_prodotti()
    return render_template("prodotti.html", prodotti=items)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT id, password FROM utente WHERE username = ?", (username,))
        user = cur.fetchone()
        conn.close()
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            flash("Login effettuato con successo!", "success")
            return redirect(url_for("prodotti"))
        else:
            flash("Username o password errati.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    flash("Logout effettuato.", "success")
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        nome = request.form["nome"]
        cognome = request.form["cognome"]
        password = request.form["password"]
        email = request.form["email"]
        telefono = request.form["telefono"]

        # Criteri di sicurezza per la password
        password_criteria = [
            (len(password) >= 8, "La password deve essere lunga almeno 8 caratteri."),
            (re.search(r"[A-Z]", password), "La password deve contenere almeno una lettera maiuscola."),
            (re.search(r"[a-z]", password), "La password deve contenere almeno una lettera minuscola."),
            (re.search(r"\d", password), "La password deve contenere almeno un numero."),
            (re.search(r"[!@#$%^&*(),.?\":{}|<>]", password), "La password deve contenere almeno un carattere speciale."),
        ]
        for valid, error in password_criteria:
            if not valid:
                flash(error, "danger")
                return render_template("register.html")

        # Controllo se username già esistente
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT id FROM utente WHERE username = ?", (username,))
        if cur.fetchone():
            flash("Username già esistente. Scegli un altro username.", "danger")
            conn.close()
            return render_template("register.html")

        # Cifra la password prima di salvarla
        hashed_password = generate_password_hash(password)

        try:
            cur.execute(
                "INSERT INTO utente (username, nome, cognome, password, email, telefono) VALUES (?, ?, ?, ?, ?, ?)",
                (username, nome, cognome, hashed_password, email, telefono)
            )
            conn.commit()
            flash("Registrazione completata! Ora puoi accedere.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Errore durante la registrazione.", "danger")
        finally:
            conn.close()
    return render_template("register.html")

if __name__ == "__main__":
    print("App is being executed on http://localhost:8080/")
    serve(app, host="0.0.0.0", port=8080)