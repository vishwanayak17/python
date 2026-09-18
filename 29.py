def digit_word(digit):
    if digit == 0:
        return "Zero"
    elif digit == 1:
        return "One"
    elif digit == 2:
        return "Two"
    elif digit == 3:
        return "Three"
    elif digit == 4:
        return "Four"
    elif digit == 5:
        return "Five"
    elif digit == 6:
        return "Six"
    elif digit == 7:
        return "Seven"
    elif digit == 8:
        return "Eight"
    else:
        return "Nine"


number = int(input("Enter 4 Digit Number: "))

d1 = number // 1000
d2 = (number // 100) % 10
d3 = (number // 10) % 10
d4 = number % 10

print(digit_word(d1), digit_word(d2), digit_word(d3), digit_word(d4))