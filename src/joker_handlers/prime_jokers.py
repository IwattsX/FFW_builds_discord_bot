import json
import os

from save_data import save_data

normal_jokers_dict = {
    "jokers": [
        {
            "name": "AMMO SUPPLY",
            "description": "+5% chance for enemies to drop an ammo box upon death",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "AVALANCHE",
            "description": "+15% damage while shielded",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "DESTROYER",
            "description": "The first 25% of your clip deals +20% damage",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "EXPLOSIVE HITS (PYRO)",
            "description": "+5% chance for your hits to cause an explosion (Pyro)",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "EXPLOSIVE HITS (Acid)",
            "description": "+5% chance for your hits to cause an explosion (Acid)",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "EXPLOSIVE HITS (Elec)",
            "description": "+5% chance for your hits to cause an explosion (Elec)",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "EXPLOSIVE HITS (Frost)",
            "description": "+5% chance for your hits to cause an explosion (Frost)",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "PEW PEW PEW",
            "description": "+20% attack speed",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "1",
        },
        {
            "name": "RAMPAGE",
            "description": "Gain 5% reload speed on kill for 10 sec., up to 100%",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "PEW PEW PEW",
            "description": "+20% attack speed",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "1",
        },
        {
            "name": "RELOAD MASTERY",
            "description": "Reloading an empty clip is 50% faster",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "SCRUB HIT",
            "description": "Your primary weapon removes elements from enemies to instantly deal 10 damage",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "1",
        },
        {
            "name": "SHARP SHOOTER",
            "description": "+20% weakspot damage",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "WEAK LINK",
            "description": "+35% weakspot damage but -20% regular hits damage",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "2",
        },
        {
            "name": "WEAKSPOT REFUND",
            "description": "+20% chance to get your ammo back after a weakspot hit",
            "rarity": "PRIME",
            "notches": "3",
            "limit": "4",
        },
    ],
}


s = json.dumps(normal_jokers_dict, indent=4)
print(s)

# get script directory for saving the dictionary to a normal_jokers file
script_dir = os.path.dirname(__file__)
data_file_dir = os.path.join(script_dir, "../data/prime_jokers.json")

save_data(data_file_dir, normal_jokers_dict)
