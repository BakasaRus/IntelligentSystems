class Entity:
    features = None
    target = None
    distance = None

    def __init__(self, features, target=None):
        self.features = features
        self.target = target

    def __str__(self):
        return f'Entity(features = {self.features}, target = {self.target}, distance = {self.distance})'

    def set_distance(self, another):
        self.distance = sum([a ** 2 + b ** 2 for (a, b) in zip(self.features, another.features)]) ** 0.5


def kernel_function(u):
    return 1/2 if abs(u) <= 1 else 0


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

for entity in data:
    entity.set_distance(query)

data.sort(key=lambda x: x.distance)
print(*data, sep='\n')

sum_up = 0
sum_down = 0
for entity in data:
    sum_up += entity.target * kernel_function(entity.distance / h)
    sum_down += kernel_function(entity.distance / h)
    print(sum_up, sum_down)

query.target = sum_up / sum_down
print(query.target)
