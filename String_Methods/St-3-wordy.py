""" 
Parse and evaluate simple math word problems returning the answer as an integer.

"""

def answer(question):
    oper_dict = {'multiplied': '*', 'plus': '+', 'minus': '-', 'divided': '/'}
    clean_question = question.replace('?', '').replace('What is', '').replace('by', '')
   
    expr_list = [x for x in clean_question.split()]
    expr_list = [oper_dict.get(word,word) for word in expr_list]
    expr_list.insert(0, '(')
    expr_list.insert(4, ')')
    other_words = [item.isalpha() for item in expr_list]

    if any(other_words):
        raise ValueError("unknown operation")
    if clean_question == '':
        raise ValueError("syntax error")
    try:
        return eval(' '.join(expr_list))
    except:
        raise ValueError("syntax error")