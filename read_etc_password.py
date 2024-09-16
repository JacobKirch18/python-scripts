#!/usr/bin/env python3

#reads the name fields out of the etc/passwd file
#prints the number of people with the same first name
#remove final instance .split() to use full names

from sys import stdin

strings = []
names = {}

for line in stdin:
    strings.append(line)

for string in strings:
    parts = string.split(":")
    if int(parts[2]) >= 1000:
        if parts[4] != '':
            name = parts[4].split()[0].capitalize()
            names[name] = names.get(name, 0) + 1

for name in names:
    print(f"{name}: {names[name]}")
