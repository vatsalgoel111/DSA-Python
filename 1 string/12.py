'''
Question 12: Reverse Words in a String 
Difficulty:   
Medium 
Asked In: Amazon, Microsoft, Oracle 
Problem Statement:
Given a string containing words separated by spaces, reverse the order of the words. 
• Remove extra spaces.  
• Keep only one space between words.  
Input:
A string s. 
Output:
Return the string with the words in reverse order. 
Constraints 
• 1 <= len(s) <= 10^4  
Example 1 
Input 
I Love Python 
Output 
Python Love I 
Example 2 
Input 
Hello   World 
Output 
World Hello 
Example 3 
Input 
OpenAI is awesome 
Output 
awesome is OpenAI 
Follow-up 
Can you solve it without using split()?

ways:
1. Manual Traversal
2. Two Poitners
'''

#Manual Traversal
sentence = input()

result = []
temp = ""

for ch in sentence:

    if ch == " ":
        if temp != "":
            result.append(temp)
            temp = ""
    else:
        temp = temp + ch

if temp != "":
    result.append(temp)

for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")