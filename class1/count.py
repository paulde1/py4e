filehandler = open(filename)
count = 0
for line in filehandler: 
    count += 1
print('Total line count:', count)

for line in filehandler:
    if line.startswith('From:') :
        print(line)

## open file handler

filename = input('Enter filename: ')
try:
    filehandler = open(filename)
except:
    print('Could not open file: ' + filename)
    quit()
    
count = 0
for line in filehandler:
    if line.startswith('subject:') :
        count += 1
print('There were ', count, ' subject lines in ', filename)