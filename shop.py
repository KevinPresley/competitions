#!usr/bin/python
import sys
import math
t = -1
s = -1

def dist(loc1, loc2):
    xdiff = loc1[0] - loc2[0]
    ydiff = loc1[1] - loc2[1]
    val = xdiff**2 + ydiff**2
    return math.sqrt(val)

print dist((3,5), (6,9))

for line in sys.stdin:
    if t == -1:
        numtests = int(line)
        s = -1
    elif s == -1:
        s = int(line)
        pairs = []
    else:
        sections = line.split()
        for i in range(0, 2*s, 2):
            pairs.append(tuple(sections[i], sections[i+1]))

mindist = dist(pairs[0], pairs[1])
for i in range(len(pairs)):
    x = pairs[i][0]
    y = pairs[i][1]
