#!/usr/bin/python3
"""
prime_game
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): A list of integers representing the numbers for each round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         If the winner cannot be determined, returns None.
    """

    if not nums or x < 1:
        return None

    max_n = max(nums)

    primes = [False, False] + [True] * (max_n - 1)
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
