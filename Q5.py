def replace_even_digits(n):
    digits = []
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            digit = 0
        digits.append(digit)
        n //= 10
    digits.reverse()
    return digits

n = int(input("Enter a positive number: "))
if n <= 0:
    print("Invalid input: n must be a positive integer")
else:
    print(replace_even_digits(n))
    