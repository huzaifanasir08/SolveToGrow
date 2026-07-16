"""
Write a program to count the number of characters in a string without using len().

eg.
Input: "Hello World"
Output: 11
"""

string = input("Enter a string: ")
def count_characters(string):
    count = 0
    for char in string:
        count += 1
    return count

print(f"Length of the string '{string}' is: ", count_characters(string))
