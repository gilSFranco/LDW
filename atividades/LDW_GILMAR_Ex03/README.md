
# API REST using Flask

I am a FATEC student from the city of Registro and I was given the task of building a REST API using Flask. The theme to be chosen was free, so I chose to do it on RPG (Role-Playing Game), more specifically, D&D. The API was created with the intention of facilitating the construction of the chips that are used in these table games. If you've never played the game, don't even know what I'm talking about, don't worry, I'll give you a step-by-step guide on how to use the API.


## API Documentation

#### Return all sheets

```http
GET /boardgames
```

#### Return example

```json
{
    "_id": "670861cec3ea40734774b979",
    "alignment": "Leal e Bom",
    "background": "Acólito",
    "classes": "Bárbaro",
    "level": 1,
    "name": "Jefferson",
    "race": "Tiefling",
    "skillpoints": {
        "charisma": 8,
        "constitution": 8,
        "dexterity": 8,
        "intelligence": 8,
        "strength": 8,
        "wisdom": 8
    }
}
```

#### Returns one sheet

```http
GET /boardgame/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Required**. The ID of the item you want. |

#### Register a sheet

```http
POST /boardgames
```

#### POST request examples

##### Example 01

```json
{
    "name": "Thalion",
    "level": 5,
    "classes": "Bárbaro",
    "background": "Forasteiro",
    "race": "Alto Elfo",
    "alignment": "Leal e Bom",
    "skillpoints": {
        "charisma": 10,
        "constitution": 12,
        "dexterity": 14,
        "intelligence": 9,
        "strength": 16,
        "wisdom": 11
    }
}
```

##### Example 02

```json
{
    "name": "Grom",
    "level": 3,
    "classes": "Guerreiro",
    "background": "Soldado",
    "race": "Anão da Montanha",
    "alignment": "Leal e Neutro",
    "skillpoints": {
        "charisma": 8,
        "constitution": 16,
        "dexterity": 10,
        "intelligence": 9,
        "strength": 18,
        "wisdom": 12
    }
}
```

##### Example 03

```json
{
    "name": "Lyra",
    "level": 4,
    "classes": "Mago",
    "background": "Sábio",
    "race": "Gnomo Pequeno",
    "alignment": "Neutro e Bom",
    "skillpoints": {
        "charisma": 11,
        "constitution": 10,
        "dexterity": 14,
        "intelligence": 17,
        "strength": 8,
        "wisdom": 12
    }
}
```

##### Example 04

```json
{
    "name": "Fendrel",
    "level": 6,
    "classes": "Ladino",
    "background": "Charlatão",
    "race": "Meio-Elfo",
    "alignment": "Caótico e Bom",
    "skillpoints": {
        "charisma": 15,
        "constitution": 10,
        "dexterity": 16,
        "intelligence": 12,
        "strength": 9,
        "wisdom": 8
    }
}
```

##### Example 05

```json
{
    "name": "Brom",
    "level": 2,
    "classes": "Clérigo",
    "background": "Acólito",
    "race": "Halfling Pés-Leves",
    "alignment": "Neutro",
    "skillpoints": {
        "charisma": 14,
        "constitution": 15,
        "dexterity": 9,
        "intelligence": 11,
        "strength": 8,
        "wisdom": 17
    }
}
```

#### Deletes one sheet

```http
DELETE /boardgame/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Required**. The ID of the item you want to delete. |

#### Updates one sheet

```http
PUT /boardgame/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `string` | **Required**. The ID of the item you want to update. |

#### POST request examples

##### Example 01

```json
{
    "name": "Thalion",
    "level": 5,
    "classes": "Bárbaro",
    "background": "Forasteiro",
    "race": "Alto Elfo",
    "alignment": "Leal e Bom",
    "skillpoints": {
        "charisma": 10,
        "constitution": 12,
        "dexterity": 14,
        "intelligence": 9,
        "strength": 16,
        "wisdom": 11
    }
}
```