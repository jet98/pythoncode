import module
import random

def main():
    list = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    r = random.randrange(0, len(list))
    double = list[r]
    list.append(double)
    round = 1
    while True:
        pick1 = module.getInt("Pick the first card to turn over (0-9)")
        while pick1 < 0 or pick1 > 9:
            pick1 = module.getInt("Pick out of bounds \nPick the first card to turn over (0-9)")
        pick2 = module.getInt("Pick the second card to turn over (0-9)")
        while pick2 < 0 or pick2 > 9:
            pick2 = module.getInt("Pick out of bounds \nPick the second card to turn over (0-9)")
        if(list[pick1] == list[pick2]):
            print "card %d is the %s" % (pick1, list[pick1])
            print "card %d is the %s" % (pick2, list[pick2])
            print "You won in %d tries" % (round)
            break
        else:
            print "card %d is the %s" % (pick1, list[pick1])
            print "card %d is the %s" % (pick2, list[pick2])
            round+=1
    
main()