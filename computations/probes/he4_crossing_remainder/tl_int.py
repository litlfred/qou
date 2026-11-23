"""Fast exact TL-quotient Markov trace at a rational q = p/D, integer arithmetic only.

Every letter a*sigma + b with (a, b) in {sigma, sigma^-1, averaged} is written
c1*1 + c2*e (e = q - sigma) and multiplied by F = 2 p D, which makes c1*F, c2*F and the
loop weight c2*F*d (d = q + 1/q) integers. The common factor F^len(word) and the closure
weights d^(loops - n) are divided out once at the end, as one Fraction. Same answer as
tl_numeric.TLQ (checked in selftest), without per-step gcds.
"""
from __future__ import annotations

from fractions import Fraction

from tl_exact import identity, times_e, loops

KIND_S, KIND_I, KIND_AV = 0, 1, 2


class TLInt:
    def __init__(self, q):
        q = Fraction(q)
        self.q = q
        self.p, self.D = q.numerator, q.denominator
        p, D = self.p, self.D
        self.c1 = {KIND_S: 2 * p * p, KIND_I: 2 * D * D, KIND_AV: p * p + D * D}
        self.c2 = -2 * p * D
        self.c2loop = -2 * (p * p + D * D)
        self.F = 2 * p * D

    # letters are (kind, 0, i), the (a, b, i) shape assembly.build shifts
    def S(self, i):
        return (KIND_S, 0, i)

    def I(self, i):
        return (KIND_I, 0, i)

    def Av(self, i):
        return (KIND_AV, 0, i)

    def V3(self, k=0, mirror=False):
        return [self.I(k), self.S(k + 1)] * 3 if mirror else [self.S(k), self.I(k + 1)] * 3

    def proton(self, k=0):
        return self.V3(k) + [self.S(k), self.Av(k), self.Av(k + 1), self.S(k), self.S(k)]

    def neutron(self, k=0):
        return self.V3(k) + [self.Av(k), self.Av(k), self.I(k + 1), self.S(k), self.S(k)]

    def tr(self, n, letters):
        num, den = self.tr_parts(n, letters)
        return Fraction(num, den)

    def tr_parts(self, n, letters):
        """(num, den) integers, tr = num / den, den = F^len * (p^2 + D^2)^n, unreduced."""
        st = {identity(n): 1}
        c2, c2l = self.c2, self.c2loop
        for kind, _, i in letters:
            c1 = self.c1[kind]
            out = {}
            for Dg, c in st.items():
                out[Dg] = out.get(Dg, 0) + c * c1
                E, lp = times_e(Dg, n, i)
                out[E] = out.get(E, 0) + c * (c2l if lp else c2)
            st = {k: v for k, v in out.items() if v}
        p, D = self.p, self.D
        s, pd = p * p + D * D, p * D
        num = sum(c * pd ** (n - L) * s ** L for Dg, c in st.items() for L in (loops(Dg, n),))
        return num, self.F ** len(letters) * s ** n


def decode_balanced(N, K):
    """Integer coefficients c_k of a polynomial with |c_k| < 2^(K-1), from N = sum c_k 2^(K k)."""
    out, k, base, half = {}, 0, 1 << K, 1 << (K - 1)
    while N:
        r = N & (base - 1)
        if r >= half:
            r -= base
        if r:
            out[k] = r
        N = (N - r) >> K
        k += 1
    return out


def tr_poly(n, letters, K=512):
    """Exact tr(q) = num(q) / ((2q)^len (q^2+1)^n), num an integer polynomial, obtained by one
    integer run at q = 2^K (Kronecker substitution) and checked at q = 11/10 and 7/3."""
    R = TLInt(1 << K)
    num, _ = R.tr_parts(n, letters)
    c = decode_balanced(num, K)
    assert max(abs(v) for v in c.values()).bit_length() < K - 8, "raise K"
    for qt in (Fraction(11, 10), Fraction(7, 3)):
        val = sum(Fraction(v) * qt ** k for k, v in c.items()) / ((2 * qt) ** len(letters) * (qt * qt + 1) ** n)
        assert val == TLInt(qt).tr(n, letters), "Kronecker decode failed"
    return c, len(letters)
