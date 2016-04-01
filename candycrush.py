#!usr/bin/python
import sys

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

def get_exact(a, x):
    count = 0
    while a != x:
        count += 1
        if a < x:
            a += 1
        elif a % 2 == 1:
            a += 1
        else:
            a = a/2
    return count
        
r = Reader()
[t] = process_line(r.next_line(), _int)
check_range(t, 1, 10)
for i in range(t):
    [x,y,z,a,b,c] = process_line(r.next_line(), _int, iterations=6)
    d = get_exact(a,x)
    e = get_exact(b,y)
    f = get_exact(c,z)
    print(d+e+f)


