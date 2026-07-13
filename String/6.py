'''
Q6. Remove All Spaces from a String 
Difficulty:   
Easy 
Asked In: TCS Digital, Cognizant, Wipro 
Problem Statement:
Given a string s, remove all spaces from the string and return the modified string. 
You must remove: 
• Leading spaces  
• Trailing spaces  
• Spaces between words  
Do not remove any other characters. 
Input:
A single string s. 
Output: 
Return the string after removing all spaces. 
Constraints:
• 1 <= len(s) <= 10^5 

3 ways:
 loop
 replace
 split and join
'''

s = input()
n = ""
for ch in s:
    if ch != " ":
        n = n + ch

print (n)


