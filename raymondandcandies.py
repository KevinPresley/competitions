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
            arg = args[i+k]
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

def has_neighbors(matrix,i,j,r,c):
    if i <= 0 or i >= r-1:
        return False
    if j <= 0 or j >= c-1:
        return False
    a = (matrix[i-1][j] == "1")
    b = (matrix[i+1][j] == "1")
    c = (matrix[i][j-1] == "1")
    d = (matrix[i][j+1] == "1")
    return a and b and c and d

def find_rhombus(matrix,r,c,level):

    points_to_remove=[]
    stillones = False
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "1":
                stillones = True
                if not has_neighbors(matrix,i,j,r,c):
                    points_to_remove.append([i,j])
    if stillones:
        for k in points_to_remove:
            matrix[k[0]][k[1]] = "0"
        return find_rhombus(matrix,r,c,level+1)
    else:
        return level

x = Reader()
[t] = process_line(x.next_line(), _int)
check_range(t, 1, 10)
for i in range(t):
    [r, c] = process_line(x.next_line(), _int, _int)
    check_range(r, 1, 50)
    check_range(c, 1, 50)
    matrix = []
    for j in range(r):
        [line] = process_line(x.next_line(), _str)
        line = list(line)
        matrix.append(line)
    l = find_rhombus(matrix,r,c,0)
    if l == 0:
        print(0)
    else:
        print(2*l-1)
