def leap_year(year):
    """
    Check if a given year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    
    four_d = year % 4
    hund_d = year % 100
    fourhund_d = year % 400
    

    if (four_d == 0 and hund_d != 0 ) or fourhund_d == 0:
        return True
    return False