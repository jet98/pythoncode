import module
import json

# opens and creates a string of a file
def readFile():
    t = ""
    file = open("games.json")
    for line in file:
        line = line.strip()
        t = t + line
    return t

# searches through objects of games and retuns title and classes you
# can play
def findGame(find, games):
    for game in games:
        for genre in game["Genre"]:
            if find.lower() in genre.lower():
                print "Title: \t%s\nClass:" % (game["Title"]),
                for c in game["Classes"]:
                    print "\t%s" % c
        
# runs file genres include mmorpg, rpg, moba, shooter, and action
def main():
    jsonTxt = readFile()
    games = json.loads(jsonTxt)
    find = module.getString("Enter a genre to search: ")
    findGame(find, games)
    
main()