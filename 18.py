def convert_distance(km):
    meter = km * 1000
    feet = meter * 3.28084
    inches = meter * 39.3701
    cm = km * 100000
    
    return meter, feet, inches, cm


km = float(input("Enter distance in KM: "))

meter, feet, inches, cm = convert_distance(km)

print("Meter =", meter)
print("Feet =", feet)
print("Inches =", inches)
print("Centimeters =", cm)