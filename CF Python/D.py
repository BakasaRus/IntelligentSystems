from typing import List
from random import randint
from math import sqrt

Vector = List[float]
Matrix = List[Vector]


def multiply_scalar(x: Vector, y: Vector) -> float:
    return sum([a * b for a, b in zip(x, y)])


def multiply_matrices(x: Matrix, y: Matrix) -> Matrix:
    rx = len(x)
    cx = len(x[0])
    ry = len(y)
    cy = len(y[0])
    res = [[float(0)] * cy for i in range(rx)]
    for i in range(rx):
        for j in range(cy):
            for ii in range(cx):
                res[i][j] += x[i][ii] * y[ii][j]

    return res


def invert(x: Matrix) -> Matrix:
    indices = list(range(len(x)))
    l = len(x)
    for index in indices:
        for j in range(l, l * 2):
            x[index].append(float(1) if (index + l == j) else float(0))

    for index in indices:
        if x[index][index] == 0:
            for j in range(index + 1, l):
                if x[j][index] != 0:
                    for k in range(2 * l):
                        x[j][k], x[index][k] = x[index][k], x[j][k]
                    break
        t = x[index][index]
        for j in range(index, 2 * l):
            x[index][j] /= t
        for j in range(index + 1, l):
            t2 = x[j][index]
            for k in range(index, l * 2):
                x[j][k] -= x[index][k] * t2

    for i in reversed(indices):
        for j in range(i - 1, -1, -1):
            t = x[j][i]
            for k in range(l, l * 2):
                x[j][k] -= x[i][k] * t

    res = [row[-1:-(l + 1):-1][::-1] for row in x]
    return res


def sgd(features: Matrix, res: Vector, n: int, m: int) -> Vector:
    n_iter = 8888
    lr = float(9595e-7)
    w = [float(0.)] * (m + 1)
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
        data = [float(x) for x in input().split()]
        features.append(data[:-1])
        features[-1].append(float(1))
        res.append(data[-1])

    answer = []

    if n * m <= 100:
        answer = linear_regression(features, res)
    else:
        ey = sum(res) / len(res)
        ey2 = sum([x ** 2 for x in res]) / len(res)
        dy = sqrt(ey2 - ey ** 2)

        dx, ex = [], []

        y2 = [(x - ey) / dy for x in res]
        for i in range(m):
            ex.append(sum([row[i] for row in features]) / n)
            ex2 = sum([row[i] ** 2 for row in features]) / n
            sq = sqrt(ex2 - ex[-1] ** 2)
            dx.append(sq if sq >= float(1e-6) else float(1))
            for j in range(n):
                features[j][i] = (features[j][i] - ex[-1]) / dx[-1]

        dx.append(float(1))
        answer = sgd(features, y2, n, m)
        answer = [answer[idx] * dy / dx[idx] for idx in range(m + 1)]
        answer[-1] = answer[-1] - sum([answer[i] * ex[i] for i in range(m)]) + ey

    print(*answer, sep='\n')


main()
