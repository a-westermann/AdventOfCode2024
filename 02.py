import re


def check_safety(nums: [int]) -> bool:
    increase = nums[1] - nums[0] > 0
    for i in range(len(nums) - 1):
        if not (1 <= abs(nums[i + 1] - nums[i]) <= 3) or (nums[i + 1] - nums[i] > 0) != increase:
            return False
    return True


safe_report_count = 0
with open('puzzle_02.txt') as f:
    reports = f.readlines()
unsafe_reports = []  # part 2

for report in reports:
    numbers = [int(n) for n in re.findall('[0-9]+', report)]
    safe = check_safety(numbers)
    if not safe:
        unsafe_reports.append(report)
    else:
        safe_report_count += 1

print(f'Part 1: {safe_report_count}')

# part 2, you can remove 1 level from the report if needed to make it safe
for report in unsafe_reports:
    numbers = [int(n) for n in re.findall('[0-9]+', report)]
    for i in range(len(numbers)):
        new_numbers = list(numbers)
        del new_numbers[i]
        if check_safety(new_numbers):
            safe_report_count += 1
            break

print(f'Part 2: {safe_report_count}')


