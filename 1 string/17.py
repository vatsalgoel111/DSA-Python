"""
Q17. Remove Duplicate Characters While Preserving Order

Print each character only once, keeping its first appearance in the input.
"""

text = input("Enter a string: ")
seen = set()
result = ""

for character in text:
    if character not in seen:
        seen.add(character)
        result += character

print(result)
