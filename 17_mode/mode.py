def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    _return = {}
    for x in nums:
        if (_return.get(x) == None):
            _return[x] = 1
        else:
            _return[x] += 1
    highest_key = -1
    highest = -1
    for x in _return.keys():
        if (_return[x] > highest):
            highest = _return[x]
            highest_key = x
    return highest_key