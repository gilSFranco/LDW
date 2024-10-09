from api import app, mongo
from api.models.BoardGameModel import Sheet
from api.services.BoardGameService import BoardGameService

if __name__ == '__main__':
    with app.app_context():
        if 'sheets' not in mongo.db.list_collection_names():
            sheet = Sheet(
                name = '',
                level = 0,
                classes = '',
                background = '',
                race = '',
                alignment = '',
                strength = 0,
                dexterity = 0,
                constitution = 0,
                intelligence = 0,
                wisdom = 0,
                charisma = 0
            )
            
            BoardGameService.save(sheet)
    app.run(port=5000, debug=True)