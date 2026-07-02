# A string in which there are some dublicate charachters, so create new string with without dublication
# For Example
# word = Neccessary
# New_word= Necsary


word = input("Enter Any string: ")
new_word=""

for fw in word:
    for ex in new_word:
        if fw == ex:
            break
    else:
        new_word += fw

print("Original string:", word)
print("String without duplicates:", new_word)



