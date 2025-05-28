#3 Count Vowels in a String Using a Set

Vowels = "Welcome to python loops"
count = 0
for items in Vowels:
    if items in ('a','e','i','o','u'):
        count+=1
print(count)        