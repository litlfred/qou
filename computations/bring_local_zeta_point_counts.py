#!/usr/bin/env python3
"""Exact point counts of Bring's curve and of the elliptic curve 50a1.

Bring's curve B in P^4: sum x_i = sum x_i^2 = sum x_i^3 = 0.  Eliminating
x_5 = -(x_1+...+x_4) gives a curve in P^3; this script counts its points over
F_p for primes 7 <= p <= 41 and over F_49, using integer arithmetic only.

It checks |B(F_p)| = p + 1 - 4 a_p with a_p = p + 1 - |E(F_p)| for
E: y^2 + xy + y = x^3 - x - 2 (Cremona 50a1), which is what the isogeny
J(B) ~ E^4 predicts, and |B(F_49)| = 49 + 1 - 4 (a_7^2 - 2*7).  It then checks
Hasse's bound a_p^2 <= 4p at each prime, the finite-field Riemann hypothesis
for B at p.  Used by sec:q-gl-weil-bound-stability (weil-bound-intro.md).

No floating point: every quantity is an int.
"""
from itertools import product

PRIMES = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def bring_count_Fp(p):
    n = 0
    for x1, x2, x3, x4 in product(range(p), repeat=4):
        x5 = -(x1 + x2 + x3 + x4) % p
        xs = (x1, x2, x3, x4, x5)
        if sum(x * x for x in xs) % p == 0 and sum(x ** 3 for x in xs) % p == 0:
            n += 1
    return (n - 1) // (p - 1)


def ec50a1_count_Fp(p):
    n = 1  # point at infinity
    for x in range(p):
        for y in range(p):
            if (y * y + x * y + y - (x ** 3 - x - 2)) % p == 0:
                n += 1
    return n


def bring_count_F49():
    p, nr = 7, 3  # F_49 = F_7[i], i^2 = 3 (3 is a non-residue mod 7)
    els = [(a, b) for a in range(p) for b in range(p)]
    add = lambda u, v: ((u[0] + v[0]) % p, (u[1] + v[1]) % p)
    mul = lambda u, v: ((u[0] * v[0] + nr * u[1] * v[1]) % p, (u[0] * v[1] + u[1] * v[0]) % p)
    neg = lambda u: ((-u[0]) % p, (-u[1]) % p)
    sq = {u: mul(u, u) for u in els}
    cu = {u: mul(sq[u], u) for u in els}
    zero = (0, 0)
    n = 0
    for x1, x2, x3, x4 in product(els, repeat=4):
        x5 = neg(add(add(x1, x2), add(x3, x4)))
        xs = (x1, x2, x3, x4, x5)
        s2 = zero
        s3 = zero
        for x in xs:
            s2 = add(s2, sq[x])
            s3 = add(s3, cu[x])
        if s2 == zero and s3 == zero:
            n += 1
    return (n - 1) // (49 - 1)


def main():
    ok = True
    for p in PRIMES:
        nb = bring_count_Fp(p)
        ap = p + 1 - ec50a1_count_Fp(p)
        match = nb == p + 1 - 4 * ap
        hasse = ap * ap <= 4 * p
        ok &= match and hasse
        print(f"p={p:2d}  #B(F_p)={nb:3d}  a_p(50a1)={ap:3d}  "
              f"#B = p+1-4a_p: {match}  a_p^2 <= 4p: {hasse}")
    a7 = 7 + 1 - ec50a1_count_Fp(7)
    n49 = bring_count_F49()
    pred = 49 + 1 - 4 * (a7 * a7 - 2 * 7)
    ok &= n49 == pred
    print(f"#B(F_49)={n49}  predicted by (1 - a_7 T + 7T^2)^4: {pred}")
    print("ALL CHECKS PASS" if ok else "CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
