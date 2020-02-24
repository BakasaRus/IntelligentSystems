k = int(input())
cm = []
total = 0
for i in range(k):
    cm.append([int(x) for x in input().split()])
    total += sum(cm[i])

stats = []
recall_w = 0
precision_w = 0
for i in range(k):
    count = sum(cm[i])
    predicted = sum(cm[j][i] for j in range(k))
    precision = cm[i][i] / count if count > 0 else 0
    recall = cm[i][i] / predicted if predicted > 0 else 0
    f_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    stats.append((count, predicted, f_score))

    recall_w += cm[i][i] / total
    precision_w += cm[i][i] * count / predicted / total

macro_f = 2 * precision_w * recall_w / (precision_w + recall_w)
micro_f = sum([stats[i][0] * stats[i][2] for i in range(k)]) / total
print(f'{macro_f:.9f}')
print(f'{micro_f:.9f}')
