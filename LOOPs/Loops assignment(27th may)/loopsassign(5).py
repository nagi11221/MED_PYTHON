#5 Categorize Numbers using if-elif-else

numbers = [5,1,0,12,-7]
for items in numbers:
    if items > 0:
        print(f"It is positive {items}")
    elif items < 0:
        print(f"It is negetive {items}")
    else :
        print("Zero Found")
print(items)