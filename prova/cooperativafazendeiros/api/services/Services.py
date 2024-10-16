from api import mongo
from ..models import Model
from bson import ObjectId

class UsuarioService():
    def save(usuario):
        novoUsuario = mongo.db.usuarios.insert_one({
            "nome": usuario.nome,
            "email": usuario.email,
        })
        
        return mongo.db.usuarios.find_one({
            "_id": ObjectId(novoUsuario.inserted_id),
        })
        
    def update(self, id):
        usuarioAtualizado = mongo.db.usuarios.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": {
                "nome": self.nome,
                "email": self.email,
            }},
            return_document=True
        )
        
        return usuarioAtualizado
    
    @staticmethod
    def findAll():
        return list(mongo.db.usuarios.find())
    
    @staticmethod
    def findById(id):
        return mongo.db.usuarios.find_one({
            "_id": ObjectId(id),
        })
        
    @staticmethod
    def delete(id):
        mongo.db.usuarios.delete_one({
            "_id": ObjectId(id),
        })