def compound_interest(p,r,n):
    formula = p * (1+r/100) ** n -p 
    return formula

p = float(input("Enter P:"))
r = float(input("Enter R:"))
n = float(input("Enter N:"))

formula = compound_interest(p,r,n)
print("Compound Interest = ", formula)