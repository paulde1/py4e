filename = input("Enter file name: ")
stringbuilder = ''
try:
    filehandler = open(filename)
except:
    print("Error opening ", filename)
    quit()

for line in filehandler:
    newline = line
    stringbuilder += newline.upper()
print(stringbuilder.rstrip())

