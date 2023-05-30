fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    lst.append(line)
    # for word in line:
    #     # letter = word.split('')
    #     lst.append(word)
    #     print(word)


    # for word in line:
    #     lst.append(word)

lst.sort()
print(lst)