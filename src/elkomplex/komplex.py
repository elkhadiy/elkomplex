"""Complex numbers type.

Home for the Komplex class that implements a complex number type
with it's associated arithmetics.

Typical usage:
    >>> from elkomplex import Komplex
    >>> Komplex.from_cartesian(2, 3)
    Komplex(re=2.00, im=3.00, r=3.61, th=0.98)
"""


from math import sqrt, cos, sin, atan2


class Komplex:
    """
    Base Komplex class

    The default constructor `Komplex()` outputs the null complex number 0.
    To build complex numbers out of cartesian or polar coordinates,
    use respective class methods `Komplex.from_cartesian` and
    `Komplex.from_polar`.

    These coordinates are not exposed as public attributes on this
    class interface.
    """

    def __init__(self):
        self._re = 0
        self._im = 0
        self._r = 0
        self._th = 0

    @classmethod
    def from_cartesian(cls, re: float, im: float) -> 'Komplex':
        c = cls()
        c._re = re
        c._im = im
        c._r = sqrt(re ** 2 + im ** 2)
        c._th = atan2(im, re)
        return c

    @classmethod
    def from_polar(cls, r: float, th: float) -> 'Komplex':
        c = cls()
        c._re = r * cos(th)
        c._im = r * sin(th)
        c._r = r
        c._th = th
        return c

    def __repr__(self) -> str:
        return (f"Komplex(re={self._re:0.2f}, im={self._im:0.2f}, "
                + f"r={self._r:0.2f}, th={self._th:0.2f})")

    def __str__(self) -> str:
        """
        Default string formating shows the complex number
        in its a + ib cartesian form.
        """
        return str(self).__format__("0.2f")

    def __format__(self, spec: str) -> str:
        if spec.endswith('p'):
            return f"{self._r:{spec[:-1]}} e ^ (i {self._th:{spec[:-1]}})"
        if spec.endswith('c'):
            return (f"{self._re:{spec[:-1]}} "
                    + f"{'+-'[self._im<0]} {abs(self._im):{spec[:-1]}} i")
        return f"{self._re:{spec}} {'+-'[self._im<0]} {abs(self._im):{spec}} i"
