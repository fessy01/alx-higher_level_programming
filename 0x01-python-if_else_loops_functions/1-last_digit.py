#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = repr(number)
last = int(number_string[-1])
if last > 5:
    print(f"Last digit of {number:d} is {last} and is greater than {5:d}")
elif last == 0:
    print(f"Last digit of {number:d} is {last} and is {0:d}")
else:
    print(f"Last digit of {number:d} is {last} and is less than {6:d} and not {0:d}")
