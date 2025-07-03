from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definição dos modelos de dados - Pessoas
class Pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    registro_id = db.Column(db.String(36), unique=True, nullable=False)

# Definição dos modelos de dados - Filmes
class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    data_lancamento = db.Column(db.Integer, nullable=False)
    registro_id = db.Column(db.String(36), nullable=False)

# Definição dos modelos de dados - Reservas e Aluguéis
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    registro_id = db.Column(db.String(36), nullable=False)
