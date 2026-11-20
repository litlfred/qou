#!/usr/bin/env python3
"""
gs_tower_jet_degree_body_order_probe — the corpus identifies "n-body cluster
term" with "jet degree-n graded component". Measured on the filtration's own
graded dimension, that identification is consistent for A <= 3 and INCONSISTENT
from A = 4 upward, because the tower is taller than the nucleus is wide.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. This is the "full GS tower /
jet order, not just degree 0" step: every binding producer in the arc evaluates
the pairwise level; this one asks what the rest of the tower is indexed BY.

## The claim under test, and where it lives

`content/.../mass-theory/bond-order-eq-jet-degree-proof.md` (label
`lem:bond-order-eq-jet-degree`) states, as Step 1 of its proof, that the GS /
jet-prefix filtration "places the n-nucleon cluster sub-word at jet vertical
degree n", and concludes

    Sum_n (n-body term) = Sum_n gr_n .

Its Lean witness `QOU.Mass.bodyorder_eq_jet_total` is sorry-free and is a
legitimate conditional in the sense of AGENTS.md §3b-cond: the degree-wise match
`body_eq_graded : forall n, bodyTerm n = gradedTerm n` is a HYPOTHESIS FIELD of
the structure `BodyOrderJetGrading`, and the theorem composes it with
exhaustiveness `total_eq` to reindex the sum. It is not a self-assuming
projection -- it derives its conclusion from two separate hypotheses. But it
proves the reindexing, NOT the premise. Per AGENTS.md
§"Conditional-proved != premise-established", `body_eq_graded` is an assumption
the corpus carries, and this probe measures it.

## The measurement

The GS filtration here is the word-length (Coxeter-length) filtration, whose
associated-graded dimension for the A-strand layer is the Gaussian factorial

    W_A(q) = [A]_q!  =  prod_{k=1..A} [k]_q ,   [k]_q = 1 + q + ... + q^(k-1),

with `rho_grad(A) = [A]_q! / [2]_q!` the reference the corpus already subtracts
(`deltalambda_kappa_interface_residual_simplex_probe`, #4316/#4320). Its
coefficients are the Mahonian numbers `M(A, l) = #{w in S_A : len(w) = l}`.

Two facts about that polynomial decide the question, and both are exact:

  1. **Top degree = C(A,2).**  deg [A]_q! = sum_{k=1..A} (k-1) = C(A,2).
  2. **Every coefficient on 0..C(A,2) is strictly positive.**  Each factor
     [k]_q has all coefficients 1 on 0..k-1, and a product of polynomials with
     non-negative coefficients whose supports are full integer intervals
     starting at 0 has full support on 0..(sum of top degrees).

So the filtration has a NON-ZERO graded piece at every degree up to C(A,2). If
degree n really were body order n, a nucleus of A nucleons would carry non-zero
n-body clusters for n up to C(A,2). For A >= 4 that exceeds A -- at A = 4 the
tower runs to degree 6, i.e. "6-body clusters" among 4 nucleons.

C(A,2) > A exactly when A > 3. So the identification is consistent for A = 2, 3
(where C(A,2) <= A) and fails from A = 4 -- which is precisely the nucleus where
the arc's closures wall and where the residual simplex puts mu_4 = -4.591.

## What this does and does not say

Scope **(a)**, and deliberately narrow. What is refuted is the reading of the
degree index as a BODY-ORDER index, at A >= 4. What is NOT refuted:

  * The filtration itself. `[A]_q!` is the correct graded dimension and nothing
    here argues otherwise.
  * `bodyorder_eq_jet_total`. It remains true as stated -- it is conditional on
    `body_eq_graded`, and this probe measures that hypothesis, not the theorem.
  * The BOND-order reading. The block's own LaTeX label says *bond*-order, and
    C(A,2) is exactly the number of BONDS in the complete graph on A nucleons.
    Under `degree <-> bond count` the top degree is not an anomaly, it is the
    saturated pair set -- and that reading is consistent at every A. The block's
    label and its Lean declaration name (`bodyorder_...`) disagree with each
    other; the arithmetic here agrees with the LABEL.

That last point is the constructive half and it is not a rescue by relabelling:
`QOU.Mass.CoordinationSaturation` caps the exchange-determinant cumulant ratio
at `rho_A <= C(A,2)`, the SAME C(A,2), reached from the coordination side. The
jet tower's height and the saturation cap are the same number.

NO FLOAT64: exact integer/`sympy.Rational` coefficient arithmetic; evaluation at
the 50-digit proton pin in mpmath `mpf`. `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

A_MAX = 8
_q = sp.symbols("q")


def q_int(k: int):
    """[k]_q = 1 + q + ... + q^(k-1)."""
    return sum(_q**i for i in range(k))


def gaussian_factorial_coeffs(A: int) -> list[int]:
    """Mahonian coefficients of [A]_q!, index = jet degree, exact integers."""
    poly = sp.Poly(sp.expand(sp.prod([q_int(k) for k in range(1, A + 1)])), _q)
    # all_coeffs() is high-degree-first; reverse so index == degree.
    return [int(c) for c in poly.all_coeffs()[::-1]]


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0 = Q_MP

    print("gs_tower_jet_degree_body_order_probe")
    print("=" * 78)
    print(f"q0 (50-digit proton pin) = {fmt(q0, 20)}")
    print()
    print("THE TOWER.  W_A(q) = [A]_q! = sum_l M(A,l) q^l, M = Mahonian numbers.")
    print("Its degree index is what the corpus reads as body order.")
    print()
    print(f"{'A':>3} {'top deg':>8} {'C(A,2)':>7} {'match':>7} "
          f"{'degrees > A':>12} {'all coeffs > 0 on range':>24}")

    rows = []
    for A in range(2, A_MAX + 1):
        c = gaussian_factorial_coeffs(A)
        top = len(c) - 1
        cA2 = A * (A - 1) // 2
        excess = [l for l in range(len(c)) if l > A and c[l] != 0]
        full_support = all(v > 0 for v in c)
        rows.append((A, c, top, cA2, excess, full_support))
        print(f"{A:>3} {top:>8} {cA2:>7} {str(top == cA2):>7} "
              f"{str(len(excess)):>12} {str(full_support):>24}")

    # Gate 1 — the two exact structural facts the argument rests on.
    assert all(top == cA2 for _A, _c, top, cA2, _e, _f in rows), \
        "top degree of [A]_q! must equal C(A,2)"
    assert all(f for *_r, f in rows), \
        "[A]_q! must have strictly positive coefficients on its whole range"
    print()
    print("  Both structural facts hold on every A tested:")
    print("    deg [A]_q! = C(A,2)      (sum_{k=1..A} (k-1))")
    print("    every coefficient on 0..C(A,2) is strictly positive, so the")
    print("    filtration has a NON-ZERO graded piece at EVERY degree in range.")
    print()

    print("THE INCONSISTENCY.  C(A,2) > A exactly when A > 3.")
    print("-" * 78)
    print("  So reading degree n as body order n forces non-zero n-body clusters")
    print("  for n up to C(A,2) among only A nucleons.  Where that bites:")
    print()
    print(f"{'A':>3} {'nucleus':>8} {'body orders available':>22} "
          f"{'degrees the tower has':>22} {'impossible degrees':>19}")
    NAMES = {2: "D", 3: "T/3He", 4: "4He", 5: "5Li", 6: "6Li", 7: "7Li", 8: "8Be"}
    first_break = None
    for A, c, top, cA2, excess, _f in rows:
        imp = f"{A+1}..{cA2}" if cA2 > A else "none"
        if cA2 > A and first_break is None:
            first_break = A
        print(f"{A:>3} {NAMES.get(A, '?'):>8} {'2..' + str(A):>22} "
              f"{'0..' + str(cA2):>22} {imp:>19}")
    print()
    print(f"  First A at which the identification is inconsistent: A = {first_break}")
    assert first_break == 4, "expected the break to open at A=4"
    print("  That is 4He -- the nucleus at which this arc's closures wall, and")
    print("  where the residual simplex (#4320) puts mu_4 = -4.591.")
    print()

    # Gate 2 — how much WEIGHT sits in the impossible degrees, at the live pin.
    # A small weight would make the identification approximately harmless; a
    # large one makes it load-bearing. This is the part that needs the pin.
    print("HOW MUCH OF THE REFERENCE LIVES IN THE IMPOSSIBLE DEGREES")
    print("-" * 78)
    print("  rho_grad(A) = [A]_q!/[2]_q! is the reference the corpus SUBTRACTS")
    print("  before decomposing the residual into cluster orders.  Evaluated at")
    print("  q0, what fraction of it sits at degree > A?")
    print()
    print(f"{'A':>3} {'rho_grad(A)':>16} {'weight at deg<=A':>18} "
          f"{'weight at deg>A':>17} {'fraction > A':>14}")
    two_fac = mp.mpf(1) + q0                      # [2]_q! = [1][2] = 1+q
    fractions = {}
    for A, c, _top, _cA2, _e, _f in rows:
        terms = [mp.mpf(v) * q0**l for l, v in enumerate(c)]
        total = mp.fsum(terms) / two_fac
        lo = mp.fsum(terms[:A + 1]) / two_fac
        hi = mp.fsum(terms[A + 1:]) / two_fac if len(terms) > A + 1 else mp.mpf(0)
        frac = hi / total
        fractions[A] = frac
        print(f"{A:>3} {fmt(total, 10):>16} {fmt(lo, 10):>18} "
              f"{fmt(hi, 10):>17} {fmt(frac * 100, 6) + ' %':>14}")
    print()
    print(f"  At A=4 the impossible degrees already carry "
          f"{fmt(fractions[4] * 100, 5)} % of the reference;")
    print(f"  by A=8 they carry {fmt(fractions[8] * 100, 5)} %.  The mis-indexing is")
    print("  not a tail effect -- past A=5 it is most of the object.")
    assert fractions[4] > mp.mpf("0.05"), "A=4 excess weight should be non-trivial"
    assert fractions[8] > fractions[4], "excess fraction should grow with A"
    print()

    # Gate 3 — the constructive reading. C(A,2) is the complete-graph bond count.
    print("THE READING THAT SURVIVES — bonds, not bodies")
    print("-" * 78)
    print("  The block's own LaTeX label is `lem:bond-order-eq-jet-degree`; its")
    print("  Lean declaration is `bodyorder_eq_jet_total`.  The two disagree, and")
    print("  the arithmetic above agrees with the LABEL: C(A,2) is exactly the")
    print("  number of BONDS in the complete graph on A nucleons, so under")
    print("  `degree <-> bond count` the top degree is the saturated pair set and")
    print("  there is no impossible region at any A.")
    print()
    print(f"{'A':>3} {'top jet degree':>15} {'complete-graph bonds':>21} {'equal':>7}")
    for A, _c, top, cA2, _e, _f in rows:
        print(f"{A:>3} {top:>15} {cA2:>21} {str(top == cA2):>7}")
    print()
    print("  This is NOT a rescue by relabelling.  QOU.Mass.CoordinationSaturation")
    print("  caps the exchange-determinant cumulant ratio at rho_A <= C(A,2),")
    print("  reached from the coordination side with no reference to the jet")
    print("  filtration.  The tower's height and the saturation cap are the same")
    print("  number, arrived at twice.")
    print()

    print("WHAT THIS CHANGES")
    print("-" * 78)
    print("  * `body_eq_graded` in QOU.Mass.BodyOrderJetGrading is a hypothesis")
    print("    field, and at A >= 4 no instance of it can be built from the jet")
    print("    filtration's own graded dimension: bodyTerm n = 0 for n > A while")
    print("    gradedTerm n != 0 for A < n <= C(A,2).  The theorem stays true;")
    print("    what is measured is that its premise is unavailable past 3He.")
    print("  * The residual-simplex work (#4316/#4320) subtracts rho_grad as a")
    print("    monolithic reference and then decomposes the REMAINDER over the")
    print("    coordination counts C(A,k).  Both sides are indexed by the same")
    print("    C(A,2); whether the subtraction double-counts bond order is the")
    print("    next question, and this probe does not answer it.")
    print("  * Nothing is wired and no closure is proposed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
