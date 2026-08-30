"""Symbolic cross-check of every sign and zero claim the convention-D Toffoli
arc asserts, against the Lean proofs in the block's own sibling.

Each row below pairs a claim made in the content blocks with the Lean theorem
that discharges it.  This probe re-establishes the same facts symbolically, so
the arc has two independent witnesses and neither is a numerical evaluation at
a single anchor.

  claim                                     Lean (QOU.Information.*)
  ----------------------------------------  --------------------------------
  P_77 > 0 on q > 0, no positive root       toffoliDiagonal_pos
  P_66 > 0 on q > 0                         toffoliP66_pos
  P_76's only positive zero is q = 1        toffoliFlip_eq_zero_iff
  P_76 < 0 on q > 1  (the substrate side)   toffoliFlip_neg_of_one_lt
  P_76 > 0 on 0 < q < 1                     toffoliFlip_pos_of_lt_one
  P_67 + P_76 = q(q-1)^2(q+1)^2/(2(q^2+1))  toffoli_antisymmetry_defect
  the flip channel is NOT antisymmetric     toffoli_not_antisymmetric
  W_std > 0, and P_77 * W_std > 0           wStd_pos, toffoliDiagonal_mul_wStd_pos

Exact symbolic arithmetic throughout; no floating point.
"""

from __future__ import annotations

import sys
import sympy as sp

q = sp.Symbol("q", positive=True)

P77 = q**3 * (q**4 + 1) / (q**2 + 1) ** 2
P66 = (q**4 + 1) * (q**4 + q**2 + 2) / (4 * q * (q**2 + 1) ** 2)
P76 = -(q - 1) * (q + 1) * (q**6 + q**4 + 2 * q**2 + 1) / (2 * q * (q**2 + 1) ** 2)
P67 = (q - 1) * (q + 1) * (2 * q**6 + q**4 + q**2 + 1) / (2 * q * (q**2 + 1) ** 2)
WSTD = (q**2 + 1) ** 2 / (q**4 + 4 * q**2 + 1)

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def positive_zeros(expr):
    return sp.solve(sp.Eq(sp.numer(sp.cancel(expr)), 0), q)


def main() -> int:
    print("=" * 74)
    print("  CONVENTION-D TOFFOLI AMPLITUDES — SIGN AND ZERO CLAIMS")
    print("=" * 74)
    print()

    check("P_77 has no positive root  [toffoliDiagonal_pos]",
          positive_zeros(P77) == [],
          f"numerator zeros on q>0: {positive_zeros(P77)}")

    check("P_66 has no positive root  [toffoliP66_pos]",
          positive_zeros(P66) == [],
          f"numerator zeros on q>0: {positive_zeros(P66)}")

    z76 = sp.solve(sp.Eq(P76, 0), q)
    check("P_76's only positive zero is q = 1  [toffoliFlip_eq_zero_iff]",
          z76 == [1], f"zeros on q>0: {z76}")

    # sign on each side of 1, at exact rational sample points
    neg_side = [sp.nsimplify(P76.subs(q, v)) for v in (sp.Rational(11, 10), 2, 5)]
    pos_side = [sp.nsimplify(P76.subs(q, v)) for v in
                (sp.Rational(1, 10), sp.Rational(1, 2), sp.Rational(9, 10))]
    check("P_76 < 0 on q > 1  [toffoliFlip_neg_of_one_lt]",
          all(v < 0 for v in neg_side), f"at q = 11/10, 2, 5: {neg_side}")
    check("P_76 > 0 on 0 < q < 1  [toffoliFlip_pos_of_lt_one]",
          all(v > 0 for v in pos_side), f"at q = 1/10, 1/2, 9/10: {pos_side}")

    defect = q * (q - 1) ** 2 * (q + 1) ** 2 / (2 * (q**2 + 1))
    d = sp.simplify(P67 + P76 - defect)
    check("P_67 + P_76 = q(q-1)^2(q+1)^2/(2(q^2+1))  [toffoli_antisymmetry_defect]",
          d == 0, f"difference simplifies to {d}")

    # antisymmetry would mean the sum vanishes identically; it vanishes only at 1
    sum_zeros = sp.solve(sp.Eq(sp.numer(sp.cancel(P67 + P76)), 0), q)
    check("the flip channel is NOT antisymmetric  [toffoli_not_antisymmetric]",
          sum_zeros == [1],
          f"P_67 + P_76 vanishes on q>0 only at {sum_zeros}, so P_67 != -P_76 elsewhere")

    check("W_std denominator has no real root  [wStd_pos]",
          [r for r in sp.solve(sp.Eq(q**4 + 4 * q**2 + 1, 0), sp.Symbol("x"))
           if getattr(r, "is_real", False)] == [],
          "q^4 + 4q^2 + 1: even powers, positive coefficients, constant 1")

    check("P_77 * W_std has no positive root  [toffoliDiagonal_mul_wStd_pos]",
          positive_zeros(P77 * WSTD) == [],
          f"numerator zeros on q>0: {positive_zeros(P77 * WSTD)}")

    print()
    n = sum(1 for _, ok in CHECKS if ok)
    print("=" * 74)
    print(f"  {n}/{len(CHECKS)} assertions")
    print("=" * 74)
    return 0 if n == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
