""" 
An anagram is a rearrangement of letters to form a new word: for example "owns" is an anagram of "snow". 
A word is not its own anagram: for example, "stop" is not an anagram of "stop".

Given a target word and a set of candidate words, this exercise requests the anagram set: the subset 
of the candidates that are anagrams of the target.

Lowercase and uppercase characters are equivalent: for example, "PoTS" is an anagram of "sTOp", but StoP is not an anagram of sTOp. 
The anagram set is the subset of the candidate set that are anagrams of the target (in any order). 
Words in the anagram set should have the same letter case as in the candidate set.
"""

def find_anagrams(word, candidates):
    l_word = word.lower()
    s_word = ''.join(sorted(word.lower()))
    anagram_list = []

    for w in candidates:
        s_candidate = ''.join(sorted(w.lower()))
        if s_candidate == s_word and w.lower() != l_word:
            anagram_list.append(w)
        
    return anagram_list