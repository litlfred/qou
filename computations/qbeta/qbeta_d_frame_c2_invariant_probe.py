#!/usr/bin/env python3
"""The D-frame N=2 rung is forced — `b² = [3]_q/[2]_q²` (bean qou-cds1).

## What this answers

`qou-cds1` names its own next step:

    "state the invariant a forced D c₂ must satisfy (D analogue of
     c₂ = −1 = 1 − b²ℏ⁴) and check if exact weights + α_D − h²/4
     determine it. Do NOT run the extractor on z_D and report the output."

This is that step, done symbolically over exact ℚ(q). No extractor is run and
no number is fitted.

## Result

**The phase leg does not enter, and the weight leg determines the rung
completely.**

`Q_beta_categorical_ofPhase_tail_common` (Lean, already landed) localises every
`z`-dependence to the N=1 phase, so `α_D − h²/4` is irrelevant to `N2_factor`.
And the D weights force the coupling:

    y_(2,1)^D = 1/[2]_q²          (stdWeightD_eq_jones, proved)
    b²        = 1 − y_(2,1)^D     (hoefsmitB_sq_eq_one_sub_stdWeightD, proved)
    [2]_q² − [3]_q = 1            (this probe, assertion 1)
    ⇒ b²      = [3]_q/[2]_q²      (this probe, assertion 2)

So under D there is **no free parameter in the N=2 rung**: `b` is not an
independent Hoefsmit input but a function of the forced D weights. Under C the
corresponding statement is FALSE — `b² ≠ 1 − y_(2,1)^C` — so the coupling there
is genuinely separate data (assertion 4).

## Scope — this settles c₂ ONLY

It says nothing about c₃/c₄/c₅, whose values remain fitted near-matches, and it
closes NO part of the numerical gap: the 41.94×C residual recorded in the bean
is untouched. What it removes is the possibility that a D-frame c₂ could be
*chosen*. Scope-(a).

Lean: `QOU.BraidKnot.bracketTwo_sq_sub_bracketThree_eq_one`,
`hoefsmitB_sq_eq_bracketThree_div_bracketTwo_sq`, `N2_factor_eq_bracketRatio`
(sorry-free; axioms [propext, Classical.choice, Quot.sound]).
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

q = sp.symbols("q", positive=True)


def qbracket(n: int):
    """[n]_q = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}."""
    return sum(q ** (n - 1 - 2 * k) for k in range(n))


# Convention-D weights (S2, Lean-proved) and the Hoefsmit coupling.
Y21_D = q**2 / (q**2 + 1) ** 2
Y3_D = (q**4 + 1) / (q**2 + 1) ** 2
B_SQ = (q**4 + q**2 + 1) / (q**2 + 1) ** 2          # hoefsmitB q ^ 2
Z_C = sp.sqrt(q) / (q + 1)                           # excised convention C
Z_D = q**3 / (q**2 + 1)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # 1 — the quantum-integer identity behind the collapse
    id1 = sp.simplify(qbracket(2) ** 2 - qbracket(3) - 1)
    checks.append(("[2]_q^2 - [3]_q = 1", id1 == 0, f"residual {id1}"))

    # 2 — b^2 IS the quantum-integer ratio
    id2 = sp.simplify(B_SQ - qbracket(3) / qbracket(2) ** 2)
    checks.append(("b^2 = [3]_q/[2]_q^2", id2 == 0, f"residual {id2}"))

    # 3 — and it follows from the weights, not from the sqrt formula
    id3 = sp.simplify(B_SQ - (1 - Y21_D))
    checks.append(("b^2 = 1 - y_(2,1)^D", id3 == 0, f"residual {id3}"))

    # 4 — the SAME statement is FALSE in convention C: solve the C weights and
    #     show the coupling is not determined by them.
    #     C weights carry sqrt(q); y_(1^3)^C != 0, so b^2 != 1 - y_(2,1)^C.
    y3c, y21c, y13c = sp.symbols("y3c y21c y13c")
    solC = sp.solve(
        [sp.Eq(y3c + 2 * y21c + y13c, 1),
         sp.Eq(q * y3c + (q - 1 / q) * y21c - y13c / q, Z_C),
         sp.Eq(q**3 * y3c - y13c / q**3, (q - 1 / q) * Z_C**2 + Z_C)],
        [y3c, y21c, y13c], dict=True)
    if solC:
        y21C = sp.simplify(solC[0][y21c])
        y13C = sp.simplify(solC[0][y13c])
        differs = sp.simplify(B_SQ - (1 - y21C)) != 0
        checks.append(("C: b^2 != 1 - y_(2,1)^C (coupling is separate data)",
                       differs, f"y_(1^3)^C = {sp.nsimplify(y13C)}"))
        checks.append(("C: y_(1^3)^C != 0 (genuinely three-row)",
                       sp.simplify(y13C) != 0, ""))
    else:
        checks.append(("C weight solve", False, "no solution found"))

    # 5 — D normalisation, so the two-row trace is complete on its own support
    id5 = sp.simplify(Y3_D + 2 * Y21_D - 1)
    checks.append(("D: y_(3) + 2 y_(2,1) = 1 (y_(1^3) = 0)", id5 == 0,
                   f"residual {id5}"))

    print(__doc__.split("\n## Result")[0].strip())
    print()
    ok = 0
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))
        ok += passed
    print(f"\n{ok}/{len(checks)} exact-symbolic assertions")
    print("\nb^2 factored:", sp.factor(sp.simplify(B_SQ)))
    print("NOT closed: c_3/c_4/c_5 values stay fitted; the 41.94xC residual is untouched.")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
