INSERT INTO utente (username, password, nome, cognome, email, telefono) VALUES
('admin','admin123', 'Admin', 'Bakery', 'admin@mickysbakery.it', '0000000000'),
('luca', 'Luca123','Luca', 'Bianchi', 'luca.bianchi@example.com', '3331234567'),
('marco', 'Marco123', 'Marco', 'Rossi', 'marco.rossi@example.com', '3349876543');

INSERT INTO prodotti (nome, descrizione, prezzo) VALUES
('Cupcake', 'tempo produzione 3-4 gg', 1.20),
('Brownie al caramello', NULL, 2.50),
('Torta alle mele', 'Torta coperta di pastafrolla con all interno mele, cannella e uvetta ', 15.00),
('Cookies', 'cookies morbidi', 2.00);

INSERT INTO ordine (username, data_ordine, stato_ordine) VALUES
('luca', '2025-06-01', NULL),
('marco', '2025-06-02', 'completato'),
('luca', '2025-06-03', 'in lavorazione');

INSERT INTO ordine_prodotto (id_ordine, id_prodotto, quantita) VALUES
(1, 1, 2),
(1, 3, 1);

INSERT INTO ordine_prodotto (id_ordine, id_prodotto, quantita) VALUES
(2, 4, 3);

INSERT INTO ordine_prodotto (id_ordine, id_prodotto, quantita) VALUES
(3, 2, 1),
(3, 1, 1),
(3, 4, 1);
