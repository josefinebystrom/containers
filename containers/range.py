def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    '''
    if c is None:
        skip = 1
    else:
        skip = c
    if not b:
        current = 0
        while current < a:
            yield current
            current += skip

    if b and c:
        if b > 0 and c < 0:
            return []

    if b:
        if b > 0:
            current = a
            while current < b:
                yield current
                current += skip

        else:
            current = a
            while current > b:
                yield current
                current += skip
