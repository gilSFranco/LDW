from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo

# Criando a instância do Flask
app = Flask(__name__)

# Definindo o endereço do banco
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api_games'

# Criando a instancia da Api do flask_restful e passando o Flask
api = Api(app)

# Criando a instancia do PyMongo
mongo = PyMongo(app)

from .views import games_views