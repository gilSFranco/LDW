from api import mongo

class Sheet():
    def __init__(self, name, level, classes, background, race, alignment, skillpoints):
        self.name = name
        self.level = level
        self.classes = classes
        self.background = background
        self.race = race
        self.alignment = alignment
        self.skillpoints = skillpoints