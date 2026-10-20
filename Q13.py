arr = list(map(int, input().split()))
k = abs(int(input()))

prefix_sum = 0

for num in arr:
    prefix_sum += num

    if prefix_sum % k == 0:
        print(True)
        break
else:
    print(False)