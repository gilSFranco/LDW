from api import mongo

class UsuarioModel():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email