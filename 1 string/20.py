"""
Q20. Find the Longest Common Prefix

Read words separated by spaces and print their shared prefix. Print -1 when
there is no common prefix.
"""

words = input("Enter words separated by spaces: ").split()

if not words:
    print(-1)
else:
    prefix = words[0]

    for word in words[1:]:
        while prefix and not word.startswith(prefix):
            prefix = prefix[:-1]

        if not prefix:
            break

    print(prefix if prefix else -1)
