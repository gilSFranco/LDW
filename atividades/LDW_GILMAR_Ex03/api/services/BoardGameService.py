from api import mongo
from ..models import BoardGameModel
from bson import ObjectId

class BoardGameService:
    def save(sheet):
        newSheet = mongo.db.sheets.insert_one({
            'name': sheet.name,
            'level': sheet.level,
            'classes': sheet.classes,
            'background': sheet.background,
            'race': sheet.race,
            'alignment': sheet.alignment,
            'skillpoints': sheet.skillpoints
        })
        
        return mongo.db.sheets.find_one({
            '_id': ObjectId(newSheet.inserted_id)
        })
        
    @staticmethod
    def findAll():
        return list(mongo.db.sheets.find())
    
    @staticmethod
    def findById(id):
        return mongo.db.sheets.find_one({
            '_id': ObjectId(id)
        })
        
    def update(self, id):
        updatedSheet = mongo.db.sheets.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {
                'name': self.name,
                'level': self.level,
                'classes': self.classes,
                'background': self.background,
                'race': self.race,
                'alignment': self.alignment,
                'skillpoints': self.skillpoints
            }},
            return_document=True
        )
        
        return updatedSheet
        
    @staticmethod
    def delete(id):
        mongo.db.sheets.delete_one({
            '_id': ObjectId(id)
        })