#!/usr/bin/env python3
"""Exact check that the homogenised colour cubic h3(X,z,w)=0 is the curve 50a1.

Companion to QOU/Mass/ColourCubicElliptic.lean, which proves the birational map
and its inverse as polynomial identities. This script checks the two facts the
Lean file does not: (1) the target y^2+xy+y = x^3-x-2 has the invariants of
Cremona 50a1 (c4 = 25, c6 = 1475, Delta = -1250), and (2) point counts of
h3 = 0 mod p agree with that curve for small good primes. Exact integer and
rational arithmetic only. Writes no witness.
"""
from fractions import Fraction
from itertools import product


def invariants(a1, a2, a3, a4, a6):
    b2 = a1 ** 2 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 ** 2 + 4 * a6
    b8 = a1 ** 2 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 ** 2 - a4 ** 2
    c4 = b2 ** 2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    disc = -b2 ** 2 * b8 - 8 * b4 ** 3 - 27 * b6 ** 2 + 9 * b2 * b4 * b6
    return c4, c6, disc


def h3(X, z, w):
    return (X ** 3 + z ** 3 + w ** 3 + X ** 2 * z + X ** 2 * w + z ** 2 * X
            + z ** 2 * w + w ** 2 * X + w ** 2 * z + X * z * w)


def proj_points(p):
    pts = [(1, a, b) for a in range(p) for b in range(p)]
    pts += [(0, 1, b) for b in range(p)]
    pts.append((0, 0, 1))
    return sum(1 for P in pts if h3(*P) % p == 0)


def weier_points(p):
    n = 1  # point at infinity
    for x, y in product(range(p), repeat=2):
        if (y * y + x * y + y - x ** 3 + x + 2) % p == 0:
            n += 1
    return n


def main():
    checks = []
    c4, c6, d = invariants(1, 0, 1, -1, -2)
    checks.append(("50a1 invariants c4=25 c6=1475 Delta=-1250", (c4, c6, d) == (25, 1475, -1250)))
    checks.append(("j = -25/2", Fraction(c4 ** 3, d) == Fraction(-25, 2)))
    for p in (3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        a, b = proj_points(p), weier_points(p)
        checks.append((f"#h3(F_{p}) = #E(F_{p}) = {a}", a == b))
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    npass = sum(ok for _, ok in checks)
    print(f"{npass}/{len(checks)}")
    raise SystemExit(0 if npass == len(checks) else 1)


if __name__ == "__main__":
    main()
