# A string in which there are some dublicate charachters, so create new string with without dublication
# For Example
# word = Neccessary
# New_word= Necsary

word = input("Enter a word: ")
marked = []
for l in word:
    if l not in marked:
        marked.append(l)
marked = ''.join(marked)

print(f'Word: {word}')
print(f'New Word: {marked}')