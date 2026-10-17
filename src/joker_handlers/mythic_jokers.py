import json
import os

from save_data import save_data

normal_jokers_dict = {
    "jokers": [
        {
            "name": "CONSUMER",
            "description": "Grants +25% wepon damage, but reloading now waste unused ammo",
            "rarity": "MYTHIC",
            "notches": "4",
            "limit": "1",
        },
        {
            "name": "EXECUTE",
            "description": "Your hits instantly kill enemies below 20% HP, except elites and bosses",
            "rarity": "MYTHIC",
            "notches": "4",
            "limit": "1",
        },
        {
            "name": "HEADBANG",
            "description": "+30% weakspot damage",
            "rarity": "MYTHIC",
            "notches": "4",
            "limit": "1",
        },
        {
            "name": "RIPOSTE",
            "description": "After your shield absorbs a hit, your next attack deals +100% damage",
            "rarity": "MYTHIC",
            "notches": "4",
            "limit": "2",
        },
    ],
}


s = json.dumps(normal_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/mythic_jokers.json")

save_data(data_file_dir, normal_jokers_dict)
