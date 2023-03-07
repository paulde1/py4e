strinput = input('Pick a Number:')
try:
    intval = int(strinput)
except:
    intval = -1

if intval > 0 :
    print('Nice work')
else: 
    print('Not a number')