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

arr = [0] * 26  #arr for lowercase letters
answer = ""     #empty string

for ch in s:
    index = ord(ch) - ord('a')   #ord('a') = 97

    if arr[index] == 0:
        answer = answer + ch
        arr[index] = 1

print (answer)
