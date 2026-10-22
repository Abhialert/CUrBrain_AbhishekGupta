arr = list(map(int, input().split()))

smallest = arr[0]

for num in arr[1:]:
    if abs(num) < abs(smallest):
        smallest = num

print(smallest)