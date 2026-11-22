"""Exact Iwahori–Hecke algebra H_N(q) on the standard (Gröbner–Shirshov normal-form) basis T_w.

Relations: σ_i² = h σ_i + 1, h = q − q⁻¹ (eigenvalues q, −q⁻¹), braid relations. Every word
reduces uniquely to Σ_w c_w T_w (w ∈ S_N) — the Gröbner–Shirshov normal form of the Hecke
presentation. Coefficients live in a polynomial ring over the rational-function field ℚ(q)
(sympy sparse polys), so photon weights may be symbolic. No floats anywhere.

Permutations are tuples of images (one-line). Right multiplication by s_i swaps POSITIONS i, i+1;
T_w σ_i = T_{w s_i} if w(i) < w(i+1), else h T_w + T_{w s_i}. Words are read left to right.

Markov trace (Ocneanu): tr(1) = 1, tr(x σ_{n-1}) = z tr(x) for x ∈ H_{n-1}, tr(xy) = tr(yx).
Computed by the coset recursion T_w = T_u σ_{N-2} T_c (lengths add), tr = z tr(T_c T_u).
"""
from __future__ import annotations

from functools import lru_cache

from sympy import QQ
from sympy.polys.fields import field
from sympy.polys.rings import ring

KF, q = field("q", QQ)
RING, p0, p1, p2, s0, s1, s2 = ring("p0 p1 p2 s0 s1 s2", KF)
ONE = RING.one
ZERO = RING.zero
h = q - 1 / q
zD = q ** 3 / (q ** 2 + 1)


def ident(N):
    return tuple(range(N))


class H:
    """Element of H_N: dict perm -> coefficient (RING element)."""

    __slots__ = ("N", "c")

    def __init__(self, N, c=None):
        self.N = N
        self.c = {} if c is None else {k: v for k, v in c.items() if v != 0}

    @staticmethod
    def one(N, coeff=ONE):
        return H(N, {ident(N): RING(coeff)})

    @staticmethod
    def gen(N, i, power=1):
        x = H.one(N)
        if power >= 0:
            for _ in range(power):
                x = x.rmul_gen(i)
        else:
            for _ in range(-power):
                x = x.rmul_geninv(i)
        return x

    def __add__(self, o):
        assert self.N == o.N
        d = dict(self.c)
        for k, v in o.c.items():
            d[k] = d.get(k, ZERO) + v
        return H(self.N, d)

    def __sub__(self, o):
        return self + o.scale(-ONE)

    def scale(self, a):
        a = RING(a)
        return H(self.N, {k: v * a for k, v in self.c.items()})

    def rmul_gen(self, i):
        d: dict = {}
        hh = RING(h)
        for w, v in self.c.items():
            ws = list(w)
            ws[i], ws[i + 1] = ws[i + 1], ws[i]
            ws = tuple(ws)
            if w[i] < w[i + 1]:
                d[ws] = d.get(ws, ZERO) + v
            else:
                d[w] = d.get(w, ZERO) + v * hh
                d[ws] = d.get(ws, ZERO) + v
        return H(self.N, d)

    def rmul_geninv(self, i):
        # σ⁻¹ = σ − h
        return self.rmul_gen(i) - self.scale(RING(h))

    def rmul_word(self, word):
        x = self
        for g in word:
            x = x.rmul_gen(g) if g >= 0 else x.rmul_geninv(-g - 1)
        return x

    def __mul__(self, o):
        assert self.N == o.N
        out = H(self.N)
        for v, cv in o.c.items():
            out = out + self.rmul_word(reduced_word(v)).scale(cv)
        return out

    def trace(self, z=zD):
        tot = ZERO
        for w, v in self.c.items():
            tot += v * RING(tr_T(w, z))
        return tot


def reduced_word(w):
    """A reduced word for w (bubble sort on positions): T_w = σ_{a1}…σ_{ak}."""
    w = list(w)
    word = []
    # sort w to identity by right-multiplying with s_i where w(i) > w(i+1); record, then reverse
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] > w[i + 1]:
                w[i], w[i + 1] = w[i + 1], w[i]
                word.append(i)
                changed = True
    return tuple(reversed(word))


def embed(x: H, N, shift=0):
    """Embed x ∈ H_n into H_N on strands shift..shift+n-1."""
    d = {}
    for w, v in x.c.items():
        img = list(range(N))
        for k, wk in enumerate(w):
            img[shift + k] = shift + wk
        d[tuple(img)] = v
    return H(N, d)


@lru_cache(maxsize=None)
def tr_T(w, z):
    N = len(w)
    if N <= 1:
        return KF.one
    if w[N - 1] == N - 1:
        return tr_T(w[:-1], z)
    p = w.index(N - 1)
    # u = w·(s_p s_{p+1} … s_{N-2})  (moves value N-1 to the last position)
    u = list(w)
    for i in range(p, N - 1):
        u[i], u[i + 1] = u[i + 1], u[i]
    # w = u · s_{N-2} s_{N-3} … s_p ; c' = s_{N-3} … s_p
    cword = tuple(range(N - 3, p - 1, -1))
    Tc = H.one(N - 1).rmul_word(cword)
    Tu = H(N - 1, {tuple(u[:-1]): ONE})
    prod = Tc * Tu
    tot = KF.zero
    for ww, vv in prod.c.items():
        tot += vv.coeff(1) * tr_T(ww, z) if vv.is_ground else _fail()
    return z * tot


def _fail():
    raise RuntimeError("non-ground coefficient in trace recursion")
