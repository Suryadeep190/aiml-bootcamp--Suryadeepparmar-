def average(nums):
    if not nums:
        return 0.0

    return sum(nums) / len(nums)


def biggest(nums):
    if not nums:
        return None

    return max(nums)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True