#10
num = int(input("Enter a number: "))

print(f"Numbers from 1 to {num} divisible by 3:")
for i in range(1, num):
    if i % 3 == 0:
        print(i)
