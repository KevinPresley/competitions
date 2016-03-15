#!usr/bin/python
import sys

t = -1
abline = False
i = 0
a = 0
b = 0
c = 0
candybags = []
return_list = []

for line in sys.stdin:
    if t == -1:
        t = int(line)
        abline = True
    elif abline:
        sections = line.split()
        a = int(sections[0])
        b = int(sections[1])
        c = a+b
        abline = False
    elif i < a:
        i += 1
        candybags.append(line.split())
    else:
        i += 1
        sections = line.split()
        name = sections[0]
        happiness = int(sections[1])
        likes = sections[2:]
        add = False
        for candy in candybags:
            current_happiness = 0
            for j in range(4):
                current_happiness += (int(candy[j]) * int(likes[j]))
            if happiness <= current_happiness:
                add = True
        if add:
            return_list.append(name)
        if i == c:
            print " ".join(sorted(return_list))
            return_list = []
            i = 0
            candybags = []
            abline = True

