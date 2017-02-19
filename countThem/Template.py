# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
    h = {}
    # goes trough each line in the file sets key and value
    for line in open(filename):
        x = line.split(", ")
        k = x[0].lower()
        v = x[1]
        # if key exist adds existing value to new value else sets new value
        if k in h:
            h[k] = (int(h[k]) + int(v))
        else:
            h[k] = int(v)
    return h

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    i = ""
    # continues loop until exit
    while(i != "exit"):
        print "Please enter bird: ",
        i = raw_input();
        # prints out the value for given key
        if i.lower() in d:
            print "I have seen that bird %d time(s)" % (d[i])
            # check for if any bird has been seen the same amount of times
            for k in d:
                if d[k.lower()] == d[i.lower()] and k.lower() != i.lower():
                    print "and %s has," % (k.lower()),
            print ""
        # checks to exit loop else bird is not in map
        elif i.lower() == "exit":
            print "bye"
        else:
            print "Bird not found"
            print ""

def main():
    d = countBirds("Birds.txt")
    askUser(d)
    
main()