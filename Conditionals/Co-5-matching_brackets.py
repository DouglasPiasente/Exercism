""" 
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, 
verify that any and all pairs are matched and nested correctly. 

The string may also contain other characters, which should be ignored.
"""
def is_paired(input_string):
    opened = "[{("
    closed = "]})"
    stack = []
    for ch in input_string:
        if ch in opened:
            stack.append(ch)
        elif ch in closed:
            if not stack or opened[closed.index(ch)] != stack.pop():
                return False
    return not stack

