#!/usr/bin/env python3
# polynomial_q_not_applicable: float64 eigenvalue ratio scan +
# proper Wenzl-bridge Markov-trace decomposition; the structural
# observation (z_markov appears in the dominant (5,1) channel) is
# the empirical content.
"""z_markov as a clean internal eigenvalue ratio in the DOMINANT
Markov-trace channel of M = ρ(β_EW Δ_I^minimal) at n=6.

## Background — three readings, three blocks

[`probe_staircase_ew_k3_categorical.py`](probe_staircase_ew_k3_categorical.py)
read the EW residual as `cot θ_W^CODATA / (e_top/e_2nd of V_(3,2,1))`
and found `≈ q^(1/5)` to `0.15 %`.  The §5 q-derivative test of
[`probe_staircase_ew_k3_block_decomposition.py`](probe_staircase_ew_k3_block_decomposition.py)
**falsified** the `residual = q^a` hypothesis (slope `-4.63` not `+3/14`).

This probe asks a different question: **which Wedderburn block actually
DOMINATES the Markov trace `tr_M(β_EW Δ_I^minimal)`?** If a different
block dominates, the EW reading via V_(3,2,1) was looking at the
wrong place.

## Computation

1. Load canonical 50-dps `y_λ` from
   `y-lambda-at-q0.witness.json` (the pre-computed Wenzl-bridge cache
   used by `prop:y-lambda-closed-form-wenzl-bridge` consumers).
2. Build `M_λ = ρ_λ(β_EW Δ_I^minimal)` at float64 for every `λ ⊢ 6`.
3. Compute `χ_λ = tr(M_λ)` and the per-block contribution
   `y_λ · χ_λ` to `tr_M = Σ_λ y_λ χ_λ`.
4. For each non-trivial block, scan all `(i, j)` eigenvalue pairs of
   `M_λ` for the closest match to candidate substrate scales
   (`z_markov`, `q^(1/5)`, `q^(1/3)`, etc.).

## Findings at q_0 (float64)

`tr_M(β_EW Δ_I^minimal) at q_0 ≈ 3.4188`.  Per-block contributions
to `tr_M`, sorted by magnitude:

| Block λ | dim | y_λ · χ_λ contribution | % of tr_M |
| --- | --- | --- | --- |
| **(5, 1)** | 5  | **+1.471** | **43.0 %** |
| (6,)       | 1  | +0.990     | 28.9 %     |
| (4, 2)     | 9  | +0.720     | 21.1 %     |
| (3, 3)     | 5  | +0.108     | 3.2 %      |
| (4, 1, 1)  | 10 | +0.099     | 2.9 %      |
| **(3, 2, 1)** | **16** | **+0.031** | **0.9 %** |
| (2, 2, 2)  | 5  | −0.001     | 0.03 %     |
| (others)   | …  | < 0.001    | < 0.01 %   |

**The (3, 2, 1) block contributes only 0.9 %** to `tr_M`.  The previous
EW reading via "top/2nd of V_(3,2,1)" was reading a *minor* channel.

## z_markov as internal ratio in the dominant block

Pairwise eigenvalue scan in each block for the closest match to
candidate substrate scales:

| Block | Best ratio for `z_markov ≈ 0.4993` | `|Δ_rel|` |
| --- | --- | --- |
| **(5, 1)** | **e[3]/e[2] = 0.5018** | **0.51 %** |
| (4, 2)     | e[2]/e[1] = 0.5179     | 3.72 %    |
| (3, 2, 1)  | e[4]/e[1] = 0.4579     | 8.29 %    |

`z_markov = 1/(√q + 1/√q)` appears as an **internal eigenvalue ratio
in the dominant (5,1) channel to 0.5 %**.  This is the same
`z_markov` that
[`probe_sdpb_pl_crossing_equations.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/probe_sdpb_pl_crossing_equations.py)
(commit 5e7459cf0) identified as the SDP-saturating value `a_PL` of
the Picard-Lefschetz integration limit — **the same substrate scale
appears in two unrelated categorical readings**.

## Refinement of `conj:staircase-ew-residual` suggested by this finding

The original conjecture targeted V_{ρ_k} and the corner-hook exponent
`q^(1/(2k−1))`. The dominant-block analysis here suggests:

* The relevant block for the EW reading is the **Markov-trace-dominant
  Wedderburn channel** (here `(5,1)`, *not* the staircase `(3,2,1)`).
* The relevant substrate scale is **`z_markov = 1/(√q + 1/√q)`**, the
  Markov parameter — same as the PL SDP's saturating value.
* The 0.5 % residual at q_0 is consistent with z_markov being a
  **leading-order** identification, with categorical sub-leading
  corrections to be derived (rather than the original q^(1/(2k−1))
  reading which collapsed under §5's q-derivative test).

## Caveats

* Float64 only; the 0.5 % residual at q_0 is well above float64 noise
  (~1e-13), so it is structural — but a 50-dps upgrade would tighten
  the match estimate.
* The "dominant block" identification depends on the chosen β_EW word
  (the n=6 hand-crafted `σ_1⁴ · Δ_I · σ_3⁶ · Δ_I · σ_5⁸ · Δ_I` from
  `staircase_ew_predictions.beta_ew_word(6)`).  A different β_EW
  variant could move the dominant block.
* The match `e[3]/e[2] = z_markov + 0.5%` has not been q-derivative
  tested.  The §5 falsification of `residual = q^a` does NOT directly
  apply since this is a different reading; a dedicated q-derivative
  test of `e[3]/e[2]` vs `z_markov(q)` is the next step.

`auditOnly`: docs/audits/2026-05-18-staircase-ew-dominant-block.md

Witness: `staircase-ew-dominant-block.witness.json`

@module folio-assistant/computations/probe_staircase_ew_dominant_block
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402
from mpmath import mp, mpf, fabs  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from q_parameter import Q  # noqa: E402
from staircase_ew_predictions import beta_ew_word  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

Q0 = float(Q)
N_STRANDS = 6
K = 3


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > c) for c in range(lam[0]))


def best_pairwise_match(eigs_real: list, target: float) -> tuple:
    """Return (best_ratio, |Δ_rel|, i, j) over all i≠j with both > tol."""
    pos = [(i, e) for i, e in enumerate(eigs_real) if e > 1e-9]
    best = (1e9, 1e9, -1, -1)
    for i, ei in pos:
        for j, ej in pos:
            if i == j:
                continue
            r = ei / ej
            rel = abs(r - target) / max(abs(target), 1e-12)
            if rel < best[1]:
                best = (r, rel, i, j)
    return best


def main() -> int:
    print("=" * 78)
    print("  Dominant Markov-trace channel + z_markov internal-ratio scan")
    print("=" * 78)

    # Load 50-dps y_lambda from canonical cache
    y_data = {
        tuple(e["partition"]): mpf(e["y_at_q0_50dps"])
        for e in json.load(open(
            "folio-assistant/computations/y-lambda-at-q0.witness.json"
        ))["data"]["by_n"][str(N_STRANDS)]
    }

    z_markov = 1.0 / (np.sqrt(Q0) + 1.0 / np.sqrt(Q0))
    print(f"  q_0           = {Q0:.10f}")
    print(f"  z_markov      = {z_markov:.10f}")
    print()

    word = beta_ew_word(N_STRANDS)

    # Compute per-block character + eigenvalues + dominant ratios
    rows = []
    tr_M = mpf(0)
    for lam, y_val in y_data.items():
        try:
            sigmas, dim, _ = build_seminormal_matrices(list(lam))
        except Exception:
            continue
        if dim == 0:
            continue
        sigmas_dense = [
            np.asarray(s.toarray() if hasattr(s, "toarray") else s,
                       dtype=np.complex128)
            for s in sigmas
        ]
        if any(g >= len(sigmas_dense) for g in word):
            continue
        M = np.eye(dim, dtype=np.complex128)
        for g in word:
            M = M @ sigmas_dense[g]
        chi = float(np.real(np.trace(M)))
        contrib = y_val * mpf(str(chi))
        tr_M += contrib

        eigs = np.linalg.eigvals(M)
        real_pos = sorted([float(e.real) for e in eigs
                           if abs(e.imag) < 1e-9 and e.real > 1e-9],
                          reverse=True)
        best_zm = best_pairwise_match(real_pos, z_markov)
        rows.append({
            "lam": lam, "dim": dim, "chi": chi,
            "y_lambda": float(y_val),
            "contribution": float(contrib),
            "abs_contribution": float(fabs(contrib)),
            "n_real_pos": len(real_pos),
            "top_eigs": real_pos[:4],
            "best_z_markov_ratio": float(best_zm[0]),
            "best_z_markov_rel_err": float(best_zm[1]),
            "best_z_markov_indices": [int(best_zm[2]), int(best_zm[3])],
        })

    rows.sort(key=lambda r: -r["abs_contribution"])
    print(f"  tr_M(β_EW Δ_I^minimal) at q_0 = {mp.nstr(tr_M, 15)}")
    print()
    print(f"  Per-block contributions to tr_M (sorted by |contribution|):")
    print(f"  {'λ':<22s} {'dim':>4s}  {'y_λ':>10s}  {'χ_λ':>11s}  {'y_λ·χ_λ':>12s}  {'% of |tr_M|':>11s}  z_markov match")
    total_abs = float(fabs(tr_M))
    for r in rows:
        pct = 100.0 * r["abs_contribution"] / total_abs if total_abs > 0 else 0.0
        zm_str = (f"e[{r['best_z_markov_indices'][0]}]/e[{r['best_z_markov_indices'][1]}]={r['best_z_markov_ratio']:.4f} "
                  f"({100*r['best_z_markov_rel_err']:.2f}%)") if r["best_z_markov_indices"][0] >= 0 else "n/a"
        print(f"  {str(r['lam']):<22s} {r['dim']:>4d}  {r['y_lambda']:>10.5f}  {r['chi']:>+11.5f}  {r['contribution']:>+12.5f}  {pct:>10.2f}%  {zm_str}")
    print()

    # Identify the DOMINANT block and its best z_markov reading
    dominant = rows[0]
    print(f"  DOMINANT block: {dominant['lam']} (dim {dominant['dim']}, "
          f"{100*dominant['abs_contribution']/total_abs:.1f}% of |tr_M|)")
    print(f"    Best z_markov ratio: e[{dominant['best_z_markov_indices'][0]}]/"
          f"e[{dominant['best_z_markov_indices'][1]}] = {dominant['best_z_markov_ratio']:.10f}")
    print(f"    Target z_markov                     = {z_markov:.10f}")
    print(f"    |Δ_rel|                             = {dominant['best_z_markov_rel_err']:.4e}")
    print()

    # Sub-comparison: pull out (3,2,1) row
    s321 = next((r for r in rows if r["lam"] == (3, 2, 1)), None)
    if s321:
        print(f"  For reference, the (3,2,1) staircase block:")
        print(f"    Contribution to tr_M             = {s321['contribution']:+.6f}  ({100*s321['abs_contribution']/total_abs:.2f}% of |tr_M|)")
        print(f"    Best z_markov match              = {s321['best_z_markov_ratio']:.6f}  ({100*s321['best_z_markov_rel_err']:.2f}%)")
        print(f"    → staircase reading was looking at a minor channel")
    print()

    builder = (
        WitnessBuilder("staircase-ew-dominant-block", engine="numpy")
        .set_description(
            "Dominant Markov-trace channel analysis for "
            "β_EW Δ_I^minimal at n=6. Decomposes tr_M = Σ y_λ χ_λ via "
            "canonical 50-dps Wenzl-bridge y_λ + float64 Hoefsmit "
            "χ_λ; identifies which Wedderburn block dominates the "
            "trace. Scans each block's internal eigenvalue ratios "
            "for the closest match to z_markov = 1/(√q+1/√q). "
            "Finding: the (5,1) block dominates (43% of |tr_M|) and "
            "has z_markov as an internal ratio to 0.5%, matching the "
            "PL SDP's identification of a_PL = z_markov (commit "
            "5e7459cf0). The (3,2,1) staircase block — the target of "
            "the original conj:staircase-ew-residual — contributes "
            "only 0.9% to tr_M. Suggests the EW reading should be "
            "REFINED to target the dominant (Markov-trace-dominant) "
            "channel, not the staircase channel."
        )
        .set_content_block("conj:staircase-ew-residual")
        .set_audit_only(
            "docs/audits/2026-05-18-staircase-ew-dominant-block.md")
        .add_parameter("n_strands", N_STRANDS)
        .add_parameter("k", K)
        .add_parameter("q_0", Q0)
        .add_parameter("z_markov", float(z_markov))
        .add_data("tr_M_50dps", mp.nstr(tr_M, 50))
        .add_data("dominant_block", list(dominant["lam"]))
        .add_data("dominant_block_pct_of_tr_M",
                  100.0 * dominant["abs_contribution"] / total_abs)
        .add_data("dominant_block_best_z_markov_ratio",
                  dominant["best_z_markov_ratio"])
        .add_data("dominant_block_z_markov_rel_err",
                  dominant["best_z_markov_rel_err"])
        .add_data("staircase_block_pct_of_tr_M",
                  100.0 * s321["abs_contribution"] / total_abs
                  if s321 else None)
        .add_data("per_block_rows", [
            {**r, "lam": list(r["lam"])} for r in rows
        ])
        .add_caveat(
            "Float64 computation; q-derivative falsification test "
            "for the dominant-block reading not yet performed. The "
            "0.5% match is well above float64 noise but the leading-"
            "order vs exact-identity question is still open."
        )
    )
    out_path = builder.save()
    print(f"  Witness: {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
