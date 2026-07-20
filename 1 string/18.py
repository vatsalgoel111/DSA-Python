"""
Q18. Run-Length Encode a String

Replace consecutive repeated characters with the character followed by its
count. For example, aaabbc becomes a3b2c1.
"""

text = input("Enter a string: ")

if text == "":
    print("")
else:
    encoded = ""
    count = 1

    for index in range(1, len(text) + 1):
        if index < len(text) and text[index] == text[index - 1]:
            count += 1
        else:
            encoded += text[index - 1] + str(count)
            count = 1

    print(encoded)
