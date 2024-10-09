from api import mongo
from ..models import BoardGameModel
from bson import ObjectId

class BoardGameService:
    def save(sheet):
        newSheet = mongo.db.insert_one({
            'name': sheet.name,
            'level': sheet.level,
            'classes': sheet.classes,
            'background': sheet.background,
            'race': sheet.race,
            'alignment': sheet.alignment,
            'strength': sheet.strength,
            'dexterity': sheet.dexterity,
            'constitution': sheet.constitution,
            'intelligence': sheet.intelligence,
            'wisdom': sheet.wisdom,
            'charisma': sheet.charisma
        })
        
        return mongo.db.find_one({
            '_id': ObjectId(newSheet.inserted_id)
        })