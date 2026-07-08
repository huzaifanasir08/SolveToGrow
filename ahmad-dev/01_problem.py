string = "programming"
new_string = str()

# Start time: 1641h, 030726d
def return_unique_characters_string(string):
    
    characters_list = []

    for char in string:
        if char in characters_list:
            pass
        else:
            characters_list.append(char)
    
    new_string = "".join(characters_list)
    return new_string

print(return_unique_characters_string(string))

# Solve time: 1644h