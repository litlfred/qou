"""Exact Markov trace at z_D through the Temperley-Lieb quotient (Kauffman-bracket form).

Why this is the same trace as hecke_exact.Ring.tr: at z_D = q^3/(q^2+1) the Ocneanu
weights of every partition with three or more rows vanish
(QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows), so the trace factors
through TL_n.  With e_i = q - sigma_i (e_i^2 = d e_i, d = q + 1/q) the Markov property
tr(x sigma_n) = z tr(x) becomes tr(x e_n) = (q - z) tr x = tr x / d, the Jones trace,
tr(D) = d^(loops(closure D) - n).  The module checks itself against hecke_exact.Ring on
random words (selftest()).

Coefficients are Laurent polynomials in q with Fraction coefficients (dict exp -> Fraction).
A letter (a, b, i) = a*sigma_i + b = (a*q + b) - a*e_i, a, b Laurent.  No floats.
"""
from __future__ import annotations

from fractions import Fraction


# ---------------------------------------------------------------- Laurent polynomials
def L(d):
    return {k: Fraction(v) for k, v in d.items() if v != 0}


ONE = {0: Fraction(1)}
Q = {1: Fraction(1)}
QI = {-1: Fraction(1)}
H = {1: Fraction(1), -1: Fraction(-1)}          # h = q - 1/q
DELTA = {1: Fraction(1), -1: Fraction(1)}       # d = q + 1/q


def ladd(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        w = out.get(k, 0) + s * v
        if w:
            out[k] = w
        else:
            out.pop(k, None)
    return out


def lmul(a, b):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            out[i + j] = out.get(i + j, 0) + u * v
    return {k: v for k, v in out.items() if v != 0}


def lscale(a, c):
    return {k: v * c for k, v in a.items() if v * c != 0}


def lpow(a, n):
    out = ONE
    for _ in range(n):
        out = lmul(out, a)
    return out


def leval(a, q):
    q = Fraction(q)
    return sum((v * q ** k for k, v in a.items()), Fraction(0))


def lkey(a):
    return tuple(sorted(a.items()))


# ---------------------------------------------------------------- TL diagrams
def identity(n):
    return tuple(list(range(n, 2 * n)) + list(range(n)))


def times_e(D, n, i):
    """D * e_i (e_i glued under D). Returns (diagram, loops created)."""
    bi, bj = n + i, n + i + 1
    x, y = D[bi], D[bj]
    if x == bj:
        return D, 1
    p = list(D)
    p[x], p[y] = y, x
    p[bi], p[bj] = bj, bi
    return tuple(p), 0


def loops(D, n):
    """Number of loops in the closure (top k joined to bottom k)."""
    seen = [False] * (2 * n)
    c = 0
    for s in range(2 * n):
        if seen[s]:
            continue
        c += 1
        k = s
        while not seen[k]:
            seen[k] = True
            m = D[k]
            seen[m] = True
            k = m - n if m >= n else m + n   # closure arc
    return c


def apply_letter(state, n, a, b, i):
    """state * (a sigma_i + b) = state * ((a q + b) - a e_i)."""
    c1 = ladd(lmul(a, Q), b)
    out = {}
    for D, c in state.items():
        if c1:
            out[D] = ladd(out.get(D, {}), lmul(c, c1))
        E, lp = times_e(D, n, i)
        t = lscale(lmul(c, a), -1)
        if lp:
            t = lmul(t, DELTA)
        out[E] = ladd(out.get(E, {}), t)
    return {D: c for D, c in out.items() if c}


def word_state(n, letters, start=None):
    st = {identity(n): ONE} if start is None else start
    for a, b, i in letters:
        st = apply_letter(st, n, a, b, i)
    return st


def trace_num(state, n):
    """Returns P with tr = P / d^n (P Laurent)."""
    P = {}
    for D, c in state.items():
        P = ladd(P, lmul(c, lpow(DELTA, loops(D, n))))
    return P


def tr_at(state, n, q):
    q = Fraction(q)
    d = q + 1 / q
    return sum((leval(c, q) * d ** (loops(D, n) - n) for D, c in state.items()), Fraction(0))


# ---------------------------------------------------------------- letters (Laurent coefficients)
def S(i):
    return (ONE, {}, i)


def I(i):  # sigma^-1 = sigma - h
    return (ONE, lscale(H, -1), i)


def Av(i):
    return (ONE, lscale(H, Fraction(-1, 2)), i)


def V3(k=0):
    return [S(k), I(k + 1)] * 3


def proton(k=0):
    return V3(k) + [S(k), Av(k), Av(k + 1), S(k), S(k)]


def neutron(k=0):
    return V3(k) + [Av(k), Av(k), I(k + 1), S(k), S(k)]


def to_sympy(P, n):
    """P / d^n as a sympy expression in q."""
    import sympy as sp
    q = sp.Symbol("q")
    num = sum(sp.Rational(v.numerator, v.denominator) * q ** k for k, v in P.items())
    return sp.together(num / (q + 1 / q) ** n)


def selftest(trials=30, seed=1):
    import random
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "he4_closed_form"))
    from hecke_exact import Ring
    R = Ring("11/10")
    rng = random.Random(seed)
    for t in range(trials):
        n = rng.choice([3, 4, 5])
        word_tl, word_h = [], []
        for _ in range(rng.randint(1, 9)):
            i = rng.randrange(n - 1)
            kind = rng.randrange(3)
            word_tl.append([S, I, Av][kind](i))
            word_h.append([R.S, R.I, R.Av][kind](i))
        a = tr_at(word_state(n, word_tl), n, Fraction(11, 10))
        b = R.tr(n, word_h)
        assert a == b, (t, n, a, b)
    return True


if __name__ == "__main__":
    print("selftest", selftest())


class SymLetters:
    """Letter factory for assembly.build over Q(q) Laurent coefficients."""
    S = staticmethod(S)
    I = staticmethod(I)
    Av = staticmethod(Av)

    @staticmethod
    def V3(k=0, mirror=False):
        return [I(k), S(k + 1)] * 3 if mirror else [S(k), I(k + 1)] * 3

    @staticmethod
    def proton(k=0):
        return proton(k)

    @staticmethod
    def neutron(k=0):
        return neutron(k)


def tr_field(n, letters):
    """tr as an element of hecke_exact.K = Q(q)."""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "he4_closed_form"))
    from hecke_exact import K, qs
    P = trace_num(word_state(n, letters), n)
    num = K.zero
    for k, v in P.items():
        num += K(v) * qs ** k
    return num / (qs + 1 / qs) ** n
