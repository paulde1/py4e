fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    line = line.split(" ")
    lst.append(line)

lst.sort()
print(lst)