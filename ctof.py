def celsius_to_fahrenheit(C):
    F = (C * (9/5) + 32)
    return F

C = float(input("Enter Temp in Celsius:"))

print("Temp in Fahrenheit=", celsius_to_fahrenheit(C))