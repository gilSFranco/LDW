from api import app, mongo

if __name__ == '__main__':
    with app.app_context():
        if 'sheet' not in mongo.db.list_collection_names():
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
    
    app.run(port=5000, debug=True)