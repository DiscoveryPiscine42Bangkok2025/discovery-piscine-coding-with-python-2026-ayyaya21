#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 2:
    param = sys.argv[1]
    word = input("What was the parameter? ")

    find = re.findall(param, word)

    if find:
        print("Good job!")
    else:
        print("Nope, sorry...")

else:
    print("none")
