# reads file into hash
def readFile(file):
    h = {}
    for line in open(file):
        x = line.split(", ")
        h[x[0]] = x[1]
    return h

# creates hash of categories
def getCategories():
    c = {}
    c['cube head'] = '0-9.99'
    c['square master'] = '10-19.99'
    c['advanced twister'] = '20-29.99'
    c['intermediate turner'] = '30-39.99'
    c['average mover'] = '40-59.99'
    c['pathetic'] = '60 and above'
    return c

# print names checking for which group they belong to
def printGroups(h, c):
    for group in c:
        g = c[group].split("-")
        if group == "pathetic":
            g[0] = g[0].replace(" and above", "")
        print "%s:" % (group)
        for person in h:
            if len(g) > 1 and float(h[person]) >= float(g[0]) and float(h[person]) <= float(g[1]):
                print "\t%s" % (person)
            elif len(g) < 2 and float(h[person]) >= float(g[0]):
                print "\t%s" % (person)
        print ""

def main():
    h = {}
    h = readFile('timing.txt')
    cat = getCategories();
    printGroups(h, cat)

main()