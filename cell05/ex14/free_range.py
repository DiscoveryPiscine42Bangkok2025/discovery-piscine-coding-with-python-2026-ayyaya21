#!/usr/bin/env python3

import sys

arr = []

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])

    for i in range(start, stop + 1):
        arr.append(i)
    
    print(arr)

else:
    print("none")
