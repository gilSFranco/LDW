# Importando o Flask que está em app
from api import app, mongo
from api.models.game_model import Game
from api.services import game_service

if __name__ == '__main__':
    # Criando o banco e a coleção se não existir
    with app.app_context():
        if 'games' not in mongo.db.list_collection_names():
            game = Game(
                title = '',
                genre = '',
                platform = '',
                year = 0
            )
            
            game_service.add_game(game)
    app.run(port=5000, debug=True)