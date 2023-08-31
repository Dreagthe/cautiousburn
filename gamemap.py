from entities import *
from teams import BlueTeam, RedTeam
from player import Player

"""
Contains the game map and all of its components, including lanes, jungle, and base and a list for players in each location
"""
class GameMap:
    def __init__(self, TopLane, MidLane, BotLane, BlueJungle, RedJungle, BlueBase, RedBase):
        self.TopLane = TopLane
        self.MidLane = MidLane
        self.BotLane = BotLane
        self.BlueJungle = BlueJungle
        self.RedJungle = RedJungle
        self.BlueBase = BlueBase
        self.RedBase = RedBase


"""
Base Classes
"""

class Lane:
    def __init__(self, RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret,
                  BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret):
        self.RedOuterTurret = RedOuterTurret
        self.RedInnerTurret = RedInnerTurret
        self.RedInhibitorTurret = RedInhibitorTurret
        self.RedNexusTurret = RedNexusTurret
        self.BlueOuterTurret = BlueOuterTurret
        self.BlueInnerTurret = BlueInnerTurret
        self.BlueInhibitorTurret = BlueInhibitorTurret
        self.BlueNexusTurret = BlueNexusTurret
        
class Jungle:
    def __init__(self, RedBlueBuff, RedRedBuff, RedGromp, RedWolves, RedRaptors, RedKrugs,
                  BlueBlueBuff, BlueRedBuff, BlueGromp, BlueWolves, BlueRaptors, BlueKrugs):
        self.RedBlueBuff = RedBlueBuff
        self.RedRedBuff = RedRedBuff
        self.RedGromp = RedGromp
        self.RedWolves = RedWolves
        self.RedRaptors = RedRaptors
        self.RedKrugs = RedKrugs
        self.BlueBlueBuff = BlueBlueBuff
        self.BlueRedBuff = BlueRedBuff
        self.BlueGromp = BlueGromp
        self.BlueWolves = BlueWolves
        self.BlueRaptors = BlueRaptors
        self.BlueKrugs = BlueKrugs

class Base:
    def __init__(self, RedNexus, BlueNexus):
        self.RedNexus = RedNexus
        self.BlueNexus = BlueNexus



"""
RED SIDE
"""
class RedTopLane(Lane):      
    def __init__(self, RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret, players = [], minions = []):
        super().__init__(RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def spawn_minions(self, minions):
        self.minions.append(minions)

class RedJungle(Jungle):
    def __init__(self, RedBlueBuff, RedRedBuff, RedGromp, RedWolves, RedRaptors, RedKrugs, players = []):
        super().__init__(RedBlueBuff, RedRedBuff, RedGromp, RedWolves, RedRaptors, RedKrugs)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)




class RedMidLane(Lane):
    def __init__(self, RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret, players = [], minions = []):
        super().__init__(RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def spawn_minions(self, minions):
        self.minions.append(minions)


class RedBotLane(Lane):
    def __init__(self, RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret, players = [], minions = []):
        super().__init__(RedOuterTurret, RedInnerTurret, RedInhibitorTurret, RedNexusTurret)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def spawn_minions(self, minions):
        self.minions.append(minions)


"""
BLUE SIDE
"""
class BlueTopLane(Lane):
    def __init__(self, BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret, players = [], minions = []):
        super().__init__(BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def spawn_minions(self, minions):
        self.minions.append(minions)

class BlueJungle(Jungle):
    def __init__(self, BlueBlueBuff, BlueRedBuff, BlueGromp, BlueWolves, BlueRaptors, BlueKrugs, players = []):
        super().__init__(BlueBlueBuff, BlueRedBuff, BlueGromp, BlueWolves, BlueRaptors, BlueKrugs)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

   


class BlueMidLane(Lane):
    def __init__(self, BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret, players = [], minions = []):
        super().__init__(BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def spawn_minions(self, minions):
        self.minions.append(minions)


class BlueBotLane(Lane):
    def __init__(self, BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret, players = [], minions = []):
        super().__init__(BlueOuterTurret, BlueInnerTurret, BlueInhibitorTurret, BlueNexusTurret)

    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def spawn_minions(self, minions):
        self.minions.append(minions)


