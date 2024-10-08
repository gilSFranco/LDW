from flask import Flask, render_template
from controllers import routes
from models.database import mongo, Game
import os

app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Definindo a string de conexão
app.config['MONGO_URI'] = 'mongodb://localhost:27017/games'

if __name__ == '__main__':
    # Verifica no início da aplicação se o BD já existe. Caso contrário ele criará o BD.
    mongo.init_app(app=app)
    # db.create_all()
    with app.app_context():
        if 'games' not in mongo.db.list_collection_names():
            game = Game(
                titulo='',
                ano=0,
                categoria='',
                plataforma='',
                preco=0,
                quantidade=0,
            )
            
            game.save()
            
    app.run(host='localhost', port=5000, debug=True) 