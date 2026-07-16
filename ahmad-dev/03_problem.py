"""
Reverse a string without using slicing ([::-1]) or reversed().

eg.
Input: "Python"
Output: "nohtyP"
"""

string = "ahmad"

def reverseStringEfficient(string):
    char_list = []
    for char in string:
        char_list.insert(0, char)
    return ''.join(char_list)

# But if using the insert method is not allowed, we can use a different approach:

def reverseStringAlternative(string):
    reversed_string_list = []
    for i in range(len(string) - 1, -1, -1): 
        reversed_string_list.append(string[i])
    return ''.join(reversed_string_list)

"""
Explaination for reverseStringAlternative:

what "range(len(string) - 1, -1, -1)" does is it starts from the last index of the string and goes to the first index, effectively reversing the string.

    Example: 
        if string = "ahmad", len(string) = 5, so range(len(string) - 1, -1, -1) will generate the indices [4, 3, 2, 1, 0]. This means we will access the characters in the order: string[4] = 'd', string[3] = 'a', string[2] = 'm', string[1] = 'h', string[0]
""" 