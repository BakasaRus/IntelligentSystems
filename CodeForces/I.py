n = int(input())

X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x_mean = sum(X) / len(X)
y_mean = sum(Y) / len(Y)

numerator = sum([(x - x_mean) * (y - y_mean) for x, y in zip(X, Y)])
denominator = (sum([(x - x_mean) ** 2 for x in X]) * sum([(y - y_mean) ** 2 for y in Y])) ** 0.5
ro = numerator / denominator if denominator != 0 else 0

print(f'{ro:.9f}')
