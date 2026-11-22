"""Same TL-quotient Markov trace as tl_exact.py, at an exact rational q (Fraction).

Letters are (a, b, i) with a, b Fractions: a*sigma_i + b = (a q + b) - a e_i.
Exploration engine; tl_int.TLInt is checked against it on random words. No floats.
"""
from __future__ import annotations

from fractions import Fraction

from tl_exact import identity, times_e, loops


class TLQ:
    def __init__(self, q):
        self.q = Fraction(q)
        self.h = self.q - 1 / self.q
        self.d = self.q + 1 / self.q
        self.one = Fraction(1)

    def S(self, i):
        return (self.one, Fraction(0), i)

    def I(self, i):
        return (self.one, -self.h, i)

    def Av(self, i):
        return (self.one, -self.h / 2, i)

    def V3(self, k=0, mirror=False):
        if mirror:
            return [self.I(k), self.S(k + 1)] * 3
        return [self.S(k), self.I(k + 1)] * 3

    def proton(self, k=0, mirror=False):
        return self.V3(k, mirror) + [self.S(k), self.Av(k), self.Av(k + 1), self.S(k), self.S(k)]

    def neutron(self, k=0, mirror=False):
        return self.V3(k, mirror) + [self.Av(k), self.Av(k), self.I(k + 1), self.S(k), self.S(k)]

    def apply(self, st, n, letters):
        q, d = self.q, self.d
        for a, b, i in letters:
            c1 = a * q + b
            out = {}
            for D, c in st.items():
                if c1:
                    out[D] = out.get(D, 0) + c * c1
                E, lp = times_e(D, n, i)
                t = -c * a * (d if lp else 1)
                out[E] = out.get(E, 0) + t
            st = {D: c for D, c in out.items() if c}
        return st

    def tr(self, n, letters):
        st = self.apply({identity(n): self.one}, n, letters)
        d = self.d
        return sum((c * d ** (loops(D, n) - n) for D, c in st.items()), Fraction(0))
