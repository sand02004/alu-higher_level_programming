::

    >>> print_square = __import__('4-print_square').print_square
    >>> print_square(1)
    #

::

    >>> print_square(4)
    ####
    ####
    ####
    ####

::

    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

If ``size`` is zero, the function prints nothing.

::

    >>> print_square(0)

Invalid Sizes
=============

The parameter ``size`` must be an integer. Otherwise, a TypeError is raised.

::

    >>> print_square("not an int")
    Traceback (most recent call last):
    TypeError: size must be an integer

::

    >>> print_square(5.5)
    Traceback (most recent call last):
    TypeError: size must be an integer

::

    >>> print_square(None)
    Traceback (most recent call last):
    TypeError: size must be an integer

If ``size`` is less than zero, a ValueError is raised.

::

    >>> print_square(-7)
    Traceback (most recent call last):
    ValueError: size must be >= 0

Note that type-checking occurs before value-checking.

::
# Temporary change to force git to see modification
    >>> print_square(-7.5)
    Traceback (most recent call last):
    TypeError: size must be an integer

At least one argument must be provided.

::

    >>> print_square()
    Traceback (most recent call last):
    TypeError: print_square() missing 1 required positional argument: 'size'
