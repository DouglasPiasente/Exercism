"""
There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. 
Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first 
square of a chess board, with the number of grains doubling on each successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

More about the Wheat and the Chessboard problem in https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem
"""


def square(number):
    """
    Given a square number of the chessboard, provide the number of grains it should have

    Args:
        number (int): number of the chessboard square

    Raises:
        ValueError: Check if the given number is between 1 and 64

    Returns:
        int: Number of grains in the chessboard square
    """
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
        
    return 2**(number -1)


def total():
    """
    Provides the total number of grains for the Wheat and the Chessboard Problem

    Returns:
        int: Total of grains in the chessboard
    """
    return 2**64 -1
