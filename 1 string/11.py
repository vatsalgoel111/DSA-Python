'''
Question 11: Remove Duplicate Characters from a String.
Difficulty:   
Medium 
Asked In: Amazon, Adobe, Walmart 
Problem Statement:
Given a string s, remove all duplicate characters while preserving the order of their first occurrence. 
Return the resulting string. 
Input:
A single string s. 
Output:
Return the string after removing duplicate characters. 
Constraints:
• 1 <= len(s) <= 10^5  
• The string contains only lowercase English letters. 
'''

s = input()
seen = {}
answer = ""

for ch in s:
    if ch not in seen:
        answer += ch
        seen[ch] = True

print(answer)
