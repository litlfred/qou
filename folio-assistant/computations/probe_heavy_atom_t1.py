"""Compute T1 = tr_M(β_atomic(Z, N)) for A ∈ {5, 6, 7, 8, 9}.

Closes the heavy-atom T1 witness gap surfaced by
`paper_six_term_isotope_sweep.py` (KeyError "no canonical T1 for
'NLi'" — see 2026-05-15-m1-mass-table.md §3).

Per-irrep numeric Hoefsmit + cached y_λ at q_0:

  tr_M(β_atomic(Z, N)) = Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ_q(β_atomic)

Same machinery as `probe_he4_canonical_tr_m_fingerprint.py`.
Y_THRESHOLD = 1e-10 skips negligible-contribution partitions
(at ~tr_M magnitude O(0.1..2), contributions below this threshold
can't affect the trace by more than ~1 ppb — appropriate for the
T1 witness precision target).

## Compute estimate

| atom | n=3A | partition count | est compute |
|------|------|-----------------|-------------|
| 5Li  | 15   | 176 | ~5 min |
| 6Li  | 18   | 385 | ~30 min |
| 7Li  | 21   | 792 | ~2 h |
| 7Be  | 21   | 792 | ~2 h (cached) |
| 8Be  | 24   | 1575 | ~5 h |
| 9Be  | 27   | 3010 | ~12 h |

y_λ load: instant if cache covers n; ~150 s recompute per n
beyond n=12 (the existing witness cache). Cache extension is the
first step.

## Output

Per-atom witness record matching the schema of
`atomic-tr-m-mpfr-50dps.witness.json`:

  {
    "atom": "...", "Z": ..., "N": ..., "A": ...,
    "n_strands_3A": 3A, "tr_M_at_q0_50dps": "...",
    "y_threshold_skipped": <count>, "compute_elapsed_sec": ...
  }
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q as Q_0_FLOAT  # noqa: E402
from mass_at_3A_proper import (  # noqa: E402
    _SEMINORMAL_DISK,
    atom_braid_word_3A,
    chi_lambda_of_word,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Standalone scientific script — set 50 dps globally per repo
# convention for documented one-shot compute. The numerical contraction
# loop below uses float64 for matrix arithmetic (Hoefsmit matrices are
# numpy arrays); the witness records the float64-precision result
# rounded to 17 sig figs (NOT 50 dps).
set_compute_dps()

_SEMINORMAL_DISK.mkdir(parents=True, exist_ok=True)

Y_THRESHOLD = 1e-10

HEAVY_ATOMS = [
    ("5Li", 3, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
    ("7Be", 4, 3),
    ("8Be", 4, 4),
    ("9Be", 4, 5),
]


def compute_t1(label: str, Z: int, N: int, q0: float) -> dict:
    A = Z + N
    n = 3 * A
    n_gens = n - 1
    print(
        f"\n=== {label} (Z={Z}, N={N}, A={A}, n={n}) ===",
        flush=True,
    )
    word = atom_braid_word_3A(Z, N, include_inter=True)
    print(f"  braid word: {len(word)} crossings", flush=True)

    t_y = time.perf_counter()
    y_vals = y_lambda_at(n, q_val=q0)
    print(
        f"  y_λ loaded: {len(y_vals)} partitions "
        f"({time.perf_counter()-t_y:.1f}s)",
        flush=True,
    )

    sorted_parts = sorted(
        y_vals.items(), key=lambda kv: abs(float(kv[1])), reverse=True
    )

    t0 = time.perf_counter()
    total = 0.0
    rows = []
    skipped = 0
    for idx, (shape, y) in enumerate(sorted_parts):
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
            "chi_at_q0": float(chi),
            "contribution": contrib,
            "elapsed_s": elapsed,
        })
        # Print progress every 10 partitions
        if (idx + 1) % 10 == 0 or elapsed > 5.0:
            print(
                f"    [{idx+1:4}/{len(sorted_parts)}] "
                f"λ={str(list(shape))[:25]:25} "
                f"dim={dim:>5} t={elapsed:.1f}s "
                f"running tr_M={total:+.6e}",
                flush=True,
            )

    elapsed = time.perf_counter() - t0
    print(
        f"  DONE: tr_M = {total:.10f}  "
        f"({len(rows)} used / {skipped} skipped) "
        f"in {elapsed:.0f}s",
        flush=True,
    )

    return {
        "atom": label,
        "Z": Z, "N": N, "A": A,
        "n_strands_3A": n,
        "word_length": len(word),
        "tr_M_at_q0": total,
        "tr_M_at_q0_float64_17sf": mp.nstr(mp.mpf(repr(total)), 17),
        "n_partitions_total": len(sorted_parts),
        "n_partitions_used": len(rows),
        "y_threshold": Y_THRESHOLD,
        "y_threshold_skipped": skipped,
        "compute_elapsed_sec": elapsed,
        "top_5_contributions": [
            {
                "partition": r["partition"],
                "dim": r["dim"],
                "contribution": r["contribution"],
            }
            for r in sorted(rows, key=lambda r: abs(r["contribution"]), reverse=True)[:5]
        ],
    }


def main() -> int:
    q0 = float(Q_0_FLOAT)
    only_atom = sys.argv[1] if len(sys.argv) > 1 else None
    targets = [(l, Z, N) for (l, Z, N) in HEAVY_ATOMS
               if only_atom is None or l == only_atom]
    if not targets:
        print(f"unknown atom {only_atom!r}; choices: "
              f"{[l for l, *_ in HEAVY_ATOMS]}", file=sys.stderr)
        return 2

    results = []
    for label, Z, N in targets:
        try:
            r = compute_t1(label, Z, N, q0)
            results.append(r)
        except Exception as exc:
            import traceback
            print(f"\nFAILED {label}: {exc}", flush=True)
            traceback.print_exc()
            results.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "error": f"{type(exc).__name__}: {exc}",
            })

    builder = (
        WitnessBuilder(
            "heavy-atom-t1-extension", engine="numpy+scipy",
        )
        .set_description(
            "T1 = tr_M(β_atomic(Z, N)) for heavy atoms A ∈ "
            "{5..9}, closing the T1 witness gap that prevented "
            "paper_six_term_isotope_sweep from running for "
            "5Li/6Li/7Li/7Be/8Be/9Be. Per-irrep numeric Hoefsmit "
            "+ cached y_λ at q_0 — same machinery as F1-braid "
            "⁴He probe."
        )
        .set_content_block("def:atomic-braid")
        .add_parameter("q_0", q0)
        .add_parameter("y_threshold", Y_THRESHOLD)
        .add_data("results", results)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
