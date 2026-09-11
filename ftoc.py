def fahrenheit_to_celsius(F):
    C = (F-32)/1.8
    return C

F = float(input("Enter Temp in Fahrenheit:"))

print("Temp in Celsius=", fahrenheit_to_celsius(F))