from elkomplex import Komplex
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

    def test_add(self):
        c1 = Komplex.from_cartesian(2, 3)
        c2 = Komplex.from_cartesian(4, 5)
        c3 = c1 + c2
        assert isclose(c3._re, 6)
        assert isclose(c3._im, 8)
        c3 = c1 + 2
        assert isclose(c3._re, 4)
        assert isclose(c3._im, 3)
        c3 = 2 + c1
        assert isclose(c3._re, 4)
        assert isclose(c3._im, 3)

    def test_sub(self):
        c1 = Komplex.from_cartesian(2, 3)
        c2 = Komplex.from_cartesian(4, 5)
        c3 = c1 - c2
        assert isclose(c3._re, -2)
        assert isclose(c3._im, -2)
        c3 = c1 - 2
        assert isclose(c3._re, 0, abs_tol=1e-15)
        assert isclose(c3._im, 3)
        c3 = 2 - c1
        assert isclose(c3._re, 0, abs_tol=1e-15)
        assert isclose(c3._im, -3)

    def test_mul(self):
        c0 = Komplex()
        i = Komplex.from_cartesian(0, 1)
        c1 = Komplex.from_cartesian(2, 3)
        c2 = Komplex.from_cartesian(4, 5)

        r0 = c0 * c1
        assert isclose(r0._re, 0, abs_tol=1e-15)
        assert isclose(r0._im, 0, abs_tol=1e-15)

        r0 = 0 * c1
        assert isclose(r0._re, 0, abs_tol=1e-15)
        assert isclose(r0._im, 0, abs_tol=1e-15)

        r0 = c1 * 0
        assert isclose(r0._re, 0, abs_tol=1e-15)
        assert isclose(r0._im, 0, abs_tol=1e-15)

        r0 = i * i
        assert isclose(r0._re, -1)
        assert isclose(r0._im, 0, abs_tol=1e-15)

        r1 = 1 * c1
        assert isclose(r1._re, c1._re)
        assert isclose(r1._im, c1._im)

        r1 = c1 * 1
        assert isclose(r1._re, c1._re)
        assert isclose(r1._im, c1._im)

        r2 = c1 * c2
        a = c1._re
        b = c1._im
        c = c2._re
        d = c2._im
        assert isclose(r2._re, a * c - b * d)
        assert isclose(r2._im, a * d + b * c)
