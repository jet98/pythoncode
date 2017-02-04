read = open('concerts.txt', 'r')
list = []
print "Please enter band name",
name = raw_input()

for line in read:
    if name in line:
        print line,
        