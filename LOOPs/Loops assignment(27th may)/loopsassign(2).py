#2 Find the First Negative Number in a Tuple

negetive_num = (3,5,9,-2,6,-7)
for items in negetive_num:
    if items < 0:
        break
print(items)  