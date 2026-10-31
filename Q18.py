arr = list(map(int, input().split()))
start = int(input())
end = int(input())

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)