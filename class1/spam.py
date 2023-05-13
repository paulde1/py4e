filename = input("Enter file name: ")
try:
    filehandler = open(filename)
except:
    print("Error opening ", filename)
    quit()
count= 0
average = 0
for line in filehandler:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        start = line.find(':')
        number = line[start +1:]
        average += float(number)

print('Average spam confidence: ', average/count)