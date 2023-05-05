def numberPicker():
    stringinput = input('Pick a Number:')
    try:
        integervalue = int(stringinput)
    except:
        integervalue = -1

    if integervalue > 0 :
        print('Nice work')
    else: 
        print('Not a number')

numberPicker()