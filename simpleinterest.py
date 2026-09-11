def simple_interest(p,r,n):
    i = p * r * n /100
    return i 

p = float(input("Enter P:"))
r = float(input("Enter R:"))
n = float(input("Enter N:"))

print("Simple Interest=", simple_interest(p,r,n))