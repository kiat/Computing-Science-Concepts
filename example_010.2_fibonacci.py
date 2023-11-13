"""
Implementation of Fibonacci numbers
The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. 
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
https://en.wikipedia.org/wiki/Fibonacci_sequence
"""

def fib(n):
  '''
  Recursive implementation of Fibonacci numbers
  Top-Down Implementation.
  '''
  if(n <= 1):
    return n 
  else:
    return fib(n-1) + fib(n-2)
      
#############################################################

def fib_iter(n):
  """
  Iterative Buttom-up Method. 
  """
  a = 0 
  b = 1 
  
  if n<=1:
    return n
  else:
    for i in range(2, n+1):
      c = a + b
      a = b 
      b = c
    return b    

#############################################################

def fib_mem(n):
   """Fibonacci Numbers, Recursive and Memoized. """
   mem={}
   def fib_memoized(n):
    """
    Recursive, Top-Down, Memoized
    """
    if n in mem:
        return mem[n]
    if n <= 2:
            value = 1
    elif n > 2:           
            value =  fib_memoized(n -1) + fib_memoized(n -2)
    mem[n] = value
    return value
   return fib_memoized(n)

#############################################################

def main():
  """A Main function to test it."""
  
  print(fib(10))
  print(fib_mem(10))
  print(fib_iter(10))
  
#############################################################

# Call the main function. 
if __name__ == "__main__":
  main()
