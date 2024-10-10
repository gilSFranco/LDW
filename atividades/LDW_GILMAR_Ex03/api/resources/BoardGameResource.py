from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import BoardGameSchema
from ..models import BoardGameModel
from ..services.BoardGameService import BoardGameService

class BoardGameResource(Resource):
    def get(self):
        sheets = BoardGameService.findAll()
        sheet = BoardGameSchema.BoardGameSchema(many=True)
        
        return make_response(sheet.jsonify(sheets), 200)
    
    def post(self):
        boardgame = BoardGameSchema.BoardGameSchema()
        validate = boardgame.validate(request.json)
        
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            jsonData = request.get_json()
            newBoardGame = BoardGameModel.Sheet(**jsonData)
            
            result = BoardGameService.save(newBoardGame)
            
            response = boardgame.jsonify(result)
            
            return make_response(response, 201)
        
class BoardGameDetails(Resource):
    def get(self, id):
        sheet = BoardGameService.findById(id)
        
        if sheet is None:
            return make_response(jsonify({'message': 'BoardGame not found'}), 404)
        
        boardgame = BoardGameSchema.BoardGameSchema()    
        return make_response(boardgame.jsonify(sheet), 200)
    
    def put(self, id):
        sheet = BoardGameService.findById(id)
        
        if sheet is None:
            return make_response(jsonify({'message': 'BoardGame not found'}), 404)
        
        boardgame = BoardGameSchema.BoardGameSchema()
        validate = boardgame.validate(request.json)
        
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            jsonData = request.get_json()
            newBoardGame = BoardGameModel.Sheet(**jsonData)
            
            updatedBoardGame = BoardGameService.update(newBoardGame, id)
            
            return make_response(boardgame.jsonify(updatedBoardGame), 200)
    
    def delete(self, id):
        sheet = BoardGameService.findById(id)
        
        if sheet is None:
            return make_response(jsonify({'message': 'BoardGame not found'}), 404)
        
        BoardGameService.delete(id)
        return make_response(jsonify({'message': 'BoardGame deleted successfully'}), 200)
        
api.add_resource(BoardGameResource, '/boardgames')
api.add_resource(BoardGameDetails, '/boardgame/<id>')