from elkomplex import Komplex
from math import sqrt, cos, sin, atan2, isclose


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
