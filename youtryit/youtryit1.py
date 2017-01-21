print "How many malcorps did you find on planet Exflon?"
exflon = raw_input();
print "How many malcorps did you find on planet Mobiles?"
mobiles = raw_input();
print "How many malcorps did you find on planet Monsantoes?"
monsontoes = raw_input();
total = int(exflon) + int(mobiles) + int(monsontoes)
avg = total/3.0
print "You found %d malcorps" % total
print "The average malcorps per planet is %.2f" % avg
