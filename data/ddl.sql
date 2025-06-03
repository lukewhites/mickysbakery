CREATE TABLE ordine (
    id_ordine INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(55) NOT NULL,
    data_ordine DATE DEFAULT (DATE('now')),
    stato_ordine TEXT DEFAULT 'in attesa',
    FOREIGN KEY (username) REFERENCES utente(username)
);


CREATE TABLE prodotti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descrizione TEXT,
    prezzo REAL NOT NULL
);

CREATE TABLE utente(
	username VARCHAR(55) PRIMARY KEY,
	password VARCHAR(55),
	nome VARCHAR(255),
	cognome VARCHAR(255),
	email VARCHAR(255),
	telefono VARCHAR(10)
);

CREATE TABLE ordine_prodotto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_ordine INTEGER NOT NULL,
    id_prodotto INTEGER NOT NULL,
    quantita INTEGER DEFAULT 1,
    FOREIGN KEY (id_ordine) REFERENCES ordine(id_ordine),
    FOREIGN KEY (id_prodotto) REFERENCES prodotti(id)
);
