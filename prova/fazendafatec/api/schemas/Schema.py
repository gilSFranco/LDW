from api import marshmallow
from marshmallow import Schema, fields

class FazendeiroSchema(marshmallow.Schema):
    class Meta:
        fields = ('_id', 'nome', 'idade', 'endereco', 'telefone')
        
    _id = fields.Str()
    nome = fields.Str(required=True)
    idade = fields.Int(required=True)
    endereco = fields.Str(required=True)
    telefone = fields.Str(required=True)