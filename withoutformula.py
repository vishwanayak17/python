def sum_num(n):
    total = 0 
    for i in range(1,n+1):
        total = total + i 
    
    return total 

n = int(input("Enter N:"))
result = sum_num(n)

print("Sum of Given Number = ", result)