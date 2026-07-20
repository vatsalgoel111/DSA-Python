"""
Q16. Check Whether One String Is a Rotation of Another

Two strings are rotations when one can be obtained by moving characters from
the beginning of the other string to its end.
"""

first = input("Enter the first string: ")
second = input("Enter the second string: ")

if len(first) != len(second):
    print(False)
else:
    doubled = first + first
    print(second in doubled)
