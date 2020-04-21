m = int(input())
layers_num = 2 ** m
f = [int(input()) for i in range(layers_num)]

print(2)
print(layers_num, 1)
for i in range(layers_num):
    binary = [1 if c == '1' else 0 for c in f'{i:0{m}b}']
    binary_sum = 0.5 - sum(binary)
    binary = [1 if digit == 1 else -1 for digit in binary]
    print(*binary, binary_sum)

print(*f, -0.5)
