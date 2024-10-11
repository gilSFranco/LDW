from api import marshmallow
from marshmallow import Schema, fields, validate


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
    name = fields.Str(required=True, validate=validate.Length(min=2, max=120))
    level = fields.Int(required=True, validate=validate.Range(min=1, max=20))
    classes = fields.Str(required=True, validate=validate.OneOf([
        "Bárbaro",
        "Bardo",
        "Clérigo",
        "Druida",
        "Guerreiro",
        "Ladino",
        "Mago",
        "Monge",
        "Paladino",
        "Feiticeiro",
        "Bruxo"
    ]))
    background = fields.Str(required=True, validate=validate.OneOf([
        "Acólito",
        "Artesão de Guilda",
        "Artista",
        "Charlatão",
        "Criminoso",
        "Eremita",
        "Forasteiro",
        "Herói do Povo",
        "Marinheiro",
        "Nobre",
        "Órfão",
        "Sábio",
        "Soldado"
    ]))
    race = fields.Str(required=True, validate=validate.OneOf([
        "Humano",
        "Anão da Montanha",
        "Anão da Colina",
        "Alto Elfo",
        "Elfo da Floresta",
        "Elfo Drow",
        "Halfling Pés-Leves",
        "Halfling Robustecido",
        "Gnomo Pequeno",
        "Gnomos das Profundezas",
        "Meio-Elfo",
        "Meio-Orc",
        "Tiefling" 
    ]))
    alignment = fields.Str(required=True, validate=validate.OneOf([
        "Leal e Bom",  
        "Neutro e Bom",  
        "Caótico e Bom",  
        "Leal e Neutro",  
        "Neutro",  
        "Caótico e Neutro",  
        "Leal e Mau",  
        "Neutro e Mau",  
        "Caótico e Mau",  
    ]))
    skillpoints = fields.Dict(required=True)
