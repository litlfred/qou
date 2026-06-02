#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical Frobenius-norm decomposition
# of pre-computed A^λ_{μν}(I) matrices; no q-polynomial arithmetic.
"""Magnitude budget: operator-valued vs scalar approximation of A^λ_{μν}(I).

Emits `operator-valued-ansatze-from-mass-endo.witness.json` for
`rem:operator-valued-magnitude-budget`.

Reads the H_6 deuteron-interface operator-valued extracts
A^λ_{μν}(I) from `sublemma-2-1-A-operator-extract.witness.json`
(produced by `sublemma_2_1_A_operator_extract.py`), and for each of
the 35 (λ, μ, ν) blocks computes the orthogonal decomposition

    A^λ_{μν}(I) = A_scalar + Δ_op

where A_scalar = tr(A) / (d_μ d_ν) · 𝟙 is the best scalar
approximation (the orthogonal projection of A onto the line ℝ·𝟙 in
the Frobenius inner product) and Δ_op is the operator-valued
residual. By Pythagoras (A_scalar ⊥ Δ_op):

    ‖A_scalar‖_F² = |tr A|² / (d_μ d_ν)
    ‖Δ_op‖_F²     = ‖A‖_F² − |tr A|² / (d_μ d_ν)

Aggregate magnitudes are root-sum-square over all blocks:

    scalar_F  = sqrt(Σ ‖A_scalar‖_F²)
    op_F      = sqrt(Σ ‖Δ_op‖_F²)
    total_F   = sqrt(scalar_F² + op_F²)   (= global Frobenius norm)

The operator-valued fraction of the total structural magnitude is

    ratio = op_F / total_F

Cited aggregate (`rem:operator-valued-magnitude-budget`):
    scalar-approximation Frobenius : 3.517
    operator-valued correction     : 3.603  (> scalar)
    ratio op / total              : 0.72
    non-scalar blocks             : 19 / 35

The operator-valued correction EXCEEDS the scalar approximation:
symmetric scalar substrate ansätze capture less than half the
structural magnitude — quantitative justification for the
operator-valued / Z↔N-asymmetric direction.

Upstream witness: `sublemma-2-1-A-operator-extract.witness.json`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

UPSTREAM = "sublemma-2-1-A-operator-extract.witness.json"


def main() -> int:
    w = WitnessBuilder(
        "operator-valued-ansatze-from-mass-endo",
        engine="python",
    )
    w.set_description(
        "Magnitude budget: scalar vs operator-valued Frobenius "
        "decomposition of the H_6 deuteron-interface A^λ_{μν}(I) "
        "extracts. For each (λ,μ,ν) block A = A_scalar + Δ_op with "
        "A_scalar = tr(A)/(d_μ d_ν)·𝟙 the best scalar approximation; "
        "by Pythagoras ‖Δ_op‖² = ‖A‖² − |tr A|²/(d_μ d_ν). Aggregate "
        "(root-sum-square over 35 blocks): scalar 3.517, operator "
        "3.603, ratio op/total 0.72, 19/35 non-scalar. The operator-"
        "valued correction exceeds the scalar approximation — symmetric "
        "scalar ansätze capture < half the structural magnitude."
    )
    w.set_content_block("rem:operator-valued-magnitude-budget")

    # Load the upstream A-operator extract witness (records its hash
    # for the anti-staleness drift validator).
    upstream = w.add_upstream(HERE / UPSTREAM)

    scalar_sq_total = 0.0
    op_sq_total = 0.0
    n_blocks = 0
    n_nonscalar = 0
    per_block = []

    for lam_str, info in upstream["results_per_lambda"].items():
        for pair_key, A in info["A_per_pair"].items():
            n_blocks += 1
            fro = float(A["frobenius_norm"])   # ‖A‖_F
            tr = float(A["trace"])             # tr(A)
            d_mu = int(A["d_mu"])
            d_nu = int(A["d_nu"])
            dd = d_mu * d_nu
            A_F2 = fro * fro
            scalar_F2 = (tr * tr) / dd         # ‖A_scalar‖_F²
            op_F2 = A_F2 - scalar_F2           # ‖Δ_op‖_F² (Pythagoras)
            if op_F2 < 0.0:
                # Guard tiny negative from float round-off.
                op_F2 = 0.0
            scalar_sq_total += scalar_F2
            op_sq_total += op_F2
            is_scalar = bool(A.get("is_scalar_multiple_of_id", False))
            if not is_scalar:
                n_nonscalar += 1
            per_block.append({
                "lambda": lam_str,
                "mu_nu": pair_key,
                "d_mu": d_mu,
                "d_nu": d_nu,
                "A_frobenius": fro,
                "trace": tr,
                "scalar_frobenius": math.sqrt(scalar_F2),
                "op_frobenius": math.sqrt(op_F2),
                "is_scalar": is_scalar,
            })

    scalar_agg = math.sqrt(scalar_sq_total)
    op_agg = math.sqrt(op_sq_total)
    total_F = math.sqrt(scalar_sq_total + op_sq_total)
    ratio_op_total = op_agg / total_F

    print(f"  n_blocks total                 = {n_blocks}")
    print(f"  n_nonscalar                    = {n_nonscalar}")
    print(f"  scalar-approximation Frobenius = {scalar_agg:.4f}")
    print(f"  operator-valued Frobenius      = {op_agg:.4f}")
    print(f"  total Frobenius (sqrt s²+o²)   = {total_F:.4f}")
    print(f"  ratio op/total                 = {ratio_op_total:.4f}")

    w.add_data("n_blocks", n_blocks)
    w.add_data("n_nonscalar_blocks", n_nonscalar)
    w.add_data("n_scalar_blocks", n_blocks - n_nonscalar)
    w.add_data("scalar_frobenius_aggregate", scalar_agg)
    w.add_data("operator_frobenius_aggregate", op_agg)
    w.add_data("total_frobenius", total_F)
    w.add_data("ratio_op_over_total", ratio_op_total)
    w.add_data("decomposition", "A = A_scalar + Delta_op; A_scalar = tr(A)/(d_mu d_nu) * I")
    w.add_data("per_block", per_block)

    # Cross-check assertions vs the cited aggregate figures.
    w.add_assertion(
        name="scalar_approximation_frobenius",
        computed=round(scalar_agg, 3),
        expected=3.517,
        tolerance=5e-3,
        source="rem:operator-valued-magnitude-budget cites scalar Frobenius 3.517",
    )
    w.add_assertion(
        name="operator_valued_frobenius",
        computed=round(op_agg, 3),
        expected=3.603,
        tolerance=5e-3,
        source="rem:operator-valued-magnitude-budget cites operator Frobenius 3.603",
    )
    w.add_assertion(
        name="ratio_op_over_total",
        computed=round(ratio_op_total, 2),
        expected=0.72,
        tolerance=5e-3,
        source=(
            "rem:operator-valued-magnitude-budget cites ratio 0.72 = "
            "op_F / sqrt(scalar_F² + op_F²) (operator-valued fraction "
            "of total Frobenius magnitude)"
        ),
    )
    w.add_assertion(
        name="non_scalar_block_count",
        computed=n_nonscalar,
        expected=19,
        tolerance=0,
        source="rem:operator-valued-magnitude-budget cites 19/35 non-scalar blocks",
    )
    w.add_assertion(
        name="total_block_count",
        computed=n_blocks,
        expected=35,
        tolerance=0,
        source="35 (λ,μ,ν) blocks across the 11 partitions of 6",
    )
    w.add_assertion(
        name="operator_exceeds_scalar",
        computed=1 if op_agg > scalar_agg else 0,
        expected=1,
        tolerance=0,
        source="operator-valued correction Frobenius exceeds scalar approximation",
    )

    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
