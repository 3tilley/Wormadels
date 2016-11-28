chars = ["Assassin", "Thief", "Magician", "King",
                "Bishop", "Merchant", "Architect", "Warlord"]

class Character(object):
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def __repr__(self):
        return "Character({})".format(self.name)

characters = [Character(i+1, v) for i, v in enumerate(chars)]