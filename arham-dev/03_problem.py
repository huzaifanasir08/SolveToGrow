# Reverse a string without using slicing ([::-1]) or reversed().


str = "Arham"
rev = ""

for c in str:
    rev = c + rev

print("The reverse string is: ", rev)