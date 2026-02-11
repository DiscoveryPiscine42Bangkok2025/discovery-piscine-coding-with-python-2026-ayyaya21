#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    word = sys.argv[1]
    text = sys.argv[2]

    find = re.findall(word, text)

    if len(find) > 0:
        print(len(find))
    else:
        print("none")

else:
    print("none")
