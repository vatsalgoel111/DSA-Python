"""
Q14. Count Vowels and Consonants

Read a string and print its vowel and consonant counts. Non-alphabetic
characters are ignored.
"""

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for character in text:
    if ("a" <= character <= "z") or ("A" <= character <= "Z"):
        if character in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
