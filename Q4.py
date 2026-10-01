def subtract_product_and_sum(n):
    product = 1
    total = 0
    while n > 0:
        digit = n % 10
        product *= digit
        total += digit
        n //= 10
    return product - total

n = int(input("Enter a positive number: "))
if n <= 0:
    print("Invalid input: n must be greater than 0")
else:
    print(subtract_product_and_sum(n))