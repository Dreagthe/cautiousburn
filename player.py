import random
import numpy as np


class Player:
    def __init__(self, igns, role, team, champion, cs, gold, kills, deaths, assists, damage, healing, damage_taken, damage_prevented, stats= []):
        self.ign = random.choice(igns)
        self.role = role
        self.team = team
        self.champion = champion
        self.cs = cs
        self.gold = gold
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.damage = damage
        self.healing = healing
        self.damage_taken = damage_taken
        self.damage_prevented = damage_prevented
        self.aggression = 0

    def go_to_lane(self, lane):
        pass

    def go_to_jungle(self, jungle):
        pass

    def go_to_base(self, base):
        pass

    def farm_minions(self, minions):
        pass

    def farm_jungle(self, jungle):
        pass

    def stats(self):
        stats = np.array([0,0,0,0,0,0,0,0])
        return stats
        """
        This array houses the stats of the player. The stats are as follows:
        0: Laning
        1: Teamwork
        2: Aggression
        3: Map Awareness
        4: Vision Control
        5: Positioning
        6: Farming
        7: Objective Control

        """
