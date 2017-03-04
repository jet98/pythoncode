import random
import module

def main():
    ans = random.randrange(1, 11)
    keepGoing = True
    count = 0;
    while keepGoing:
        count += 1
        guess = module.getInt("Enter a guess between 1 - 10: ")
        if guess > ans:
            print "Your guess is too high"
        elif guess < ans:
            print "Your guess is too low"
        else:
            print "You won in %d guesses!" % (count)
            keepGoing = False

main()