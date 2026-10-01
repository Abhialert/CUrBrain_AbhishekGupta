def has_even_digits(n):
    n = abs(n)
    count = 0
    if n == 0:
        count = 1
    while n > 0:
        count += 1
        n //= 10
    return count % 2 == 0

n = int(input("Enter a number: "))
print(has_even_digits(n))