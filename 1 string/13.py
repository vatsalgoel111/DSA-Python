"""
Q13. Check Whether Two Strings Are Anagrams

Given two strings, print True when they contain the same characters with the
same frequencies; otherwise print False. Spaces and letter case are preserved.
"""

first = input("Enter the first string: ")
second = input("Enter the second string: ")

if len(first) != len(second):
    print(False)
else:
    frequency = {}

    for character in first:
        frequency[character] = frequency.get(character, 0) + 1

    for character in second:
        frequency[character] = frequency.get(character, 0) - 1

    is_anagram = True
    for count in frequency.values():
        if count != 0:
            is_anagram = False
            break

    print(is_anagram)
