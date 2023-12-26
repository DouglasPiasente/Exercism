"""
Your task is to change the data format of letters and their point values in the game.

Currently, letters are stored in groups based on their score, in a one-to-many mapping.

This needs to be changed to store each individual letter with its score in a one-to-one mapping.

As part of this change, the team has also decided to change the letters to be lower-case rather than upper-case.

"""

def transform(legacy_data):
    new_values = {}

    for key, value in legacy_data.items():
        for i in value:
            new_values[i.lower()] = key

    return new_values


#print(transform({1: ["A", "E"], 2: ["D", "G"]}))