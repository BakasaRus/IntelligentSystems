import math


kx, ky = map(int, input().split())
n = int(input())
count = {x: {} for x in range(1, kx + 1)}
count_x = {x: 0 for x in range(1, kx + 1)}
x_y = {x: set() for x in range(1, kx + 1)}

for i in range(n):
    x, y = map(int, input().split())
    count_x[x] += 1
    if y in x_y[x]:
        count[x][y] += 1
    else:
        count[x][y] = 1
        x_y[x].add(y)

s = 0.
for x in range(1, kx + 1):
    ps = 0.
    for y in x_y[x]:
        temp = count[x][y] / count_x[x]
        ps -= temp * math.log(temp)
    s += count_x[x] / n * ps

print(s)
