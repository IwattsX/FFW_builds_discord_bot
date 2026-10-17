import json
import os

from save_data import save_data

normal_jokers_dict = {
    "jokers": [
        {
            "name": "ALL MIGHTY",
            "description": "Gain +1% damage per 1 shield point, up to 80%",
            "rarity": "LEGENDARY",
            "notches": "5",
            "limit": "1",
        },
        {
            "name": "MACHINE GUN",
            "description": "Per mission, the weapon gains +0.3% attack speed for every 50 damage dealt",
            "rarity": "LEGENDARY",
            "notches": "5",
            "limit": "1",
        },
        {
            "name": "JOKER TRICK",
            "description": "Gain +7% damage and attack speed fo every distinct joker rarity equipped on the weapon",
            "rarity": "LEGENDARY",
            "notches": "5",
            "limit": "1",
        },
        {
            "name": "RICOCHET",
            "description": "The fired bullet ricochets, with a 30% chance to automatically hit a nearby enemy",
            "rarity": "LEGENDARY",
            "notches": "5",
            "limit": "1",
        },
        {
            "name": "SPEEDSTER",
            "description": "+1% damage and attack speed per 3% bonus move speed, up to 40%",
            "rarity": "LEGENDARY",
            "notches": "5",
            "limit": "1",
        },
        {
            "name": "VAMPIRE",
            "description": "The weapon gains +4% lifesteal",
            "rarity": "LEGENDARY",
            "notches": "5",
            "limit": "1",
        },
    ],
}


s = json.dumps(normal_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/legendary_jokers.json")

save_data(data_file_dir, normal_jokers_dict)
