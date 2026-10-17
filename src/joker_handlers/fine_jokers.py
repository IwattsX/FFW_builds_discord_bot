import json
import os

from save_data import save_data

normal_jokers_dict = {
    "jokers": [
        {
            "name": "ANTI-GRAVITY FALLS",
            "description": "+2% chance to spawn an anti-gravity area when an enemy dies",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "BELL SHOT",
            "description": "+5% chance for weakspot hits to summon a healing ghost bell",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "CACTUS DAY",
            "description": "+5% chance for a Cactus Mino to Spawn when an enemy dies",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "CLUTCH",
            "description": "+2 explosive bullets at the end of your magazine",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "CRACKSHOT",
            "description": "+7% damage",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "SWITCHSHOT",
            "description": "Your first hit after equipping a weapon deals 30% more damage",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "FAST HANDS",
            "description": "+20% reload speed",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "LUCKY STRIKE",
            "description": "+10% chance to deal double damage per hit",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "PICK PICK",
            "description": "+10% chance on hit to spawn damage pickaxes on the target",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "PRECIOUS RUSH",
            "description": "+10% chance for a speed-boosting ring to spawn when an enemy dies",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "RUN & GUN",
            "description": "+30% move speed when shooting",
            "rarity": "FINE",
            "notches": "2",
            "limit": "6",
        },
        {
            "name": "RUN & RELOAD",
            "description": "+50% move speed when reloading",
            "rarity": "FINE",
            "notches": "2",
            "limit": "6",
        },
        {
            "name": "SHROOM GRAVE",
            "description": "+10% chance for a shroom to spawn when an enemy dies",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
        {
            "name": "SLOW AND STEADY",
            "description": "Gain 25% accuracy, but -10% attack speed",
            "rarity": "FINE",
            "notches": "2",
            "limit": "2",
        },
    ],
}


s = json.dumps(normal_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/fine_jokers.json")

save_data(data_file_dir, normal_jokers_dict)
