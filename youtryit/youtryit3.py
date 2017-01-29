import youTryIt

adjective1 = youTryIt.getString("Enter an adjective: ")
adjective2 = youTryIt.getString("Enter another adjective: ")
pluralNoun1 = youTryIt.getString("Enter a plural noun: ")
pluralNoun2 = youTryIt.getString("Enter another plural noun: ")
celeb = youTryIt.getString("Enter a celebrity: ")
noun = youTryIt.getString("Enter a noun: ")

print "In the shadowy world of spies, a/an %s organization like to US Government uses spies to infultrate %s groups for the purpose of containing secret %s. A teacher, %s, or even the little old %s with a cane and fifteen pet %s could be a spy." % (adjective1, adjective2, pluralNoun1, celeb, noun, pluralNoun2)