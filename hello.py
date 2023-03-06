#print
print('hello Paul')
#considtional
x=11
if x > 15:
    print('larger')
if x < 15:
    print('smaller')
#while loop
n= 5
while n > 0:
    print(n)
    n = n -1
print('gottaBlast')
#for loop, get the name of the file and open it 
name = input('Enter File:')
handle = open(name, 'r')

#count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

largeCount = None
largeWord = None
#locate the most common word
for word, count in counts.items():
    if largeCount is None or count > largeCount:
        largeWord = word
        largeCount  = count
#print results
print(largeWord,largeCount)
