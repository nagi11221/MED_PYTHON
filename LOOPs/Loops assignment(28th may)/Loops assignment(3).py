numbers = int(input("Enter numbers:"))
while numbers % 2 == 0:
    print(f"Even number {numbers}")
    break
else:
    print(f"Odd {numbers}")