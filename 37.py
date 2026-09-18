def check_vowel(alphabet):
    if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
        return "Vowel"
    else:
        return "Not Vowel"


alphabet = input("Enter an Alphabet: ")

result = check_vowel(alphabet)

print(result)