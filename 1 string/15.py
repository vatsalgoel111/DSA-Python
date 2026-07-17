"""
Q15. Find the Longest Word in a Sentence

Print the first longest word after treating consecutive spaces as a single
separator. Punctuation remains part of the word.
"""

sentence = input("Enter a sentence: ")
longest_word = ""
current_word = ""

for character in sentence + " ":
    if character == " ":
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""
    else:
        current_word += character

if longest_word == "":
    print(-1)
else:
    print(longest_word)
