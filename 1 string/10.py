'''
Question 10: First Non-Repeating Character 
Difficulty:   
Medium 
Asked In: Amazon, Meta, Microsoft 
Problem Statement: 
Given a string s, find the first character that appears exactly once. 
If no such character exists, return -1. 
Input:
A single string s. 
Output: 
Return the first non-repeating character or -1. 
Constraints: 
• 1 <= len(s) <= 10^5  
• String contains only lowercase English letters. 
'''

#Dictionary
s= input()
freq= {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break        #to stop

else:
    print(-1)
