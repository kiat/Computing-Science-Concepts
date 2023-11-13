"""
    Implementation of Factorial
    https://en.wikipedia.org/wiki/Factorial
"""

def factorial(n):
    """Calculates the factorial of a number n using recursion.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#############################################################

def factorial_iter(n):
    """Calculates the factorial of a number n.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
#############################################################

def factorial_mem(n):
    """Calculates the factorial of a number n using recursion.

    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    mem= {}
    def factorial_helper(n):
        if n in mem:
            return mem[n]
        
        if n == 0 or n == 1:
            return 1
        else:
            value = n * factorial_helper(n - 1)
            mem[n] = value
            return value
    return factorial_helper(n)
#############################################################


def main():
  """A Main function to test it."""
  print(factorial(10))
  print(factorial_mem(10))
  print(factorial_iter(10))


# Call the main function. 
if __name__ == "__main__":
  main()

