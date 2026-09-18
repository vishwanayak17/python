def angle_degree(angle):
    formula = (angle * 3.14)/180
    return formula

angle = float(input("Enter angle in degrees:"))

radian = angle_degree(angle)
print("Angle in radian=", radian)