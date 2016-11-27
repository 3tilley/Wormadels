
colours = ["Red", "Blue", "Gold", "Green", "Purple"]

class District(object):
    """District card object"""

    def __init__(self, cardId, name, cost, victoryPoints, colour, eventListeners=None):
        self.cardId = cardId
        self.name = name
        self.cost = cost
        self.victoryPoints = victoryPoints

        assert colour.title() in colours
        self.colour = colour.title()

        # These are listeners that will trigger on certain events, mainly for purple cards
        self.eventListeners = eventListeners

    def __repr__(self):
        return self.name


class Deck(object):
    def __init__(self, cards):
        self._cards = cards

    def drawCards(self, number):
        cards = [self._cards.pop() for i in range(number)]
        return cards

    def returnCards(self, returnCards): 
        self._cards = returnCards + self._cards

    def cardCount(self):
        return len(self._cards)

    def __repr__(self):
        return "Deck({})".format(self.cardCount())



        

# Eventually this will become a load from disk or something 
districts = [
    ("Tavern", 1, 1, "Green"),
    ("Temple", 1, 1, "Blue"),
    ("Palace", 5, 5, "Gold"),
    ("Monastery", 3, 3, "Blue"),
    ("Castle", 4, 4, "Gold"),
    ("Battlefield", 3, 3, "Red"),
    ("Watchtower", 1, 1, "Red"),
    ("University", 6, 8, "Purple")
]

cardList = [District(*((i,) + v)) for i, v in enumerate(districts)]

def createUnshuffledDeck(cards=None):
    if cards:
        unshuffled = sorted(cards, key=lambda x: x.cardId)
    else:
        unshuffled = cardList

    return Deck(cardList)
    