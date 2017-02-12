# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename, 'r')
    list = []
    for line in file:
        list.append(line)
    return list
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    avg = 0.0
    for num in l:
        avg += float(num)
    avg = float(avg) / len(l)
    return avg
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    counter = 0
    for line in l:
        if int(line) > int(maxSpeed):
            counter += 1
    return counter
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    rush = readData("data-rush.txt")
    noRush = readData("data-not-rush.txt")
    rushAvg = getAverage(rush)
    noRushAvg = getAverage(noRush)
    rushSpeeder = countSpeeders(rush, 69)
    noRushSpeeder = countSpeeders(noRush, 69)
    
    print "The average speed during rush hour was %.2f." % (rushAvg)
    print "The average speed not during rush hour was %.2f." % (noRushAvg)
    print "There were %d speeders during rush hour.  Total fine = $%.2f" % (rushSpeeder, rushSpeeder * 150)
    print "There were %d speeders during rush hour.  Total fine = $%.2f" % (noRushSpeeder, noRushSpeeder * 100)
    
# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()