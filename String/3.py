'''
Q3. Find the Length of a String Without Using len()
Difficulty: Easy
Asked In: Infosys, Accenture, Wipro
Problem Statement:
Given a string s, determine its length without using Python's built-in len() function.
Input:
A string s.
Output:
Return the total number of characters.
Constraints
• 1 <= length <= 10^5

3 ways:
using for and while loop and Recursion
'''

#loop
s = input()
count = 0
for ch in s:
    count = count + 1

print (count)    
