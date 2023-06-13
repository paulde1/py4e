filename = input("Enter file: ")
if len(filename) < 1 : name = "mboxshort.txt"
handler = open(filename)

list = list()

for line in handler :
    if not line.startswith( "From:"): continue
    line = line.split()
    list.append(line[1])

container = dict()
for word in list:
    container[word]= container.get(word,0) + 1

bigcount = None
bigword = None

for word,count in container.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword =word

print(bigword,bigcount)