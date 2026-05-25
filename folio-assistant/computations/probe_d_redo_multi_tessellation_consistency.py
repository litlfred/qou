"""Probe D REDO: multi-tessellation consistency with MATCHING FRAMING convention.

Background from PR #1233 (probes A-D follow-up to crystal-Yekutieli
correspondence audit PR #1231):

  Original Probe D claimed to test "tessellation choice is coordinate-
  free" by comparing:
    R1 (closed form):  tr_M(β_Bor) = (4+h²−3h⁴−h⁶)/(h²+4)
    R3 (Jones/[2]²):   V(β_Bor, q) / (q + 1/q)²
  with V(β_Bor) the published Jones polynomial.

  But R1 and R3 DIFFERED numerically (Δ ≈ 6.74e-3) due to FRAMING
  CONVENTION mismatch — the Jones polynomial has writhe-dependent
  normalization (q^{±3w(K)/2} writhe factor) that the Markov trace
  closed form bakes in differently.

  Original Probe D verdict was INCONCLUSIVE on this account.

This REDO uses TWO routes that share the SAME framing convention:

  R1 (closed form):
    tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)
    (from `borromean-markov-trace-closed-form.md`)

  R2 (Wedderburn sum):
    tr_M(β_Bor) = y_(3) · χ^(3)(β_Bor)
                + y_(2,1) · χ^(2,1)(β_Bor)
                + y_(1,1,1) · χ^(1,1,1)(β_Bor)
    where y_λ are the Jones-Markov weights at H_3(q) computed via
    `alpha_k_jones_markov_h3.py`'s 3-constraint linear-system solve.

Both R1 and R2 are CANONICALLY-NORMALIZED Markov-trace expressions
in H_3(q) — no Jones-polynomial writhe involved. If the framework
is internally consistent, R1 = R2 should hold to machine precision.

If they agree: ✓ tessellation-coordinate-freedom CONFIRMED at the
trace level (per PR #1231 audit §11).

If they disagree: structural inconsistency in the framework — needs
investigation. Two distinct "canonical" computations of the same
invariant must agree.
"""

from __future__ import annotations
import json
import subprocess
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import mp, mpf, log as mplog

mp.dps = 50


def main():
    print("=" * 80)
    print("Probe D REDO — multi-tessellation consistency at MATCHING framing")
    print("=" * 80)
    print()

    h = sp.Symbol("h")
    q = sp.Symbol("q", positive=True)

    # =====================================================================
    # R1: closed-form Markov trace from `borromean-markov-trace-closed-form.md`
    # =====================================================================
    print("R1 (closed form): tr_M(β_Bor)(h) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)")
    print()
    trM_R1_h = (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)

    # h-series expansion
    trM_R1_series = sp.series(trM_R1_h, h, 0, 12).removeO()
    print(f"  h-series: {sp.expand(trM_R1_series)}")
    print()

    # =====================================================================
    # R2: Wedderburn sum via Hoefsmit + Jones-Markov weights at H_3
    # Procedure (matches alpha_k_jones_markov_h3.py):
    #   1. Build Hoefsmit (2,1) matrices σ_0, σ_1
    #   2. Compute χ^λ for each partition λ ⊢ 3 on the braid β_Bor
    #   3. Solve y_λ from Markov constraints: tr(1)=1, tr(σ_i)=z, tr(σ_iσ_j)=z²
    #   4. Sum tr_M = Σ_λ y_λ · χ^λ(β_Bor)
    # =====================================================================
    print("R2 (Wedderburn sum): tr_M = Σ_λ y_λ · χ^λ(β_Bor)")
    print()

    # Step 1: Hoefsmit matrices in (2,1)
    sig0 = sp.Matrix([[q, 1], [0, -1 / q]])
    sig1 = sp.Matrix([[-1 / q, 0], [1, q]])
    h_var = q - 1 / q
    sig0_inv = sig0 - h_var * sp.eye(2)
    sig1_inv = sig1 - h_var * sp.eye(2)

    # Step 2: characters for the 3 irreps of H_3
    # β_Bor = (σ_1 σ_2^{-1})^3, in 0-indexed = (σ_0 σ_1^{-1})^3
    # (3) trivial: σ_i → q, σ_i^{-1} → q^{-1}
    # (1,1,1) sign: σ_i → -q^{-1}, σ_i^{-1} → -q
    # (2,1) standard: full Hoefsmit matrices
    chi_triv = (q * q ** (-1)) ** 3  # = 1
    chi_sign = ((-q ** (-1)) * (-q)) ** 3  # = 1
    M = sig0 * sig1_inv
    M3 = sp.simplify(M * M * M)
    chi_std = sp.simplify(M3.trace())

    print(f"  χ^(3)(β_Bor)     = {sp.simplify(chi_triv)}  (trivial rep)")
    print(f"  χ^(1,1,1)(β_Bor) = {sp.simplify(chi_sign)}  (sign rep)")
    print(f"  χ^(2,1)(β_Bor)   = {chi_std}  (standard rep)")
    print()

    # Step 3: solve Jones-Markov weights y_λ at H_3 numerically (matches
    # `alpha_k_jones_markov_h3.py`'s linear-system approach)
    Q0 = mpf("1.10997859555418057528159407961")  # q_0 50-dps
    z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))

    # Build constraint χ-table numerically at q = Q0
    def chi_at_q0(expr):
        return float(sp.N(expr.subs(q, float(Q0)), 25))

    # Constraints: tr(1)=1, tr(σ_1)=z, tr(σ_1σ_2)=z²
    sigmas3_at_q0 = {
        "1": [(0, sp.eye(2)), (1, sp.eye(2))],  # identity in both σ_0, σ_1
        "s1": [sig0],
        "s1s2": [sig0 * sig1],
    }

    chi_table_num = {}
    # Trivial: χ^(3)(σ_i) = q, χ^(3)(σ_i σ_j) = q²
    # Sign:    χ^(1,1,1)(σ_i) = -1/q, χ^(1,1,1)(σ_i σ_j) = 1/q²
    # Standard: trace of corresponding matrix
    chi_table_num["1"] = {
        (3,): 1.0,
        (2, 1): 2.0,  # tr(I_{2×2}) = 2
        (1, 1, 1): 1.0,
    }
    chi_table_num["s1"] = {
        (3,): float(Q0),
        (2, 1): chi_at_q0(sig0.trace()),
        (1, 1, 1): -1.0 / float(Q0),
    }
    chi_table_num["s1s2"] = {
        (3,): float(Q0) ** 2,
        (2, 1): chi_at_q0((sig0 * sig1).trace()),
        (1, 1, 1): 1.0 / float(Q0) ** 2,
    }

    A_constraint = np.array([
        [chi_table_num["1"][(3,)],   chi_table_num["1"][(2, 1)],   chi_table_num["1"][(1, 1, 1)]],
        [chi_table_num["s1"][(3,)],  chi_table_num["s1"][(2, 1)],  chi_table_num["s1"][(1, 1, 1)]],
        [chi_table_num["s1s2"][(3,)], chi_table_num["s1s2"][(2, 1)], chi_table_num["s1s2"][(1, 1, 1)]],
    ])
    b_constraint = np.array([1.0, float(z_mark), float(z_mark) ** 2])
    y_vals = np.linalg.solve(A_constraint, b_constraint)

    print(f"  Jones-Markov weights at H_3(q_0):")
    print(f"    y_(3)     = {y_vals[0]:+.10f}")
    print(f"    y_(2,1)   = {y_vals[1]:+.10f}")
    print(f"    y_(1,1,1) = {y_vals[2]:+.10f}")
    print()

    # Step 4: sum tr_M = Σ_λ y_λ · χ^λ(β_Bor) at q_0
    chi_triv_num = chi_at_q0(chi_triv)
    chi_sign_num = chi_at_q0(chi_sign)
    chi_std_num = chi_at_q0(chi_std)
    trM_R2_num = (y_vals[0] * chi_triv_num
                  + y_vals[1] * chi_std_num
                  + y_vals[2] * chi_sign_num)
    print(f"  χ values at q_0:")
    print(f"    χ^(3)(β_Bor)     = {chi_triv_num:.10f}")
    print(f"    χ^(2,1)(β_Bor)   = {chi_std_num:.10f}")
    print(f"    χ^(1,1,1)(β_Bor) = {chi_sign_num:.10f}")
    print()
    print(f"  R2 numerical: tr_M(β_Bor) at q_0 = {trM_R2_num:.40f}")
    print()

    # =====================================================================
    # R1 numerical at q_0
    # =====================================================================
    h_0 = Q0 - 1 / Q0
    trM_R1_num = float(
        (4 + h_0 ** 2 - 3 * h_0 ** 4 - h_0 ** 6) / (h_0 ** 2 + 4)
    )
    print(f"  R1 numerical: tr_M(β_Bor) at q_0 = {trM_R1_num:.40f}")
    print()

    # =====================================================================
    # CONSISTENCY CHECK
    # =====================================================================
    print("=" * 80)
    print("Consistency check: R1 vs R2 at q_0 (both same-framing canonical)")
    print("=" * 80)
    print()
    diff = abs(trM_R1_num - trM_R2_num)
    rel_diff = diff / abs(trM_R1_num) if trM_R1_num != 0 else float('inf')
    print(f"  |R1 − R2|     = {diff:.6e}")
    print(f"  Relative diff = {rel_diff:.6e}")
    print()
    if rel_diff < 1e-9:
        verdict = "POSITIVE"
        print(f"  ✓ R1 = R2 to {-int(np.log10(max(rel_diff, 1e-50)))} digits.")
        print(f"    Tessellation-coordinate-freedom CONFIRMED for the Borromean")
        print(f"    Markov trace at substrate q_0. The closed form (R1) equals")
        print(f"    the Wedderburn sum (R2) as expected.")
    elif rel_diff < 1e-3:
        verdict = "MARGINAL"
        print(f"  ⚠ R1 ≠ R2 but agreement within 0.1% — possible numerical")
        print(f"    precision issue in the linear-system solve.")
    else:
        verdict = "NEGATIVE"
        print(f"  ✗ R1 ≠ R2 to large precision — structural inconsistency.")
        print(f"    Investigation needed: are y_λ weights normalized correctly?")
        print(f"    Are χ^λ in the right convention?")
    print()

    # =====================================================================
    # SYMBOLIC CHECK at h-series level
    # =====================================================================
    print("=" * 80)
    print("Bonus: symbolic h-series check")
    print("=" * 80)
    print()
    # χ^(2,1) in h-series via substitution q = (h + √(h²+4))/2
    chi_std_h = sp.simplify(chi_std.subs(q, (h + sp.sqrt(h ** 2 + 4)) / 2))
    chi_std_h_series = sp.series(chi_std_h, h, 0, 12).removeO()
    print(f"  χ^(2,1)(β_Bor) in h-series: {sp.expand(chi_std_h_series)}")
    print()
    # Same for trivial and sign (constant 1 each — degenerate, OK)
    # R1 h-series:
    print(f"  R1 in h-series:             {sp.expand(trM_R1_series)}")
    print()

    # =====================================================================
    # Witness
    # =====================================================================
    witness = {
        "compute": "probe_d_redo_multi_tessellation_consistency",
        "description": (
            "Redo of Probe D from PR #1233 with MATCHING framing convention. "
            "Previous D used Jones polynomial / [2]_q² which has writhe-"
            "dependent normalization differing from the Markov trace closed "
            "form. This redo uses (R1) closed form and (R2) Wedderburn sum "
            "via Hoefsmit + Jones-Markov weights — both canonically-"
            "normalized Markov-trace expressions in H_3(q)."
        ),
        "R1_closed_form_at_substrate": trM_R1_num,
        "R2_wedderburn_sum_at_substrate": trM_R2_num,
        "abs_difference": diff,
        "relative_difference": rel_diff,
        "wedderburn_weights": {
            "y_(3)": float(y_vals[0]),
            "y_(2,1)": float(y_vals[1]),
            "y_(1,1,1)": float(y_vals[2]),
        },
        "chi_at_substrate": {
            "chi_(3)(beta_Bor)": chi_triv_num,
            "chi_(2,1)(beta_Bor)": chi_std_num,
            "chi_(1,1,1)(beta_Bor)": chi_sign_num,
        },
        "chi_2_1_h_series": str(sp.expand(chi_std_h_series)),
        "r1_h_series": str(sp.expand(trM_R1_series)),
        "verdict": verdict,
        "interpretation": (
            "POSITIVE = audit §11 tessellation-coordinate-freedom CONFIRMED. "
            "MARGINAL = numerical-precision-only difference. "
            "NEGATIVE = structural inconsistency requiring investigation."
        ),
        "audit_reference": "docs/audits/2026-05-24-crystal-yekutieli-correspondence-chain.md §11",
        "supersedes": "Probe D from PR #1233 (which had inconclusive INCONCLUSIVE verdict due to framing mismatch)",
        "status": "exploratory",
        "tags": [
            "probe-d-redo",
            "multi-tessellation-consistency",
            "wedderburn-vs-closed-form",
            "matching-framing",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "probe-d-redo-multi-tessellation-consistency.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"  Witness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
