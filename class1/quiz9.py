fhand = open('mboxshort.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ')