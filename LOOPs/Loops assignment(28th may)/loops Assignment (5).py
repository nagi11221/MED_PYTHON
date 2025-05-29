
names =list(input("enter any 5 names :"))
search =(input("enter a name to search:"))
for i in names:
    if i == search:
        print("found")
    break  
else:
    print("Not found")