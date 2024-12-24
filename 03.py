import re


result = 0
with open('puzzle_03.txt') as f:
    instructions = f.read()

valid_inputs = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)
[print(x) for x in valid_inputs]
