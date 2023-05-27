fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    for word in line:
        lst.append(word)
print(list)