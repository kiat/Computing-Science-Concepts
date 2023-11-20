def is_power_of_two(n):
    # Base cases:
    # If n is 0 or negative, it's not a power of two
    if n <= 0:
        return False
    # If n is 1, it's a power of two
    elif n == 1:
        return True
    # If n is even, check if n/2 is a power of two
    elif n % 2 == 0:
        return is_power_of_two(n // 2)
    # If n is odd, it's not a power of two
    else:
        return False

# Example usage:
number = 16
result = is_power_of_two(number)
print(f"{number} is a power of two: {result}")



