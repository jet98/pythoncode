import module
import json

# opens and creates a string of a file
def readFile():
    t = ""
    file = open("PetStore.json")
    for line in file:
        line = line.strip()
        t = t + line
    return t

# gets search criteria from user and returns array
def getUserInput():
    print "Search by category |c| or keyword |k|:"
    c = raw_input()
    if c.lower() == "c":
        print "Enter a category"
        x = raw_input()
    elif c.lower() == "k":
        print "Enter a keyword"
        x = raw_input()
    #return user inputs
    z = []
    z.append(c)
    z.append(x)
    return z
    
# searches inventory by keyword
def keywordSearch(i, c):
    for inventory in i:
        if c.lower() in inventory["Product"].lower():
            print "%s - %s" % (inventory["Product"], inventory["Price"])

#search inventory by category
def categorySearch(i, c):
    for inventory in i:
        if c.lower() in inventory["Category"].lower():
            print "%s - %s" % (inventory["Product"], inventory["Price"])
 
def main():
    jsonTxt = readFile()
    inventory = json.loads(jsonTxt)
    criteria = getUserInput()
    if criteria[0].lower() == "k":
        keywordSearch(inventory, criteria[1])
    else:
        categorySearch(inventory, criteria[1])
    
main()