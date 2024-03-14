#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    This function returns the prime game winner
    """
    def sieve(n):
        primes = [True for _ in range(n + 1)]
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p] is True:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    def play(n):
        """
        This function returns the name of the winner
        """
        primes = sieve(n)
        count = sum(primes)
        return 'Maria' if count % 2 == 1 else 'Ben'

    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        scores[play(n)] += 1

    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    elif scores['Maria'] < scores['Ben']:
        return 'Ben'
    else:
        return None
