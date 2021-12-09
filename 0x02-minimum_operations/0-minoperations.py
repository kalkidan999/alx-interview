#!/usr/bin/python3

'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
'''


def minOperations(n):
    '''
    returns minimum operations
    '''
    result = 0
    index = 2
    if n < 2:
        return 0
    while (index < n + 1):
        # Check if number is even
        while n % index == 0:
            # add number to the result
            result += index
            # Create number to get to n
            n /= index
        index += 1
    return result