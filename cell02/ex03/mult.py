#!/usr/bin/env python3

first_num = int(input("Enter the first number:\n"))
sec_num = int(input("Enter the second number:\n"))

result = first_num * sec_num

print(f"{first_num} x {sec_num} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
