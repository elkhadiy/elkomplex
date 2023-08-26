from elkomplex import Komplex, i
from math import sqrt, pi, cos, sin, atan2, isclose


class TestKomplex:

    def test_default_constructor(self):
        zero = Komplex()
        assert isclose(zero._re, 0, abs_tol=1e-15)
        assert isclose(zero._im, 0, abs_tol=1e-15)
        assert isclose(zero._r, 0, abs_tol=1e-15)

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

    def test_eq(self):
        assert Komplex.from_cartesian(0, 0) == Komplex()
        assert Komplex.from_polar(0, 4.6) == Komplex()
        assert (Komplex.from_cartesian(sqrt(2) / 2, sqrt(2) / 2)
                == Komplex.from_polar(1, pi / 4))

    def test_add(self):
        c1 = Komplex.from_cartesian(2, 3)
        c2 = Komplex.from_cartesian(4, 5)

        assert c1 + c2 == Komplex.from_cartesian(6, 8)
        assert c1 + 2 == Komplex.from_cartesian(4, 3)
        assert 2 + c1 == Komplex.from_cartesian(4, 3)

    def test_sub(self):
        c1 = Komplex.from_cartesian(2, 3)
        c2 = Komplex.from_cartesian(4, 5)

        assert c1 - c2 == Komplex.from_cartesian(-2, -2)
        assert c1 - 2 == Komplex.from_cartesian(0, 3)
        assert 2 - c1 == Komplex.from_cartesian(0, -3)

    def test_mul(self):
        c1 = Komplex.from_cartesian(2, 3)
        c2 = Komplex.from_cartesian(4, 5)

        assert Komplex() * c1 == Komplex()
        assert 0 * c1 == Komplex()
        assert c1 * 0 == Komplex()

        assert i * i == -1

        assert 1 * c1 == c1
        assert c1 * 1 == c1

        a = c1._re
        b = c1._im
        c = c2._re
        d = c2._im
        assert c1 * c2 == Komplex.from_cartesian(a*c - b*d, a*d + b*c)
