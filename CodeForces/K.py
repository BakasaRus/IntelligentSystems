def sum_differences(nums: list):
    l = len(nums)
    coef = range(-(l - 1), l, 2)
    s = 0
    for i in range(l):
        s += coef[i] * nums[i]

    return s * 2


k = int(input())
n = int(input())
nums_in_cat = {y: [] for y in range(1, k + 1)}
all_nums = []

for i in range(n):
    x, y = map(int, input().split())
    nums_in_cat[y].append(x)
    all_nums.append(x)

all_nums.sort()
for i in range(1, k + 1):
    nums_in_cat[i].sort()

whole = sum_differences(all_nums)
inner = 0
for nums in nums_in_cat.values():
    inner += sum_differences(nums)

print(inner)
print(whole - inner)
