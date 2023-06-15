filehandler = open("romeo.txt")
counts = dict()
for line in filehandler :
    words = line.split()
    for word in line :
        counts[word] = counts.get(word,0) + 1

list = list()
for key, value in counts.items() :
    newtuple = (value,key)
    list.append(newtuple)

list = sorted(list, reverse = True)

for value, key in list[:10] : # list slicing that allows us to onlyy go throughthe first 10
    print(key, value)


