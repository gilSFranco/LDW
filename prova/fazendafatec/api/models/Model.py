from api import mongo

class Fazendeiro():
    def __init__(self, nome, idade, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone