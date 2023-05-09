def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    l1.sort()
    l2.sort()
    y = 0
    lst = []
    for x in range(len(l1)):
        if (l1[x] == l2[y]):
            lst.append(l1[x])
            y += 1
            if (y == len(l2)):
                return lst
        elif (l1[x] > l2[y]):
            while (l1[x] > l2[y]):
                y += 1
                if (y == len(l2)):
                    return lst
            if (l1[x] == l2[y]):
                lst.append(l1[x])
                y += 1
                if (y == len(l2)):
                    return lst
        continue
    return lst
intersection([1, 2, 3], [2, 3, 4])