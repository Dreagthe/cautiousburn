import random 
from player import Player



"""
Define positions
"""
role = ["Top", "Jungle", "Mid", "Bot", "Support"]

# TODO: IMPLEMENT CHAMPIONS
champions = [
    "Arcane Duelist",
    "Shadow Whisperer",
    "Celestial Guardian",
    "Warden of the Wild",
    "Rune Enchanter",
    "Stormfury",
    "Soulweaver",
    "Elemental Mystic,"
    "Dragon Disciple",
    "Void Seer",
    "Abyssal Hunter",
    "Eldritch Knightmare",
    "Time Manipulator",
    "Spirit Caller",
    "Beastmaster Ranger",
    "Infernal Alchemist",
    "Astral Voyager",
    "Chaos Magician",
    "Seraphic Paladin",
    "Necro Healer",
    ]



class BlueTeam:
    def __init__(self):
        self.name = "Blue Team"
        self.color = "blue"
        self.players = []
        self.gold_total = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.damage = 0
        self.healing = 0
        self.damage_taken = 0
        self.damage_prevented = 0
        

    def generate_players(self, igns, champions):
        # Shuffle the list of roles before assigning
        random.shuffle(role)
        for player in role:
            self.players.append(
                Player(
                    igns,
                    self.name,
                    random.choice(champions),
                    0, 0, 0, 0, 0, 0, 0, 0, 0  # These zeros represent other stats; adjust as needed
                )
            )
class RedTeam:
    def __init__(self):
        self.name = "Red Team"
        self.color = "red"
        self.players = []
        self.gold_total = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.damage = 0
        self.healing = 0
        self.damage_taken = 0
        self.damage_prevented = 0
        

    def generate_players(self, igns, champions):
        # Shuffle the list of roles before assigning
        random.shuffle(role)
        for player in role:
            self.players.append(
                Player(
                    igns,
                    role,
                    self.name,
                    random.choice(champions),
                    0, 0, 0, 0, 0, 0, 0, 0, 0  # These zeros represent other stats; adjust as needed
                )
            )