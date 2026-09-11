def area_of_rectangle(length,breath):
    area = length*breath
    return area

length = float(input("Enter Length:"))
breath = float(input("Enter Breath:"))

print("Area of Rectangle=", area_of_rectangle(length,breath))