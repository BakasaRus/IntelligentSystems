from math import exp, log


k = int(input())
penalties = [int(x) for x in input().split()]
alpha = int(input())
n = int(input())

class_count = {x: 0 for x in range(1, k + 1)}
classes = {x: {} for x in range(1, k + 1)}
classes2 = {x: {} for x in range(1, k + 1)}
alphabet = set()

for i in range(n):
    cur_class, _, *words = input().split()
    cur_class = int(cur_class)
    class_count[cur_class] += 1
    for word in {*words}:
        if word not in alphabet:
            alphabet.add(word)
            for j in range(1, k + 1):
                classes[j][word] = 0.0
        classes[cur_class][word] += 1

for cur_class, words in classes.items():
    for word in alphabet:
        if word in words:
            words[word] += alpha
            words[word] /= class_count[cur_class] + 2.0 * alpha
            classes2[cur_class][word] = log(1 - words[word])
            words[word] = log(words[word])
    class_count[cur_class] /= n

m = int(input())
for i in range(m):
    known_words = [word for word in input().split()[1:] if word in alphabet]
    count_mask = [v > 0 for v in class_count.values()]
    p = {k: log(v) if v > 0 else 1.0 for k, v in class_count.items()}
    for word in alphabet:
        classes_source = classes if word in known_words else classes2
        for cur_class, words in classes_source.items():
            p[cur_class] += words[word]
    values = p.values()
    p_max = max(values)
    l = [exp(value - p_max) if count_mask[index] else 0.0 for index, value in enumerate(values, 0)]
    l = [v * p for v, p in zip(l, penalties)]
    s = sum(l)
    res = [v / s for v in l]
    print(*res)
