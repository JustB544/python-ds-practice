def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    ages.sort()
    y = 1
    const = len(ages)-1
    if (ages[const] == ages[const - y]):
        while (ages[const] == ages[const - y]):
            y += 1
    return (ages[const - y], ages[const])