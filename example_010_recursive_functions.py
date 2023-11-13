"""
Recursive Functions. 
"""

# Print n numbers like this iterative implementation. 
def print_num(n):
    """
    Simple print of n numbers. 
    """
    for item in range(n+1):
        print(item)

#####################################
## Let us do the same recursively. ##
#####################################

def print_recursive(n):
    if n <= 0:
        print(0)
    else:
        print_recursive(n-1)
        print(n)


# Print n numbers reverse like this iterative implementation. 
def print_num_reverse(n):
    """
    Simple print of n numbers. 
    """
    for item in range(n+1):
        print(n-item)

#####################################
## Let us do the same recursively. ##
#####################################

def print_recursively_reverse(n):
    if n <= 0:
        print(0)
    else:
        print(n)        
        print_recursively_reverse(n-1)
        

def main():
    print_num(4)
    print("####################")
    print_recursive(4)
    print("####################")
    print("####################")

    print_num_reverse(4)
    print("####################")
    print_recursively_reverse(4)

if __name__ == "__main__":
    main()

