'''
Q2. Valid Palindrome
Difficulty: Easy
Asked In: Amazon, Facebook (Meta), Microsoft
Problem Statement:
Given a string s, determine whether it is a palindrome.
A palindrome reads the same forward and backward.
Return True if it is a palindrome; otherwise return False.
Input:
A string s.
Output:
True
or
False
Constraints:
• 1 <= len(s) <= 10^5
'''
#Indexing:
s= input()
rev = ""
for i in range(len(s)-1,-1,-1):      #range(start,stop,step) so start = len(s)-1
    rev = rev + s[i]

if s == rev:
    print(True)

else:
    print(False)    

