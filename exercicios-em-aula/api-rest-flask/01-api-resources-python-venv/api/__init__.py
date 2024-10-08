from flask import Flask
from flask_restful import Api

# Criando a instância do Flask
app = Flask(__name__)

# Criando a instancia da Api do flask_restful e passando o Flask
api = Api(app)

from .resources import game_resource