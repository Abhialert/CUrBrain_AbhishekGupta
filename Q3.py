def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return sign * result

def palindrome_or_sum(n):
    reversed_num = reverse_number(n)
    if n >= 0 and n == reversed_num:
        return n
    return n + reversed_num

n = int(input("Enter a number: "))
print(palindrome_or_sum(n))