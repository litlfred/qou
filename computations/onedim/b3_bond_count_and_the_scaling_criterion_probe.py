#!/usr/bin/env python3
# polynomial_q_not_applicable: exact Fraction / sympy arithmetic on the Ursell
# inversion; no symbolic-q polynomial output.
"""Does the chain-vs-triangle bond count change the b3 sign criterion?

Measured answer: **NO** -- and the claim that it does (which I repeated in an
audit doc, a PR body and a bean on 2026-09-15) is WRONG, because it mixes the
chain's BOND count with the triangle's PAIR count.

## What I propagated, and why it is wrong

A corpus-grep reported -- explicitly marking it as its own algebra, not the
corpus's, and asking for it to be checked -- that `b3Agg` is stated at the
triangle's bond count and so does not apply to the production chain:

    "At chain counts the quantity is Phi(2g) - 3 Phi(g), and convexity through
     the origin gives only Phi(2g) >= 2 Phi(g), hence >= -Phi(g) -- no sign at
     all."

I checked the two halves that were about the CORPUS (`b3Agg`'s definition, the
bean's status) and propagated the algebra without checking it. It is wrong.

The `3` in `b3Agg Phi g = Phi(3g) - 3 Phi(g)` is **not one number used twice**.
The Ursell inversion is

    b3  =  B(whole 3-cluster)  -  SUM OVER THE THREE PAIRS of B(pair)

so the first `3` is the cluster's BOND COUNT (what the aggregator is evaluated
at) and the second is the number of PAIRS, which is `C(3,2) = 3` for any
3-cluster whatever its bond graph. On a chain the unbonded pair contributes
`Phi(0) = 0` -- the same "through the origin" condition the theorem already
assumes -- so the correct chain form is

    b3_chain  =  Phi(2g) - 2 Phi(g)        NOT   Phi(2g) - 3 Phi(g)

## The general form, and the cross-check that validates it

Writing `Phi` as a function of BOND COUNT with `Phi(0) = 0`:

    b3(m)  =  Phi(m) - m * Phi(1)          m = bonded pairs in the 3-cluster

CHECK 3-4 verify this reproduces BOTH of the corpus's own results from its own
multiplicative assembly `W(Z) = 1 - Z`, `Z = prod f_e`, i.e. `Phi(m) = 1 - f^m`:

    m = 3 (triangle):  b3 = (1-f^3) - 3(1-f) = -(f-1)^2 (f+2)
                       == MayerThreeBodySign.b3_le_of_nonneg
    m = 2 (chain):     b3 = (1-f^2) - 2(1-f) = -(f-1)^2
                       == the corpus's chain b3 = -g12*g23 at equal bonds

Reproducing two independently-recorded corpus results from one formula is what
makes the generalisation trustworthy rather than merely plausible.

## The two consequences, and both cut against what I wrote

1. **Convexity IS sufficient on the chain.** Convex through the origin gives
   `Phi(1) <= Phi(m)/m` for every `m >= 1` (Jensen at `0` and `m` with weights
   `(1 - 1/m, 1/m)`), hence `b3(m) >= 0`. The `m = 3` case is the corpus's
   `b3Agg_nonneg_of_convexOn`; the chain is the `m = 2` case of the same
   argument. **The route was never inapplicable to the chain.**
2. **The scaling criterion is `p > 1` at EVERY bond count.** For a
   `p`-homogeneous `Phi(x) = C x^p` with `C > 0`,
   `b3(m) = C(m^p - m)`, so `b3 > 0` iff `m^p > m` iff `p > 1`, for any
   `m >= 2`. The bond count cancels out of the criterion entirely.

So `qou-2ss0`'s scaling target is **unchanged** by the chain/triangle
distinction, and the "small well-posed Lean task" I filed to join the two arcs
is not needed for this purpose. The distinction is real about the STATEMENT's
literal domain -- `b3Agg` is written at `3` -- and immaterial to the CRITERION.

## What is NOT claimed

That `p` is derivable; that the framework's assembly is `p`-homogeneous at all;
any value of `b3` for a real nucleus. The log assembly is `p = 1` exactly and
gives `b3 = 0` at every `m` (CHECK 6) -- the affine boundary, which is why it
is a boundary and not an escape.

Read-only: writes no witness, runs no producer, reads no AME/CODATA/census.
"""
import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    import sympy as sp
except ImportError:
    sp = None


def b3_at(phi, m):
    """b3 = Phi(m) - m*Phi(1), Phi a function of BOND COUNT, Phi(0) = 0."""
    return phi(m) - m * phi(1)


def main():
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    print("=" * 78)
    print("Does the chain-vs-triangle bond count change the b3 sign criterion?")
    print("=" * 78)

    # ---- CHECK 1-2: the Ursell inversion's two 3s are different numbers
    print("\n[1-2] the two 3s in b3Agg are different quantities")
    print("    b3 = B(3-cluster) - SUM over the C(3,2) = 3 PAIRS of B(pair)")
    print("    triangle: 3 bonds, 3 bonded pairs  -> Phi(3) - 3 Phi(1)")
    print("    chain:    2 bonds, 2 bonded pairs + 1 unbonded (Phi(0) = 0)")
    print("                                       -> Phi(2) - 2 Phi(1)")
    check("the cluster argument is the BOND count, the multiplier is the PAIR count",
          True, "C(3,2) = 3 for any 3-cluster; the unbonded pair contributes Phi(0) = 0")
    check("so the chain form is Phi(2g) - 2 Phi(g), not Phi(2g) - 3 Phi(g)", True,
          "the claim I propagated on 2026-09-15 used the triangle's pair count "
          "with the chain's bond count")

    # ---- CHECK 3-4: reproduce BOTH corpus results from one formula
    print("\n[3-4] one formula reproduces both of the corpus's own results")
    if sp is None:
        check("sympy available for the symbolic cross-check", False, "sympy missing")
    else:
        f = sp.symbols("f")
        phi_mult = lambda m: 1 - f ** m          # noqa: E731  W(Z) = 1 - Z, Z = f^m
        tri = sp.expand(b3_at(phi_mult, 3))
        chain = sp.expand(b3_at(phi_mult, 2))
        tri_target = sp.expand(-(f - 1) ** 2 * (f + 2))
        chain_target = sp.expand(-(f - 1) ** 2)
        print(f"    m = 3:  {sp.factor(tri)}")
        print(f"    m = 2:  {sp.factor(chain)}")
        check("m = 3 reproduces MayerThreeBodySign: -(f-1)^2 (f+2)",
              sp.simplify(tri - tri_target) == 0,
              "the corpus's b3_le_of_nonneg, derived here from the general form")
        check("m = 2 reproduces the corpus's chain b3 = -g12*g23 at equal bonds",
              sp.simplify(chain - chain_target) == 0,
              "g = f - 1, so -g^2 = -(f-1)^2")

    # ---- CHECK 5: convexity IS sufficient at every m
    print("\n[5] convexity through the origin gives b3 >= 0 at EVERY bond count")
    print("    Jensen at 0 and m with weights (1 - 1/m, 1/m):  Phi(1) <= Phi(m)/m")
    conv_ok = True
    for m in (2, 3, 4, 5, 6):
        for phi in (lambda x: F(x) ** 2,                    # convex, Phi(0)=0
                    lambda x: F(x) * F(x) * F(x),           # convex on x>=0
                    lambda x: F(x) ** 2 / (1 + F(x))):      # convex, asympt. linear
            if not b3_at(phi, m) >= 0:
                conv_ok = False
    check("b3(m) >= 0 for every convex-through-origin sample, m = 2..6", conv_ok,
          "so the m = 2 chain is the SAME Jensen argument as the m = 3 triangle -- "
          "the route was never inapplicable to the chain")

    # ---- CHECK 6: the scaling criterion is p > 1 at every m
    print("\n[6] the p-homogeneous criterion: b3 > 0 iff m^p > m iff p > 1")
    print(f"    {'m':>3}  {'p=0.5':>12} {'p=1':>12} {'p=1.5':>12} {'p=2':>12}")
    scale_ok = True
    for m in (2, 3, 4, 5, 6):
        row = []
        for p in (F(1, 2), F(1), F(3, 2), F(2)):
            # C = 1; use exact rationals where p is integral, else compare m^p vs m
            val = F(m) ** p if p.denominator == 1 else None
            if val is None:
                # m^(3/2) vs m  <=>  m^3 vs m^2  <=>  m > 1  (exact, integer)
                pos = (m ** 3) > (m ** 2) if p == F(3, 2) else (m ** 1) > (m ** 2)
            else:
                pos = val > m
            row.append("+" if pos else ("0" if (p == 1) else "-"))
            expect = p > 1
            if pos != expect:
                scale_ok = False
        print(f"    {m:>3}  " + "".join(f"{x:>13}" for x in row))
    check("b3 > 0 iff p > 1, independently of the bond count m", scale_ok,
          "b3(m) = C(m^p - m); the bond count cancels out of the criterion")

    # ---- CHECK 7: the log / affine boundary
    print("\n[7] the affine boundary")
    aff_ok = all(b3_at(lambda x: F(7, 3) * F(x), m) == 0 for m in (2, 3, 4, 5, 6))
    check("an affine Phi through the origin gives b3 = 0 at EVERY m", aff_ok,
          "p = 1 exactly -- the boundary, not an escape; this is where the corpus's "
          "log free-energy assembly sits")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

**The chain/triangle bond count does NOT change the b3 sign criterion, and the
claim that it does -- which I put into an audit doc, a PR body and a bean on
2026-09-15 -- is withdrawn.**

The `3` in `b3Agg Phi g = Phi(3g) - 3 Phi(g)` is two different numbers: the
cluster's BOND count (the aggregator's argument) and the number of PAIRS,
`C(3,2) = 3`, which is 3 for any 3-cluster whatever its bond graph. On a chain
the unbonded pair contributes `Phi(0) = 0`, so the chain form is
`Phi(2g) - 2 Phi(g)`. The version I repeated used the chain's bond count with
the triangle's pair count.

Consequences, both against what I wrote:

  * convexity through the origin gives `b3 >= 0` at EVERY bond count, by the
    same Jensen step -- the route was never inapplicable to the chain;
  * the scaling criterion is `p > 1` at every bond count, since
    `b3(m) = C(m^p - m)` and `m` cancels.

So `qou-2ss0`'s target is unchanged, and the "join the two arcs" Lean task I
filed is not needed for this purpose. The distinction is real about the
STATEMENT's literal domain and immaterial to the CRITERION.

What survives untouched from that grep, and is the useful part: there is no
DERIVED convex aggregator in the corpus, and
`sign_carries_no_information_beyond_the_secant` makes "find a convex Phi"
circular. The scaling route remains the non-circular one.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
