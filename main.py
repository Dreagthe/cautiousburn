from gamemap import GameMap, RedJungle, BlueJungle, RedTopLane, RedMidLane
from gamemap import RedBotLane, BlueTopLane, BlueMidLane, BlueBotLane
from player import Player
from gamesetup import GameSetup
from gamesetup import BlueTeam, RedTeam
from teams import BlueTeam, RedTeam
import random
import time


# Open ign.txt
with open("ign.txt", "r") as f:
    lines = f.readlines()
    igns = [line.strip() for line in lines]

# Open champions.txt
with open("champions.txt", "r") as f:
    lines = f.readlines()
    champions = [line.strip() for line in lines]

def main():
    #create a game setup
    game_setup = GameSetup()
    #generate players for each team
    game_setup.blue_team.generate_players(igns, champions)
    game_setup.red_team.generate_players(igns, champions)
    #create a game map
    game_map = GameMap()

    #assign players to lanes
    for player in game_setup.blue_team.players:
        if player.role == "top":
            BlueTopLane.add_player(player)
        elif player.role == "mid":
            BlueMidLane.add_player(player)
        elif player.role == "bot":
            BlueBotLane.add_player(player)
        else:
            BlueJungle.add_player(player)
    
    for player in game_setup.red_team.players:
        if player.role == "top":
            RedTopLane.add_player(player)
        elif player.role == "mid":
            RedMidLane.add_player(player)
        elif player.role == "bot":
            RedBotLane.add_player(player)
        else:
            RedJungle.add_player(player)

    #start a timer that counts up 
    start_time = time.time()
    #while loop that runs until the game is over
    while True:
        
        #spawn minions (3 melee, 3 caster) every minute, spawn jungle every 2 minutes
        spawn_minions()
        spawn_jungle()
    


if __name__ == "__main__":
    main()
