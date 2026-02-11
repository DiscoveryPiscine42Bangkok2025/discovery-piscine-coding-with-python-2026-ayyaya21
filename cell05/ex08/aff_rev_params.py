#!/usr/bin/env python3

import sys

if len(sys.argv) > 3:
    for i in sys.argv[:0:-1]:
        print(i)
else:
    print("none")
