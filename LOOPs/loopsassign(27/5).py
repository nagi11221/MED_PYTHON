#1 print the sum of even numbers in the list

# numbers = [1,4,7,10,13,16]

# sum = 0
# for items in numbers:
#     if items%2 == 0:
#         sum+=items
# print(sum)

#2 

# negetive_num = (3,5,9,-2,6,-7)
# for items in negetive_num:
#     if items < 0:
#         break
# print(items)   

#3

# Vowels = "Welcome to python loops"
# count = 0
# for items in Vowels:
#     if items in ('a','e','i','o','u'):
#         count+=1
# print(count)        

#4

# numbers = (1,2,3,5,6,7,8,9,10)
# for items in numbers:
#     if items % 3 == 0:
#         continue
#     print(items**2)    

#5

numbers = [5,1,0,12,-7]
for items in numbers:
    if items > 0:
        print(f"It is positive {items}")
    elif items < 0:
        print(f"It is negetive {items}")
    else :
        print("Zero Found")
print(items)