#1 
numbers =(input("enter any 5 numbers: "))
Search = (input("enter a number to search: "))
for i in numbers:
    if i == Search:
        print("found")
        break
else:
    print("Not found")