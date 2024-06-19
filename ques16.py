from collections import Counter

def count_character(input_string):
    return Counter(input_string)

# Example usage
str1 = input("Enter a string: ")
frequency = count_character(str1)
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")