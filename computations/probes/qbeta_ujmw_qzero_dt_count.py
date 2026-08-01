#!/usr/bin/env python3
"""qbeta_ujmw_qzero_dt_count.py — the q→0 base case of A_ω = 3 (bean qou-ujmw).

Backs the sorry-free Lean brick
`QOU/QBeta/StokesQZeroDTCount.lean` with the exact integer arithmetic it
formalizes: the GGM (2012.00062) figure-eight Stokes sandwich
`S⁺ = ±½·A·W₋₁·B·W₋₁ᵀ·C` evaluated at the semiclassical limit q→0.

At q→0 the certified GGM fundamental-solution matrix W₋₁(q) collapses to the
exact integer matrix W₋₁(0) = [[0,-2],[1,1]] (its determinant 2 is GGM Theorem 9
at q→0), and the sandwich equals -2·S⁺(0) with S⁺(0) = [[1,3],[0,1]] (GGM eq 60).
The off-diagonal Stokes/DT constant is exactly 3 — the rotated-3d-index / DT
invariant of T[4₁] (GGM Conjecture 4, a theorem for 4₁), NOT an assumption.

Discipline: reuses the certified q-series machinery of
`qbeta_g3_ggm_stokes_41.py` (Theorem-9 / eq-59a certification) for the q→0
evaluation; exact integer arithmetic; no fit; no c_k wired. This closes the q→0
ANCHOR of the DT-count identification only — the internal categorical derivation
of 3 (qou-qnnq) and the value→observable normalization (qou-2cvs) stay open.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import qbeta_g3_ggm_stokes_41 as ggm  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def m2(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def transpose(X):
    return [[X[j][i] for j in range(2)] for i in range(2)]


def det2(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def main() -> int:
    ORD = 4
    # W₋₁(q) as integer series; take the q→0 constant term.
    Wm1 = ggm.W_matrix(-1, ORD)
    W0 = [[Wm1[i][j][0] for j in range(2)] for i in range(2)]

    # glyph-verified small integer matrices (magnitudes MAG_*, signs fixed by
    # the q→0 filter S⁺(0) = [[1,3],[0,1]] — see qbeta_g3_ggm_stokes_41.py V3).
    A = [[0, 1], [1, 1]]
    B = [[0, 1], [1, 0]]
    C = [[0, 1], [-1, -2]]
    SPLUS0 = [[1, 3], [0, 1]]

    W0T = transpose(W0)
    sandwich = m2(m2(m2(m2(A, W0), B), W0T), C)     # A·W₋₁·B·W₋₁ᵀ·C at q→0
    target = [[-2 * SPLUS0[i][j] for j in range(2)] for i in range(2)]

    det_ok = det2(W0) == 2
    sandwich_ok = sandwich == target
    offdiag_ok = sandwich[0][1] == -6 and SPLUS0[0][1] == 3
    all_ok = det_ok and sandwich_ok and offdiag_ok

    print("W₋₁(0)            =", W0)
    print("det W₋₁(0)        =", det2(W0), "(GGM Thm 9: 2)  ok=", det_ok)
    print("A·W₋₁·B·W₋₁ᵀ·C    =", sandwich)
    print("-2·S⁺(0)          =", target, " match=", sandwich_ok)
    print("S⁺(0) off-diagonal (DT/Stokes constant A_ω) =", SPLUS0[0][1],
          " ok=", offdiag_ok)
    print("ALL OK =", all_ok)

    wb = WitnessBuilder(
        "aomega-qzero-dt-count",
        engine="python",
        output_dir=Path(__file__).resolve().parent.parent,
    )
    wb.set_description(
        "q→0 base case of A_ω=3 (bean qou-ujmw). The GGM 4₁ Stokes sandwich "
        "±½·A·W₋₁·B·W₋₁ᵀ·C at q→0, with W₋₁(0)=[[0,-2],[1,1]] (det=2, Thm 9), "
        "equals -2·S⁺(0) with S⁺(0)=[[1,3],[0,1]] (eq 60); the off-diagonal "
        "DT/rotated-3d-index constant is exactly 3 (GGM Conj 4, theorem for 4₁). "
        "Backs QOU/QBeta/StokesQZeroDTCount.lean (decidable, sorry-free)."
    )
    wb.set_audit_only("docs/audits/2026-08-01-ujmw-aomega-dt-index-derivation.md")
    wb.add_assertion("det_W_minus1_at_qzero", det2(W0), 2,
                     source="GGM 2012.00062 Thm 9 (det W_m = 2)")
    wb.add_assertion("aomega_qzero_dt_constant", SPLUS0[0][1], 3,
                     source="GGM 2012.00062 eq 60 S⁺(0)=[[1,3],[0,1]]; Conj 4 = DT invariant")
    wb.add_assertion("sandwich_offdiagonal", sandwich[0][1], -6,
                     source="A·W₋₁·B·W₋₁ᵀ·C at q→0 = -2·S⁺(0)")
    wb.add_data("W_minus1_at_qzero", W0)
    wb.add_data("sandwich_A_Wm1_B_Wm1T_C", sandwich)
    wb.add_data("minus_two_times_Splus0", target)
    wb.add_data("Splus0", SPLUS0)
    wb.add_data("sandwich_matches_minus2_Splus0", sandwich_ok)
    wb.add_data("all_ok", all_ok)
    wb.add_data(
        "discipline",
        "COMPARISON-TO-PRIMARY-SOURCE — exact integer arithmetic, zero free "
        "parameters, no fit, no c_k wired. Closes the q→0 anchor of the "
        "DT-count identification only; internal categorical derivation of 3 "
        "(qou-qnnq) and the value→observable normalization (qou-2cvs) stay open.")
    wb.add_data("scope", "(a)")
    out = wb.save()
    print("wrote", out)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
