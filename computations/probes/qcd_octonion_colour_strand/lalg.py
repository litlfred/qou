"""Exact sparse matrices over the Laurent ring Z[q, q^-1] (and Q coefficients via Fraction).

A Laurent polynomial is a dict {exponent: Fraction}; a matrix is a dict {(row, col): Laurent}.
No floats anywhere. Used by the octonion colour-strand probe.
"""
from fractions import Fraction as Fr


def L(d=None):
    return {k: Fr(v) for k, v in (d or {}).items() if v != 0}


def lc(c, e=0):
    return L({e: c})


def ladd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, Fr(0)) + s * v
        if r[k] == 0:
            del r[k]
    return r


def lmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = k1 + k2
            r[k] = r.get(k, Fr(0)) + v1 * v2
    return {k: v for k, v in r.items() if v != 0}


def lstr(a):
    if not a:
        return "0"
    return " + ".join(f"{v}*q^{k}" for k, v in sorted(a.items()))


def leval(a, qv):
    return sum((v * Fr(qv) ** k for k, v in a.items()), Fr(0))


H = L({1: 1, -1: -1})  # q - q^-1


class M:
    def __init__(self, n, d=None):
        self.n = n
        self.d = {k: v for k, v in (d or {}).items() if v}

    @staticmethod
    def eye(n):
        return M(n, {(i, i): lc(1) for i in range(n)})

    @staticmethod
    def e(n, i, j, c=None):
        return M(n, {(i, j): c if c is not None else lc(1)})

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = ladd(d.get(k, {}), v)
        return M(self.n, d)

    def __sub__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = ladd(d.get(k, {}), v, -1)
        return M(self.n, d)

    def scale(self, c):
        return M(self.n, {k: lmul(v, c) for k, v in self.d.items()})

    def __matmul__(self, o):
        rows = {}
        for (i, j), v in self.d.items():
            rows.setdefault(j, []).append((i, v))
        d = {}
        for (j, k), w in o.d.items():
            for (i, v) in rows.get(j, []):
                d[(i, k)] = ladd(d.get((i, k), {}), lmul(v, w))
        return M(self.n, d)

    def kron(self, o):
        n = self.n * o.n
        d = {}
        for (i, j), v in self.d.items():
            for (k, l), w in o.d.items():
                d[(i * o.n + k, j * o.n + l)] = lmul(v, w)
        return M(n, d)

    def T(self):
        return M(self.n, {(j, i): v for (i, j), v in self.d.items()})

    def is_zero(self):
        return all(not v for v in self.d.values())

    def nonzero(self):
        return {k: v for k, v in self.d.items() if v}

    def __eq__(self, o):
        return (self - o).is_zero()
