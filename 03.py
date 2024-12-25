import re


with open('puzzle_03.txt') as f:
    instructions = f.read()

valid_inputs = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)
result = 0
for x in valid_inputs:
    num_1, num_2 = re.findall('[0-9]+', x)
    result += int(num_1) * int(num_2)
print(f'Part 1: {result}')

# part 2... iterate over each char and try to build instructions for next x chars
result = 0
enabled = True
for i, c in enumerate(instructions):
    if c == 'd':
        func = ''.join([ch for ch in instructions[i:i+7]])
        if func[:4] == 'do()':
            enabled = True
        elif func == "don't()":
            enabled = False
    elif enabled and c == 'm':
        mul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions[i:i+12])
        if mul:
            num_1, num_2 = re.findall('[0-9]+', mul[0])
            result += int(num_1) * int(num_2)

print(f'Part 2: {result}')
