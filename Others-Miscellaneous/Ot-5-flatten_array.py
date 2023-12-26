""" 
Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like 
structure and returns a flattened structure without any nil/null values.

For example:

input: [1,[2,3,null,4],[null],5]

output: [1,2,3,4,5]
"""
def flatten(iterable):
    n_list = []
    for item in iterable:
        if type(item) is list:
            n_list.extend(flatten(item))
        elif item is not None:
            n_list.append(item)

    return n_list