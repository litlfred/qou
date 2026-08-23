#!/usr/bin/env python3
"""Two exact checks on the QOU perpetual-obstruction argument (bean qou-lrnd).

The documented derivation is: at q = zeta_{2p} the Habiro expansion of the QOU
Frobenius collapses, `Frob_p == 4 (mod P)` where P is the prime above p, and
therefore Frob_p is a non-unit at (almost) every prime.  The Lean scaffolding
in MotivicPerpetualObstructionFromTrace.lean encodes the last step as
`not_isUnit_of_image : not IsUnit (reduce x) -> not IsUnit x` with
`reduce : R p ->+* Z`.

This probe tests the two steps AFTER the collapse.  Both fail.

  CHECK 1 -- the target ring cannot be Z.
      A ring hom phi : Z[zeta_{2p}] ->+* Z with phi(zeta) = -1 would force
      Phi_{2p}(-1) = 0.  We compute Phi_{2p} exactly, from the defining
      recursion x^n - 1 = prod_{d|n} Phi_d(x) (no closed form assumed), and
      evaluate at -1.  It equals p, never 0.  So `reduce` must land in
      O/P = F_p, not in Z.

  CHECK 2 -- with the correct target F_p, the residue 4 is a UNIT.
      Exhibited, not searched: the cyclotomic unit
          u4 = 1 + zeta + zeta^2 + zeta^3 = (1 - zeta^4)/(1 - zeta)
      has inverse v = 1 + zeta^4 + ... + zeta^{4(b-1)} where 4b == 1 (mod p),
      because u4 * v = (1 - zeta^{4b})/(1 - zeta) = 1.  Both are manifestly in
      Z[zeta], so u4 is a unit of the ring of integers.  And zeta == 1 (mod P)
      gives u4 == 4 (mod P).
      So `x == 4 (mod P)` is COMPATIBLE with x being a unit.

NO FLOATS ANYWHERE.  Every value below is a Python int; the polynomial
arithmetic is exact integer arithmetic and every division is checked to have
zero remainder.  (AGENTS.md: probes are not exempt from the precision gates.)

Ref: [manuscript] bean qou-lrnd
Ref: QOU.LiftingDescent.map_habiro_expansion  (the collapse itself, in Lean)
Ref: QOU.LiftingDescent.isUnit_four_zmod      (CHECK 2, in Lean)
"""

# ---------------------------------------------------------------- polynomials
# Dense integer coefficient lists, index = degree.

def p_trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def p_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] += ai * bj
    return p_trim(out)

def p_divexact(a, b):
    """Exact quotient a / b over Z; asserts the remainder is zero."""
    a = a[:]
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        num, den = a[i + len(b) - 1], b[-1]
        assert num % den == 0, "non-exact division -- not a polynomial identity"
        c = num // den
        q[i] = c
        for j, bj in enumerate(b):
            a[i + j] -= c * bj
    assert all(x == 0 for x in a), f"nonzero remainder {a}"
    return p_trim(q)

def p_eval(a, x):
    return sum(c * x ** i for i, c in enumerate(a))

def cyclotomic(n, cache):
    """Phi_n from x^n - 1 = prod_{d|n} Phi_d(x). No closed form assumed."""
    if n in cache:
        return cache[n]
    num = [-1] + [0] * (n - 1) + [1]              # x^n - 1
    for d in range(1, n):
        if n % d == 0:
            num = p_divexact(num, cyclotomic(d, cache))
    cache[n] = num
    return num

# ------------------------------------------------------- cyclotomic integers
# Z[zeta_p] as length-p coefficient vectors; zeta^p = 1, then reduce by
# 1 + zeta + ... + zeta^{p-1} = 0 (subtract the top coefficient from all).

def cy_mul(a, b, p):
    out = [0] * p
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[(i + j) % p] += ai * bj
    return out

def cy_reduce(a, p):
    c = a[p - 1]
    return [a[i] - c for i in range(p)]

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 101, 1009]

def main() -> int:
    ok = True
    cache: dict = {}

    print("CHECK 1 -- Phi_{2p}(-1); a hom to Z sending zeta -> -1 needs this to be 0")
    print(f"  {'p':>6} {'deg Phi_2p':>11} {'Phi_2p(-1)':>11} {'== 0?':>7}")
    for p in PRIMES[:8]:
        Phi = cyclotomic(2 * p, cache)
        val = p_eval(Phi, -1)
        ok &= (val != 0) and (val == p)
        print(f"  {p:>6} {len(Phi) - 1:>11} {val:>11} {str(val == 0):>7}")
    print("  -> Phi_2p(-1) = p for every p tested; never 0.")
    print("     No ring hom Z[zeta_2p] ->+* Z sends zeta to -1.")
    print("     (Indeed none exists at all: O/ker would be an infinite quotient")
    print("      of a rank-(p-1) ring of integers.)  The target is O/P = F_p.\n")

    print("CHECK 2 -- is there a UNIT of Z[zeta_p] with residue 4 mod P?")
    print(f"  {'p':>6} {'b (4b=1 mod p)':>15} {'u4*v == 1':>11} {'u4 mod P':>9}")
    for p in PRIMES:
        b = pow(4, -1, p)
        u4 = [0] * p
        for k in range(4):
            u4[k % p] += 1
        v = [0] * p
        for j in range(b):
            v[(4 * j) % p] += 1
        prod = cy_reduce(cy_mul(u4, v, p), p)
        one = cy_reduce([1] + [0] * (p - 1), p)
        is_one = prod == one
        resid = sum(cy_reduce(u4, p)) % p
        ok &= is_one and resid == 4 % p
        print(f"  {p:>6} {b:>15} {str(is_one):>11} {resid:>9}")
    print("  -> u4 is a unit with residue exactly 4 (mod P) at every odd prime.")
    print("     `Frob_p == 4 (mod P)` therefore CANNOT establish non-unitness.\n")

    print("ALL EXACT CHECKS PASS" if ok else "A CHECK FAILED")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
