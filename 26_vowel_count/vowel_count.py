def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    _return = {}
    for x in phrase:
        if (x.lower() == 'a' or x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u'):
            if (_return.get(x.lower()) == None):
                _return[x.lower()] = 0
            _return[x.lower()] += 1
    return _return