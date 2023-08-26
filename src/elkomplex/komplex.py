"""Complex numbers type.

Home for the Komplex class that implements a complex number type
with it's associated arithmetics.

Typical usage:
    >>> from elkomplex import Komplex
    >>> Komplex.from_cartesian(2, 3)
    Komplex(re=2.00, im=3.00, r=3.61, th=0.98)
"""

from __future__ import annotations
from math import sqrt, pi, cos, sin, atan2, isclose


EQTOL = 1e-15


class Komplex:
    """Base Komplex class

    The default constructor `Komplex()` outputs the null complex number 0.
    To build complex numbers out of cartesian or polar coordinates,
    use respective class methods `Komplex.from_cartesian` and
    `Komplex.from_polar`.

    These coordinates are not exposed as public attributes on this
    class interface.
    """

    def __init__(self):
        """Creates the null complex number 0."""
        self._re = 0
        self._im = 0
        self._r = 0
        self._th = 0

    @classmethod
    def from_cartesian(cls, re: float, im: float) -> Komplex:
        """Creates a complex number from its real and imaginary parts

        Args:
            re (float): Real part.
            im (float): Imaginary part.
        """
        c = cls()
        c._re = re
        c._im = im
        c._r = sqrt(re ** 2 + im ** 2)
        c._th = atan2(im, re)
        return c

    @classmethod
    def from_polar(cls, r: float, th: float) -> Komplex:
        """Creates a complex number from its polar coordiates (r, theta)

        Args:
            r (float): Module.
            th (float): Argument.
        """
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
        """Default string format for a Komplex number.

        Shows the complex number in its a + ib cartesian form.
        """
        return str(self).__format__("0.2f")

    def __format__(self, spec: str) -> str:
        """Adds str formating options `c` and `p` for Komplex numbers.

        Since complex numbers can be represented by either a cartesian or polar
        form, this method add options for string formating to choose between
        the two.

        Args:
            spec (str):
                Usual string formating spec.
                The complex values (real, imaginary, module and argument)
                shown will conform to this spec. Additionaly if `c` or `p`
                is added at the end of the spec, representation will be
                respectively cartesian or polar.

        Example:
            `2.0fc` will represent complex numbers with real and imaginary
            parts with the `2.0f` spec in the cartesian format : `2.0 + 3.0 i`
        """
        if spec.endswith('p'):
            return f"{self._r:{spec[:-1]}} e ^ (i {self._th:{spec[:-1]}})"
        if spec.endswith('c'):
            return (f"{self._re:{spec[:-1]}} "
                    + f"{'+-'[self._im<0]} {abs(self._im):{spec[:-1]}} i")
        return f"{self._re:{spec}} {'+-'[self._im<0]} {abs(self._im):{spec}} i"

    def __eq__(self, other: int | float | Komplex) -> bool:
        """Check if real and imaginary parts are close enough to be equal"""
        match other:
            case int() | float():
                return (isclose(self._re, other, abs_tol=EQTOL)
                        and isclose(self._im, 0, abs_tol=EQTOL))
            case Komplex():
                return (isclose(self._re, other._re, abs_tol=EQTOL)
                        and isclose(self._im, other._im, abs_tol=EQTOL))
            case _:
                return NotImplemented

    def __add__(self, other: int | float | Komplex) -> Komplex:
        """Piecewise addition between real and imaginary parts"""
        match other:
            case int() | float():
                return Komplex.from_cartesian(other + self._re, self._im)
            case Komplex():
                return Komplex.from_cartesian(self._re + other._re,
                                              self._im + other._im)
            case _:
                return NotImplemented

    def __radd__(self, other: int | float | Komplex) -> Komplex:
        """Addition is symmetric"""
        return self.__add__(other)

    def __sub__(self, other: int | float | Komplex) -> Komplex:
        """Piecewise substraction between real and imaginary parts"""
        match other:
            case int() | float():
                return Komplex.from_cartesian(self._re - other, self._im)
            case Komplex():
                return Komplex.from_cartesian(self._re - other._re,
                                              self._im - other._im)
            case _:
                return NotImplemented

    def __rsub__(self, other: int | float | Komplex) -> Komplex:
        """Piecewise substraction between real and imaginary parts"""
        match other:
            case int() | float():
                return Komplex.from_cartesian(other - self._re, -self._im)
            case Komplex():
                return Komplex.from_cartesian(other._re - self._re,
                                              other._im - self._im)
            case _:
                return NotImplemented

    def __mul__(self, other: int | float | Komplex) -> Komplex:
        """Simple implementation using polar coordinates

        z1 = rho1 e^(i th1)

        z2 = rho2 e^(i th2)

        z1 * z2 = (rho1 * rho2) e^(i (th1 + th2) % 2pi)
        """
        match other:
            case int() | float():
                return Komplex.from_polar(other * self._r, self._th)
            case Komplex():
                return Komplex.from_polar(other._r * self._r,
                                          (other._th + self._th) % (2 * pi))
            case _:
                return NotImplemented

    def __rmul__(self, other: int | float | Komplex) -> Komplex:
        """Multiplication is symmetric.

        See :py:meth:`__mul__` for more details."""
        return self.__mul__(other)
