def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

nums = list(map(int, input().split()))
k = int(input())

n = len(nums)
k = k % n

reverse(nums, 0, n - 1)
reverse(nums, 0, k - 1)
reverse(nums, k, n - 1)

print(nums)