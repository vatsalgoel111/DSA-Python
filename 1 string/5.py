'''
Q5. Count Frequency of Each Character 
Difficulty:   
Easy 
Asked In: Amazon, Deloitte, TCS Digital 
Problem Statement:
Given a string s, count how many times each character appears in the string. 
Return the frequency of every character. 
Input:
A string s. 
Output:
Print each character followed by its frequency. 
Constraints 
• 1 <= length <= 10^5 

2 ways:
Nested loop and Dictionary
'''

s = input()
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for ch in freq:
    print(ch,"=",freq[ch])
                  


