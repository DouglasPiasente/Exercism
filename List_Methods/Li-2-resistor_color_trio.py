""" 
If you want to build something using a Raspberry Pi, you'll probably use resistors. For this exercise, you need to know only three things about them:

Each resistor has a resistance value.

Resistors are small - so small in fact that if you printed the resistance value on them, it would be hard to read. 
To get around this problem, manufacturers print color-coded bands onto the resistors to denote their resistance values.

Each band acts as a digit of a number. For example, if they printed a brown band (value 1) followed by a green band (value 5), 
it would translate to the number 15. In this exercise, you are going to create a helpful program so that you don't 
have to remember the values of the bands. The program will take 3 colors as input, and outputs the correct value, in ohms. 
The color bands are encoded as follows:

Black: 0
Brown: 1
Red: 2
Orange: 3
Yellow: 4
Green: 5
Blue: 6
Violet: 7
Grey: 8
White: 9

When we get to larger resistors, a metric prefix is used to indicate a larger magnitude of ohms, such as "kiloohms". 
That is similar to saying "2 kilometers" instead of "2000 meters", or "2 kilograms" for "2000 grams".
"""

colorcode = {"black": 0,
             "brown": 1,
             "red": 2,
             "orange": 3,
             "yellow": 4,
             "green": 5,
             "blue": 6,
             "violet": 7,
             "grey": 8,
             "white": 9
            }

def label(colors):
    c_one, c_two, c_three = colorcode[colors[0]], colorcode[colors[1]], colorcode[colors[2]]

    value = (10 * c_one + c_two) * 10**c_three

    if value <= 1000:
        return str(value) + ' ohms'
    elif value <= 1000000:
        return str(value//1000) + ' kiloohms'
    elif value <= 1000000000:
        return str(value//1000000) + ' megaohms'
    else:
        return str(value//1000000000) + ' gigaohms'