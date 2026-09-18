def sphere(r):
    volume = (4*3.14*r*r*r) /3
    area = 4 * 3.14 * r *r 
    return volume , area

r = float(input("Enter radius:"))
volume,area = sphere(r)

print("Volume = ",volume)
print("Surface area = ",area)