def convert_time(seconds):
    hour = seconds // 3600
    remaining = seconds % 3600
    
    minute = remaining // 60
    second = remaining % 60
    
    return hour, minute, second


seconds = int(input("Enter seconds: "))

hour, minute, second = convert_time(seconds)

print("Hour =", hour)
print("Minute =", minute)
print("Seconds =", second)