#!usr/bin/python
import sys
import math

#####################################################################
#prewritten section of code to check arguments and handle inputs
_int = "int"
_dec = "dec"
_str = "str"

class Reader:
    def __init__(self, myfile=sys.stdin):
        self.current_line = 0
        self.lines = myfile.readlines()
    def has_line(self):
        return self.current_line < len(self.lines)
    def next_line(self):
        return self.get_lines()[0]
    def get_lines(self, number=1):
        result = self.lines[self.current_line:(self.current_line+number)]
        self.current_line += number
        return result

def check_range(number, minimum, maximum, exc=False, bot_exc=False, top_exc=False):
    if exc or bot_exc:
        assert(number > minimum)
    else:
        assert(number >= minimum)
    if exc or top_exc:
        assert (number < maximum)
    else:
        assert (number <= maximum)

def process_line(line, *args, iterations=1, nested=False):
    result = []
    sections = line.split()
    assert(len(sections) == iterations * len(args))
    for j in range(iterations):
        k = j * len(args)
        subresult = []
        for i in range(len(args)):
            arg = args[i]
            sect = sections[i+k]
            if arg == _int:
                sect = int(sect)
            elif arg == _dec:
                sect = float(sect)
            if nested:
                subresult.append(sect)
            else:
                result.append(sect)
        if nested:
            result.append(subresult)
    return result
#end section of processing
#####################################################################

def recursion(l):
    if len(l) <= 20:
        d = float("inf")
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                d = min(d, dist(l[i], l[j]))
        return d
    else:
        midpoint = math.floor(len(l)/2)
        d1 = recursion(l[:midpoint])
        d2 = recursion(l[midpoint:])
        d = min(d1, d2)
        yline = (l[midpoint-1][0] + l[midpoint][0])/2
        mergelist = [point for point in l if abs(point[0]-yline) < d]
        mergelist = sorted(mergelist, key=lambda x: x[1])
        for i in range(len(mergelist)):
            for j in range(1,8):
                if i+j < len(mergelist):
                    d = min(d, dist(mergelist[i], mergelist[i+j]))
        return d

def dist(loc1, loc2):
    xdiff = loc1[0] - loc2[0]
    ydiff = loc1[1] - loc2[1]
    val = xdiff**2 + ydiff**2
    return math.sqrt(val)

x = Reader()
[t] = process_line(x.next_line(), _int)
check_range(t, 1, 10)
for i in range(t):
    [s] = process_line(x.next_line(), _int)
    pts = process_line(x.next_line(), _int, _int, iterations=s, nested=True)
    l = sorted(pts, key=lambda x: x[0])
    print("%.4f" % recursion(l))
