def readTemps():
    file = open('temps.txt', 'r')
    list = []
    for line in file:
        list.append(line)
    return list
def calcAvg(temps, start, stop):
    avg = 0
    counter = 0
    for temp in temps:
        if counter < stop and counter >= start:
            avg += float(temp)
            counter += 1
        else:
            counter += 1
    avg = avg / float(stop - start)
    return avg
def count(temps, start, stop):
    count = 0
    counter = 0
    for temp in temps:
        if counter < stop and counter >= start and float(temp) > 0:
            count += 1
            counter += 1
        else:
            counter += 1
    return count
def main():
    list = readTemps()
    print "Please enter percentage split ex. 35 (will split 35/65): ",
    split1 = raw_input()
    first = len(list) * (float(split1) * .01)
    avg = calcAvg(list, 0, int(first))
    annom = count(list, 0, int(first))
    print "During the first %.0f years, the average deviation from the temperature annually is %.2f" % (first, avg)
    print "During the last %.0f years, %.0f had a positive temperature annomoly" % (first, annom)
    avg = calcAvg(list, int(first), len(list))
    annom = count(list, int(first), len(list))
    print "During the last %.0f years, the average deviation from the temperature annually is %.2f" % (len(list) - first, avg)
    print "During the last %.0f years, %.0f had a positive temperature annomoly" % (len(list) - first, annom)
  
main()