#!usr/bin/python
import sys

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

lines = []
setf = False

for line in sys.stdin:
    if not setf:
        setf = True
        numlines = int(line)
    else:
        lines.append(line)

for i in range(numlines):
    line = lines[i]
    sections = line.split()
    shiftkey = int(sections[1])
    current_string = ""
    for letter in sections[0]:
        current_string += alphabet[(alphabet.index(letter) + shiftkey) % 26]
    print current_string