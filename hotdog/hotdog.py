import module
import random
import time

# checks out the player at the end of the game returning their new balance
def checkout(p, b, c, w):
    count = 0
    for player in p:
        if p[player] > 50 and w == player:
            c = c + b
            print "Your new total: %d" % (c)
        else:
            count += 1
    if count == 3:
        c = c - b
        print "Your new total: %d" % (c)
    return c
    
# checks to see if a player has eaten 50 hotdogs returning false to exit loop
def checkWinner(p, kg):
    for player in p:
        if p[player] > 50:
            print "%s is the winner!" % (player)
            kg = False
    return kg

# cycles through each player counting how many hotdogs has been eaten
def startGame(p):
    print "chomp... chomp... chomp..."
    time.sleep(1)
    for player in p:
        x = random.randrange(1, 11)
        p[player] += x
        print "%s has eaten %d hot dogs!" % (player, p[player])
    print ""
    return p

def main():
    # set initial balances
    cash = 100
    bet = 0
    players = {}
    # plays the game until out of cash
    while cash > 0:
        # resets players hotdog total
        players["John"] = 0
        players["Stacey"] = 0
        players["Sarah"] = 0
        keepGoing = True
        # allows user to make a bet
        choice = module.getString("Choose a winner: %s" % (players))
        bet = module.getInt("Place your bet %d:" % (cash))
        # plays the game
        if bet <= cash and bet > 0:
            while keepGoing:
                players = startGame(players)
                keepGoing = checkWinner(players, keepGoing)
            cash = checkout(players, bet, cash, choice)
        else:
            print "Check you account and place a new bet :P"
    # game over
    if cash <= 0:
        print "The house wins!"
            
main()