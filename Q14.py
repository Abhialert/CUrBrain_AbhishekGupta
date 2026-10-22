sales = list(map(int, input().split()))
threshold = int(input())

result = []

for sale in sales:
    if sale >= threshold:
        result.append(sale)

print(result)