#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print(f"parameter: {len(sys.argv) - 1}")
    for i in sys.argv[1:len(sys.argv):1]:
        print(f"{i}: {len(i)}")

else:
    print("none")
