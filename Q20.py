arr = list(map(int, input().split()))

total = 0

for i in range(len(arr) - 1, -1, -1):
    current = arr[i]
    arr[i] = total
    total += current

print(arr)