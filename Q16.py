scores = list(map(int, input().split()))

highest = None
second = None

for score in scores:
    if highest is None or score > highest:
        second = highest
        highest = score
    elif score != highest and (second is None or score > second):
        second = score

if second is None:
    print(-1)
else:
    print(second)