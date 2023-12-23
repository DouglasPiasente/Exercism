""" 
Recite the nursery rhyme 'This is the House that Jack Built'.

[The] process of placing a phrase of clause within another phrase of clause is called embedding. 
It is through the processes of recursion and embedding that we are able to take a finite number of 
forms (words and phrases) and construct an infinite number of expressions. Furthermore, embedding 
also allows us to construct an infinitely long structure, in theory anyway.

to know more: https://papyr.com/hypertextbooks/grammar/ph_noun.htm
"""

def recite(start_verse, end_verse):
    verbs = [
        '',
       'belonged to ',
       'kept ', 
       'woke ', 
       'married ',
       'kissed ', 
       'milked ', 
       'tossed ', 
       'worried ',
       'killed ',
       'ate ',
       'lay in ',
    ]

    subject = ['the horse and the hound and the horn',
               'the farmer sowing his corn',
               'the rooster that crowed in the morn', 
               'the priest all shaven and shorn',
                'the man all tattered and torn', 
                'the maiden all forlorn', 
                'the cow with the crumpled horn', 
                'the dog',
                'the cat',
                'the rat',
                'the malt',
                'the house that Jack built',
    ]

    result = []
    while start_verse <= end_verse:
        

        n_rhymes = end_verse
        rhymes = []

        while n_rhymes > 1:
            n_rhymes -= 1
            rhymes.append(' that ' + verbs[-n_rhymes - 1] + subject[-n_rhymes - 1])

        if end_verse == 1:
            result.append("This is " + subject[-end_verse] + '.')
        else:
            result.append("This is " + subject[-end_verse] + ''.join(rhymes[1:]) +' that ' + verbs[-1] + subject[-1] + '.')

        end_verse -= 1
    
    return result[::-1]