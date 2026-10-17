import json
import os

sidearm_jokers_dict = {
    "REVOLVER": {
        "jokers": [
            {
                "name": "FANNING ACE",
                "description": "Fire mid-reload at the right moment to chain-fire all bullets",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
            {
                "name": "MARK ACE",
                "description": "Bullets mark enemies for 5 sec. Marked enemies take +15% damage",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
        ]
    },
    "BOW": {
        "jokers": [
            {
                "name": "OVERDRAW",
                "description": "Charge for 2 sec. to fire 3 arrows in a cone. Attack speed reduces charge time",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
            {
                "name": "ULTRA DRAW",
                "description": "Charge for 4 sec. to fire a massive explosive arrow. Attack speed reduces charge time",
                "rarity": "UNIQUE",
                "notches": "7",
                "limit": "1",
            },
        ]
    },
    "DUAL REVOLVERS": {
        "jokers": [
            {
                "name": "ECO TRICK",
                "description": "Reloading no longer waste ammo",
                "rarity": "UNIQUE",
                "notches": "2",
                "limit": "1",
            },
            {
                "name": "SWAMP TRICK",
                "description": "Reload explosions now leave puddles on the ground",
                "rarity": "UNIQUE",
                "notches": "2",
                "limit": "1",
            },
        ]
    },
    "BOOMERANG": {
        "jokers": [
            {
                "name": "CHONKY THROW",
                "description": "The boomerang is twice as big and passes through the shields",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
            {
                "name": "LINGERING THROW",
                "description": "Doubles the lingering time. Combines with Lingering Time upgrade",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
        ]
    },
    "SHERIFF STARS": {
        "jokers": [
            {
                "name": "JUMP STAR",
                "description": "+2 Jumps while holding the Sheriff Stars",
                "rarity": "UNIQUE",
                "notches": "4",
                "limit": "1",
            },
            {
                "name": "SCAVENGER STAR",
                "description": "Gain +100% pickup range. Gain +30% move speed while holding the Sheriff Stars",
                "rarity": "UNIQUE",
                "notches": "3",
                "limit": "1",
            },
        ]
    },
    "BANJO": {
        "jokers": [
            {
                "name": "BARDBARIAN",
                "description": "Hold the slam attack longer to release a more powerful blow",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
            {
                "name": "LULLABARD",
                "description": "Gain an extra chord per hit and a wider healing zone, but lose the slam attack",
                "rarity": "UNIQUE",
                "notches": "5",
                "limit": "1",
            },
        ]
    },
}


s = json.dumps(sidearm_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/sidearm_unique_jokers.json")

with open(data_file_dir, "w+") as file:
    json.dump(sidearm_jokers_dict, file, indent=4)
