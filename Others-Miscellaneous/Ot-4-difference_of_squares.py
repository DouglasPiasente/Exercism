"""
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers 
and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.
"""

def square_of_sum(number):
    counter = 1
    n_list = []
    while counter <= number:
        n_list.append(counter)
        counter += 1
    calc = sum(n_list)**2
    return calc

def sum_of_squares(number):
    counter = 1
    n_list = []
    while counter <= number:
        n_list.append(counter)
        counter += 1
    squared_list = [n**2 for n in n_list]
    return sum(squared_list)
        
def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)