"""F1-braid: ⁴He canonical Markov-trace + per-partition fingerprint.

Forward step from `2026-05-15-three-pr-integration.md` F1 prompt:
the rigorous companion to `probe_he4_sdp_compositional.py`. Computes
the full canonical β_{⁴He} Markov trace via Hoefsmit per-irrep at
q_0, identifies which Wedderburn blocks (partitions of 12) carry
the binding via per-partition contribution.

## What's canonical

Per `mass_at_3A_proper.atom_braid_word_3A(2, 2)`, the ⁴He braid
word has 47 crossings on 12 strands with 3 inter-nucleon operator
interfaces (pp at gen 2, pn at gen 5, nn at gen 8). The legacy
`atomic_tr_m_helium4.py` (44-crossing disjoint-product) uses a
deprecated convention that's known to fail the canonical
Schur-Weyl identity at A ≥ 2 (cite: that script's own docstring).

This probe takes the rigorous canonical word and computes:

  tr_M(β_{⁴He}) = Σ_{λ ⊢ 12} y_λ(q_0) · χ^λ_q(β_{⁴He})

via [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](wedderburn_jones_markov.py)
machinery, with the y_λ values pre-loaded from
`y-lambda-at-q0.witness.json` (already covers n=12).

## Compute optimization

- Pre-loaded `y_lambda_at(n=12, q_val=q_0)` — no fresh y_λ compute
  (77 partitions, all cached on disk).
- Per-partition skip when |y_λ| < `Y_THRESHOLD` (default 1e-12) —
  contributions below this can't affect the trace by more than
  ~1 ppb against |tr_M(⁴He)| ~ O(10).
- Per-partition Hoefsmit matrices via the cached
  `build_seminormal_matrices` (`.cache/seminormal/` disk cache
  composes with the `_SEMINORMAL_CACHE` in-memory layer).
- Single pass through 77 partitions; max-dim partition for n=12 is
  ~3300 in the symmetric tableau — most are O(10²–10³).

## Channel fingerprint

The per-partition contribution `c_λ := y_λ · χ^λ_q(β_{⁴He})` is
the **trace-level analog of the SDP active set**. Partitions with
the largest |c_λ| are the binding-receptive Wedderburn blocks.
Cross-compared with the SDP active channels from the sibling
probe `probe_he4_sdp_compositional.py`: if the SDP picks D⊕D and
the dominant partition shape factors through `(2,2)·(2,2)`-type
tableaux, the two approaches agree structurally.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from q_parameter import Q as Q_0_FLOAT
from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word
from hecke_characters import build_seminormal_matrices
from wedderburn_jones_markov import y_lambda_at


Y_THRESHOLD = 1e-12


def main() -> int:
    q0 = float(Q_0_FLOAT)
    Z, N = 2, 2
    A = Z + N
    n = 3 * A  # = 12

    print(f"=== F1-braid: ⁴He canonical Markov trace at q_0 = {q0:.6f} ===", flush=True)
    word = atom_braid_word_3A(Z, N, include_inter=True)
    n_gens = n - 1
    bad = [g for *_, g in word if not (0 <= g < n_gens)]
    if bad:
        raise ValueError(f"out-of-range generators: {sorted(set(bad))}")
    print(f"β_{{⁴He}} word: {len(word)} crossings on {n} strands", flush=True)

    t0 = time.perf_counter()
    y_vals = y_lambda_at(n, q_val=q0)
    print(
        f"y_λ load: {len(y_vals)} partitions in "
        f"{time.perf_counter()-t0:.3f}s",
        flush=True,
    )

    sorted_partitions = sorted(
        y_vals.items(),
        key=lambda kv: abs(float(kv[1])),
        reverse=True,
    )

    total = 0.0
    rows = []
    skipped = 0
    t_compute_start = time.perf_counter()
    for idx, (shape, y) in enumerate(sorted_partitions):
        y_f = float(y)
        if abs(y_f) < Y_THRESHOLD:
            skipped += 1
            continue
        t_p0 = time.perf_counter()
        sigmas, dim, _ = build_seminormal_matrices(shape, q=q0)
        if dim == 0:
            skipped += 1
            continue
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens)
        contrib = y_f * float(chi)
        total += contrib
        elapsed = time.perf_counter() - t_p0
        rows.append({
            "partition": list(shape),
            "dim": int(dim),
            "y_at_q0": y_f,
            "chi_q_at_q0": float(chi),
            "contribution": contrib,
            "abs_contribution": abs(contrib),
            "elapsed_s": elapsed,
        })
        print(
            f"  [{idx+1:2}/77] λ={str(list(shape)):>30}  dim={dim:>5}  "
            f"y={y_f:>+11.4e}  χ={float(chi):>+11.4e}  "
            f"c={contrib:>+11.4e}  t={elapsed:.2f}s",
            flush=True,
        )
    t_compute = time.perf_counter() - t_compute_start
    print(f"\n  total tr_M(β_{{⁴He}}) = {total:.10f}")
    print(
        f"  used {len(rows)}/77 partitions ({skipped} skipped at "
        f"|y|<{Y_THRESHOLD}); compute time {t_compute:.1f}s"
    )

    rows.sort(key=lambda r: r["abs_contribution"], reverse=True)
    print(f"\n=== Top-5 binding-receptive Wedderburn blocks ===")
    cumulative = 0.0
    for i, r in enumerate(rows[:5]):
        cumulative += r["contribution"]
        pct = 100 * abs(r["contribution"]) / abs(total) if abs(total) > 0 else 0
        cum_pct = 100 * cumulative / total if abs(total) > 0 else 0
        print(
            f"  #{i+1}  λ={r['partition']:>30}  dim={r['dim']:>5}  "
            f"|c|={r['abs_contribution']:>.4e} ({pct:>5.1f}%)  "
            f"cum={cum_pct:>5.1f}%"
        )

    msei = json.load(open(HERE / "magic-shell-empirical-instantiation.witness.json"))
    delta_cat_he4 = float(mp.mpf(
        msei["data"]["per_atom_delta_cat"]["he4"]["delta_cat_MeV_50dps"]
    ))
    print(f"\n=== Comparison with empirical anchor ===")
    print(f"  Δ_cat(⁴He) from witness = {delta_cat_he4:.6f} MeV")
    print(f"  tr_M(β_{{⁴He}}) raw       = {total:.6f}")

    builder = (
        WitnessBuilder("he4-canonical-tr-m-block-fingerprint", engine="numpy+scipy")
        .set_description(
            "Canonical ⁴He Markov trace via Hoefsmit per-irrep at "
            "q_0 + per-partition contribution fingerprint. "
            "Forward F1-braid step; companion to "
            "probe_he4_sdp_compositional.py (SDP active-set "
            "approach). Identifies which Wedderburn blocks "
            "(partitions of 12) carry the ⁴He binding. Uses "
            "cached y_lambda + cached Hoefsmit per-irrep — the "
            "same numeric path that wired V2 mirror chirality."
        )
        .set_content_block("prop:operator-selection-lp")
        .add_parameter("q_0", q0)
        .add_parameter("Z", Z)
        .add_parameter("N", N)
        .add_parameter("y_threshold", Y_THRESHOLD)
        .add_data("braid_word_length", len(word))
        .add_data("n_strands", n)
        .add_data("partitions_used", len(rows))
        .add_data("partitions_skipped", skipped)
        .add_data("compute_time_s", t_compute)
        .add_data("tr_M_he4", total)
        .add_data("delta_cat_he4_empirical_MeV", delta_cat_he4)
        .add_data("per_partition_contributions", rows)
        .add_data(
            "top_5_blocks",
            [
                {
                    "partition": r["partition"],
                    "dim": r["dim"],
                    "contribution_pct_of_total":
                        100 * abs(r["contribution"]) / abs(total)
                        if abs(total) > 0 else 0,
                }
                for r in rows[:5]
            ],
        )
        .add_caveat(
            f"Partitions with |y_λ| < {Y_THRESHOLD} are skipped — "
            "their contribution is sub-1ppb at the trace level for "
            "|tr_M| ~ O(10). For ppb-precision targets, lower the "
            "threshold."
        )
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
