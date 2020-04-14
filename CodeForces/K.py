def sum_differences(nums: list):
    s = 0
    for a in nums:
        for b in nums:
            s += abs(a - b)
    return s


k = int(input())
n = int(input())
nums_in_cat = {y: [] for y in range(1, k + 1)}
all_nums = []

for i in range(n):
    x, y = map(int, input().split())
    nums_in_cat[y].append(x)
    all_nums.append(x)

whole = sum_differences(all_nums)
inner = 0
for nums in nums_in_cat.values():
    inner += sum_differences(nums)

print(inner)
print(whole - inner)
