# Problem

# Given two strings, determine whether they are at most one edit away.

#  *An edit is:* 
# Insert one character
# Delete one character
# Replace one character

#  *Example:* 
#  *Input:* 
# "pale"
# "ple"
#  *Output:* 
# True

#  *Input:* 
# "pale"
# "bake"

#  *Output:* 
# False


# Solution
string_1 = input('Enter a string: ')
string_2 = input('Enter another string: ')

same = False 
for char in string_1:
    s = string_1.replace(char,'')
    if string_2 == s:
        same = True
        break

print(same)


# Time & Space Complexity
# Time Complexity: O(n²)
# Space Complexity: O(n)