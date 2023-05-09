def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    _lst = []
    for x in lst:
        if (x):
            _lst.append(x)
    return _lst