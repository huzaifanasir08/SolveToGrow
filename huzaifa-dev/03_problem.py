# Problem
# Reverse a string without using slicing ([::-1]) or reversed().

# eg.
# Input: "Python"
# Output: "nohtyP"


# Solution
string = input('Enter you string:')
reverse = ''
for char in string:
    reverse = char + reverse

print(f"Inverse string of {string} is {reverse}")


# Time & Space Complexity
# Time Complexity: O(n²)
# Space Complexity: O(n)