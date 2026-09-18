def right_angle(base,height):
    formula = 0.5 * base * height
    return formula

base = float(input("Enter base:"))
height = float(input("Enter Height:"))

formula = right_angle(base,height)
print("Right angle of Triangle = ", formula)