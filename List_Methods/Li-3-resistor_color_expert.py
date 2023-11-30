"""
Create a helpful program so that you don't have to remember the values of the bands. 
The program will take 1, 4, or 5 colors as input, and outputs the correct value, in ohms. The color bands are encoded as follows:

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

In resistor-color trio you decoded the first three colors. 
For instance: orange-orange-brown translated to the main value 330. 
In this exercise you will need to add tolerance to the mix. 
Tolerance is the maximum amount that a value can be above or below the main value. 
For example, if the last band is green, the maximum tolerance will be ±0.5%.

The tolerance band will have one of these values:

Grey - 0.05%
Violet - 0.1%
Blue - 0.25%
Green - 0.5%
Brown - 1%
Red - 2%
Gold - 5%
Silver - 10%
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

tolerance = {"grey": '0.05%',
             "violet": '0.1%',
             "blue": '0.25%',
             "green": '0.5%',
             "brown": '1%',
             "red": '2%',
             "gold": '5%',
             "silver": '10%'
            }

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        c_one, c_two, c_three = colorcode[colors[0]], colorcode[colors[1]], colorcode[colors[2]]
        value = (10 * c_one + c_two) * 10**c_three
    if len(colors) == 5:
        c_one, c_two, c_three, c_four= colorcode[colors[0]], colorcode[colors[1]], colorcode[colors[2]], colorcode[colors[3]]
        value = (100 * c_one + 10 * c_two + c_three) * 10**c_four


    if value <= 1000:
        str_value =  str(value) + ' ohms ±' + tolerance[colors[-1]]
    elif value <= 1000000:
        str_value = str(value/1000) + ' kiloohms ±' + tolerance[colors[-1]]
    elif value <= 1000000000:
        str_value = str(value/1000000) + ' megaohms ±' + tolerance[colors[-1]]
    else:
        str_value = str(value/1000000000) + ' gigaohms ±' + tolerance[colors[-1]]

    str_value = str_value.replace('.0 ', ' ')

    return str_value