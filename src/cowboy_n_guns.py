from jokers import joker_card


class Cowboy:
    def __init__(self, jokers: list[joker_card]):
        self.jokers = jokers


class gun:
    def __init__(self, name, jokers: list[joker_card]):
        self.name = name
        self.jokers = jokers
