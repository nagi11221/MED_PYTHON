#4 Print Squares of Numbers, Skip Multiples of 3

numbers = (1,2,3,5,6,7,8,9,10)
for items in numbers:
    if items % 3 == 0:
        continue
    print(items**2) 