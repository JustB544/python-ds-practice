def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    _str = ''
    for x in phrase:
        if (x == to_swap.upper()):
            _str += to_swap.lower()
        elif (x == to_swap.lower()):
            _str += to_swap.upper()
        else:
            _str += x
    return _str
