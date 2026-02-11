#!/usr/bin/env python3

msg = input()

for i in range(len(msg)):
    if msg[i].isupper():
        print(msg[i].lower(), end="")
    else:
        print(msg[i].upper(), end="")
