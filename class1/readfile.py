filename = input("Enter file name: ")
stringbuilder = ''
try:
    filehandler = open(filename)
except:
    print("Error opening ", filename)
    quit()

for line in filehandler:
    line = line.upper().lstrip()
    stringbuilder += line
print(stringbuilder)

