from enum import Enum


class rarity(Enum):
    LEGENDARY = "LEGENDARY"
    MYTHIC = "MYTHIC"
    PRIME = "PRIME"
    FINE = "FINE"
    NORMAL = "NORMAL"


class joker_card:
    def __init__(self, name: str, description: str, rarity: rarity, notches: int):
        """
        Arguments:
            - name: card name
            - description: Describes what the card does
            - rarity: Gets the rarity of the card defined in the Enum
            - notches: how many slots it takes on the cowboy/guns
        """
        self.name = name
        self.description = description
        self.notches = notches
        self.rarity = rarity.value

    def __str__(self):
        return f"{self.name} joker has the ability of {self.description} and takes {self.notches} slots and has a rarity: {self.rarity}"


if __name__ == "__main__":
    joker_test = joker_card("Chickshot", "+50%", rarity.FINE, 1)
    print(joker_test)
