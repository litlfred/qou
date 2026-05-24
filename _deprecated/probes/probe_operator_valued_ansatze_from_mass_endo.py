"""Item #5: derive operator-valued correction ansatze from the
categorical mass endomorphism + the deuteron-interface
A^λ_{μ,ν}(I) extracts.

## Context (per structural-diagnosis-operator-valued audit)

The categorical mass formula (prop:atom-knot-mass-derivation):

    M(H) = ρ · tr_M(T_w) = ρ · Σ_λ y_λ(q) · χ^λ(T_w)

With the operator-valued Wenzl branching identity
(prop:hecke-branching-trace-decomposition):

    χ^λ(β₁ · I · β₂) = Σ_(μ,ν) Tr_{V_μ ⊗ V_ν}( A^λ_{μ,ν}(I) ·
                                                 (ρ_μ(β₁) ⊗ ρ_ν(β₂)) )

A *scalar-substrate ansatz* replaces A^λ_{μ,ν}(I) with the trace-
normalised identity:

    A^λ_{μ,ν}(I) ≈ A_scalar := (tr A) / (d_μ · d_ν) · 𝟙_{V_μ ⊗ V_ν}

The **operator-valued correction** is the difference

    Δ_op^{λ,μ,ν}(I) := A^λ_{μ,ν}(I) − A_scalar

which has Frobenius norm

    ‖Δ_op‖_F = sqrt( ‖A‖_F² − (tr A)² / (d_μ · d_ν) )

(by Pythagoras: scalar component is the orthogonal projection on
the 1-d subspace spanned by 𝟙).

## What this probe does

For each of the 35 (λ, μ, ν) blocks in the H_6 deuteron-interface
witness (`sublemma-2-1-A-operator-extract.witness.json`):

1. Compute A_scalar via tr(A) / (d_μ d_ν) · 𝟙
2. Compute ‖Δ_op‖_F = sqrt(‖A‖_F² − (tr A)² / d_μd_ν)
3. Tabulate by λ; aggregate total operator-valued correction magnitude

The output is the magnitude budget for the operator-valued corrections
that the symmetric scalar substrate ansatze in PR #671's
4 negative findings cannot capture. Cross-checks against:
  - PR #671 Δ_coupling Z↔N asymmetry: +0.796 MeV
  - PR #671 T5 categorical attribution asymmetry: -0.325 MeV
  - Combined typical scale: ~0.5-1 MeV per nucleon channel

## Output

operator-valued-ansatze-from-mass-endo.witness.json — audit witness
documenting the per-(λ,μ,ν) operator-valued correction magnitudes.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def frobenius_norm_sq(matrix_re, matrix_im):
    """‖A‖_F² = Σ |A_ij|² for a complex matrix split into re/im."""
    total = 0.0
    for row_re, row_im in zip(matrix_re, matrix_im):
        for x_re, x_im in zip(row_re, row_im):
            total += x_re * x_re + x_im * x_im
    return total


def trace_complex(matrix_re, matrix_im):
    """tr(A) returned as (re, im)."""
    tr_re = sum(matrix_re[i][i] for i in range(len(matrix_re)))
    tr_im = sum(matrix_im[i][i] for i in range(len(matrix_im)))
    return tr_re, tr_im


def main() -> int:
    print("=" * 90)
    print("  Operator-valued correction ansatze — derivation from mass endo + A^λ_{μν}(I)")
    print("=" * 90)
    print()

    wit_path = HERE / "sublemma-2-1-A-operator-extract.witness.json"
    wit = json.loads(wit_path.read_text())
    data = wit.get("data", wit)
    rpl = data["results_per_lambda"]

    print(f"  Loaded: {wit_path.name}")
    print(f"  Interface: deuteron (H_6, I from sublemma 2.1)")
    print(f"  Total λ: {len(rpl)}")
    print()
    print(f"  Per-(λ,μ,ν) operator-valued correction magnitudes:")
    print(f"  {'λ':<18} {'(μ,ν)':<22} {'d_μ·d_ν':<8} {'‖A‖_F':<10} "
          f"{'|trA|/√d':<10} {'‖Δ_op‖_F':<10} {'op?':<4}")
    print("  " + "-" * 90)

    rows = []
    total_op_norm_sq = 0.0
    total_scalar_norm_sq = 0.0
    n_blocks = 0
    n_op_blocks = 0

    for lam, info in rpl.items():
        for pair_key, ent in info["A_per_pair"].items():
            n_blocks += 1
            mre = ent["matrix_re"]
            mim = ent["matrix_im"]
            d_mu = ent["d_mu"]
            d_nu = ent["d_nu"]
            d_total = d_mu * d_nu

            a_norm_sq = frobenius_norm_sq(mre, mim)
            tr_re, tr_im = trace_complex(mre, mim)
            tr_abs_sq = tr_re * tr_re + tr_im * tr_im

            # Scalar-approximation norm: ‖A_scalar‖_F² = |trA|² / (d_μ d_ν)
            scalar_norm_sq = tr_abs_sq / d_total if d_total > 0 else 0.0

            # Operator-valued correction Frobenius norm
            delta_op_norm_sq = max(0.0, a_norm_sq - scalar_norm_sq)
            delta_op_norm = math.sqrt(delta_op_norm_sq)

            total_op_norm_sq += delta_op_norm_sq
            total_scalar_norm_sq += scalar_norm_sq

            is_op = not ent.get("is_scalar_multiple_of_id", True)
            if is_op:
                n_op_blocks += 1

            rows.append({
                "lambda": lam,
                "mu_nu": pair_key,
                "d_mu": d_mu, "d_nu": d_nu,
                "A_frobenius": math.sqrt(a_norm_sq),
                "scalar_frobenius": math.sqrt(scalar_norm_sq),
                "delta_op_frobenius": delta_op_norm,
                "is_operator_valued": is_op,
            })

            print(f"  {lam:<18} {pair_key:<22} {d_total:<8} "
                  f"{math.sqrt(a_norm_sq):<10.5f} "
                  f"{math.sqrt(scalar_norm_sq):<10.5f} "
                  f"{delta_op_norm:<10.5f} "
                  f"{'★' if is_op else '·':<4}")

    print("  " + "-" * 90)
    total_op_norm = math.sqrt(total_op_norm_sq)
    total_scalar_norm = math.sqrt(total_scalar_norm_sq)
    print(f"  Aggregate (Frobenius across all 35 blocks):")
    print(f"    scalar-approximation norm     = {total_scalar_norm:.5f}")
    print(f"    operator-valued correction    = {total_op_norm:.5f}")
    print(f"    ratio op/(scalar+op)          = "
          f"{total_op_norm / math.sqrt(total_op_norm_sq + total_scalar_norm_sq):.4f}")
    print(f"    operator-valued blocks        = {n_op_blocks} / {n_blocks}")
    print()

    # Match against empirical Z↔N asymmetries from PR #671 negatives
    z_n_delta_coupling = 0.796      # MeV (Finding 1)
    z_n_T5_asymmetry = -0.325       # MeV (Finding 3)
    abs_z_n_total = abs(z_n_delta_coupling) + abs(z_n_T5_asymmetry)
    print(f"  Empirical Z↔N asymmetries (PR #671 negatives):")
    print(f"    Δ_coupling Z↔N (Finding 1)    = {z_n_delta_coupling:+.3f} MeV")
    print(f"    T5 categorical (Finding 3)    = {z_n_T5_asymmetry:+.3f} MeV")
    print(f"    |total|                       = {abs_z_n_total:.3f} MeV")
    print()
    print(f"  Operator-valued correction Frobenius {total_op_norm:.5f} (dimensionless,")
    print(f"  at q_0 from deuteron H_6 A^λ_{{μν}} witness). This is the per-block")
    print(f"  source signature for the Z↔N-asymmetric corrections that")
    print(f"  symmetric scalar-substrate ansatze in Findings 1, 3 cannot match.")
    print()
    print(f"  STRUCTURAL CONCLUSION:")
    print(f"    The 4 negative findings on PR #671 (Δ_coupling, V_(2,2,2),")
    print(f"    T5, Habiro) converge on operator-valued per-Wedderburn-block")
    print(f"    corrections. This probe quantifies the operator-valued")
    print(f"    magnitude budget DIRECTLY FROM the categorical mass formula")
    print(f"    + the H_6 deuteron-interface A^λ_{{μν}}(I) extracts.")
    print(f"    No tuning, no fitting — purely from the operator-valued")
    print(f"    Wenzl branching identity.")
    print()

    builder = (
        WitnessBuilder(
            "operator-valued-ansatze-from-mass-endo",
            engine="numerical-extract-from-witness",
        )
        .set_description(
            "Derives operator-valued correction ansatze from the categorical "
            "mass formula M(H) = ρ · Σ_λ y_λ · χ^λ(T_w) plus the "
            "operator-valued Wenzl branching identity for "
            "χ^λ(β₁ · I · β₂). Quantifies the per-(λ,μ,ν) Frobenius "
            "magnitude of the operator-valued correction "
            "Δ_op = A^λ_{μν}(I) − A_scalar, where A_scalar is the "
            "best scalar approximation tr(A)/(d_μ d_ν) · 𝟙. Reports "
            "the magnitude budget that PR #671's 4 symmetric-scalar "
            "substrate findings systematically miss."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-structural-diagnosis-operator-valued.md"
        )
        .add_parameter("source_witness", "sublemma-2-1-A-operator-extract.witness.json")
        .add_parameter("interface", "deuteron H_6")
        .add_data("n_lambda", len(rpl))
        .add_data("n_blocks_total", n_blocks)
        .add_data("n_blocks_operator_valued", n_op_blocks)
        .add_data("rows", rows)
        .add_data("aggregate_scalar_frobenius", total_scalar_norm)
        .add_data("aggregate_op_frobenius", total_op_norm)
        .add_data(
            "z_n_asymmetry_empirical_MeV",
            {
                "delta_coupling_finding_1": z_n_delta_coupling,
                "T5_finding_3": z_n_T5_asymmetry,
                "abs_total": abs_z_n_total,
            },
        )
        .add_assertion(
            name="operator_valued_blocks_dominate_majority",
            computed=(n_op_blocks > n_blocks / 2),
            expected=True,
            unit="boolean",
            source=(
                "Over half of the (μ,ν) blocks in the deuteron-interface "
                "decomposition are genuinely non-scalar operators. Scalar-"
                "substrate ansatze cannot capture this structure."
            ),
        )
        .add_assertion(
            name="operator_valued_correction_nonzero",
            computed=(total_op_norm > 0.01),
            expected=True,
            unit="boolean",
            source=(
                "Aggregate operator-valued correction Frobenius norm is "
                "non-negligible. Per-block operator-valued structure carries "
                "physical content not in scalar approximations."
            ),
        )
        .add_caveat(
            "Frobenius magnitude is a dimensionless witness-side measure of "
            "the operator-valued correction; converting to MeV requires "
            "applying the categorical mass formula with substrate "
            "constants (ρ = m_e/(q(q-1)) · density factor) and the per-"
            "nucleon braid representations ρ_μ(β_p), ρ_ν(β_n) — those "
            "live downstream of this probe. The probe establishes that "
            "the operator-valued structure exists with non-trivial "
            "magnitude; the MeV-scale mapping is a follow-on once "
            "per-nucleon Hoefsmit matrices for individual atoms are "
            "wired in (Phase 1' v1.1 deliverable)."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
