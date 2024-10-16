from api import mongo
from ..models.Model import Fazendeiro
from bson import ObjectId

class FazendeiroService:
    def save(fazendeiro):
        novoFazendeiro = mongo.db.fazendeiros.insert_one({
            "nome": fazendeiro.nome,
            "idade": fazendeiro.idade,
            "endereco": fazendeiro.endereco,
            "telefone": fazendeiro.telefone
        })
        
        return mongo.db.fazendeiros.find_one({
            "_id": ObjectId(novoFazendeiro.inserted_id),
        })
        
    def update(self, id):
        fazendeiroAtualizado = mongo.db.fazendeiros.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": {
                "nome": self.nome,
                "idade": self.idade,
                "endereco": self.endereco,
                "telefone": self.telefone   
            }},
            return_document=True,
        )
        
        return fazendeiroAtualizado
        
    @staticmethod
    def findAll():
        return list(mongo.db.fazendeiros.find())
    
    @staticmethod
    def findById(id):
        return mongo.db.fazendeiros.find_one({
            "_id": ObjectId(id)
        })
        
    @staticmethod
    def delete(id):
        mongo.db.fazendeiros.delete_one({
            "_id": ObjectId(id)
        })