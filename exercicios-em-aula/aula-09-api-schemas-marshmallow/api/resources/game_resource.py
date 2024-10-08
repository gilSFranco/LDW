from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import game_schema
from ..models import game_model
from ..services.game_service import GameService

class GameList(Resource):
    def get(self):
        games = GameService.get_games()
        game = game_schema.GameSchema(many=True)
        return make_response(game.jsonify(games), 200)
    
    def post(self):
        gameschema = game_schema.GameSchema()
        validate = gameschema.validate(request.json)
        
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            # Capturar os dados do json
            json_data = request.get_json()
            # Cria uma nova instancia da classe Game usando o desempacotamento
            new_game = game_model.Game(**json_data)
            result = GameService.add_game(new_game)
            
            response = gameschema.jsonify(result)
            
            return make_response(response, 201)
        
class GameDetails(Resource):
    def get(self, id):
        game = GameService.get_game_by_id(id)
        
        if game is None:
            return make_response(jsonify("Game não encontrado."), 400)
        
        gameschema = game_schema.GameSchema()
        return make_response(gameschema.jsonify(game), 200)
    
    def put(self, id):
        game_bd = GameService.get_game_by_id(id)
        
        if game_bd is None:
            return make_response(jsonify("Game não foi encontrado."), 404)
        
        gameschema = game_schema.GameSchema()
        validate = gameschema.validate(request.json)
        
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_game = game_model.Game(**json_data)
            updated_game = GameService.update_game(new_game, id)
            return make_response(gameschema.jsonify(updated_game), 200)
        
    def delete(self, id):
        game_bd = GameService.get_game_by_id(id)
        
        if game_bd is None:
            return make_response(jsonify("Game não foi encontrado."), 404)
        
        GameService.delete_game(id)
        return make_response(jsonify("Game excluido com sucesso."), 200)

api.add_resource(GameList, '/games')
api.add_resource(GameDetails, '/game/<id>')
