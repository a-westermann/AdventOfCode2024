import re


left_list = []
right_list = []
with open('puzzle_01.txt') as f:
    for row in f.readlines():
        numbers = re.findall('[0-9]+', row)
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

left_list.sort()
right_list.sort()
result = 0
for i in range(len(left_list)):
    result += abs(left_list[i] - right_list[i])

print(f'Part 1: {result}')

# part 2: find how many times a number in the left list appears in right list, multiply that number by the result
# then add up all the numbers from the left list
result = 0
for num in left_list:
    count = right_list.count(num)
    result += num * count

print(f'Part 2: {result}')
