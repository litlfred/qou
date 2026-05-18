"""Δ_λ closure v5 — per-partition Δ_λ via V2 chirality (categorical).

Tests the natural categorical ansatz from
`conj:knot-factor-frobenius-pairing`:

  Δ_λ(K) := χ^λ(β_K · β_K_mirror⁻¹) at q = q_0

Under this ansatz, the LO closure becomes:

  Σ_λ y_λ · χ^λ(β_K) · Δ_λ(K)
     = Σ_λ y_λ · χ^λ(β_K) · χ^λ(β_K · β_K_mirror⁻¹)
     = ?

Note: this is NOT a_K (which is Σ_λ y_λ · χ^λ(β_K · β_K_mirror⁻¹)).

We test BOTH closures:

  (A) Direct a_K test: does a_K = τ(β·β_mirror⁻¹) match binding/m_e?
      → Σ_λ y_λ · χ^λ(β·β_mirror⁻¹) =? binding/m_e

  (B) Per-(K,λ) Δ test: does Σ_λ y_λ · χ^λ(β) · χ^λ(β·β_mirror⁻¹)
      match binding/m_e?
      → Σ_λ y_λ · χ^λ(β_K) · Δ_λ_chirality(K) =? binding/m_e

Background: aK_v2 already computes Σ_λ y_λ·χ^λ(β·β_mirror⁻¹).
This probe additionally computes the cross-product
Σ_λ y_λ·χ^λ(β)·χ^λ(β·β_mirror⁻¹) which is the natural Δ_λ closure
candidate.

If EITHER closes to binding/m_e (up to a fixed normalization across
atoms), we have a CLOSED-FORM categorical Δ_λ via Frobenius pairing.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)
from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q_0_FLOAT  # noqa: E402
from term5_v2_chirality import aK_v2_full, v2_composite_word  # noqa: E402


M_CODATA = {
    "D": float(M_D_MEV_VALIDATION), "T": float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION), "4He": float(M_HE4_MEV_VALIDATION),
}


def main() -> int:
    mp.mp.dps = 50
    q_val = float(Q_0_FLOAT)
    m_e = float(M_E_MEV)
    m_p = float(M_P_MEV_VALIDATION)
    m_n = float(M_N_MEV_VALIDATION)

    print("=" * 100)
    print("  Δ_λ closure v5 — per-partition Δ_λ via V2 chirality (Frobenius pairing)")
    print("=" * 100)
    print()

    atoms = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    rows = []
    for label, Z, N in atoms:
        A = Z + N
        n_strands = 3 * A
        n_gens = n_strands - 1
        binding = M_CODATA[label] - (Z * m_p + N * m_n)
        target = binding / m_e

        # Get V2 chirality breakdown (per-λ contribution to a_K)
        aK_data = aK_v2_full(Z, N, q_val=q_val)
        aK_value = aK_data["aK_value"]

        # Map from partition → χ^λ(β·β_mirror⁻¹)
        chi_v2_per_lam = {
            tuple(r["partition"]): r["chi_v2_at_q0"]
            for r in aK_data["rows"]
        }

        # Compute χ^λ(β_K) per partition
        word = atom_braid_word_3A(Z, N, include_inter=True)
        y_vals = y_lambda_at(n_strands, q_val=q_val)

        per_lam_records = []
        sum_y_chi_v1_v2 = 0.0  # Σ_λ y_λ · χ^λ(β) · χ^λ(β·β_mirror⁻¹)
        sum_y_chi_v1 = 0.0     # Σ_λ y_λ · χ^λ(β) — should equal |tr_M(β)|
        for lam, y in y_vals.items():
            sigmas, dim, _ = build_seminormal_matrices(lam, q=q_val)
            if dim == 0:
                continue
            chi_v1 = float(chi_lambda_of_word(sigmas, dim, word, n_gens))
            chi_v2 = chi_v2_per_lam.get(lam, 0.0)
            y_f = float(y)
            y_chi_v1 = y_f * chi_v1
            y_chi_v1_v2 = y_f * chi_v1 * chi_v2
            sum_y_chi_v1 += y_chi_v1
            sum_y_chi_v1_v2 += y_chi_v1_v2
            per_lam_records.append({
                "lambda": list(lam),
                "y_at_q0": y_f,
                "chi_v1": chi_v1,   # χ^λ(β_K)
                "chi_v2": chi_v2,   # χ^λ(β·β_mirror⁻¹)
                "y_chi_v1": y_chi_v1,
                "y_chi_v1_v2": y_chi_v1_v2,
            })

        # Closure tests
        # (A) Direct a_K vs binding/m_e
        delta_A_ratio = aK_value / target if abs(target) > 1e-30 else None
        # (B) Cross-product Σ y·χ_v1·χ_v2 vs binding/m_e
        delta_B_ratio = sum_y_chi_v1_v2 / target if abs(target) > 1e-30 else None

        # Sort by |contribution to Δ_B|
        per_lam_records.sort(key=lambda r: -abs(r["y_chi_v1_v2"]))

        print(f"  ── {label} (Z={Z}, N={N}, A={A}, n={n_strands}) ──")
        print(f"  binding/m_e = {target:+.6f}")
        print(f"  a_K (V2)    = {aK_value:+.6e}")
        print(f"  Σ y·χ(β)         (≈ tr_M)       = {sum_y_chi_v1:+.6e}")
        print(f"  Σ y·χ(β)·χ(β·β_mir^-1) (Δ_B)   = {sum_y_chi_v1_v2:+.6e}")
        if delta_A_ratio is not None:
            print(f"  Closure A:  a_K / (binding/m_e)  = {delta_A_ratio:+.6e}")
        if delta_B_ratio is not None:
            print(f"  Closure B:  Δ_B / (binding/m_e)  = {delta_B_ratio:+.6e}")
        print()
        print(f"  Top-5 partitions ranked by |y·χ_v1·χ_v2|:")
        print(f"  {'λ':>18} {'χ^λ(β)':>12} {'χ^λ(β·m^-1)':>14} {'y·χ_v1·χ_v2':>14}")
        for r in per_lam_records[:5]:
            print(f"  {str(r['lambda']):>18} {r['chi_v1']:>+12.4e} "
                  f"{r['chi_v2']:>+14.4e} {r['y_chi_v1_v2']:>+14.4e}")
        print()

        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n_strands,
            "binding_MeV": binding, "target": target,
            "aK_V2": aK_value,
            "sum_y_chi_v1": sum_y_chi_v1,
            "sum_y_chi_v1_v2": sum_y_chi_v1_v2,
            "closure_A_aK_over_target": delta_A_ratio,
            "closure_B_yChi1Chi2_over_target": delta_B_ratio,
            "top5": per_lam_records[:5],
        })

    # Summary — check if any closure stabilizes
    print("=" * 100)
    print("  Δ closure v5 — summary")
    print("=" * 100)
    print(f"  {'atom':>5} {'binding/m_e':>13} {'a_K':>13} "
          f"{'a_K/target':>13} {'Σ_y·χ_v1·χ_v2':>16} "
          f"{'_yyxx/target':>14}")
    print("  " + "-" * 95)
    for r in rows:
        a = f"{r['aK_V2']:+.4e}"
        ar = (f"{r['closure_A_aK_over_target']:+.4e}"
              if r['closure_A_aK_over_target'] is not None else "—")
        s = f"{r['sum_y_chi_v1_v2']:+.4e}"
        br = (f"{r['closure_B_yChi1Chi2_over_target']:+.4e}"
              if r['closure_B_yChi1Chi2_over_target'] is not None else "—")
        print(f"  {r['atom']:>5} {r['target']:>+13.6f} {a:>13} "
              f"{ar:>13} {s:>16} {br:>14}")
    print()

    print("Interpretation:")
    print("  Closure A: a_K ≈ binding/m_e → V2 chirality directly = LO closure")
    print("  Closure B: Σ y·χ(β)·χ(β·β_mir⁻¹) ≈ binding/m_e →")
    print("              Δ_λ(K) = χ^λ(β_K·β_K_mirror⁻¹) is the per-(K,λ)")
    print("              categorical ansatz.")
    print("  If either ratio is STABLE across atoms (= one universal constant),")
    print("  that constant is the missing dimensional normalization.")

    builder = (
        WitnessBuilder("delta-lambda-closure-v5-frobenius-chirality",
                       engine="numpy+scipy")
        .set_description(
            "Δ_λ closure v5: tests per-(K, λ) categorical ansatz "
            "Δ_λ(K) = χ^λ(β·β_mirror⁻¹) (V2 chirality). Two closures "
            "checked: (A) a_K = τ(β·β_mirror⁻¹) vs binding/m_e, "
            "(B) Σ_λ y_λ·χ^λ(β)·χ^λ(β·β_mirror⁻¹) vs binding/m_e. "
            "If either ratio is universal, the categorical Δ_λ is closed."
        )
        .set_content_block("prop:rho-k-h3a-refinement")
        .add_parameter("q_0", q_val)
        .add_data("rows", rows)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
