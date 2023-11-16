""" 
The ISBN-10 verification process is used to validate book identification numbers. 
These normally contain dashes and look like: 3-598-21508-8

The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only).
In the case the check character is an X, this represents the value '10'. 
These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
"""
def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn_list = list(str(isbn))
    possible_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    if  isbn_list != [] and isbn_list[-1] == 'X':
        isbn_list[-1] = '10'

    calc_list = []
    multiplier = 10

    for x in isbn_list:
        if x not in possible_values:
            calc_list.append(0*multiplier)
        else:
            calc_list.append(int(x)*multiplier)
        multiplier -= 1

    if any([x not in possible_values for x in isbn_list]) or len(isbn_list) != 10 or sum(calc_list) % 11 != 0 or isbn_list == '':
       return False
    return True