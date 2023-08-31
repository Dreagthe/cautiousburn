import numpy as np


"""
base class entity 
"""

class Entity:
    def __init__(self, name, hp, ad, ap, armor, mr, speed, range, team):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.speed = speed
        self.range = range
        self.team = team

    def move(self, position):
        pass

    def attack(self, target):
        pass

    def take_damage(self, damage):
        pass

    def die(self):
        pass


"""
Minion class
"""

class Minion(Entity):
    def __init__(self, name, hp, ad, ap, armor, mr, speed, range, team):
        super().__init__(name, hp, ad, ap, armor, mr, speed, range, team)

    def move(self, position):
        pass

    def attack(self, target):
        pass

    def take_damage(self, damage):
        pass

    def die(self):
        pass

    def is_ranged(self):
        pass

    def is_melee(self):
        pass

    def is_cannon(self):
        pass

    def is_siege(self):
        pass

    