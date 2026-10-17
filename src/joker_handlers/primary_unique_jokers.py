import json
import os

from save_data import save_data

normal_jokers_dict = {
    "QUAD CYLINDER": {
        "jokers": [
            {
                "name": "AIMING BURST",
                "description": "+30% weakspot damage and piercing bullets while aiming",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
            {
                "name": "HOMING BURST",
                "description": "Every 8 bullets fired, shoot 2 homing bullets at nearby enemies",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
        ]
    },
    "LONG RANGER": {
        "jokers": [
            {
                "name": "FOCUS SHOT",
                "description": "Every weakspot hit reduced the colldown of your spells by 2 sec.",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
            {
                "name": "MINDSHOT",
                "description": "Weakspot hits cause an explosion",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
        ]
    },
    "MINIGUN": {
        "jokers": [
            {
                "name": "ELEMENTAL SPIN",
                "description": "The minigun has a 30% chance to fire a random elemental bullet instead of a regular one",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
            {
                "name": "FRENZY SPIN",
                "description": "While your kill counter is above 10, the minigun fires twice as fast",
                "rarity": "UNIQUE",
                "notches": "4",
                "limit": "1",
            },
        ]
    },
    "SHOTGUN": {
        "jokers": [
            {
                "name": "OVERBLAST",
                "description": "Shoots an extra pellet for every 4 missing shots in the magazine",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
            {
                "name": "RUSH BLAST",
                "description": "The first 3 bullets in your magazine have a 100% accuracy and shoot further away",
                "rarity": "UNIQUE",
                "notches": "4",
                "limit": "1",
            },
        ]
    },
    "LEVEREDGE": {
        "jokers": [
            {
                "name": "EAGLE LEVER",
                "description": "Consecutive shots without missing grants +10% damage, stacking up to 50%",
                "rarity": "UNIQUE",
                "notches": "4",
                "limit": "1",
            },
            {
                "name": "STACKED LEVER",
                "description": "Instantly reload 2 bullets from your reserve ammo on kill",
                "rarity": "UNIQUE",
                "notches": "4",
                "limit": "1",
            },
        ]
    },
    "KNUCKLES": {
        "jokers": [
            {
                "name": "FIST RAGE",
                "description": "Taking damage generates charge and grants +30% attack speed for 2 sec.",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
            {
                "name": "FIST RO DAH",
                "description": "The charged attack propels you backwards and has a 20% chance to apply Frost to enemies",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
        ]
    },
    "LASSO": {
        "jokers": [
            {
                "name": "SKY LASH",
                "description": "The charged attack gants +50% move speed and lets you fly",
                "rarity": "UNIQUE",
                "notches": "4",
                "limit": "1",
            },
            {
                "name": "SPELL LASH",
                "description": "Casting a spell instantly fills your charge bar",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
        ]
    },
}


s = json.dumps(normal_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/primary_unique_jokers.json")

save_data(data_file_dir, normal_jokers_dict)
