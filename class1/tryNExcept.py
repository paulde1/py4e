def numberPicker():
    stringinput = input('Pick a Number:')
    try:
        intval = int(stringinput)
    except:
        intval = -1

    if intval > 0 :
        print('Nice work')
    else: 
        print('Not a number')

numberPicker()