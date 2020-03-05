def ranking(a):
    seq = sorted(a)
    index = [seq.index(v) + 1 for v in a]
    return index


n = int(input())

X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X_ranks = ranking(X)
Y_ranks = ranking(Y)

sigma_D2 = sum([(x - y) ** 2 for x, y in zip(X_ranks, Y_ranks)])

P = 1 - 6 * sigma_D2 / n / (n ** 2 - 1)
print(f'{P:.9f}')
