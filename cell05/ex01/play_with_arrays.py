#!/usr/bin/env python3

original_arr =  [2, 8, 9, 48, 8, 22, -12, 2]

new_arr = []

for i in range(len(original_arr)):
    new_arr.append(original_arr[i]+2)

print(f"Original array: {original_arr}")
print(f"New array: {new_arr}")
