""" 
Your task is to convert a number between 1 and 31 to a sequence of actions in the secret handshake.

The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary. 
Start at the right-most digit and move left.

The actions for each number place are:

00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump
10000 = Reverse the order of the operations in the secret handshake.
"""

def commands(binary_str):
    actions = []

    if binary_str[-1] == '1':
        actions.append('wink')
    if binary_str[-2] == '1':
        actions.append('double blink')
    if binary_str[-3] == '1':
        actions.append('close your eyes')
    if binary_str[-4] == '1':
        actions.append('jump')

    if binary_str[-5] == '1':
        return actions[::-1]
    else:
        return actions