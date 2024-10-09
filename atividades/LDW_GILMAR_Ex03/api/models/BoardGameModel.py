from api import mongo

class Sheet():
    def __init__(self, name, level, classes, background, race, alignment, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.level = level
        self.classes = classes
        self.background = background
        self.race = race
        self.alignment = alignment
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma