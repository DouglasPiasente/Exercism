"""
OVERVIEW

Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler's math skills aren't good. 
He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency calculator for him

"""


def exchange_money(budget, exchange_rate):
    """Calculate the value after exchange
    
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    This function should return the amount of money that is left from the budget.

    This function should return the value of the exchanged currency.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.

    Your function should return only the total value of the bills (excluding fractional amounts)
    the booth would give back. Unfortunately, the booth keeps the remainder/change as a bonus.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """Calculate the number of bills you receive

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.

    This function should return the number of currency bills that you can receive within the 
    given budget. In other words: How many whole bills of currency fit into the amount of 
    currency you have in your budget?
    """

    return budget // denomination


def get_leftover_of_bills(budget, denomination):
    """Calculate the leftover after exchanging the bills

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.

    This function should return the leftover amount that cannot be exchanged from your budget 
    given the denomination of bills.
    """

    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate value after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    This function should return the maximum value of the new currency after calculating
    the exchange rate plus the spread.
    """

    exchange_spread = exchange_rate * (spread/100) + exchange_rate
    final_exchange = budget / exchange_spread  
    
    return int(final_exchange // denomination * denomination)