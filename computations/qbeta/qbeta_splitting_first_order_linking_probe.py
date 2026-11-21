#!/usr/bin/env python3
"""First-order term of the z_D trace of a closed braid: it is the linking number (qou-99qc, audit section 16).

Audit section 15 said a difference between two writhe-0 gamma-gamma words is a link-invariant
difference and so "starts at second order". That holds for KNOTS (V(1)=1, V'(1)=0) but not for
links: the first derivative of the Jones polynomial of a link is proportional to its total
linking number [murakami-1986 style; checked here, not cited]. This probe measures it.

Method: exact. The trace is the normalised quantum trace on (C^2)^{(x)n} with the Jimbo R-matrix
and K = diag(q, 1/q) per strand (equal to the Markov trace at z_D = q^3/(q^2+1); checked on one
crossing). Matrices are carried as dual numbers over Fraction at q = 1 + e, i.e. exactly to
first order in e = q - 1. Every word on n strands up to length L is enumerated; for each word we
record writhe w, component count c, total linking number lk and the pair (t0, t1) of
t = t0 + t1 e + O(e^2). Claim tested: t0 = 2^{-(n-c)} and t1 = (2w - 3 lk) 2^{-(n-c)}. The
probe FITS NOTHING: it reports whether one formula in (w, c, lk) covers every word, and prints
the distinct (w, c, lk) -> t1 / t0 values so the formula can be read off.

Prints only; writes no witness.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

N_STRANDS = (3, 4)
MAX_LEN = {3: 7, 4: 6}


class D:
    """Dual number a + b e over Fraction, e^2 = 0."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=F(0)):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        return D(self.a + o.a, self.b + o.b)

    def __mul__(self, o):
        return D(self.a * o.a, self.a * o.b + self.b * o.a)

    def iszero(self):
        return self.a == 0 and self.b == 0


ZERO, ONE = D(0), D(1)
Q, QI, H = D(1, 1), D(1, -1), D(0, 2)          # q, 1/q, h = q - 1/q to first order
# Jimbo R on basis 00,01,10,11 and its inverse (R - h)
R = [[Q, ZERO, ZERO, ZERO], [ZERO, ZERO, ONE, ZERO], [ZERO, ONE, H, ZERO], [ZERO, ZERO, ZERO, Q]]
MH = D(0, -2)
RI = [[QI, ZERO, ZERO, ZERO], [ZERO, MH, ONE, ZERO], [ZERO, ONE, ZERO, ZERO], [ZERO, ZERO, ZERO, QI]]


def apply_letter(M, n, g):
    """Right-multiply the 2^n x 2^n matrix M (list of rows, sparse dicts) by the letter g."""
    i = abs(g) - 1
    B = R if g > 0 else RI
    shift = n - i - 2
    out = []
    for row in M:
        new = {}
        for col, v in row.items():
            hi = (col >> shift) & 3
            for k in range(4):
                c = B[hi][k]
                if c.iszero():
                    continue
                ncol = (col & ~(3 << shift)) | (k << shift)
                new[ncol] = new.get(ncol, ZERO) + v * c
        out.append({k: v for k, v in new.items() if not v.iszero()})
    return out


def qtrace(M, n):
    tot = ZERO
    for r, row in enumerate(M):
        v = row.get(r)
        if v is None:
            continue
        kq = D(1)
        for s in range(n):
            kq = kq * (Q if (r >> (n - 1 - s)) & 1 == 0 else QI)
        tot = tot + kq * v
    inv = F(1, 2**n)
    return D(tot.a * inv, tot.b * inv)


def invariants(n, word):
    pos = list(range(n))
    cross = []
    for g in word:
        i = abs(g) - 1
        a, b = pos[i], pos[i + 1]
        cross.append((a, b, 1 if g > 0 else -1))
        pos[i], pos[i + 1] = b, a
    end = {s: k for k, s in enumerate(pos)}
    comp, c = {}, 0
    for s in range(n):
        if s in comp:
            continue
        t = s
        while t not in comp:
            comp[t] = c
            t = end[t]
        c += 1
    lk2 = sum(e for a, b, e in cross if comp[a] != comp[b])
    w = sum(e for _, _, e in cross)
    return w, c, F(lk2, 2)


def main() -> int:
    # sanity: one crossing on two strands gives z_D to first order: q^3/(q^2+1) = 1/2 + e + O(e^2)
    M = [{r: ONE} for r in range(4)]
    t = qtrace(apply_letter(M, 2, 1), 2)
    ok = (t.a, t.b) == (F(1, 2), F(1))
    print(f"[{'PASS' if ok else 'FAIL'}] tr(sigma) = z_D = 1/2 + e + O(e^2): got {t.a} + {t.b} e")
    table = {}
    for n in N_STRANDS:
        letters = [g for i in range(1, n) for g in (i, -i)]
        ident = [{r: ONE} for r in range(2**n)]
        stack = [((), ident)]
        while stack:
            word, M = stack.pop()
            if word:
                tt = qtrace(M, n)
                w, c, lk = invariants(n, word)
                key = (n, w, c, lk)
                table.setdefault(key, set()).add((tt.a, tt.b))
            if len(word) < MAX_LEN[n]:
                for g in letters:
                    if word and g == -word[-1]:
                        continue
                    stack.append((word + (g,), apply_letter(M, n, g)))
    t0_ok = all(len({a for a, _ in v}) == 1 and next(iter(v))[0] == F(1, 2 ** (k[0] - k[2])) for k, v in table.items())
    det = all(len({b for _, b in v}) == 1 for v in table.values())
    formula = all(next(iter(v))[1] == F(1, 2 ** (k[0] - k[2])) * (2 * F(k[1], 1) - 3 * k[3]) for k, v in table.items())
    for name, passed in [("t0 = 2^{-(n-c)} for every word", t0_ok),
                         ("t1 is a function of (n, w, c, lk) alone", det),
                         ("t1 = (2w - 3 lk) 2^{-(n-c)} for every word", formula)]:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        ok &= passed
    print("\nsample (n, writhe, components, lk) -> t1/t0 at writhe 0:")
    for k in sorted(table):
        if k[1] == 0:
            b = next(iter(table[k]))[1]
            print(f"  {k} -> {b * 2 ** (k[0] - k[2])}")
    # Owner option 1: the only n/p word split on record (PR #8636, S-w + C-lep, 4 strands)
    # appears above q* = 1.1510: n selects V1V2 = s1 s3^-1, p selects V1^3 = (s1 s2^-1)^3.
    print("\n#8636 split above q* (4 strands): (writhe, components, lk)")
    for name, word in (("n: V1V2 = s1 s3^-1", (1, -3)), ("p: V1^3", (1, -2) * 3), ("p: V2^3", (2, -3) * 3)):
        print(f"  {name}: {invariants(4, word)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
