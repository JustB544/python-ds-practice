def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    _return = {}
    for x in phrase:
        if (_return.get(x) == None):
            _return[x] = 1
        else:
            _return[x] += 1
    return _return