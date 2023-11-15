""" 
Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

The Greek mathematician Nicomachus devised a classification scheme for positive integers, 
identifying each as belonging uniquely to the categories of perfect, abundant, or deficient 
based on their aliquot sum. The aliquot sum is defined as the sum of the factors of a number 
not including the number itself. For example, the aliquot sum of 15 is 1 + 3 + 5 = 9.

- Perfect: aliquot sum = number

- Abundant: aliquot sum > number

- Deficient: aliquot sum < number

More on Nicomachus: https://en.wikipedia.org/wiki/Nicomachus
More on Aliquot sum: https://en.wikipedia.org/wiki/Aliquot_sum
"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    x = 1
    list_for_sum = []
    while x < number:
        if number % x == 0:
            list_for_sum.append(x)
        x += 1
    
    list_sum = sum(list_for_sum)

    if list_sum == number:
        return 'perfect'
    if list_sum > number:
        return 'abundant'
    if list_sum < number:
        return 'deficient'