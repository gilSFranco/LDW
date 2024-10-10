from api import marshmallow
from marshmallow import Schema, fields

class BoardGameSchema(marshmallow.Schema):
    class Meta:
        fields = (
            '_id',
            'name',
            'level',
            'classes',
            'background',
            'race',
            'alignment',
            'skillpoints'
        )
        
    _id = fields.Str()
    name = fields.Str(required=True)
    level = fields.Int(required=True)
    classes = fields.Str(required=True)
    background = fields.Str(required=True)
    race = fields.Str(required=True)
    alignment = fields.Str(required=True)
    skillpoints = fields.Dict(required=True)
    