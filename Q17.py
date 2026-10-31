sales = list(map(int, input().split()))

freq = {}

for item in sales:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

most_popular = min(freq)

for item in freq:
    if freq[item] > freq[most_popular]:
        most_popular = item
    elif freq[item] == freq[most_popular] and item < most_popular:
        most_popular = item

print(most_popular)