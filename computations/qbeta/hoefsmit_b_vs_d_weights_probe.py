#!/usr/bin/env python3
"""hoefsmit_b_vs_d_weights_probe.py — what is Lean-provable about the N2..N5
Kashiwara/Hopf tails of the Q_β ladder under convention D (bean qou-cds1).

The categorical ladder's rungs N=2..5 are built entirely from the Hoefsmit
off-diagonal coupling `b = √(q⁴+q²+1)/(q²+1)` and `ℏ_q = (q−1)/q`
(`QBetaCategoricalPrecisionLadder.lean`; localised to those two blocks in
`LadderConventionLocalisation.lean`, PR #5364). This probe asks whether `b`
connects **provably** to the convention-D Wedderburn weights of `H₃(q)`, and
whether that connection is D-specific.

## Method (exact, symbolic over ℚ(q) — no float)

Solve the three H₃ Markov equations
  y₃ + 2y₂₁ + y₁₃ = 1
  q·y₃ + (q−q⁻¹)·y₂₁ − q⁻¹·y₁₃ = z
  q²·y₃ − y₂₁ + q⁻²·y₁₃ = z²
at z = z_D = q³/(q²+1) and at z = z_C = √q/(1+q), and compare to
b² = (q⁴+q²+1)/(q²+1)².

## Result (all exact)

- **D-frame:** the system forces y₁₃ = 0 (two-row Temperley–Lieb), with
  y₂₁ᴰ = q²/(q²+1)², y₃ᴰ = (q⁴+1)/(q²+1)², and
      **b² = 1 − y₂₁ᴰ = y₃ᴰ + y₂₁ᴰ**   (exact).
  So the Kashiwara coupling squared is the complement of the D standard-block
  weight. Formalised in Lean as `hoefsmitB_sq_eq_one_sub_stdWeightD`.
- **C-frame:** y₁₃ᶜ ≠ 0 (genuinely three-row; half-integer q-powers), and
  **b² ≠ 1 − y₂₁ᶜ**. The identity is D-specific.

## What is Lean-provable about N2..N5 (the honest map)

| object | status | why |
|---|---|---|
| `b² = 1 − y₂₁ᴰ` (Kashiwara coupling = complement of D standard weight) | **PROVABLE** | pure algebra + `Real.sq_sqrt` |
| `b²` identity FAILS in C | provable (structural) | C weights carry √q; identity is D-only |
| `N2_factor = 1 − b²ℏ⁴ = 1 − (bℏ²)²` (`c₂ = −1`) | **PROVABLE** | `ring` re-reading of the ansatz factor |
| `c₃ = −2 = J_Hopf(1)`, `c₄`, `c₅` values | **NOT** provable-as-forced | near-matches / fits (3.47 %, 0.91 %, …); only the *form* `J_Hopf·b^k` is structural |

Conclusion: the D-frame provability of N2..N5 lives in the **coupling** `b`
(`b² = 1 − y₂₁ᴰ`, D-specific) and the **c₂ Taylor form**; the higher-rung
*values* remain fitted, so the fence stands. No value wired; no tier change.

-- Ref: [manuscript] conj:dilogarithm-archimedean-limit (arc)
-- Ref: docs/audits/2026-08-21-cds1-d-frame-ladder-state-synthesis.md
"""
from __future__ import annotations

import sympy as sp


def main() -> int:
    q = sp.symbols("q", positive=True)
    qi = 1 / q
    y3, y21, y13, z = sp.symbols("y3 y21 y13 z")
    eqs = [
        sp.Eq(y3 + 2 * y21 + y13, 1),
        sp.Eq(q * y3 + (q - qi) * y21 + (-qi) * y13, z),
        sp.Eq(q**2 * y3 + (-1) * y21 + qi**2 * y13, z**2),
    ]
    b2 = (q**4 + q**2 + 1) / (q**2 + 1) ** 2

    def solve_at(zval):
        e = [x.subs(z, zval) for x in eqs]
        sol = sp.solve(e, [y3, y21, y13], dict=True)
        return sol[0]

    zD = q**3 / (q**2 + 1)
    zC = sp.sqrt(q) / (1 + q)

    wD = solve_at(zD)
    wC = solve_at(zC)

    checks = {
        "D_forces_y13_zero": sp.simplify(wD[y13]) == 0,
        "D_b2_eq_one_sub_y21": sp.simplify(b2 - (1 - wD[y21])) == 0,
        "D_b2_eq_y3_plus_y21": sp.simplify(b2 - (wD[y3] + wD[y21])) == 0,
        "D_y21_closed_form": sp.simplify(wD[y21] - q**2 / (q**2 + 1) ** 2) == 0,
        "C_is_three_row_y13_nonzero": sp.simplify(wC[y13]) != 0,
        "C_b2_ne_one_sub_y21": sp.simplify(b2 - (1 - wC[y21])) != 0,
        "zD_jones_pin": sp.simplify(zD * (q + qi) - q**2) == 0,
    }
    for k, v in checks.items():
        print(f"  {k:32s}: {'PASS' if v else 'FAIL'}")

    ok = all(checks.values())
    print(f"\nVERDICT: b² = 1 − y₂₁ᴰ (D-specific, provable); c₂ form provable; "
          f"c₃/c₄/c₅ values remain fitted. {'ALL PASS' if ok else 'FAILURE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
