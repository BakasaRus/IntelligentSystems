from typing import List
from random import randint
from decimal import Decimal
from copy import deepcopy

Vector = List[Decimal]
Matrix = List[Vector]


def multiply_scalar(x: Vector, y: Vector) -> Decimal:
    return sum([a * b for a, b in zip(x, y)])


def multiply_matrices(x: Matrix, y: Matrix) -> Matrix:
    rx = len(x)
    cx = len(x[0])
    ry = len(y)
    cy = len(y[0])
    res = [[Decimal(0)] * cy for i in range(rx)]
    for i in range(rx):
        for j in range(cy):
            for ii in range(cx):
                res[i][j] += x[i][ii] * y[ii][j]

    return res


def invert(x: Matrix) -> Matrix:
    source = deepcopy(x)
    indices = list(range(len(source)))
    l = len(source)
    for index in indices:
        for j in range(l, l * 2):
            source[index].append(Decimal(1) if (index + l == j) else Decimal(0))

    for index in indices:
        t = source[index][index]
        for j in range(index, 2 * l):
            source[index][j] /= t
        for j in range(index + 1, l):
            t2 = source[j][index]
            for k in range(index, l * 2):
                source[j][k] -= source[index][k] * t2

    for i in reversed(indices):
        for j in range(i - 1, -1, -1):
            t = source[j][i]
            for k in range(l, l * 2):
                source[j][k] -= source[i][k] * t

    res = [row[-1:-(l + 1):-1][::-1] for row in source]
    return res


def sgd(features: Matrix, res: Vector, n: int, m: int) -> Vector:
    n_iter = 6666
    lr = Decimal(9e-4)
    w = [Decimal(0.)] * (m + 1)
    for i in range(n_iter):
        idx = randint(0, n - 1)
        x = features[idx]
        error = multiply_scalar(w, x) - res[idx]
        for j in range(m + 1):
            w[j] -= lr * error * x[j]

    return w


def transpose(matrix: Matrix) -> Matrix:
    return list(map(list, zip(*matrix)))


def linear_regression(features: Matrix, res: Vector) -> Vector:
    features_t = transpose(features)
    result = multiply_matrices(features_t, features)
    result = invert(result)
    result = multiply_matrices(result, features_t)
    result = multiply_matrices(result, [[x] for x in res])
    result = [row[0] for row in result]
    return result


def main():
    n, m = map(int, input().split())
    features, res = [], []

    for i in range(n):
        data = [Decimal(x) for x in input().split()]
        features.append(data[:-1])
        features[-1].append(Decimal(1))
        res.append(data[-1])

    answer = []

    if n * m <= 10000:
        answer = linear_regression(features, res)
    else:
        ey = sum(res) / len(res)
        ey2 = sum([x ** 2 for x in res]) / len(res)
        dy = (ey2 - ey ** 2).sqrt()

        dx, ex = [], []

        y2 = [(x - ey) / dy for x in res]
        for i in range(m):
            ex.append(sum([row[i] for row in features]) / n)
            ex2 = sum([row[i] ** 2 for row in features]) / n
            sq = (ex2 - ex[-1] ** 2).sqrt()
            dx.append(sq if sq >= Decimal(1e-6) else Decimal(1))
            for j in range(n):
                features[j][i] = (features[j][i] - ex[-1]) / dx[-1]
            dx.append(Decimal(1))
            ans = sgd(features, y2, n, m)
            ans = [ans[idx] * dy / dx[idx] for idx in range(m + 1)]
            last = ans[-1]
            answer = ans[:-1] + [(last - sum([ans[i] * ex[i] for i in range(m)]) + ey)]

    print(*answer, sep='\n')


main()
