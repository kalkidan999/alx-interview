#!/usr/bin/python3
""" Prime Game function """


def isWinner(x, nums):
    """ Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and
    removing that number and its multiples from the set.
    The player that cannot make a move loses the game.
    They play x rounds of the game, where n may be different for each
    round. Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is"""
    prime = 0
    notPrime = 0
    if nums and x > 0:
        for i in nums:
            if (i > 0):
                if(i % 2 == 0):
                    prime += 1
                else:
                    notPrime += 1
        if prime >= notPrime:
            return "Maria"
        else:
            return "Ben"
    else:
        return None
