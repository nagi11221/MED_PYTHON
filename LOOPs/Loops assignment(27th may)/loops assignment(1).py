# 1 print the sum of even numbers in the list

numbers = [1,4,7,10,13,16]

sum = 0
for items in numbers:
    if items%2 == 0:
        sum+=items
print(sum)
  