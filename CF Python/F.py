def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini


def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}


def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del (node['groups'])
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)


def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root


def flatten_tree(tree, res) -> int:
    cur_order = len(res)
    node = {'index': tree['index'], 'value': tree['value'], 'order': cur_order}
    res.append(node)

    if isinstance(tree['left'], dict):
        res[cur_order]['left'] = flatten_tree(tree['left'], res)
    else:
        res.append({'class': tree['left']})
        res[cur_order]['left'] = len(res) - 1
        res[-1]['order'] = len(res) - 1

    if isinstance(tree['right'], dict):
        res[cur_order]['right'] = flatten_tree(tree['right'], res)
    else:
        res.append({'class': tree['right']})
        res[cur_order]['right'] = len(res) - 1
        res[-1]['order'] = len(res) - 1

    return cur_order


def main():
    m, k, h = map(int, input().split())
    n = int(input())
    dataset = []

    for i in range(n):
        dataset.append([int(x) for x in input().split()])

    tree = build_tree(dataset, h, 1)

    res = []
    flatten_tree(tree, res)
    res.sort(key=lambda node: node['order'])

    for node in res:
        if 'index' in node:
            print('Q', node['index'] + 1, node['value'], node['left'] + 1, node['right'] + 1)
        else:
            print('C', node['class'])


main()
