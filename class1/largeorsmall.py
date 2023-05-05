def smallorlarge():
    list = []
    while True:
        try:
            number = input("Enter a number:")
            if number == 'done':
                break
            converted = int(number)
            list.append(converted)
            maximum = max(list)
            minimum = min(list)
        except:
            print("input is not a valid number")
            
    print("Maximum is",maximum)
    print("Minimum is",minimum)

smallorlarge()