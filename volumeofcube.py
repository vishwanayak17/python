def volume_of_cube(length,breath,height):
    area = length * breath * height
    return area

length = float(input("Enter Length:"))
breath = float(input("Enter Breath:"))
height = float(input("Enter Height:"))

print("Volume of Cube=", volume_of_cube(length,breath,height))