def convert_days(days):
    year = days // 365
    remaining = days % 365
    
    month = remaining // 30
    remaining_days = remaining % 30
    
    return year, month, remaining_days


days = int(input("Enter number of days: "))

year, month, remaining_days = convert_days(days)

print("Year =", year)
print("Month =", month)
print("Remaining Days =", remaining_days)