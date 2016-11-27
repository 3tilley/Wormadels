
import random

import districts
import characters
import interactions
from player import Player


class Game(object):
    """Holds game information"""

    def __init__(self, playerCount, deck=None, seed=None):
        self.playerCount=playerCount
        self.players = [Player(i+1) for i in range(playerCount)]
        self.deck = deck if deck else districts.createUnshuffledDeck()
        self.rng = random.Random(seed)
        self.characterInteration = interactions.getCharacterInput
        self.characters = characters.characters

    def gameSetup(self):
        for p in players:
            p.districts.append(deck.drawCards(4))