#!/usr/bin/env python3

original_arr =  [2, 8, 9, 48, 8, 22, -12, 2]

new_arr = set()

for i in range(len(original_arr)):
    num = original_arr[i]+2
    if num > 5 :
        new_arr.add(num)

print(f"Original array: {original_arr}")
print(f"New array: {new_arr}")
