import random 

from teams import BlueTeam, RedTeam
from player import Player


class GameSetup:
    def __init__(self):
        self.blue_team = BlueTeam()
        self.red_team = RedTeam()
        self.blue_team.players = []
        self.red_team.players = []
        self.blue_team.gold_total = 0
        self.red_team.gold_total = 0
        self.blue_team.kills = 0
        self.red_team.kills = 0
        self.blue_team.deaths = 0
        self.red_team.deaths = 0
        self.blue_team.assists = 0
        self.red_team.assists = 0
        self.blue_team.damage = 0
        self.red_team.damage = 0
        self.blue_team.healing = 0
        self.red_team.healing = 0
        self.blue_team.damage_taken = 0
        self.red_team.damage_taken = 0
        self.blue_team.damage_prevented = 0
        self.red_team.damage_prevented = 0
        
