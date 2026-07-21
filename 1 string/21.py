"""
Q21. Count Word Frequencies

Read a sentence and print each word with its frequency in order of first
appearance. Matching is case-insensitive.
"""

words = input("Enter a sentence: ").lower().split()
frequency = {}
order = []

for word in words:
    if word not in frequency:
        frequency[word] = 0
        order.append(word)
    frequency[word] += 1

for word in order:
    print(word + ":", frequency[word])
