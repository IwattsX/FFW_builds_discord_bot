from enum import Enum


class rarity(Enum):
    LEGENDARY = "LEGENDARY"
    MYTHIC = "MYTHIC"
    PRIME = "PRIME"
    FINE = "FINE"
    NORMAL = "NORMAL"


class joker_card:
    def __init__(
        self, name: str, description: str, rarity: rarity, notches: int, limit: int
    ):
        """
        Arguments:
            - name: card name
            - description: Describes what the card does
            - rarity: Gets the rarity of the card defined in the Enum
            - notches: how many slots it takes on the cowboy/guns
            - limit: how much of this card can you put on the cowboy/guns
        """
        self.name = name
        self.description = description
        self.notches = notches
        self.rarity = rarity.value
        self.limit = limit

    def __repr__(self) -> str:
        return f"name: {self.name}\n\
        desc: {self.description}\n\
        notches:{self.notches}\n\
        rarity:{self.rarity}\n\
        limit:{self.limit}"


if __name__ == "__main__":
    joker_test = joker_card("Chickshot", "+50%", rarity.FINE, 1, 2)
    print(joker_test)
