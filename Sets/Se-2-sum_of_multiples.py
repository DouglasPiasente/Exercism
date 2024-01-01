""" 
The player completed level 20 and found two magical items with base values of 3 and 5.

To calculate the energy points earned by the player, we need to find all the unique multiples of these base values that are less than level 20.

Multiples of 3 less than 20: {3, 6, 9, 12, 15, 18}
Multiples of 5 less than 20: {5, 10, 15}
Combine the sets and remove duplicates: {3, 5, 6, 9, 10, 12, 15, 18}
Sum the unique multiples: 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78
Therefore, the player earns 78 energy points for completing level 20 and finding the two magical items with base values of 3 and 5.
"""

def sum_of_multiples(limit, multiples):
    list_of_energy = []

    if not multiples:
        return 0
    else:
        for i in multiples:
            if i != 0:
                base_value = i
                while i < limit:
                    list_of_energy.append(i)
                    i += base_value
            sum_list = sum(list(set(list_of_energy)))
        return sum_list
            