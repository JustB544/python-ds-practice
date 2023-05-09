def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    _str = phrase.lower().split()
    for x in range(len(_str)):
        _str[x] = _str[x].capitalize()
    return ' '.join(_str)