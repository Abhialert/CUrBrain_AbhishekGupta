base = int(input())
power = int(input())
MOD = int(input())

result = 1 % MOD

for i in range(power):
    result = (result * base) % MOD

print(result)