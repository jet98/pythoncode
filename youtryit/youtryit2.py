print "Enter a sentence"
sentence = raw_input()
length = len(sentence)
sentence = sentence.replace('a', str(length))
sentence = sentence.replace('e', str(length + 1))
sentence = sentence.replace('i', str(length + 2))
sentence = sentence.replace('o', str(length + 3))
sentence = sentence.replace('u', str(length + 4))
print "The encrypted sentence is: %s" % sentence
sentence = sentence.replace(str(length), 'a')
sentence = sentence.replace(str(length + 1), 'e')
sentence = sentence.replace(str(length + 2), 'i')
sentence = sentence.replace(str(length + 3), 'o')
sentence = sentence.replace(str(length + 4), 'u')
print "The decrypted sentence is: %s" % sentence