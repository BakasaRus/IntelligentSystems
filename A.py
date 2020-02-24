n, m, k = map(int, input().split())
c = list(map(int, input().split()))

groups = [[] for i in range(m)]
for i, group in enumerate(c, 1):
    groups[group - 1].append(i)

buckets = [[] for i in range(k)]
current_bucket = 0
for group in groups:
    for el in group:
        buckets[current_bucket].append(el)
        current_bucket = (current_bucket + 1) % k

for bucket in buckets:
    bucket.sort()
    print(len(bucket), *bucket)
