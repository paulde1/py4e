hrs = input("Enter Hours:")
rate = input("Enter Rate:")
pay = float(hrs) * float(rate)
print("Pay:", pay)

#overtime pay calculator
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