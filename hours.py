def weekly_pay(rate,hours):
    pay = rate * hours
    return pay 

rate = float(input("Enter hourly pay rate:"))
hours = float(input("Enter hours worked:"))

pay = weekly_pay(rate,hours)
print("Weekly pay = ",pay)