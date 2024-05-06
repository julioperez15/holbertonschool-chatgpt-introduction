#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python script_name.py number")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Number must be non-negative.")
        sys.exit(1)
    result = factorial(number)
    print(result)
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)