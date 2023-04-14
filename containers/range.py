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

    if b is None:
        a, b = 0, a
    if c is None:
        c = 1
    i = a
    while i < b if c > 0 else i > b:
        yield i
        i += c
