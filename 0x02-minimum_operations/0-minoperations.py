#!/usr/bin/python3

'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
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
        # check if problem can be broken into smaller problem
        while n % index == 0:
            # if yes then add no of smaller problems to result
            result += index
            # create smaller problem
            n /= index
        index += 1
    return result
