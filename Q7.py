import math

arr = list(map(int, input().split()))
gcd = arr[0]
for num in arr[1:]:
    gcd = math.gcd(gcd, num)

print(gcd)