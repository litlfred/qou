#!/usr/bin/env python3
"""Does INTEGRALITY escape the relative-interior exclusion? No — and the
reason is a Pisot bound, not a search.

WHY THE QUESTION IS LIVE, and it is a fair one.
`operator_selection_what_selects_b3.py` (S4, bean qou-v7qj) excludes every
linear objective from selecting B_3, by the face argument: a linear functional
attains its extrema on a FACE of a polyhedron, so a relative-interior minimiser
forces the functional constant. **That argument is about a CONVEX POLYHEDRON.**
An integer program's feasible set is a set of lattice points, which is not
convex, and the relevant object becomes the INTEGER HULL `conv(P ∩ L)` — whose
faces need not be faces of `P` at all. A point in the relative interior of `P`
really can be a vertex of `conv(P ∩ L)`, and then a linear objective selects it.

So "use an ILP" is not hand-waving. It is the one structural escape the S4
argument leaves open, and it has to be closed rather than waved away.

IT DOES NOT ESCAPE, in either reading of "the lattice", and the two readings
fail for opposite reasons.

READING 1 — the lattice is Z^6 (integer multiplicities of the six NF basis
operators). Then B_3 IS NOT FEASIBLE AT ALL: its NF coordinates are Z-Laurent
polynomials in q evaluated at q_0, and they are not integers ([A5] below
measures how far). An ILP over Z^6 cannot select a point outside its own
feasible set, so this reading does not merely fail to select B_3 — it excludes
it. That is a stronger negative than S4's and an easier one to check.

READING 2 — the lattice is Z[q_0, q_0^-1]^6, the ring the NF coordinates
actually live in. **That is not a lattice.** For real `q > 1`, the additive
group `Z[q]` is DISCRETE in R if and only if `q` is a Pisot number (classical;
the "only if" is the content). By Siegel (1944) the smallest Pisot number is
the plastic number `theta = 1.3247179572...`, the real root of `x^3 - x - 1`.
The substrate pin is `q_0 = 1.1099785828 < theta`, so `q_0` is not Pisot,
`Z[q_0]` is not discrete, and a non-discrete subgroup of R is dense. Hence
`Z[q_0, q_0^-1] ⊇ Z[q_0]` is DENSE in R and the "lattice" is dense in R^6.

A dense feasible subset has the same closed convex hull as `P`, so the integer
hull adds no faces: the S4 face argument applies verbatim and the exclusion
transfers. [A6] makes this constructive rather than asymptotic — it exhibits an
actual feasible LATTICE point with strictly lower objective than B_3.

THE PISOT TEST IS EXACT AND NEEDS NO DECIMAL EXPANSION OF theta. `x^3 - x - 1`
has positive derivative `3x^2 - 1` on `(1, ∞)`, so it is increasing there and
`q_0 < theta` is EXACTLY equivalent to `q_0^3 - q_0 - 1 < 0` — one rational
comparison. That is [A1], and it is why this file makes no floating-point claim
about theta.

AND THE ARGUMENT IS UNCONDITIONAL — it does NOT rest on q_0 being irrational,
which this corpus cannot prove (q_0 is pinned through `Vol(4_1) = 2 Cl_2(pi/3)`,
whose irrationality is open). All three cases give density:

  * `q_0` rational, not an integer: write `q_0 = p/r` in lowest terms, `r >= 2`.
    Bezout gives `a*p + b*r = 1`, so `a*q_0 + b = 1/r` and `a + b*q_0^-1 = 1/p`
    are BOTH in the ring, i.e. `Z[q_0, q_0^-1] = Z[1/(p*r)]`, which is dense.
    [A3] exhibits both explicitly — and since every consumer in this corpus
    evaluates at the 50-digit DECIMAL q_0, this is the case that literally
    applies to the compute, not a hypothetical.

    ⚠ The ring is `Z[1/(p*r)]`, NOT `Z[1/r]`, because `q_0^-1 = r/p` puts
    powers of `p` in denominators. This file's first run tested membership
    against `Z[1/r]` and reported a FALSE NEGATIVE at [A6] on a point that was
    plainly in the ring — B_3's own coordinates have denominators of 192 to 479
    digits for exactly this reason.
  * `q_0` irrational algebraic: not Pisot by [A1], so `Z[q_0]` is not discrete.
  * `q_0` transcendental: `Z[q_0]` is not discrete either (discreteness of
    `Z[q]` forces `q` algebraic).

Only `q_0 ∈ Z` would be discrete, and `1 < q_0 < 2` rules that out ([A2]).

SCOPE — (b), a structural exclusion, with the invariant cited: the Pisot bound
for reading 2, and non-membership for reading 1. It says an ILP over either
lattice cannot select B_3 by a linear objective. It says NOTHING about
non-linear selection principles (S4 already refuted two of those separately),
and nothing about whether some other element is selectable.

Arithmetic is EXACT: sympy over Q with q_0 the exact 50-digit rational, and
Python ints for the Bezout. `float` appears only inside f-strings for display.

Emits no witness: a decision probe whose output is an argument (bean qou-pb1w).

Beans qou-99qc (the selection question), qou-v7qj (S4, the exclusion this
extends).

-- Ref: [manuscript] computations/meson/operator_selection_what_selects_b3.py
-- Ref: [manuscript] docs/audits/2026-08-24-operator-selection-lp-objective-defect.md
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parents[2]
for _p in (_REPO / "computations", _REPO / "computations" / "meson",
           _REPO / "tools" / "qou-substrate" / "python"):
    sys.path.insert(0, str(_p))

from operator_selection_lattice_symbolic import (  # noqa: E402
    NF_BASIS, q, structure_constants, derive_trace, build_gram, _reduce_nf,
)
from operator_selection_what_selects_b3 import rmul  # noqa: E402

FAILURES: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    print(f"   [{tag}] {'PASS' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILURES.append(tag)


def main() -> int:
    from qou_substrate.constants import Q_50_DIGIT_STR

    q0 = sp.Rational(Q_50_DIGIT_STR)          # EXACT, the value all compute uses

    print("=" * 74)
    print("[A1] q_0 IS BELOW THE SMALLEST PISOT NUMBER -- so it is not Pisot")
    print("=" * 74)
    # x^3 - x - 1 is increasing on (1, oo) since 3x^2 - 1 > 0 there, so
    # q_0 < theta  <=>  q_0^3 - q_0 - 1 < 0.  One exact rational comparison.
    pisot_val = q0 ** 3 - q0 - 1
    print(f"   q_0                 = {sp.N(q0, 30)}")
    print(f"   q_0^3 - q_0 - 1     = {sp.N(pisot_val, 30)}")
    print("   theta (plastic no.) = 1.32471795724474602596...  (root of x^3-x-1)")
    print("   x^3-x-1 is increasing on (1,oo) (3x^2-1>0), so the sign IS the test.")
    check("A1", pisot_val < 0,
          f"q_0 < theta, so q_0 is NOT a Pisot number (margin {sp.N(-pisot_val, 8)})")

    print()
    print("=" * 74)
    print("[A2] q_0 IS NOT A RATIONAL INTEGER -- the one discrete case is out")
    print("=" * 74)
    check("A2", 1 < q0 < 2 and q0 != 1,
          "1 < q_0 < 2, so q_0 is not in Z (Z[n] = Z[1/n] is dense for n >= 2 anyway)")

    print()
    print("=" * 74)
    print("[A3] THE CONSTRUCTIVE DENSITY WITNESS, exact in Python ints")
    print("=" * 74)
    fr = Fraction(int(sp.numer(q0)), int(sp.denom(q0)))
    p_num, r_den = fr.numerator, fr.denominator
    print(f"   q_0 = p/r in lowest terms, r has {len(str(r_den))} digits")
    gg, aa, bb = _ext_gcd(p_num, r_den)
    check("A3a", gg == 1, f"gcd(p, r) = {gg}")
    # a*p + b*r = 1  =>  a*q_0 + b = a*p/r + b = (a*p + b*r)/r = 1/r
    lattice_elt = sp.Rational(aa) * q0 + sp.Rational(bb)
    check("A3b", lattice_elt == sp.Rational(1, r_den),
          f"a*q_0 + b = 1/r exactly, an element of Z + Z*q_0 of size {sp.N(lattice_elt, 6)}")
    # Dividing the same Bezout relation by p instead: a + b*(r/p) = 1/p, and
    # r/p IS q_0^-1, so 1/p is in the ring too. Hence the ring is Z[1/(p*r)] --
    # NOT Z[1/r]. That distinction is not pedantry: B_3's own coordinates carry
    # powers of p in their denominators (q_0^-1 = r/p), so a membership test
    # against Z[1/r] alone REJECTS points that are plainly in the ring. This
    # file's first run did exactly that and reported a false negative at [A6].
    lattice_elt_p = sp.Rational(aa) + sp.Rational(bb) * (1 / q0)
    check("A3c", lattice_elt_p == sp.Rational(1, p_num),
          f"a + b*q_0^-1 = 1/p exactly, so the ring is Z[1/(p*r)], not Z[1/r]")
    print("   so Z[q_0, q_0^-1] = Z[1/(p*r)], whose spacing is 1/(p*r) -- dense.")

    print()
    print("=" * 74)
    print("[A4] WHERE B_3 SITS -- re-measured, not quoted from S4")
    print("=" * 74)
    C = structure_constants()
    t = derive_trace(C)
    G = build_gram(C, t)
    Gn = G.subs(q, q0)
    tn = sp.Matrix([e.subs(q, q0) for e in t])

    y = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for _ in range(3):                        # B_3 = (sigma_0 sigma_1^-1)^3
        y = rmul(y, 0)
        y = rmul(y, 1, inv=True)
    B3 = sp.Matrix([sp.nsimplify(e.subs(q, q0)) for e in y])
    n_target = sum(B3)
    gx = [sp.together(sp.expand((Gn * B3)[i])) for i in range(6)]
    active = sum(1 for g in gx if g == 0)
    min_slack = min(gx)
    for i, g in enumerate(gx):
        print(f"   (G x)_{i} = {float(g):+.9f}")
    check("A4", active == 0 and min_slack > 0,
          f"0 of 6 Frobenius constraints active, min slack {float(min_slack):+.9f} "
          f"> 0 -- B_3 is relative-interior, exactly as S4 reports")

    print()
    print("=" * 74)
    print("[A5] READING 1 -- over Z^6, B_3 IS NOT EVEN FEASIBLE")
    print("=" * 74)
    worst_name, worst_dist = None, sp.Integer(0)
    for i, name in enumerate(["gamma", "s0", "s1", "L+", "L-", "e-"]):
        c = B3[i]
        d = min(c - sp.floor(c), sp.ceiling(c) - c)
        print(f"   x_{name:<6s} = {float(c):+.12f}   distance to Z = {float(d):.12f}")
        if d > worst_dist:
            worst_name, worst_dist = name, d
    check("A5", worst_dist > 0,
          f"B_3 has a non-integer coordinate (worst: {worst_name}, "
          f"{float(worst_dist):.6f} from Z), so it is OUTSIDE the Z^6 feasible set")

    print()
    print("=" * 74)
    print("[A6] READING 2 -- a feasible LATTICE point beating B_3, constructed")
    print("=" * 74)
    # S4's descent direction: -t projected onto {sum d = 0}, so the step stays
    # on the equality hyperplane and lowers the objective t.x.
    one = sp.Matrix([1] * 6)
    d = -(tn - (tn.dot(one) / 6) * one)
    step = sp.Rational(1, 2)
    x_cont = B3 + step * d

    # Snap into (1/r)Z^6 ⊆ Z[1/r]^6 ⊆ Z[q_0, q_0^-1]^6. This is a LATTICE point
    # by construction -- no tolerance decides membership. The last coordinate
    # absorbs the rounding residue so `sum x` is preserved EXACTLY; n_target is
    # itself in the lattice (a Z-Laurent polynomial in q_0 = p/r).
    snapped = [sp.Rational(round(x_cont[i] * r_den), r_den) for i in range(5)]
    snapped.append(n_target - sum(snapped))
    x_lat = sp.Matrix(snapped)

    # Membership in Z[1/(p*r)] is "every prime factor of the denominator divides
    # p*r", NOT "p*r times it is an integer" -- B_3's coordinates are Z-Laurent
    # polynomials in q_0 = p/r, so their denominators are products of powers of
    # p and r (measured: 192 to 479 digits), and the narrower test rejects a
    # point that is plainly in the ring. Decided by stripping common factors:
    # exact, and no 48-digit factorisation is needed.
    in_lattice = all(_in_z_one_over(sp.denom(x_lat[i]), p_num * r_den)
                     for i in range(6))
    sum_ok = (sum(x_lat) == n_target)
    g_lat = [sp.together(sp.expand((Gn * x_lat)[i])) for i in range(6)]
    feasible = min(g_lat) >= 0
    obj_b3, obj_lat = tn.dot(B3), tn.dot(x_lat)

    print(f"   lattice point in Z[1/(p*r)]^6  : {in_lattice}")
    print(f"   sum x preserved EXACTLY        : {sum_ok}")
    print(f"   feasible (min slack)           : {feasible}  ({float(min(g_lat)):+.9f})")
    print(f"   objective t.x at B_3           : {float(obj_b3):+.12f}")
    print(f"   objective t.x at lattice point : {float(obj_lat):+.12f}")
    print(f"   improvement                    : {float(obj_b3 - obj_lat):+.12f}")
    check("A6", in_lattice and sum_ok and feasible and obj_lat < obj_b3,
          "a feasible Z[q_0,q_0^-1]-lattice point has STRICTLY lower objective "
          "than B_3 -- so B_3 is not the ILP optimum either")

    print()
    print("=" * 74)
    print("VERDICT" if not FAILURES else "VERDICT -- NOT ESTABLISHED, see failures")
    print("=" * 74)
    if FAILURES:
        print("   An assertion above failed, so the argument below is NOT")
        print("   established by this run. Read the failure, not the verdict.")
        print()
    print("   Integrality does NOT escape the S4 relative-interior exclusion.")
    print()
    print("   * over Z^6   : B_3 is not in the feasible set at all      [A5]")
    print("   * over Z[q_0,q_0^-1]^6 : that ring is DENSE in R, because")
    print("       q_0 < theta_plastic so q_0 is not Pisot [A1], q_0 is not")
    print("       an integer [A2], and it EQUALS Z[1/(p*r)] explicitly [A3].")
    print("       A dense feasible subset has the same closed convex hull, so")
    print("       the integer hull adds no faces and the face argument stands.")
    print("       Exhibited concretely: a feasible lattice point that beats")
    print("       B_3 on the objective                                  [A6]")
    print()
    print("   SCOPE (b) -- structural, invariant cited (the Pisot bound). It")
    print("   excludes LINEAR objectives over these lattices. It says nothing")
    print("   about non-linear principles, and nothing about other elements.")

    print()
    if FAILURES:
        print(f"FAILED: {', '.join(FAILURES)}")
        return 1
    print("All assertions passed.")
    return 0


def _in_z_one_over(den, r: int) -> bool:
    """Is a rational with denominator `den` an element of `Z[1/r]`?

    Exactly when every prime factor of `den` divides `r`. Decided by repeatedly
    stripping `gcd(den, r)` — exact integer arithmetic, and no factorisation of
    a 48-digit number is needed.
    """
    d = int(den)
    while True:
        g = math.gcd(d, r)
        if g == 1:
            return d == 1
        while d % g == 0:
            d //= g


def _ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclid on Python ints -- returns (g, x, y) with a*x + b*y = g."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quo = old_r // r
        old_r, r = r, old_r - quo * r
        old_s, s = s, old_s - quo * s
        old_t, t = t, old_t - quo * t
    return old_r, old_s, old_t


if __name__ == "__main__":
    raise SystemExit(main())
