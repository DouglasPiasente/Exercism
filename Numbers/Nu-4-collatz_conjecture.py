"""
The Collatz Conjecture or 3x+1 problem can be summarized as follows:

Take any positive integer n. 
If n is even, divide n by 2 to get n / 2. 
If n is odd, multiply n by 3 and add 1 to get 3n + 1. 
Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

Given a number n, return the number of steps required to reach 1.
"""

def steps(number):
    """Return the number os steps taken to reach 1

    Args:
        number (int): given number to test the number of steps

    Raises:
        ValueError: only positive integers are allowed

    Returns:
        int: number of steps taken to reach 1
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    n_steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3 + 1
        n_steps += 1
    return n_steps