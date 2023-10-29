"""
You work for a company that sells fonts through their website. 
They'd like to show a different sentence each time someone views a font on their website. 
To give a comprehensive sense of the font, the random sentences should use all the letters in the English alphabet.

They're running a competition to get suggestions for sentences that they can use. 
You're in charge of checking the submissions to see if they are valid.

List of 14 pangrams: https://people.howstuffworks.com/14-pangrams.htm 
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_pangram(sentence):
    """
    Check if the word is a pangram.

    Args:
        sentence (str): sentence to be checked

    Returns:
        boolean: True if the sentence is a pangram, False otherwise
    """
    sentence = sentence.lower()
    letters = [letter for letter in sentence]
    pangram_check = all(letter in letters for letter in alphabet)
    return pangram_check