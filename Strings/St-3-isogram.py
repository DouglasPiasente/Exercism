"""
Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter,
however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.
"""

def is_isogram(string):
    """
    Check if a word is an isogram

    Args:
        string (str): string to be tested

    Returns:
        boolean: True if it is an isogram, False otherwise
    """
    letters = ''.join(letter for letter in string if letter.isalnum()).lower()
    unique_letters = set(letters)

    if len(letters) == len(unique_letters):
        return True
    return False