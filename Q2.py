def reverse_and_double(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return 2 * sign * reversed_num

n = int(input("Enter a number: "))
print(reverse_and_double(n))