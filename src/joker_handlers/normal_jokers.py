import json
import os

from save_data import save_data

normal_jokers_dict = {
    "jokers": [
        {
            "name": "BRACING",
            "description": "+5% attack and reload speed",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "CHICKSHOT",
            "description": "+50% chance for attacks to make a chicken sounds. Useless!",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "FREE COCKTAIL",
            "description": "When you reload an empty clip, heal for 2 hp",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "GOLD TOOTH",
            "description": "+10% chance for enemies to drop 1 gold nugget upon death",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "10",
        },
        {
            "name": "HEAVY WEAPON",
            "description": "+10% damage, but 30% gravity while the weapon is active",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "PANIC ATTACK",
            "description": "When you take HP damage, gain +20% damage for 3 sec.",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "1",
        },
        {
            "name": "PARTY SHOT",
            "description": "+50% chance for weakspot hits to blow confetti. Useless!",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "PIGSHOT",
            "description": "+5% chance to spawn a pig on impact. Attack them to make them explode",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "QUICKDRAW",
            "description": "+40% swap speed",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "2",
        },
        {
            "name": "SWIFT SHOT",
            "description": "+10% attack speed when aiming",
            "rarity": "NORMAL",
            "notches": "1",
            "limit": "4",
        },
    ],
}


s = json.dumps(normal_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/normal_jokers.json")

save_data(data_file_dir, normal_jokers_dict)
