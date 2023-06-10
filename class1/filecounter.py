name = input("Enter File:")
filehandler = open(name)

counts = dict()
for line in filehandler:
    words = line.split()
    for word in words:
        counts[word]= counts.get(word, 0) + 1

bigCounter = None
bigWord = None
for word,count in counts.items():
    if bigCounter is None or count > bigCounter :
        bigWord = word
        bigCounter = count

print (bigCounter, bigWord)
