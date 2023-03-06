print('hello Paul')

x=11
if x > 15:
    print('larger')
if x < 15:
    print('smaller')

n= 5
while n > 0:
    print(n)
    n = n -1
print('gottaBlast')

name = input('Enter File:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

largeCount = None
largeWord = None

for word, count in counts.items():
    if largeCount is None or count > largeCount:
        largeWord = word
        largeCount  = count

print(largeWord,largeCount)
