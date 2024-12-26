def find_xmas(p_grid: [[]], direction: (int, int), x: int, y: int) -> bool:
    for i in range(1, 4):
        x_check, y_check = x + direction[0] * i, y + direction[1] * i
        if y_check < 0 or y_check >= len(p_grid) or x_check < 0 or x_check >= len(p_grid[0]):
            continue
        letter = p_grid[y + direction[1] * i][x + direction[0] * i]
        print(f'    x = {x_check}        y = {y_check}     letter = {letter}')
        if letter != 'MAS'[i-1]:
            return False
        xmas_grid[y_check][x_check] = letter

    return True


with open('puzzle_04.txt') as f:
    puzzle = f.readlines()

grid = []
for row in puzzle:
    grid.append([])
    for c in row.strip():
        grid[-1].append(c)

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
xmas_grid = []
for y in grid:
    xmas_grid.append(list(y))
for y in range(len(xmas_grid)):
    for x in range(len(xmas_grid[0])):
        xmas_grid[y][x] = ''



result = 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != 'X':
            continue

        for d in dirs:
            if find_xmas(grid, d, x, y):
                result += 1
                xmas_grid[y][x] = grid[y][x]

print(result)
for row in xmas_grid:
    print(row)
