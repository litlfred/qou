#!/usr/bin/env python3
"""option_e_phase1_h3_cross_check.py — Option E Phase 1 H_3 cross-check.

Verifies that the per-block Hoefsmit-seminormal data from
`gram_matrix_seminormal_block` reassembles to the published H_3 NF-basis
6×6 Gram matrix from
`tools/pyhecke/python/pyhecke/gram.py` (`G` and `TR_M`).

**Wedderburn isomorphism cross-check** at H_3:

    tr_M(b_i · b_j) = Σ_{λ ⊢ 3} y_λ · tr(ρ_λ(b_i) · ρ_λ(b_j))

where:
- {b_0, ..., b_5} is the H_3 NF basis {1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1}
  (= {γ, σ₀, σ₁, L₊, L₋, e⁻} in `pyhecke.gram` naming)
- λ ∈ {(3), (2,1), (1,1,1)}, dim_λ ∈ {1, 2, 1}
- y_λ = Jones-Markov weights at q_0 (derived by solving the Wedderburn
  linear system from known TR_M values)
- ρ_λ(b) = Hoefsmit-seminormal block representation of b

The cross-check produces:
1. y_λ at H_3 solved from TR_M ↔ per-block χ_λ system
2. The 6×6 reassembled Gram G_reassembled[i, j]
3. The 6×6 published Gram G_NF[i, j] from pyhecke.gram (numerical at q_0)
4. Max |G_reassembled − G_NF| per entry

Acceptance: max residual ≤ 10⁻¹² (well above float64 noise floor).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke" / "python"))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()  # canonical compute precision per qou_substrate.precision

from gram_matrix_seminormal_n import (  # noqa: E402
    gram_matrix_seminormal_block,
    partitions_of_descending,
)
from witness_base import WitnessBuilder  # noqa: E402

# Pull canonical NF-basis Gram + TR_M from pyhecke.gram
from pyhecke.gram import G as NF_GRAM_AT_DEFAULT_Q  # noqa: E402
from pyhecke.gram import TR_M as NF_TR_M_AT_DEFAULT_Q  # noqa: E402
from pyhecke.gram import NF_NAMES  # noqa: E402


Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
Q0_MP = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
Q0_F64 = float(Q0_MP)

# NF basis indexing: σ_1 = matrices[0], σ_2 = matrices[1] in Hoefsmit
# convention. The pyhecke.gram NF_BASIS uses {γ=1, σ_0, σ_1, L_+, L_-, e^-}
# where σ_0/σ_1 (pyhecke) = σ_1/σ_2 (algebra).
# NF basis as products of σ_1, σ_2:
NF_AS_PRODUCTS = [
    [],            # b_0 = 1
    [1],           # b_1 = σ_1   (pyhecke σ_0)
    [2],           # b_2 = σ_2   (pyhecke σ_1)
    [1, 2],        # b_3 = σ_1 σ_2 = L_+
    [2, 1],        # b_4 = σ_2 σ_1 = L_-
    [1, 2, 1],     # b_5 = σ_1 σ_2 σ_1 = e^-  (longest word in S_3)
]


def matrix_for_word(sigma_k_at_q: list[np.ndarray], word_1based: list[int],
                    dim: int) -> np.ndarray:
    """ρ_λ(σ_{k_1} · σ_{k_2} · ... · σ_{k_m})."""
    if dim == 0:
        return np.zeros((0, 0))
    M = np.eye(dim)
    for k in word_1based:
        M = M @ sigma_k_at_q[k - 1]
    return M


def main() -> None:
    # Witness builder created up front so durationMs measures actual
    # solve/reassembly time, not just JSON serialisation.
    w = WitnessBuilder(name="option-e-phase1-h3-cross-check", engine="python")
    w.set_description(
        "Option E Phase 1 cross-check: verify that the per-block "
        "Hoefsmit-seminormal data from `gram_matrix_seminormal_block` "
        "reassembles to the published H_3 NF-basis 6×6 Gram from "
        "pyhecke.gram via the Wedderburn isomorphism "
        "tr_M(b_i·b_j) = Σ_λ y_λ · tr(ρ_λ(b_i)·ρ_λ(b_j))."
    )

    print("=" * 78)
    print(f"Option E Phase 1 — H_3 NF-basis Gram cross-check at q_0 = {Q0_F64:.10f}")
    print("=" * 78)
    print()

    # Build per-block data for all λ ⊢ 3
    blocks: dict[tuple, dict] = {}
    for lam in partitions_of_descending(3):
        blocks[lam] = gram_matrix_seminormal_block(3, lam, Q0_F64)
        print(f"  λ = {lam}: dim = {blocks[lam]['dim_lambda']}, "
              f"χ_λ(w_0) = {blocks[lam]['chi_lambda_w0']:+.10e}")
    print()

    # ρ_λ(b_i) for each NF element b_i, per block λ
    rho_lambda_b = {}  # rho_lambda_b[lam][i] = ρ_λ(b_i)
    for lam, data in blocks.items():
        rho_lambda_b[lam] = []
        for prod_word in NF_AS_PRODUCTS:
            M_b = matrix_for_word(data["sigma_k_at_q"], prod_word,
                                   data["dim_lambda"])
            rho_lambda_b[lam].append(M_b)

    # Solve for y_λ from the Wedderburn linear system:
    # TR_M[i] = Σ_λ y_λ · χ_λ(b_i) = Σ_λ y_λ · trace(ρ_λ(b_i))
    chi_matrix = np.zeros((6, 3))  # rows: NF index, cols: λ index
    lams = list(blocks.keys())
    for i in range(6):
        for j, lam in enumerate(lams):
            chi_matrix[i, j] = float(np.trace(rho_lambda_b[lam][i]))
    tr_m_target = np.array([float(NF_TR_M_AT_DEFAULT_Q[i]) for i in range(6)])
    y_lambda, *_ = np.linalg.lstsq(chi_matrix, tr_m_target, rcond=None)
    print("  Wedderburn weights y_λ at H_3 (solved):")
    for j, lam in enumerate(lams):
        print(f"    y_{lam} = {y_lambda[j]:+.15f}")
    print()

    # Reassemble G_NF[i, j] = Σ_λ y_λ · tr(ρ_λ(b_i) · ρ_λ(b_j))
    G_reassembled = np.zeros((6, 6), dtype=np.float64)
    for i in range(6):
        for j in range(6):
            tot = 0.0
            for k, lam in enumerate(lams):
                prod = rho_lambda_b[lam][i] @ rho_lambda_b[lam][j]
                tot += y_lambda[k] * float(np.trace(prod))
            G_reassembled[i, j] = tot

    # Published 6×6 NF Gram from pyhecke.gram at default q
    G_published = np.array(NF_GRAM_AT_DEFAULT_Q, dtype=np.float64)

    # Compare. The published G is at the pyhecke.gram default q (which
    # tracks q_parameter.Q ≈ q_0); my reassembly is at the same q_0.
    residual = np.abs(G_reassembled - G_published)
    max_resid = float(residual.max())
    rms_resid = float(np.sqrt((residual ** 2).mean()))

    print("  6×6 reassembled vs published NF-basis Gram:")
    print(f"  {'pair':>10}  {'reassembled':>22}  {'published':>22}  {'|Δ|':>10}")
    for i in range(6):
        for j in range(i, 6):  # upper triangle
            print(f"  G[{NF_NAMES[i]:>3},{NF_NAMES[j]:>3}]  "
                  f"{G_reassembled[i,j]:>+22.15e}  "
                  f"{G_published[i,j]:>+22.15e}  "
                  f"{residual[i,j]:>10.2e}")
    print()
    # Tolerance: 1 ppQ (10⁻¹⁵) per AGENTS.md §Precision goals L1 floor
    # and the Phase-1 scope-doc acceptance criterion. Actual residual at
    # H_3 is 2.22e-16 (float64 epsilon) — well below the gate.
    PPQ = 1e-15
    print(f"  Max |Δ| = {max_resid:.2e}")
    print(f"  RMS Δ  = {rms_resid:.2e}")
    print(f"  Verdict: {'✓ PASS' if max_resid < PPQ else '✗ FAIL'}  "
          f"(threshold {PPQ:.0e} = 1 ppQ)")
    print()

    # Witness assembly (builder created at top of main for durationMs accuracy)
    w.add_data("q_0", Q0_F64)
    w.add_data("nf_basis_names", list(NF_NAMES))
    w.add_data("y_lambda_solved",
               {str(lam): float(y_lambda[j]) for j, lam in enumerate(lams)})
    w.add_data("G_reassembled", G_reassembled.tolist())
    w.add_data("G_published", G_published.tolist())
    w.add_data("residual_matrix", residual.tolist())
    w.add_assertion(
        "h3_nf_gram_reassembly_max_residual",
        computed=max_resid,
        expected=0.0,
        tolerance=PPQ,
        source="Σ_λ y_λ · tr(ρ_λ(b_i)·ρ_λ(b_j)) == tr_M(b_i·b_j) for all i,j ∈ NF basis; 1 ppQ gate",
    )
    w.add_assertion(
        "h3_nf_gram_reassembly_rms_residual",
        computed=rms_resid,
        expected=0.0,
        tolerance=PPQ,
        source="RMS over 36 NF Gram entries; 1 ppQ gate",
    )
    w.save()
    print("Witness saved: option-e-phase1-h3-cross-check.witness.json")
    sys.exit(0 if max_resid < PPQ else 1)


if __name__ == "__main__":
    main()
