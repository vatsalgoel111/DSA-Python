'''
Q1. Problem Statement:
Given a string s, reverse the string and return the reversed string.
You are not allowed to use any built-in reverse function.
Input:
A single string s.
Output:
Return the reversed string.
Constraints:
• 1 <= len(s) <= 10^5
• The string contains English letters, digits, and special character.

2 ways:
Using loop and indexing
'''

s = input("Enter a string:")
rev = ""
for ch in s:
    rev = ch + rev

print(rev)


''' #Indexing:
s= input()
rev = ""
for i in range(len(s)-1,-1,-1):      #range(start,stop,step) so start = len(s)-1
    rev = rev + s[i]

print(rev)
'''

'''
s= input()
rev = ""
for i in s:
    rev = i + rev

print(rev)    

'''



