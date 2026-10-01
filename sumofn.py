def sum_even(n):
    total = 0 

    for i in range(1, n+1):
        total = total + (i * 2)

    return total 

n = int(input("Enter N:"))
result = sum_even(n)

print("Sum of N numbers = ", result)