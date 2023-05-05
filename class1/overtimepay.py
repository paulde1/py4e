#overtime pay calculator
def overtimePay():
    hours = input("Enter Hours:")
    rate = input("Enter Rate:")
    hours = float(hours)
    rate = float(rate)
    if hours > 40 :
        overtime = (hours % 10) * 15.75
        pay = (40 * rate) + overtime
    else : 
        pay = hours * rate
        
    print(pay)

overtimePay()