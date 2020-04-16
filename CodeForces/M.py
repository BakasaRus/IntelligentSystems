kx, ky = map(int, input().split())
n = int(input())

count_x = {x: 0 for x in range(1, kx + 1)}
count_y = {y: 0 for y in range(1, ky + 1)}
count_xy = {}

for i in range(n):
    x, y = map(int, input().split())
    count_x[x] += 1
    count_y[y] += 1
    if (x, y) in count_xy:
        count_xy[(x, y)] += 1
    else:
        count_xy[(x, y)] = 1

x0 = {x: n for x in range(1, kx + 1)}
s = 0
for (x, y), count in count_xy.items():
    p = count_x[x] * count_y[y] / n
    s += (count - p) ** 2 / p
    x0[x] -= count_y[y]

for x in range(1, kx + 1):
    s += x0[x] / n * count_x[x]

print(s)
