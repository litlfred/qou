"""Exact Hecke-tower Markov trace over Q(q) (or Q at a rational q).

Convention of QOU/.../MarkovTraceHeckeFunctional.lean (towerTr): generators
sigma_i with sigma^2 = h sigma + 1, h = q - 1/q, Markov tr(x sigma_n) = z tr(x),
tr(1) = 1, z = z_D = q^3/(q^2+1). A letter (a, b, i) is a*sigma_i + b*1, the
format of mass_at_3A_proper.atom_braid_word_3A. No floats anywhere.
"""
from __future__ import annotations

from functools import lru_cache

from sympy import QQ
from sympy.polys.fields import field

K, qs = field("q", QQ)


class Ring:
    """Coefficient ring: K = Q(q) symbolically, or Q at an exact rational q."""

    def __init__(self, qval=None):
        if qval is None:
            self.q = qs
            self.one = K.one
        else:
            from fractions import Fraction
            self.q = Fraction(qval)
            self.one = Fraction(1)
        self.h = self.q - self.one / self.q
        self.z = self.q ** 3 / (self.q ** 2 + 1)
        self._tr = lru_cache(maxsize=None)(self._trT)

    def mulgen(self, x, i, a, b):
        out = {}
        h = self.h
        for w, c in x.items():
            if b:
                out[w] = out.get(w, 0) + c * b
            if a:
                l = list(w)
                up = l[i] < l[i + 1]
                l[i], l[i + 1] = l[i + 1], l[i]
                u = tuple(l)
                out[u] = out.get(u, 0) + c * a
                if not up:
                    out[w] = out.get(w, 0) + c * a * h
        return {w: c for w, c in out.items() if c != 0}

    def _trT(self, w):
        n = len(w)
        if n == 1:
            return self.one
        if w[-1] == n - 1:
            return self._tr(w[:-1])
        p = w.index(n - 1)
        l = list(w)
        for i in range(p, n - 1):
            l[i], l[i + 1] = l[i + 1], l[i]
        x = {tuple(l[:-1]): self.one}
        for i in range(n - 3, p - 1, -1):
            x = self.mulgen(x, i, self.one, 0)
        return self.z * sum((c * self._tr(u) for u, c in x.items()), 0 * self.one)

    def word(self, n, letters):
        x = {tuple(range(n)): self.one}
        for a, b, i in letters:
            x = self.mulgen(x, i, a, b)
        return x

    def tr(self, n, letters):
        x = self.word(n, letters)
        return sum((c * self._tr(w) for w, c in x.items()), 0 * self.one)

    # letters --------------------------------------------------------------
    def S(self, i):
        return (self.one, 0, i)

    def I(self, i):  # sigma_i^{-1} = sigma_i - h
        return (self.one, -self.h, i)

    def Av(self, i):  # averaged letter sigma_i - h/2
        return (self.one, -self.h / 2, i)

    def V3(self, k=0):
        return [self.S(k), self.I(k + 1)] * 3

    def proton(self, k=0):
        """Production proton block (mass_at_3A_proper.atom_braid_word_3A)."""
        return self.V3(k) + [self.S(k), self.Av(k), self.Av(k + 1), self.S(k), self.S(k)]

    def neutron(self, k=0):
        return self.V3(k) + [self.Av(k), self.Av(k), self.I(k + 1), self.S(k), self.S(k)]
