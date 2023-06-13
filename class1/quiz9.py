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
