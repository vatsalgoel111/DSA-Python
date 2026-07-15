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

'''
#sort Strings
s = input()
t = input()

if sorted(s) == sorted(t):
    print(True)
else:
    print(False)
'''

#Count Frequenct Using Dictionary
s = input()
t = input()

if len(s) != len(t):
    print(False)

else:
    freq1 = {}
    freq2 = {}

    for ch in s:
        if ch in freq1:
            freq1[ch] = freq1[ch] + 1
        else:
            freq1[ch] = 1

    for ch in t:
        if ch in freq2:
            freq2[ch] = freq2[ch] + 1
        else:
            freq2[ch] = 1

    if freq1 == freq2:
        print(True)
    else:
        print(False)


