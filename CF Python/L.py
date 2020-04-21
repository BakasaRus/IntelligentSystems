k = int(input())
n = int(input())
count = {x: {} for x in range(1, k + 1)}
count_x = {x: 0 for x in range(1, k + 1)}
x_y = {x: set() for x in range(1, k + 1)}

for i in range(n):
    x, y = map(int, input().split())
    count_x[x] += 1
    if y in x_y[x]:
        count[x][y] += 1
    else:
        count[x][y] = 1
        x_y[x].add(y)

dy = 0
for x in range(1, k + 1):
    ey = 0
    ey2 = 0
    for y in x_y[x]:
        r = (count[x][y] / count_x[x])
        ey += r * y
        ey2 += r * y * y
    dy += (ey2 - ey ** 2) * (count_x[x] / n)

print(dy)
