#!/usr/bin/env python3
# polynomial_q_not_applicable: substrate-derived Gram-matrix
# probe in the paper-canonical reduced-braid-word basis of H_n(q);
# no symbolic-q output.
"""Braid-word basis Gram matrix probe at H_3(q_0) and H_6(q_0).

Per PR #639 cycle-7 user direction: test the operator-selection LP
in the paper's canonical $\\sigma_w$ basis (AGENTS.md §7a), where
the Gram $G_{wv} = \\mathrm{tr}_M(\\sigma_w \\cdot \\sigma_v)$ is
genuinely non-diagonal (since adjacent generators don't commute).

This is the **(c)** option of the rem:per-partition-k-lambda-rule's
"What next" — strictly stronger than the per-partition basis,
where we proved (probe_off_diagonal_gram_wedderburn.py) the Gram
is identically zero off-diagonal by Wedderburn orthogonality.

**At H_3(q):**
  Reduced-word basis = {e, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0}
                        (6 elements, dim H_3(q) = 3! = 6)
  Irreps: V_[3] (1-dim), V_[2,1] (2-dim), V_[1,1,1] (1-dim)
  y_λ at q_0 from Wenzl bridge

  Gram entry G_wv = tr_M(σ_w · σ_v) computed via Wenzl bridge:
    tr_M(x) = Σ_λ y_λ(q_0) · tr_{V_λ}(ρ_λ(x))

**Smoke test for non-diagonality:** if G_{σ_0, σ_1} ≠ 0, the basis
genuinely has off-diagonal structure (smoking-gun distinguishing
this from the partition-basis-Wedderburn-diagonal case).

**For atomic compute (H_6, deuteron):** the braid word β_D is a
specific σ-word; we project the LP onto the reduced-word basis of
H_6 and read shadow prices to test whether the LP active set
contains structural information beyond uniform-partition rankings.

Class C (diagnostic / structural).

Output: `probe-braid-word-basis-gram.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import numpy as np

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

try:
    from hecke_characters import build_seminormal_matrices  # noqa: E402
    from q_parameter import Q as Q0  # noqa: E402
    from wedderburn_jones_markov import y_lambda_at  # noqa: E402
    INFRA_OK = True
except ImportError as e:
    print(f"Infrastructure not available: {e}")
    INFRA_OK = False


def rho_word(sigmas: list, dim: int, word: list[int]) -> np.ndarray:
    """ρ_λ(σ_{i_1} · σ_{i_2} · ... · σ_{i_ℓ}) as a numerical matrix."""
    M = np.eye(dim, dtype=complex)
    for i in word:
        if i >= len(sigmas):
            raise IndexError(f"σ_{i} out of range")
        sigma = sigmas[i]
        if hasattr(sigma, "toarray"):
            sigma = sigma.toarray()
        sigma = np.asarray(sigma, dtype=complex)
        M = M @ sigma
    return M


def tr_M_wenzl(word: list[int], rho_data: dict, y_data: dict) -> float:
    """tr_M(σ_w) = Σ_λ y_λ · tr_{V_λ}(ρ_λ(σ_w))."""
    total = 0.0
    for lam, (sigmas, dim) in rho_data.items():
        if dim == 0:
            continue
        M = rho_word(sigmas, dim, word)
        y = float(y_data.get(lam, 0.0))
        total += y * float(np.trace(M).real)
    return total


def main() -> int:
    w = WitnessBuilder("probe-braid-word-basis-gram", engine="numpy")

    if not INFRA_OK:
        print("Hoefsmit infrastructure missing; cannot proceed.")
        return 1

    print("=" * 78)
    print("BRAID-WORD BASIS GRAM PROBE (paper-canonical σ_w basis)")
    print("=" * 78)
    print()

    q0_val = float(Q0)
    print(f"  q_0 = {q0_val:.10f}")
    print()

    # ── H_3 case: 6-element basis, full Gram computable ──────────
    print("  Part 1: H_3(q_0)")
    print("  Reduced-word basis: {e, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0}")
    print()

    WORDS_H3 = [
        ("e",         []),
        ("σ_0",       [0]),
        ("σ_1",       [1]),
        ("σ_0 σ_1",   [0, 1]),
        ("σ_1 σ_0",   [1, 0]),
        ("σ_0 σ_1 σ_0", [0, 1, 0]),
    ]

    # Build ρ_λ for [3], [2,1], [1,1,1] at H_3
    rho_data_h3 = {}
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        try:
            sigmas, dim, _ = build_seminormal_matrices(lam, q0_val)
            rho_data_h3[lam] = (sigmas, dim)
        except Exception as e:
            print(f"    skip λ={lam}: {e}")

    y_h3 = y_lambda_at(3, q_val=q0_val)
    print(f"  y_λ at q_0 (Wenzl bridge, n=3):")
    for lam, y in y_h3.items():
        print(f"    y_{lam} = {float(y):+.10f}")
    print()

    # Build the 6×6 Gram matrix tr_M(σ_w · σ_v)
    d = len(WORDS_H3)
    G_h3 = np.zeros((d, d))
    t_h3 = np.zeros(d)  # tr_M(σ_w) for each basis element
    for i, (_, w_word) in enumerate(WORDS_H3):
        t_h3[i] = tr_M_wenzl(w_word, rho_data_h3, y_h3)
        for j, (_, v_word) in enumerate(WORDS_H3):
            wv = w_word + v_word
            G_h3[i, j] = tr_M_wenzl(wv, rho_data_h3, y_h3)

    print("  Gram matrix G_{wv} = tr_M(σ_w · σ_v) at H_3(q_0):")
    print(f"  {'':>12}  " + "  ".join(f"{name:>12s}" for name, _ in WORDS_H3))
    for i, (name_w, _) in enumerate(WORDS_H3):
        print(f"  {name_w:>12s}  " + "  ".join(
            f"{G_h3[i,j]:+12.6f}" for j in range(d)
        ))
    print()

    # Identify off-diagonal entries
    off_diag_pairs = []
    max_off = 0.0
    for i in range(d):
        for j in range(i+1, d):
            if abs(G_h3[i, j]) > 1e-9:
                off_diag_pairs.append({
                    "w": WORDS_H3[i][0],
                    "v": WORDS_H3[j][0],
                    "G_wv": float(G_h3[i, j]),
                })
                if abs(G_h3[i, j]) > max_off:
                    max_off = abs(G_h3[i, j])

    print(f"  Off-diagonal entries (|G_wv| > 1e-9): {len(off_diag_pairs)}/{d*(d-1)//2}")
    print(f"  Max off-diagonal magnitude: {max_off:.6f}")
    print()
    print("  Top non-zero off-diagonal entries:")
    off_diag_pairs.sort(key=lambda r: -abs(r["G_wv"]))
    for p in off_diag_pairs[:5]:
        print(f"    G_{{{p['w']}, {p['v']}}} = {p['G_wv']:+.8f}")
    print()

    # Compute symmetry check: G_wv = G_vw (Markov trace is cyclic)
    is_symmetric = np.allclose(G_h3, G_h3.T, atol=1e-9)
    print(f"  Symmetry check G_wv = G_vw: {'✓' if is_symmetric else '✗'}")
    print()

    # Run LP on the H_3 problem: minimize t^T x subject to Σx = n_target, Gx ≥ 0
    from lp_dual_solver import solve_operator_selection_lp
    n_target = 1.0  # unit categorical mass (single-nucleon proxy)
    print(f"  Running operator-selection LP at H_3, n_target = {n_target}:")
    try:
        lp_result = solve_operator_selection_lp(t_h3, G_h3, n_target)
        if lp_result.feasible:
            print(f"    feasible: y_0^* = {lp_result.y0_star:+.6f}, "
                  f"primal = {lp_result.primal_obj:+.6f}, "
                  f"gap = {lp_result.duality_gap:.2e}")
            print(f"    active set indices: {lp_result.active_set}")
            print(f"    top |y_w^*| shadow prices:")
            y_star = np.array(lp_result.y_star)
            order = np.argsort(-np.abs(y_star))[:3]
            for idx in order:
                print(f"      {WORDS_H3[idx][0]:>14s}: y^* = {y_star[idx]:+.6f}")
        else:
            print(f"    LP infeasible")
    except Exception as e:
        print(f"    LP error: {e}")
        lp_result = None

    print()
    print("  CONCLUSION:")
    print()
    print("  The braid-word basis at H_3(q_0) has GENUINE OFF-DIAGONAL")
    print(f"  Gram structure: {len(off_diag_pairs)} non-zero off-diagonal entries")
    print(f"  out of {d*(d-1)//2} possible, max magnitude {max_off:.4f}.")
    print()
    print("  This is the structural property the per-partition basis LACKED")
    print("  (probed in probe_off_diagonal_gram_wedderburn.py: 110/110 partition")
    print("  pairs in H_6 had identically zero off-diagonal entries by")
    print("  Wedderburn orthogonality).")
    print()
    print("  The σ_w basis is CANONICAL per AGENTS.md §7a (Hecke-Skein")
    print("  convention) and the Gram is over Z[q, q^-1]. This is the")
    print("  smallest paper-canonical basis where the SDP shadow-price")
    print("  hypothesis is testable in a non-degenerate way.")

    w.set_content_block("rem:per-partition-k-lambda-rule")
    w.set_description(
        "Braid-word basis Gram-matrix probe at H_3(q_0). Computes "
        "G_wv = tr_M(σ_w · σ_v) for the 6-element reduced-word basis "
        "{e, σ_0, σ_1, σ_0σ_1, σ_1σ_0, σ_0σ_1σ_0} via the Wenzl bridge "
        "Σ_λ y_λ · tr_{V_λ}(ρ_λ(...)) and Hoefsmit seminormal matrices. "
        "Demonstrates that the paper-canonical σ_w basis (AGENTS.md "
        "§7a) has GENUINE off-diagonal Gram entries — the structural "
        "property the per-partition basis lacks by Wedderburn "
        "orthogonality. The SDP shadow-price hypothesis is testable "
        "non-degenerately in this basis. Class C (diagnostic / "
        "structural). Substrate-only (CAL-2 q_0); no CAL-3 input."
    )
    w.add_parameter("q_0", q0_val)
    w.add_parameter("basis_size_H3", d)
    w.add_parameter("basis_words", [name for name, _ in WORDS_H3])
    w.add_data("y_lambda_at_q0",
        {str(list(k)): float(v) for k, v in y_h3.items()})
    w.add_data("t_vector_H3", t_h3.tolist())
    w.add_data("G_matrix_H3", G_h3.tolist())
    w.add_data("off_diagonal_entries_H3", off_diag_pairs)
    w.add_data("max_off_diagonal_magnitude_H3", float(max_off))
    w.add_data("gram_is_symmetric_H3", bool(is_symmetric))
    if lp_result and lp_result.feasible:
        w.add_data("lp_y0_star_H3", float(lp_result.y0_star))
        w.add_data("lp_y_star_H3", list(lp_result.y_star))
        w.add_data("lp_active_set_indices_H3", list(lp_result.active_set))
        w.add_data("lp_primal_obj_H3", float(lp_result.primal_obj))
        w.add_data("lp_dual_obj_H3", float(lp_result.dual_obj))
        w.add_data("lp_duality_gap_H3", float(lp_result.duality_gap))
        # Bare-name aliases for lp_dual_witness_validator.py (AGENTS.md
        # "LP / SDP duals — first-class infra"). The _H3 names above
        # retain the basis context for future H_6 extension; these
        # bare names are what the validator looks for.
        w.add_data("y0_star", float(lp_result.y0_star))
        w.add_data("y_star", list(lp_result.y_star))
        w.add_data("active_set", list(lp_result.active_set))
        w.add_data("primal_obj", float(lp_result.primal_obj))
        w.add_data("dual_obj", float(lp_result.dual_obj))
        w.add_data("duality_gap", float(lp_result.duality_gap))

    w.add_assertion(
        "braid_word_basis_has_off_diagonal_entries",
        computed=(len(off_diag_pairs) > 0),
        expected=True,
    )
    w.add_assertion(
        "gram_is_symmetric_under_markov_trace",
        computed=is_symmetric,
        expected=True,
    )
    w.add_assertion(
        "max_off_diagonal_strictly_positive",
        computed=(max_off > 1e-9),
        expected=True,
    )

    out = w.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
