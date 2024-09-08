from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Ficha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    classe = db.Column(db.String(150))
    antecedente = db.Column(db.String(150))
    raca = db.Column(db.String(150))
    tendencia = db.Column(db.String(150))
    forca = db.Column(db.Integer)
    destreza = db.Column(db.Integer)
    constituicao = db.Column(db.Integer)
    inteligencia = db.Column(db.Integer)
    sabedoria = db.Column(db.Integer)
    carisma = db.Column(db.Integer)
    
    def __init__(self, nome, classe, antecedente, raca, tendencia, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        self.nome = nome
        self.classe = classe
        self.antecedente = antecedente
        self.raca = raca
        self.tendencia = tendencia
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        
class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade