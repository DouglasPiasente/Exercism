""" 
Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below), 
but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. 
        Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. 
        Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, 
        and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter 
        in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
"""
def translate(text):
    vowel_sound = ['a','e','i','o','u']
    word_list = text.split()
    pig_latin_list = []

    for word in word_list:
        if word[0] in vowel_sound or word[:2] in ['xr', 'yt']:
            pig_latin_list.append(word + 'ay' )
        elif len(word) == 2 and word[-1] == 'y':
            pig_latin_list.append(word[1] + word[0] + 'ay' )
        elif 'y' in word[2:4]:
            if word[2] == 'y':
                pig_latin_list.append( word[2:] + word[:2] + 'ay' )
            if word[3] == 'y':
                pig_latin_list.append( word[3:] + word[:3] + 'ay' )
        elif word[0] not in vowel_sound and word[1] not in vowel_sound and word[2] not in vowel_sound:
            pig_latin_list.append( word[3:] + word[:3] + 'ay' )
        elif 'qu' in word[:3]:
            if word[0] == 'q':
                pig_latin_list.append( word[2:] + word[:2] + 'ay' )
            if word[1] == 'q':
                pig_latin_list.append( word[3:] + word[:3] + 'ay' )
        elif word[0] not in vowel_sound:
            if word[1] in vowel_sound:
                pig_latin_list.append( word[1:] + word[0] + 'ay' )
            if word[1] not in vowel_sound:
                pig_latin_list.append( word[2:] + word[:2] + 'ay' )

    return ' '.join(pig_latin_list)