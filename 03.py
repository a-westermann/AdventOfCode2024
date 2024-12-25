import re


with open('puzzle_03.txt') as f:
    instructions = f.read()

valid_inputs = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)
result = 0
for x in valid_inputs:
    num_1, num_2 = re.findall('[0-9]+', x)
    result += int(num_1) * int(num_2)
print(result)
