def sum_num(n):
    total = n * (n+1)/2

    return total

n = int(input("Enter N:"))
result = sum_num(n)

print("Sum of given number=", result)