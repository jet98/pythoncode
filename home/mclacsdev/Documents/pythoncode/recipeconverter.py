print "-- Original Recipe --"
print "Enter the amount of flour (cups): "
flour = raw_input()
print "Enter the amount of water (cups): "
water = raw_input()
print "Enter the amount of salt (teaspoon): "
salt = raw_input()
print "Enter the amount of yeast (teaspoon): "
yeast = raw_input()
print "Enter the loaf ajuustment factor (e.g. 2.0 double the size): "
loaf = raw_input()
print "-- Modified Recipe --"
print "BreadFlour: %.2f cups" % (float(flour) * float(loaf))
print "water: %.2f cups" % (float(water) * float(loaf))
print "salt: %.2f cups" % (float(salt) * float(loaf))
print "yeast: %.2f cups" % (float(yeast) * float(loaf))
print "Happy Baking! \n"
print "-- Modified Recipe in Grams --"
print "BreadFlour: %.2f cups" % (float(flour) * 125 * float(loaf))
print "water: %.2f cups" % (float(water) * 235.59 * float(loaf))
print "salt: %.2f cups" % (float(salt) * 5.69 * float(loaf))
print "yeast: %.2f cups" % (float(yeast) * 2.83 * float(loaf))
print "Happy Baking! \n"