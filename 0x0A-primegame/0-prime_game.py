#!/usr/bin/python3
"""Module for Prime game"""

def isWinner(x, nums):
    """Function to determine the winner of the Prime game."""
    
    # Check if x is less than 1 or nums is empty, return None in that case
    if x < 1 or not nums:
        return None

    # Initialize counters for Maria and Ben's wins
    x_maria, x_ben = 0, 0

    # Find the maximum number in nums to know the limit for prime checking
    n = max(nums)

    # Create a list to store the prime status of numbers from 1 to n (True means prime)
    primes = [True for _ in range(1, n + 1)]
    
    # 1 is not prime, so set it to False
    primes[0] = False
    
    # Use the Sieve of Eratosthenes to find all primes up to n
    for i, is_prime in enumerate(primes, 1):
        # Skip 1 (not prime) and any already marked non-prime numbers
        if i == 1 or not is_prime:
            continue
        # Mark all multiples of the prime number as non-prime
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Loop through each number in the nums list and determine the winner
    for _, n in zip(range(x), nums):
        # Count how many primes are there less than or equal to the current number 'n'
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        
        # Update Ben's or Maria's win count based on whether the number of primes is even or odd
        x_ben += primes_count % 2 == 0
        x_maria += primes_count % 2 == 1

    # If Maria and Ben have the same number of wins, return None (no winner)
    if x_maria == x_ben:
        return None
    
    # Return 'Maria' if Maria has more wins, otherwise 'Ben'
    return 'Maria' if x_maria > x_ben else 'Ben'
