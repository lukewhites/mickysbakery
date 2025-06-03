CREATE TABLE ordine (
    id_ordine INTEGER PRIMARY KEY AUTOINCREMENT,
    data_ordine DATE
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
	