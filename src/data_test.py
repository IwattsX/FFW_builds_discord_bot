import json

all_jokers_dict = {
    "data": {
        "UNIVERSAL": [
            {
                "name": "name",
                "description": "description",
                "rarity": "rarity",
                "notches": "notches",
                "limit": "limit",
            }
        ],
        "QUAD_CYLINDER": [
            {
                "name": "name",
                "description": "description",
                "rarity": "rarity",
                "notches": "notches",
                "limit": "limit",
            }
        ],
    }
}


s = json.dumps(all_jokers_dict, indent=4)
print(s)

# 3. Write the Python dictionary DIRECTLY to the file
with open("data.json", "w") as file:
    json.dump(all_jokers_dict, file, indent=4)
