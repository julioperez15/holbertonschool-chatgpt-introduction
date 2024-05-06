#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Function Description:
    ---------------------
    Computes the factorial of a non-negative integer 'n' using a recursive approach.
    The factorial of a non-negative integer 'n' is the product of all positive integers
    less than or equal to 'n'.

    Parameters:
    -----------
    n : int
        The non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the input integer 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieving the number from the command-line argument
# and calculating its factorial
f = factorial(int(sys.argv[1]))

# Printing the factorial result
print(f)
