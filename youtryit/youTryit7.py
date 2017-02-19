h = {}
for line in open("dictionary.txt"):
    grades = []
    name = line.split(": ")
    grade = name[1].split(", ")
    for g in grade:
        grades.append(g.strip())
    for n in name:
        h[n] = grades

print "Enter name: ",
n = raw_input()
if n in h:
    print h[n]
else:
    print "%s is not found" % (n)