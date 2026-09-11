def area_of_triangle(length,breath):
    area = length*breath/2
    return area

length = float(input("Enter Length:"))
breath = float(input("Enter Breath:"))

print("Area of Triangle=", area_of_triangle(length,breath))