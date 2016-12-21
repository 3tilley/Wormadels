
from ..game import Game

def makeTestGame(players):
    return Game(players)

def testNumberOfAvailableCharacters():
    players = 2
    game = makeTestGame(players)
    assert len(game.characters) == 8

def testStartingVictoryPoints():
    players = 2
    game = makeTestGame(players)
    assert game.countVictoryPoints() == [0] * players

def testEndDistricts():
    players = 2
    game = makeTestGame(players)
    assert game.endDistricts == 8