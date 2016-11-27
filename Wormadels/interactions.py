
from player import players

def getCharacterInput(gameChars, playerNo, isPick):
    verb = None
    if isPick:
        verb = "pick"
    else:
        verb = "discard"

    print "\nPlayer {} please {} a card".format(players[playerNo], verb)

    for i in sorted(gameChars.keys()):
        print "{}. {}".format(i, gameChars[i])

    pick = input()

    while pick not in gameChars.keys():
        print "Naughty, that's not a valid choice. Try again."
        pick = input()

    print "You chose {}".format(gameChars[pick])

    del gameChars[pick]

    return pick