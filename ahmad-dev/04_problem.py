"""
Given two strings, determine whether they are at most one edit away

An Edit is:
insert one charachter
Delete one charachter
Replace one charachter

Example:
Input:
"pale"
"ple"

Output: True

Input:
"pale"
"bake"
Output: False
"""

string1 = input("Enter your first string: ")
string2 = input("Enter your second string: ")

def is_one_edit_away(string1, string2):
    unique_indices_count = 0
    len1 = len(string1)
    len2 = len(string2)

    if len1 == len2:
        print(
            f"""
                ====================================================
                      Identified Case 01: Same Length Strings.
                ====================================================
            """)
        for idx in range(len(string1)):
            if string1[idx] == string2[idx]:
                continue
            else:
                unique_indices_count +=1
    
    if len1 != len2:
        result = len1 - len2 if len1 > len2 else len2 -len1
        if result > 1:
            print(
            f"""
                ====================================================
                Identified Case 02: Length Difference of more than 1.
                ====================================================
            """)
            return False
        else:
            print(
            f"""
                ====================================================
                    Identified Case 03: Length Difference of 1.
                ====================================================
            """)

            longer_string = string1 if len1 > len2 else string2
            print(f"Longer String = {longer_string}, Length = {len(longer_string)}")

            shorter_string = string2 if len2 < len1 else string1
            print(f"Shorter String = {shorter_string}, Length = {len(shorter_string)} \n")

            longer_array = list(char for char in longer_string)
            shorter_array = list(char for char in shorter_string)

            unique_characters_count = 0
            
            for char in longer_array:
                if char in shorter_array:
                    continue
                else:
                    unique_characters_count += 1
            
            if unique_characters_count > 1:
                return False
            return True

    
    if unique_indices_count > 1:
        return False
    
    return True

print(is_one_edit_away(string1, string2))