def digit_frequency_difference(n, a, b):
    count_a = 0
    count_b = 0
    while True:
        digit = n % 10
        if digit == a:
            count_a += 1
        if digit == b:
            count_b += 1
        n //= 10
        if n == 0:
            break
    return abs(count_a - count_b)

n = int(input("Enter n: "))
a = int(input("Enter digit a: "))
b = int(input("Enter digit b: "))

if n < 0:
    print("Invalid input: n cannot be negative")
elif not (0 <= a <= 9 and 0 <= b <= 9):
    print("Invalid input: a and b must be single digits")
else:
    print(digit_frequency_difference(n, a, b))