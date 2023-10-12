"""
The objective of this function is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. 
A factor is a number that evenly divides into another number, leaving no remainder.

The rules of raindrops are that if a given number:

- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
"""

def response(number):
    """
    Converts a number into a string based on the factor of 3, 5 and 7 of that number

    Args:
        number (int): Number of raindrops

    Returns:
        string: Sound of the raindrops or the number of raindrops if it doesn't fit any rule
    """
    pling = not bool((number % 3))
    plang = not bool((number % 5))
    plong = not bool((number % 7))

    sound = ''

    if pling:
        sound += 'Pling'
    if plang:
        sound += 'Plang'
    if plong:
        sound += 'Plong'

    return sound if sound else str(number)