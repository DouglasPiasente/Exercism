"""
An Armstrong number (also known as Narcissistic number) is a number that is the sum of its 
own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

More in: https://en.wikipedia.org/wiki/Narcissistic_number
"""

def is_armstrong_number(number):
    """
    Checks if the input number is an Armstrong Number

    Args:
        number (int): input number

    Returns:
        boolean: True in case it is an Armstrong Number, False otherwise
    """
    str_number = str(number)
    len_number = len(str_number)
    number_list = [int(n)**len_number for n in str_number]
    list_sum = sum(number_list)

    if list_sum == number:
        return True
    return False