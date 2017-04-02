import os
import module

# gets all .txt files
def getTextFiles():
    files = os.listdir('.')
    fileNames = []
    fileNames = [f for f in files if '.txt' in f]
    return fileNames

# looks through each line in each file and prints line
# that contains the word
def findInFiles(files, word):
    print
    for f in files:
        file = open(f)
        for line in file:
            if word.upper() in line.upper():
                l = line.strip()
                print "%s: %s" % (f, l.upper().lstrip())
    
def main():
    # gets filese
    files = getTextFiles()
    # gets word to search
    word = module.getString("Enter a word to search")
    # search files for word
    findInFiles(files, word)
    
main()