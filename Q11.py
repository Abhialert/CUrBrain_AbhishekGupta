MOD = 10**9 + 7

arr = list(map(int, input().split()))

result = 0

for num in arr:
    result = (result + num) % MOD

print(result)