#overtime pay calculator
def overtimePay():
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    hrs = float(hrs)
    rate = float(rate)
    if hrs > 40 :
        overtime = (hrs % 10) * 15.75
        pay = (40 * rate) + overtime
    else : 
        pay = hrs * rate
        
    print(pay)

overtimePay()