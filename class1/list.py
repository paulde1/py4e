fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    line = line.split(" ")

print(line)
    # for word in line:
    #     lst.append(word)

lst.sort()
print(lst)