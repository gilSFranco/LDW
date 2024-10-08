from flask_restful import Resource
from api import api

class GameList(Resource):
    def get(self):
        return "Hello, world! Api rodando."
    
class RecursosAPI(Resource):
    def get(self):
        return "GET /api/v1/test"
    
    def post(self):
        return "POST /api/v1/test"
    
    def put(self):
        return "PUT /api/v1/test"
    
    def delete(self):
        return "DELETE /api/v1/test"

api.add_resource(GameList, '/games')
api.add_resource(RecursosAPI, '//api/v1/test')