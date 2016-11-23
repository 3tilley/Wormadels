
import cards

class Game(object):
    """Holds game information"""

    def __init__(self, playerCount, deck=None, seed=None):
        self.playerCount=playerCount
        self.deck = deck if deck else cards.createUnshuffledDeck()