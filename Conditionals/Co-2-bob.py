"""
Bob is a lackadaisical teenager. He likes to think that he's very cool. 
And he definitely doesn't get excited about things. That wouldn't be cool.

When people talk to him, his responses are pretty limited.

Bob only ever answers one of five things:

- "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
- "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
- "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
- "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
- "Whatever." This is what he answers to anything else.
"""

def response(hey_bob):
    """
    Returns Bob's answers to what people say to him

    Args:
        hey_bob (string): What people talk to Bob

    Returns:
        string: Bob's answer to what people talk
    """
    if len(hey_bob) == 0 or hey_bob.isspace():
        return 'Fine. Be that way!'
    if hey_bob.rstrip()[-1] == '?' and hey_bob.isupper():
        return 'Calm down, I know what I\'m doing!'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob.rstrip()[-1] == '?':
        return 'Sure.'
    return 'Whatever.'