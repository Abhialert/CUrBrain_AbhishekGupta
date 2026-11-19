arr = list(map(int, input().split()))
target = int(input())

for i in range(len(arr)):
    if arr[i] == target:
        for j in range(i, len(arr) - 1):
            arr[j] = arr[j + 1]
        arr.pop()
        break

print(arr)