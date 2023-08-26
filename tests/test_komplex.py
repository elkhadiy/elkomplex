from elkomplex import Komplex
from math import sqrt, pi, cos, sin, atan2, isclose


class TestKomplex:

    def test_default_constructor(self):
        zero = Komplex()
        assert isclose(zero._re, 0)
        assert isclose(zero._im, 0)
        assert isclose(zero._r, 0)

    def test_cartesian_constructor(self):
        c = Komplex.from_cartesian(2, 3)
        assert isclose(c._re, 2)
        assert isclose(c._im, 3)
        assert isclose(c._r, sqrt(2 ** 2 + 3 ** 2))
        assert isclose(c._th, atan2(3, 2))

    def test_polar_constructor(self):
        c = Komplex.from_polar(1, pi / 4)
        assert isclose(c._re, sqrt(2) / 2)
        assert isclose(c._im, sqrt(2) / 2)
        r = 2.3
        th = 0.65
        c = Komplex.from_polar(r, th)
        assert isclose(c._re, r * cos(th))
        assert isclose(c._im, r * sin(th))
