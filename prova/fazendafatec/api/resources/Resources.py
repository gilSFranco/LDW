from api import api
from flask import make_response, jsonify, request
from flask_restful import Resource
from ..models import Model
from ..schemas import Schema
from ..services.Services import FazendeiroService

class FazendeiroResource(Resource):
    def get(self):
        fazendeiros = FazendeiroService.findAll()
        validacaoFazendeiro = Schema.FazendeiroSchema(many=True)
        
        return make_response(validacaoFazendeiro.jsonify(fazendeiros), 200)
    
    def post(self):
        validacaoFazendeiro = Schema.FazendeiroSchema()
        validacao = validacaoFazendeiro.validate(request.json)
        
        if validacao:
            return make_response(jsonify(validacao), 400)
        else:
            corpoRequisicao = request.get_json()
            fazendeiro = Model.Fazendeiro(**corpoRequisicao)
            
            novoFazendeiro = FazendeiroService.save(fazendeiro)
            response = validacaoFazendeiro.jsonify(novoFazendeiro)
            
            return make_response(response, 201)
        
class FazendeiroDetails(Resource):
    def get(self, id):
        fazendeiro = FazendeiroService.findById(id)
        
        if fazendeiro is None:
            return make_response(jsonify({'erro': 'fazendeiro não encontrado'}), 404)
        
        validacaoFazendeiro = Schema.FazendeiroSchema()
        return make_response(validacaoFazendeiro.jsonify(fazendeiro), 200)
    
    def put(self, id):
        fazendeiro = FazendeiroService.findById(id)
        
        if fazendeiro is None:
            return make_response(jsonify({'erro': 'fazendeiro não encontrado'}), 404)
        
        validacaoFazendeiro = Schema.FazendeiroSchema()
        validacao = validacaoFazendeiro.validate(request.json)
        
        if validacao:
            return make_response(jsonify(validacao), 400)
        else:
            corpoRequisicao = request.get_json()
            fazendeiroRequisicao = Model.Fazendeiro(**corpoRequisicao)
            
            fazendeiroAtualizado = FazendeiroService.update(fazendeiroRequisicao, id)
            
            return make_response(validacaoFazendeiro.jsonify(fazendeiroAtualizado), 200)
    
    def delete(self, id):
        fazendeiro = FazendeiroService.findById(id)
        
        if fazendeiro is None:
            return make_response(jsonify({'erro': 'fazendeiro não encontrado'}), 404)
        
        FazendeiroService.delete(id)
        return make_response(jsonify({'mensagem': 'fazendeiro deletado com sucesso'}), 200)

api.add_resource(FazendeiroResource, '/fazendeiros')
api.add_resource(FazendeiroDetails, '/fazendeiro/<id>')