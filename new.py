#!/usr/bin/env python
_author_="Oumar Cisse"

with open("roster.txt", 'r') as inputFile:
    for line in inputFile.readlines():
        print(line.strip());