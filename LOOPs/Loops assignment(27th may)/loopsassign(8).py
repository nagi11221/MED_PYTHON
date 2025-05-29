#8. Check if Any Number is a Perfect Square
import math

numbers = [10,25,36,40]

for items in numbers:
    if math.isqrt(items)**2 == items:
        print(f"perfect square:{items}")
     