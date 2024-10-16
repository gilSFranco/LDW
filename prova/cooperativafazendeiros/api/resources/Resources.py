from api import api
from flask import make_response, jsonify, request
from flask_restful import Resource
from ..models import Model
from ..services.Services import UsuarioService
from ..schemas import Schema

class UsuarioResource(Resource):
    def get(self):
        usuarios = UsuarioService.findAll()
        validacaoUsuario = Schema.UsuarioSchema(many=True)
        
        return make_response(validacaoUsuario.jsonify(usuarios), 200)
    
    def post(self):
        validacaoUsuario = Schema.UsuarioSchema()
        validacao = validacaoUsuario.validate(request.json)
        
        if validacao:
            return make_response(jsonify(validacao), 400)
        else:
            corpoRequisicao = request.get_json()
            usuario = Model.UsuarioModel(**corpoRequisicao)
            
            novoUsuario = UsuarioService.save(usuario)
            
            response = validacaoUsuario.jsonify(novoUsuario)
            
            return make_response(response, 201)

class UsuarioDetails(Resource):
    def get(self, id):
        usuario = UsuarioService.findById(id)
        
        if usuario is None:
            return make_response(jsonify({'erro': 'usuario não encontrado'}), 404)
        
        validacaoUsuario = Schema.UsuarioSchema()
        return make_response(validacaoUsuario.jsonify(usuario), 200)
    
    def put(self, id):
        usuario = UsuarioService.findById(id)
        
        if usuario is None:
            return make_response(jsonify({'erro': 'usuario não encontrado'}), 404)
        
        validacaoUsuario = Schema.UsuarioSchema()
        validacao = validacaoUsuario.validate(request.json)
        
        if validacao:
            return make_response(jsonify(validacao), 400)
        else:
            corpoRequisicao = request.get_json()
            usuario = Model.UsuarioModel(**corpoRequisicao)
            
            usuarioAtualizado = UsuarioService.update(usuario, id)
            
            response = validacaoUsuario.jsonify(usuarioAtualizado)
            
            return make_response(response, 200)
            
    def delete(self, id):
        usuario = UsuarioService.findById(id)
        
        if usuario is None:
            return make_response(jsonify({'erro': 'usuario não encontrado'}), 404)
        
        UsuarioService.delete(id)
        return make_response(jsonify({'mensagem': 'usuario deletado com sucesso'}), 200)

api.add_resource(UsuarioResource, '/usuarios')
api.add_resource(UsuarioDetails, '/usuario/<id>')