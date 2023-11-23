""" 
Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.

The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that the resulting alphabet is backwards. 
The first letter is replaced with the last letter, the second with the second-last, and so on.

An Atbash cipher for the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba

It is a very weak cipher because it only has one possible key, and it is a simple mono-alphabetic substitution cipher. 
However, this may not have been an issue in the cipher's time.

Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, leaving numbers unchanged, 
and punctuation is excluded. This is to make it harder to guess things based on word boundaries. All text will be encoded as lowercase letters.
"""

cipher_code = 'abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba'

def encode(plain_text):
    plain_text = plain_text.lower().replace(' ', '')
    charcount = 0
    encrypted = ''
    
    for letter in plain_text:
        if letter in cipher_code:
            encrypted += cipher_code[(cipher_code.index(letter)+26)]
            charcount += 1
        if letter.isnumeric():
            encrypted += letter
            charcount += 1
        if charcount%5 == 0 and charcount != 0:
            encrypted += ' '
            charcount -= 5

    return encrypted.strip()

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower().replace(' ', '')
    decrypted = ''

    for letter in ciphered_text:
        if letter in cipher_code:
            decrypted += cipher_code[(cipher_code.index(letter)+26)]
        if letter.isnumeric():
            decrypted += letter

    return decrypted.strip()