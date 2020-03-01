import math

class Entity:
    features = None
    target = None
    distance = None

    def __init__(self, features, target=None):
        self.features = features
        self.target = target

    def __str__(self):
        return f'Entity(features = {self.features}, target = {self.target}, distance = {self.distance})'

    def set_distance(self, another, dist_function):
        self.distance = dist_function(self.features, another.features)


def get_kernel_function(name):
    kernels = {
        'uniform': lambda u: 1/2 if abs(u) < 1 else 0,
        'triangular': lambda u: 1 - abs(u) if abs(u) < 1 else 0,
        'epanechnikov': lambda u: 3/4 * (1 - u ** 2) if abs(u) < 1 else 0,
        'quartic': lambda u: 15/16 * (1 - u ** 2) ** 2 if abs(u) < 1 else 0,
        'triweight': lambda u: 35/32 * (1 - u ** 2) ** 3 if abs(u) < 1 else 0,
        'tricube': lambda u: 70/81 * (1 - u ** 3) ** 3 if abs(u) < 1 else 0,
        'gaussian': lambda u: 1 / math.sqrt(math.tau) * math.exp(-1/2 * u ** 2),
        'cosine': lambda u: math.pi / 4 * math.cos(math.pi / 2 * u) if abs(u) < 1 else 0,
        'logistic': lambda u: 1 / (math.exp(u) + math.e + math.exp(-u)),
        'sigmoid': lambda u: 2 / math.pi * 1 / (math.exp(u) + math.exp(-u)),
    }
    return kernels[name]


def get_distance_function(name):
    distances = {
        'manhattan': lambda x, y: sum([abs(a - b) for (a, b) in zip(x, y)]),
        'euclidean': lambda x, y: sum([a ** 2 + b ** 2 for (a, b) in zip(x, y)]) ** 0.5,
        'chebyshev': lambda x, y: max([abs(a - b) for (a, b) in zip(x, y)])
    }
    return distances[name]


n, m = map(int, input().split())
data = []
for i in range(n):
    raw = [int(x) for x in input().split()]
    data.append(Entity(raw[:m], raw[m]))

query = Entity([int(x) for x in input().split()])
dist = input()
kernel = input()
window = input()
h = int(input())

kernel_function = get_kernel_function(kernel)
distance_function = get_distance_function(dist)

for entity in data:
    entity.set_distance(query, distance_function)

if window == 'variable':
    data.sort(key=lambda x: x.distance)
    h = data[h].distance

overall = sum([entity.target for entity in data]) / n

if h == 0:
    same = [entity.target for entity in data if entity.features == query.features]
    query.target = sum(same) / len(same) if len(same) > 0 else overall
else:
    sum_up = 0
    sum_down = 0
    for entity in data:
        kf = kernel_function(entity.distance / h)
        sum_up += entity.target * kf
        sum_down += kf
    query.target = sum_up / sum_down if sum_down != 0 else overall

print(f'{query.target:.10f}')
