"""
Q19. Check for Balanced Parentheses

Given a string containing parentheses, brackets, and braces, print True when
every opening symbol is closed in the correct order.
"""

text = input("Enter brackets: ")
opening = "([{"
matching = {")": "(", "]": "[", "}": "{"}
stack = []
is_balanced = True

for character in text:
    if character in opening:
        stack.append(character)
    elif character in matching:
        if not stack or stack.pop() != matching[character]:
            is_balanced = False
            break

if stack:
    is_balanced = False

print(is_balanced)
