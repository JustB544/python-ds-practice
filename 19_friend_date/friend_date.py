def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    a[2].sort()
    b[2].sort()
    y = 0
    for x in range(len(a[2])):
        if (a[2][x] == b[2][y]):
            return True
        elif (a[2][x] > b[2][y]):
            while (a[2][x] > b[2][y]):
                y += 1
                if (y == len(b[2])):
                    return False
            if (a[2][x] == b[2][y]):
                return True
    return False