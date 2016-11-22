import random

characters = ["Assassin", "Thief", "Magician", "King",
                "Bishop", "Merchant", "Architect", "Warlord"]

players = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]


def getCharacterInput(player, isPick):
    verb = None
    if isPick:
        verb = "pick"
    else:
        verb = "discard"

    print "\nPlayer {} please {} a card".format(players[player], verb)

    for i in sorted(gameChars.keys()):
        print "{}. {}".format(i, gameChars[i])

    pick = input()

    while pick not in gameChars.keys():
        print "Naughty, that's not a valid choice. Try again."
        pick = input()

    print "You chose {}".format(gameChars[pick])

    del gameChars[pick]

    return pick

if __name__=="__main__":
    rnd = random.Random()

    # Copy game characters so we don't destroy it
    gameChars = { i+1: c for i, c in enumerate(characters)}

    # Pick a character to discard
    discardIndex = rnd.randint(1,8)

    del gameChars[discardIndex]

    p1Pick1 = getCharacterInput(1, True)

    p2Pick1 = getCharacterInput(2, True)

    p2discard1 = getCharacterInput(2, False)

    p1Pick2 = getCharacterInput(1, True)

    p1discard1 = getCharacterInput(1, False)

    p2Pick2 = getCharacterInput(2, True)

    print "\n"
    print "=" * 40
    print "Player One you picked {} and {}".format(characters[p1Pick1-1], characters[p1Pick2-1])
    print "-" * 40
    print "Player Two you picked {} and {}".format(characters[p2Pick1-1], characters[p2Pick2-1])
    print "=" * 40