import module
import json
import requests

def askAgain():
    a = module.getString("Would you like to search another city? (y/n)")
    if a.lower() == "y":
        return True
    elif a.lower() == "n":
        return False
    else:
        print "Error with continuing"
        return False

def printResults(r):
    print "Here is the current weather for %s, %s" % (r["location"]["name"], r["location"]["region"])
    print "%s and %s degrees(f), %s degrees(c)" % (r["current"]["condition"]["text"], r["current"]["temp_f"], r["current"]["condition"]["text"])
    print "humidity %s%%, feels like %s degree(f), %s degrees(c)" % (r["current"]["humidity"], r["current"]["temp_f"], r["current"]["temp_c"])
    print 
    
def main():
    j = "https://api.apixu.com/v1/current.json?key=803271436ffa493da5e71343172103&q="
    keepGoing = True
    while keepGoing:
        loc = module.getString("Enter a zip code or city to start: ")
        request = requests.get(j + loc)
        results = json.loads(request.text)
        if "location" in results:
            printResults(results);
        elif "error" in results:
            print results["error"]["message"]
        
        keepGoing = askAgain()
    
main()