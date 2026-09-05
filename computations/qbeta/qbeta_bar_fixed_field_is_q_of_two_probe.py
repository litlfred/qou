#!/usr/bin/env python3
"""WHY parity cannot select the generator: the bar-fixed subfield is Q([2]_q).

Bean `qou-cds1`, tranche S1.  This upgrades the empirical finding of
`qbeta_d_gate_inventory_is_exhausted_probe.py` ("the parity gate admits every
symmetric q-integer") to a structural one, and gives the reason.

TWO RESULTS.

(1) A CORRECTION to PR #6282's own wording.  That PR said D's bar action is a
    multiplicative grading, `bar(x)/x = q^w`.  Measured, the ratio is `+/- q^w`
    -- there is a Z/2 sign as well as the Z weight -- and the sign is not a
    curiosity:

        q        +q^-2        b          +q^0
        h        -q^0    <--  z_D        +q^-4
        hbar_q   -q^1    <--  u          +q^2
        h^2      +q^0         Vhat_D     +q^-2
                              u*Vhat_D   +q^0

    `h`, the ladder's primary ingredient, is bar-ANTI-invariant of weight 0.
    Its square is invariant, which is why `u = b*hbar^2` comes out clean: the
    sign squares away.  The Z-grading statement is right about `u` and `Vhat_D`
    by accident of their even degree in `h`.

(2) THE REASON PARITY CANNOT SELECT.  Bar-invariance is exactly membership in
    the fixed field, and that field is Q(s) with s = q + 1/q = [2]_q:

      - bar(s) = s;
      - q satisfies q^2 - s*q + 1 = 0 over Q(s), so [Q(q) : Q(s)] = 2;
      - bar is a nontrivial Q(s)-automorphism of Q(q) (it exchanges the two
        roots q and 1/q of that quadratic);
      - so by Galois for a degree-2 extension, Fix(bar) = Q(s) EXACTLY.

    And every symmetric q-integer is a Chebyshev polynomial in s:

        [1] = 1        [2] = s          [3] = s^2 - 1     [4] = s^3 - 2s
        [5] = s^4 - 3s^2 + 1            [6] = s^5 - 4s^3 + 3s   ...

    so they all lie in Z[s] subset Q(s).  That is not a coincidence about the
    first few -- it is the recurrence U_k = s*U_{k-1} - U_{k-2}.

    CONSEQUENCE: "rho is bar-invariant" is the single condition "rho lies in an
    index-2 subfield".  An index-2 subfield of Q(q) is still an infinite-
    dimensional Q-vector space.  A condition that admits an entire function
    field cannot pick one element out of it -- no refinement of parity-type
    reasoning will, because there is nothing left to refine.

    The ladder's own ingredients sit there too: `h^2 = s^2 - 4` in Q(s), and
    `b = sqrt([3]_q)/[2]_q = sqrt(s^2-1)/s` in the quadratic extension
    Q(s)[sqrt(s^2-1)].

Exact sympy; no float64; emits no witness.
"""
import sys

import sympy as sp

q, s = sp.symbols("q s", positive=True)


def bar(e):
    return sp.simplify(e.subs(q, 1 / q))


def eigen(e):
    """Return (sign, w) with bar(e)/e == sign * q**w, or None if not homogeneous."""
    r = sp.simplify(bar(e) / e)
    for sg in (1, -1):
        for w in range(-8, 9):
            if sp.simplify(r - sg * q**w) == 0:
                return sg, w
    return None


def qint(n):
    return sp.simplify((q**n - q ** (-n)) / (q - 1 / q))


def cheby_U(k):
    """U_k(s) via U_0 = 1, U_1 = s, U_k = s*U_{k-1} - U_{k-2}."""
    U = [sp.Integer(1), s]
    for i in range(2, k + 1):
        U.append(sp.expand(s * U[i - 1] - U[i - 2]))
    return U[k]


def main() -> int:
    checks = []
    S = q + 1 / q                       # s = [2]_q

    h = q - 1 / q
    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    zD = q**3 / (q**2 + 1)
    u = b * hbar**2
    VD = sp.simplify(zD * h + 1)

    # --- (1) the sign is real, and h carries it ---------------------------
    ing = (("q", q), ("h", h), ("hbar_q", hbar), ("b", b), ("z_D", zD),
           ("u", u), ("Vhat_D", VD), ("u*Vhat_D", u * VD), ("h^2", h**2))
    print("bar eigenvalue of each ladder ingredient  (bar/orig = sign * q^w):\n")
    print(f"  {'ingredient':12} {'sign':>5} {'w':>4}")
    for name, e in ing:
        sg, w = eigen(e)
        print(f"  {name:12} {'+' if sg > 0 else '-':>5} {w:>4}")

    checks.append(("h is bar-ANTI-invariant of weight 0", eigen(h) == (-1, 0)))
    checks.append(("hbar_q carries the sign too", eigen(hbar) == (-1, 1)))
    checks.append(("but h^2 is bar-invariant", eigen(h**2) == (1, 0)))
    checks.append(("u is +q^2 (the sign squares away)", eigen(u) == (1, 2)))
    checks.append(("Vhat_D is +q^-2", eigen(VD) == (1, -2)))
    checks.append(("u*Vhat_D is bar-invariant", eigen(u * VD) == (1, 0)))

    # --- (2) the fixed field ----------------------------------------------
    checks.append(("s = q + 1/q is bar-invariant", sp.simplify(bar(S) - S) == 0))
    checks.append(("q is a root of x^2 - s x + 1 over Q(s), so [Q(q):Q(s)] = 2",
                   sp.simplify(q**2 - S * q + 1) == 0))
    checks.append(("1/q is the OTHER root -- bar exchanges them",
                   sp.simplify((1 / q) ** 2 - S * (1 / q) + 1) == 0))

    print("\nevery symmetric [n]_q is the Chebyshev polynomial U_{n-1}(s):\n")
    for n in range(1, 9):
        cand = cheby_U(n - 1)
        ok = sp.simplify(cand.subs(s, S) - qint(n)) == 0
        print(f"  [{n}]_q = {sp.expand(cand)}")
        checks.append((f"[{n}]_q = U_{n-1}([2]_q)", ok))

    checks.append(("h^2 = s^2 - 4 lies in Q(s)",
                   sp.simplify(h**2 - (S**2 - 4)) == 0))
    checks.append(("b = sqrt([3]_q)/[2]_q, in the quadratic ext Q(s)[sqrt(s^2-1)]",
                   sp.simplify(b - sp.sqrt(S**2 - 1) / S) == 0))

    print(f"\n  h^2 = s^2 - 4        (in Q(s))")
    print(f"  b   = sqrt(s^2-1)/s  = sqrt([3]_q)/[2]_q")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
FINDING

  Bar-invariance IS membership in Fix(bar) = Q(s), s = [2]_q -- an index-2
  subfield of Q(q), and still an infinite-dimensional Q-vector space.

  So the parity gate is not weak by accident.  It is the single condition
  "rho lies in an index-2 subfield", and every symmetric q-integer satisfies it
  because [n]_q = U_{n-1}(s) is a POLYNOMIAL in s.  That is the reason the
  filter admitted [2]_q ... [5]_q in #6282, and it will admit every further one.

  A condition whose solution set is an entire function field cannot select one
  element of that field.  No sharpening of parity-type reasoning can help --
  there is nothing left to sharpen.

  This is why the gate inventory being exhausted is a STRUCTURAL fact rather
  than a gap in the search: the three gates are all consequences of, or weaker
  than, membership in Q(s).

SCOPE.  (b)-style STRUCTURAL for the narrow claim -- Fix(bar) = Q(s) is a Galois
statement about a degree-2 extension, not a numerical observation, and the
Chebyshev identity is a recurrence, not a fit.  What is scope (a) is the
CONSEQUENCE for the ladder: it says parity cannot select the generator, NOT that
the generator is unselectable by any means.  An input that is not a parity
condition -- a degree bound, an anchor-independent functional equation, a
derivation from the H_4 Wenzl projector -- is untouched by this.

NEXT, and not done here: formalise Fix(bar) = Q(s) and the Chebyshev identity in
Lean.  The corpus already carries bar-invariance lemmas for individual
quantumInt values; the general statement is what is missing, and it is the
honest thing to prove rather than to keep testing candidates against.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
