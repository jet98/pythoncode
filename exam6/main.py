import module

# make a guess to narrow possibilites
def guess(p, w, s):
    temp = []
    g = module.getString("Is the clue about a weapon or suspect (w or s)")
    if g.lower() == "w":
        print "Enter a weapon that was not used %s " % (w),
        r = raw_input()
        for possibility in p:
            if r.lower() not in possibility.lower():
                temp.append(possibility)
    elif g.lower() == "s":
        print "Enter an innocent suspect %s " % (s),
        r = raw_input()
        for possibility in p:
            if r.lower() not in possibility.lower():
                temp.append(possibility)
    return temp;
    
# count possibilities
def possibilities(w, s):
    p = []
    for weapon in w:
        for suspect in s:
            p.append("%s with the %s" % (suspect, weapon))
    return p
    
def main():
    weapons = ["Candlestick", "Wrench", "Pipe"]
    suspects = ["Miss Scarlet", "Col Musturd", "Mr Green"]
    p = possibilities(weapons, suspects)
    
    while len(p) > 1:
        print "%s possibilities left" % (len(p))
        p = guess(p, weapons, suspects)
    print "%s possibility left\n %s" % (len(p), p)
    
main()