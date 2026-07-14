'''
Q9. Valid Anagram 
Difficulty:   
Medium 
Asked In: Amazon, Google, Microsoft 
Problem Statement:
Given two strings s and t, determine whether t is an anagram of s. 
Two strings are anagrams if they contain the same characters with the same frequencies, 
but the order of characters may differ. 
Return True if they are anagrams; otherwise return False. 
Input:
Two strings. 
Output:
True 
or 
False 
Constraints: 
• 1 <= len(s), len(t) <= 5 × 10^4  
• Strings contain only lowercase English letters. 
'''

s = input()
t = input()

if sorted(s) == sorted(t):
    print(True)
else:
    print(False)
    