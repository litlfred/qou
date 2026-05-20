#!/usr/bin/env python3
# polynomial_q_not_applicable: substrate-derived per-cell weight
# decomposition; no symbolic-q output.
"""Murphy / cellular per-cell weights for atomic braid words.

Bridges PR #639 cycle 7's σ-basis probe to per-cell resolution.
The atomic braid word $\\beta_\\mathfrak{H} = \\mathtt{atom\\_braid\\_word\\_3A}(Z, N)$
is a specific σ-product; its Murphy expansion at $H_{3A}(q_0)$ gives
substrate-derivable per-cell weights

  $w_{\\lambda, S, T} := \\bigl|\\langle v_S,\\ \\rho_\\lambda(\\beta) v_T\\rangle\\bigr|$

via the Hoefsmit seminormal basis $\\{v_T : T \\in \\mathrm{SYT}(\\lambda)\\}$ of
$V_\\lambda$, where $(\\rho_\\lambda(\\beta))_{S,T} = \\langle v_S, \\rho_\\lambda(\\beta) v_T\\rangle$
is exactly the per-cell matrix entry in the SYT basis.

**Key structural questions tested:**

1. **Per-partition rollup**: $w_\\lambda^{\\mathrm{sum}} := \\sum_{S, T} w_{\\lambda, S, T}$
   — does this match PR #639 cycle 5b's empirical max-$|\\mu|$ dominant
   partition $[2, 2, 1, 1]$ for deuteron?

2. **Per-cell argmax**: $(\\lambda^*, S^*, T^*) := \\mathop{\\mathrm{argmax}}_{\\lambda, S, T} w_{\\lambda, S, T}$
   — the strictly-finer cell-level identification.

3. **Aligned with #639 max-|μ| selector?** The dominant partition I
   identified via uniform-k contribution is the partition where
   $\\rho_\\lambda(\\beta)$ has the largest eigenvalue magnitudes. Per-cell
   weights probe the same operator from a different angle (matrix
   entries vs eigenvalues).

This probe runs on **deuteron** ($H_6$, 11 partitions, 720 cells) as
the smallest atomic case. T / ³He ($H_9$, ~362k cells) is the
follow-up; the probe pattern is identical, only the scale grows.

Class C (diagnostic / probe). Substrate-only (CAL-2 $q_0$).

Output: `probe-murphy-per-cell-weights.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import mpmath as mp
import numpy as np

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from syt_prefix_cache import BlockCache

from witness_base import WitnessBuilder  # noqa: E402

try:
    from hecke_characters import build_seminormal_matrices  # noqa: E402
    from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
    from q_parameter import Q as Q0  # noqa: E402
    from wedderburn_jones_markov import y_lambda_at  # noqa: E402
    INFRA_OK = True
except ImportError as e:
    print(f"Infrastructure not available: {e}")
    INFRA_OK = False


def partitions(n: int, max_part: int | None = None) -> Iterator[tuple[int, ...]]:
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def rho_word(sigmas: list, dim: int, word: list) -> np.ndarray:
    """ρ_λ(β) as a dim × dim complex matrix."""
    M = np.eye(dim, dtype=complex)
    I = np.eye(dim, dtype=complex)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(f"σ_{g} out of range for {len(sigmas)} sigmas")
        sigma_g = sigmas[g]
        if hasattr(sigma_g, "toarray"):
            sigma_g = sigma_g.toarray()
        sigma_g = np.asarray(sigma_g, dtype=complex)
        M = M @ (c * sigma_g + d * I)
    return M


def main() -> int:
    w = WitnessBuilder("probe-murphy-per-cell-weights", engine="numpy")

    if not INFRA_OK:
        print("Hoefsmit infrastructure missing; cannot proceed.")
        return 1

    q0_val = float(Q0)
    print("=" * 78)
    print("MURPHY / CELLULAR PER-CELL WEIGHTS for atomic braid words")
    print("=" * 78)
    print()
    print(f"  q_0 = {q0_val:.10f}")
    print()

    # ── Deuteron at H_6 ──────────────────────────────────────────
    Z, N = 1, 1
    n = 6
    atom_name = "deuteron"
    print(f"  Test atom: {atom_name} (Z={Z}, N={N}, n={n})")
    print(f"  Computing per-cell weights w_{{λ, S, T}} = |⟨v_S, ρ_λ(β) v_T⟩|")
    print()

    word = atom_braid_word_3A(Z, N, include_inter=True)
    y_at_q0 = y_lambda_at(n, q_val=q0_val)

    all_partitions = list(partitions(n))
    per_partition_summary = []
    all_cells = []  # (λ, S_idx, T_idx, weight)
    total_cells = 0
    for lam in all_partitions:
        try:
            sigmas, dim, _ = build_seminormal_matrices(lam, q0_val)
        except Exception as e:
            print(f"    skip λ={lam}: {e}")
            continue
        if dim == 0:
            continue
        rho_beta = rho_word(sigmas, dim, word)

        # Per-cell weights = |matrix entries| of ρ_λ(β) in Hoefsmit basis
        cell_weights = np.abs(rho_beta)
        # Per-partition rollup
        weight_sum = float(cell_weights.sum())
        max_cell_idx = np.unravel_index(np.argmax(cell_weights), cell_weights.shape)
        max_cell_weight = float(cell_weights[max_cell_idx])

        y_lam = float(y_at_q0.get(lam, 0.0))
        per_partition_summary.append({
            "partition": list(lam),
            "dim": int(dim),
            "y_at_q0": y_lam,
            "n_cells": int(dim * dim),
            "weight_sum_unweighted": weight_sum,
            "weight_sum_y_weighted": abs(y_lam) * weight_sum,
            "max_cell_indices": [int(max_cell_idx[0]), int(max_cell_idx[1])],
            "max_cell_weight": max_cell_weight,
            "max_cell_y_weighted": abs(y_lam) * max_cell_weight,
        })
        total_cells += dim * dim

        # Track top-10 across all (λ, S, T)
        for S_idx in range(dim):
            for T_idx in range(dim):
                all_cells.append((
                    list(lam), S_idx, T_idx,
                    float(cell_weights[S_idx, T_idx]),
                    abs(y_lam) * float(cell_weights[S_idx, T_idx]),
                ))

    # Sort cells by y-weighted magnitude
    all_cells.sort(key=lambda r: -r[4])  # y-weighted

    print(f"  Total cells across all partitions: {total_cells}")
    print()
    print(f"  Per-partition rollup (sorted by y-weighted sum):")
    per_partition_summary.sort(key=lambda r: -r["weight_sum_y_weighted"])
    print(f"  {'λ':>14}  {'dim':>4}  {'cells':>5}  {'Σ|·|':>10}  {'y·Σ|·|':>12}  {'max cell':>10}  {'y·max':>10}")
    print(f"  " + "-" * 78)
    for r in per_partition_summary[:10]:
        print(f"  {str(r['partition']):>14}  {r['dim']:>4}  {r['n_cells']:>5}  "
              f"{r['weight_sum_unweighted']:>10.4f}  "
              f"{r['weight_sum_y_weighted']:>12.6f}  "
              f"{r['max_cell_weight']:>10.4f}  "
              f"{r['max_cell_y_weighted']:>10.6f}")
    print()
    print(f"  Top-10 cells by y-weighted |⟨v_S, ρ_λ(β) v_T⟩|:")
    print(f"  {'λ':>16}  {'(S, T)':>10}  {'|cell|':>10}  {'y · |cell|':>12}")
    print(f"  " + "-" * 60)
    for lam_list, S, T, raw, y_w in all_cells[:10]:
        print(f"  {str(lam_list):>16}  ({S:>2}, {T:>2})  "
              f"{raw:>10.6f}  {y_w:>12.8f}")
    print()

    # Empirical dominant partition from PR #639 cycle 5b
    empirical_dominant = [2, 2, 1, 1]
    rollup_argmax = per_partition_summary[0]["partition"]
    cell_argmax_lambda = all_cells[0][0]

    print(f"  Empirical dominant partition (PR #639 cycle 5b): {empirical_dominant}")
    print(f"  Per-partition rollup argmax:                     {rollup_argmax}")
    print(f"  Per-cell argmax partition:                       {cell_argmax_lambda}")
    print()
    print(f"  Rollup matches empirical: "
          f"{'✓' if rollup_argmax == empirical_dominant else '✗'}")
    print(f"  Cell argmax matches:     "
          f"{'✓' if cell_argmax_lambda == empirical_dominant else '✗'}")
    print()

    if rollup_argmax == empirical_dominant or cell_argmax_lambda == empirical_dominant:
        print("  POSITIVE: per-cell Murphy decomposition identifies the empirical")
        print("  dominant partition. The cell-level structure provides substrate-")
        print("  derivable ranking finer than per-partition alone.")
    else:
        print("  NEGATIVE: per-cell rollup does NOT identify the empirical")
        print("  dominant for deuteron. The Murphy/Hoefsmit matrix-entry sum")
        print("  measures a different observable than the per-partition")
        print("  contribution to the brane-tower truncation; the two rankings")
        print("  are different objects from the same operator data.")

    w.set_content_block("rem:per-partition-k-lambda-rule")
    w.set_description(
        "Murphy / cellular per-cell weight decomposition of the deuteron "
        "braid word β_D at H_6(q_0). Computes w_{λ,S,T} = |⟨v_S, ρ_λ(β_D) "
        "v_T⟩| in the Hoefsmit seminormal basis for each cell (λ, S, T). "
        "Per-partition rollup is Σ_{S,T} w_{λ,S,T}; per-cell argmax gives "
        "the strictly-finer (λ, S, T) selector. Tests whether the cell-"
        "level structure recovers PR #639 cycle 5b's empirical max-|μ| "
        "dominant partition [2,2,1,1]. Substrate-only (CAL-2 q_0). "
        "Class C (diagnostic). Over Z[q^{±1}] (Murphy cellular basis "
        "parameter ring matches Habiro / brane-tower bicompletion)."
    )
    w.add_parameter("atom", atom_name)
    w.add_parameter("n_strands", n)
    w.add_parameter("q_0", q0_val)
    w.add_data("per_partition_summary", per_partition_summary)
    w.add_data("top_10_cells_by_y_weighted_magnitude",
        [{"partition": p, "S": s, "T": t, "weight": r, "y_weighted": yw}
         for (p, s, t, r, yw) in all_cells[:10]])
    w.add_data("total_cells", total_cells)
    w.add_data("empirical_dominant", empirical_dominant)
    w.add_data("rollup_argmax", rollup_argmax)
    w.add_data("cell_argmax_lambda", cell_argmax_lambda)
    w.add_data("rollup_matches_empirical",
               rollup_argmax == empirical_dominant)
    w.add_data("cell_argmax_matches_empirical",
               cell_argmax_lambda == empirical_dominant)

    w.add_assertion(
        "total_cells_equals_n_factorial",
        # Σ dim_λ² = n! by Wedderburn
        computed=total_cells,
        expected=720,  # 6! = 720
    )
    w.add_assertion(
        "deuteron_per_partition_argmax_recorded",
        computed=bool(rollup_argmax),
        expected=True,
    )

    out = w.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
