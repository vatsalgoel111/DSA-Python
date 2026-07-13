'''
Q4. Count Vowels and Consonants
Difficulty: Easy
Asked In: Wipro, Cognizant, Capgemini
Problem Statement:
Given a string consisting only of English alphabets, count the number of vowels and consonants.
The vowels are:
a, e, i, o, u
All remaining alphabetic characters are considered consonants.
Input:
A single string s.
Output:
Vowels = X
Consonants = Y
Constraints
• The string contains only alphabets.
• 1 <= length <= 10^5

3 ways:
using in operator and by checking every character and using sets
'''

s = input()
vowel=0
consonant=0
for ch in s:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":   #also use in operator
        vowel=vowel+1
    else:
        consonant=consonant+1

print("Vowels=",vowel)
print("Consonants=",consonant)