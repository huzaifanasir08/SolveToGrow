# Problem
# Write a program to count the number of characters in a string without using len().

# eg.
# Input: "Hello World"
# Output: 11


# Solution
string = input('Enter you string:')
length = 0
for char in string:
    length +=1

print(f"length of {string} is {length}")


# Time & Space Complexity
# Time: O(n), where n is the number of characters.
# Space: O(1).