from api import marshmallow
from marshmallow import Schema, fields

class UsuarioSchema(marshmallow.Schema):
    class Meta:
        fields = ('_id', 'nome', 'email')
        
    _id = fields.Str()
    nome = fields.Str(required=True)
    email = fields.Str(required=True)