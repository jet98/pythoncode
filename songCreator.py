import module

firstVerse = module.getString("Enter the first verse: ")
secondVerse = module.getString("Enter the second verse: ")
thirdVerse = module.getString("Enter the third verse: ")
fourthVerse = module.getString("Enter the fourth verse: ")
chorus = module.getString("Enter the chorus: ")
repeat = module.getInt("Enter the chorus repeat: ")

song = [firstVerse.replace("cookies", "_______").lower(), chorus.upper(), secondVerse.replace("cookies", "_______").lower(), chorus.upper(), thirdVerse.replace("cookies", "_______").lower(), chorus.upper(), fourthVerse.replace("cookies", "_______").lower(), chorus.upper()]
song.append("---one more time---")
song = song + [firstVerse.replace("cookies", "_______").lower(), chorus.upper(), secondVerse.replace("cookies", "_______").lower(), chorus.upper(), thirdVerse.replace("cookies", "_______").lower(), chorus.upper(), fourthVerse.replace("cookies", "_______").lower(), chorus.upper()]
print song
print ""
for line in song:
    module.printString(line)