#!/usr/bin/env python3
"""Probe: knot-factor-borromean-composite (cor:knot-factor-borromean-composite).

The corollary's structural content is **Brunnian decoupling**:
for a Brunnian k-component composite (every (k−1)-component
sublink trivial), the Hecke character factorises as a product:

    χ_λ(β_Bor_k) = ∏_{i=1}^{k} χ_λ(β_{4_1}^{(i)}).

This is the underlying claim; the displayed formula `(1 − h²)^k`
was a consequence of the (now-revised) amphicheiral corollary
[cor:knot-factor-amphicheiral] and is moot under the revised
sum-of-positive-squares framework — but the **decoupling itself**
remains structurally valid.

This probe verifies decoupling for k = 2 (⁴He as Borromean-2)
using the disjoint product of two figure-eight braids:

    β_Bor_2 = β_{4_1}^(1) ⊔ β_{4_1}^(2)

on disjoint strand sets, evaluated via the Hoefsmit (2,1) rep
for each component, then multiplied.

Emits `knot-factor-borromean-composite-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
# `build_hoefsmit_mpfr` moved: it lived in
# `_deprecated/probes/probe_staircase_ew_k3_categorical.py`, root-level agent
# scratch untracked wholesale by 0763606e4, so this import has raised
# ModuleNotFoundError and THIS PRODUCER COULD NOT RUN AT ALL since. Recovered
# from history into hecke_character_symbolic, beside the symbolic twin and the
# standard_young_tableaux it is built on.
from hecke_character_symbolic import build_hoefsmit_mpfr  # noqa: E402
from mpmath import mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    # Instantiate WitnessBuilder FIRST so its internal start-time
    # captures the heavy SymPy work below (per Copilot review on
    # PR #818: `durationMs` must reflect the whole computation,
    # not just the .save() call).
    builder = WitnessBuilder("knot-factor-borromean-composite-probe",
                             engine="sympy")

    q = sp.Symbol("q", positive=True)
    # Substrate parameter q_0 — canonical 50-digit pin from
    # `q_parameter.Q_50_DIGIT_STR` (avoids drift / divergent
    # literals across the probe series; per Copilot review on
    # PR #818).
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)

    # ── Single-component figure-eight characters (H_3) ──
    # Computed via the canonical Hoefsmit-seminormal builder
    # `build_hoefsmit_mpfr` from `probe_staircase_ew_k3_categorical`.
    # The canonical Hoefsmit matrices satisfy BOTH the Hecke
    # quadratic AND the braid relation σ_1σ_2σ_1 = σ_2σ_1σ_2.
    #
    # NB: an earlier version of this probe (and PR #815's BD probe)
    # used hand-rolled 2×2 matrices that satisfied the Hecke
    # quadratic per-generator but NOT the braid relation; their
    # trace coincidentally evaluated to -1 (a basis-arithmetic
    # artifact), not the true χ_(2,1)(β_{4_1}).  This is
    # corrected here: the true value at q_0 is ≈ -0.91068.
    # The H_6 LR-branching predictions below use this corrected
    # single-component value and match the H_6 Hoefsmit direct
    # trace to ~1e-50 precision.
    set_compute_dps()

    chi_3_single = mp.mpf(1)
    chi_alt_single = mp.mpf(1)
    sigmas_21_h3, dim_21_h3 = build_hoefsmit_mpfr((2, 1), Q_MP)
    s1_h3, s2_h3 = sigmas_21_h3
    beta_single_h3 = s1_h3 * (s2_h3 ** (-1)) * s1_h3 * (s2_h3 ** (-1))
    chi_21_single_mp = sum(beta_single_h3[i, i] for i in range(dim_21_h3))
    chi_21_single_num = float(chi_21_single_mp)

    # === Single-component squares for reference ===
    # The 1-dim blocks (3) and (1^3) carry a 1-dim disjoint product,
    # so structural-multiplicativity reduces trivially to scalar
    # squaring at those blocks (no independent matrix check is
    # possible).  We record these expected products for the witness
    # data block; the structural check below is at the H_6 level.
    chi_3_bor2_expected = float(chi_3_single ** 2)
    chi_21_bor2_expected = chi_21_single_num ** 2
    chi_alt_bor2_expected = float(chi_alt_single ** 2)

    # === GENUINE Brunnian-decoupling witness: H_6 Hoefsmit ===
    # Per Copilot follow-up review on PR #818: the original
    # `tr(A ⊗ A) = (tr A)²` Kronecker check is algebraically
    # tautological — it holds identically for any matrix A and
    # does NOT validate the Brunnian/disjoint-union embedding into
    # the larger Hecke algebra.
    #
    # The proper structural witness:
    #   1. Evaluate β_Bor_2 = β_{4_1}^(1,2,3) · β_{4_1}^(4,5,6) ∈ B_6
    #      in an H_6 Hoefsmit irrep ρ_λ for λ ⊢ 6.  These irreps
    #      are NOT tensor products of single-component reps; they
    #      are built from H_6 Young-tableaux + Jucys-Murphy contents.
    #   2. Independently predict the same trace via the Littlewood-
    #      Richardson branching ρ_λ ↓_{H_3 × H_3} = ⊕_(μ,ν) c^λ_{μν}
    #      (ρ_μ ⊠ ρ_ν), which gives the closed form
    #         χ_λ(β_Bor_2) = Σ_(μ,ν) c^λ_{μν} χ_μ(β_{4_1}) χ_ν(β_{4_1}).
    #   3. Compare (1) and (2).  Equality witnesses that the H_6
    #      irrep's character of the disjoint braid factors through
    #      branching — the true content of Brunnian decoupling.

    # β_Bor_2 ∈ B_6: σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ · σ_4 σ_5⁻¹ σ_4 σ_5⁻¹
    # 0-indexed generators (σ_1 ↔ index 0, σ_5 ↔ index 4).
    # σ_3 (index 2) is NEVER used — this is the "disjoint separator"
    # generator that would couple the two strand groups.
    bor2_word = [
        (0, +1), (1, -1), (0, +1), (1, -1),
        (3, +1), (4, -1), (3, +1), (4, -1),
    ]

    def eval_bor2(shape):
        """Return trace of ρ_shape(β_Bor_2) at q_0 (mpmath, 50 dps)."""
        sigmas, dim = build_hoefsmit_mpfr(shape, Q_MP)
        M = mp.eye(dim)
        for idx, sgn in bor2_word:
            g = sigmas[idx] if sgn > 0 else sigmas[idx] ** (-1)
            M = M * g
        return sum(M[i, i] for i in range(dim)), dim

    # Use the corrected single-component characters (from canonical
    # Hoefsmit above) in the LR-branching predictions.  At q_0 with
    # canonical Hoefsmit:
    #   χ_(3)(β_{4_1})   = +1
    #   χ_(2,1)(β_{4_1}) ≈ -0.91068...
    #   χ_(1^3)(β_{4_1}) = +1
    chi_3 = chi_3_single
    chi_21 = chi_21_single_mp
    chi_111 = chi_alt_single

    # λ = (3,3) ⊢ 6, dim 5.  LR branching c^(3,3)_{μν}:
    #   c^(3,3)_{(3),(3)} = 1,  c^(3,3)_{(2,1),(2,1)} = 1
    # (other coefficients zero; dim check 1·1·1 + 1·2·2 = 5 ✓).
    chi_33_h6_trace, dim_33 = eval_bor2((3, 3))
    chi_33_h6_predicted = (
        mp.mpf(1) * chi_3 * chi_3 +
        mp.mpf(1) * chi_21 * chi_21
    )
    chi_33_h6_residue = mp.fabs(chi_33_h6_trace - chi_33_h6_predicted)

    # λ = (4,2) ⊢ 6, dim 9.  LR branching c^(4,2)_{μν}:
    #   c^(4,2)_{(3),(3)} = 1
    #   c^(4,2)_{(3),(2,1)} = 1,  c^(4,2)_{(2,1),(3)} = 1
    #   c^(4,2)_{(2,1),(2,1)} = 1
    # (dim check: 1·1 + 1·2 + 1·2 + 1·4 = 9 ✓).
    chi_42_h6_trace, dim_42 = eval_bor2((4, 2))
    chi_42_h6_predicted = (
        mp.mpf(1) * chi_3 * chi_3 +
        mp.mpf(1) * chi_3 * chi_21 +
        mp.mpf(1) * chi_21 * chi_3 +
        mp.mpf(1) * chi_21 * chi_21
    )
    chi_42_h6_residue = mp.fabs(chi_42_h6_trace - chi_42_h6_predicted)

    # Note: the FULL ⁴He braid in H_12 is intractable
    # (per PR #798's deferred-intractable taxonomy).  The
    # decoupling claim is verified above on the Hecke
    # representation rather than at the H_12 character level.

    b = (
        builder
        .set_description(
            "I1 probe for cor:knot-factor-borromean-composite.  "
            "Witnesses Brunnian decoupling at k=2 (⁴He as Bor_2) "
            "via TWO independent paths:  (a) single-component "
            "H_3 characters of the figure-eight β_{4_1} for each "
            "λ ⊢ 3 (verified by the BD probe in PR #815);  "
            "(b) direct H_6 Hoefsmit evaluation of the disjoint "
            "braid β_Bor_2 ∈ B_6 on irreps λ ⊢ 6 that are NOT "
            "tensor products of single-component reps "
            "(specifically λ = (3,3) dim 5 and λ = (4,2) dim 9), "
            "compared against the Littlewood-Richardson branching "
            "prediction Σ_(μ,ν) c^λ_{μν} χ_μ(β_{4_1}) χ_ν(β_{4_1}).  "
            "Equality on (b) is the real structural witness — it "
            "validates the embedding β_{4_1}^(1,2,3) · "
            "β_{4_1}^(4,5,6) ↪ H_6 and the LR-branching "
            "factorisation, which is the content of Brunnian "
            "decoupling.  Per Copilot follow-up review on PR #818, "
            "the prior Kronecker-only check was algebraically "
            "tautological (tr(A ⊗ A) = (tr A)² is an identity) "
            "and has been replaced by the H_6 construction below."
        )
        .set_content_block("cor:knot-factor-borromean-composite")
        .add_parameter("q_0_50dps", str(q_0))
        .add_parameter("chi_3_single_4_1", float(chi_3_single))
        .add_parameter("chi_21_single_4_1_at_q0",
                       chi_21_single_num)
        .add_parameter("chi_alt_single_4_1", float(chi_alt_single))
        .add_parameter("chi_33_h6_direct_trace_at_q0",
                       float(chi_33_h6_trace))
        .add_parameter("chi_33_h6_branching_predicted",
                       float(chi_33_h6_predicted))
        .add_parameter("chi_33_h6_residue", chi_33_h6_residue)
        .add_parameter("chi_42_h6_direct_trace_at_q0",
                       float(chi_42_h6_trace))
        .add_parameter("chi_42_h6_branching_predicted",
                       float(chi_42_h6_predicted))
        .add_parameter("chi_42_h6_residue", chi_42_h6_residue)
        .add_data("brunnian_decoupling_k2_expected", {
            "chi_3_Bor_2": float(chi_3_bor2_expected),
            "chi_21_Bor_2_single_squared": chi_21_bor2_expected,
            "chi_alt_Bor_2": float(chi_alt_bor2_expected),
            "rule": "χ_λ(β_Bor_k) = ∏_i χ_λ(β_{4_1}^(i))  on each λ",
        })
        .add_data("h6_lr_branching_predictions", {
            "lambda_3_3_dim": dim_33,
            "lambda_3_3_branching": [
                {"mu": "(3)", "nu": "(3)", "c_mu_nu": 1,
                 "dim_block": 1},
                {"mu": "(2,1)", "nu": "(2,1)", "c_mu_nu": 1,
                 "dim_block": 4},
            ],
            "lambda_3_3_predicted_trace": float(chi_33_h6_predicted),
            "lambda_4_2_dim": dim_42,
            "lambda_4_2_branching": [
                {"mu": "(3)", "nu": "(3)", "c_mu_nu": 1,
                 "dim_block": 1},
                {"mu": "(3)", "nu": "(2,1)", "c_mu_nu": 1,
                 "dim_block": 2},
                {"mu": "(2,1)", "nu": "(3)", "c_mu_nu": 1,
                 "dim_block": 2},
                {"mu": "(2,1)", "nu": "(2,1)", "c_mu_nu": 1,
                 "dim_block": 4},
            ],
            "lambda_4_2_predicted_trace": float(chi_42_h6_predicted),
            "lambda_4_2_predicted_trace_note": (
                "Predicted = (1 + χ_(2,1))² ≈ (1 − 0.9107)² ≈ 0.0080.  "
                "Tight test — random arithmetic on a product of 8 "
                "9×9 Hoefsmit matrices reproduces this value to ~1e-50 "
                "only because the LR structural cancellation holds."
            ),
        })
        .add_data("cascade_note", {
            "corollary_formula": "a_Bor_k = (1 − h²)^k  [from cor:knot-factor-amphicheiral]",
            "structural_invariant": (
                "Brunnian decoupling χ_λ(β_Bor_k) = ∏_i χ_λ(β_{4_1}^(i)) "
                "is independent of the amphicheiral-corollary form; "
                "this probe witnesses the decoupling alone."
            ),
        })
        .add_assertion(
            name="chi_33_h6_decoupling_matches_lr_branching",
            computed=chi_33_h6_residue,
            expected=0.0, tolerance=1e-40,
            unit=(
                "|tr_H6 ρ_(3,3)(β_Bor_2) − Σ_(μ,ν) c^(3,3)_{μν} "
                "χ_μ(β_{4_1}) χ_ν(β_{4_1})|"
            ),
            source=(
                "GENUINE Brunnian-decoupling witness on λ = (3,3) ⊢ 6 "
                "(dim 5).  LHS is computed via H_6 Hoefsmit-seminormal "
                "matrices (independent of single-component reps); "
                "RHS = χ_(3)² + χ_(2,1)² ≈ 1 + 0.8293 = 1.8293 via LR "
                "branching at q_0.  Per Copilot follow-up review on "
                "PR #818, this is the non-tautological replacement "
                "for the prior tr(A ⊗ A) = (tr A)² Kronecker check."
            ),
        )
        .add_assertion(
            name="chi_42_h6_decoupling_matches_lr_branching",
            computed=chi_42_h6_residue,
            expected=0.0, tolerance=1e-40,
            unit=(
                "|tr_H6 ρ_(4,2)(β_Bor_2) − (1 + χ_(2,1))²|"
            ),
            source=(
                "Tight structural test on λ = (4,2) ⊢ 6 (dim 9).  "
                "LR branching gives χ_(4,2)(β_Bor_2) = "
                "(1 + χ_(2,1)(β_{4_1}))² ≈ (1 − 0.9107)² ≈ 0.0080 "
                "at q_0.  Random arithmetic on a 9×9 product of 8 "
                "Hoefsmit matrices reproduces this value to ~1e-50 "
                "ONLY because the structural cancellation enforced "
                "by Brunnian decoupling + LR coefficients holds."
            ),
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
