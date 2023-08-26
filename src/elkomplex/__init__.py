"""Toy implementation of a complex data type in Python

This module is a basic implementation of complex numbers in Python.
The goal is to demonstrate basic know-how in Python packaging,
project managment, documentation and testing.

This package is not in any way, shape or form suitable for production!

Examples:
    Create a complex number from real and imaginary parts

    >>> from elkomplex import Komplex
    >>> Komplex.from_cartesian(2, 3)
    Komplex(re=2.00, im=3.00, r=3.61, th=0.98)

    Create a complex number from polar coordinates

    >>> from math import pi
    >>> Komplex.from_polar(1, pi / 4)
    Komplex(re=0.71, im=0.71, r=1.00, th=0.79)

    Import the special ``i`` number from the module and use it
    as a more intuitive interface to work with complex numbers

    >>> from elkomplex import i
    >>> f"{i}"
    '0 + 1 i'
    >>> f"{i ** 2}"
    '-1.00 + 0 i'
    >>> f"{2 + 3 * i}"
    '2.00 + 3.00 i'
    >>> f"{(2 + 3 * i) * (4 + 5 * i)}"
    '-7.00 + 22.00 i'
"""

from elkomplex.komplex import Komplex

i = Komplex.from_cartesian(0, 1)
