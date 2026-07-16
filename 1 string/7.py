'''
Q7. Check if Two Strings are Equal 
Difficulty:   
Easy 
Asked In: Infosys, Capgemini, Tech Mahindra 
Problem Statement:
Given two strings s1 and s2, determine whether they are exactly equal. 
Return: 
• "Equal" if both strings are identical.  
• "Not Equal" otherwise.  
Comparison is case-sensitive. 
Input:
Two strings. 
Output: 
Equal 
or 
Not Equal 
Constraints: 
• 1 <= len(s1), len(s2) <= 10^5  

2 ways:
using ==
using characters first by length then ch
'''

s1 = input()
s2 = input()

if s1 == s2:
    print ("Equal")
else:
    print ("Not Equal")
    
        
