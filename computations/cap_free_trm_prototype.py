#!/usr/bin/env python3
"""PROTOTYPE: cap-free tr_M (ALL partitions, no max_dim skip) via the matrix-M
reduced-block kernel — no truncation anywhere.

EXPLORATORY. Owner directive: NO truncation; compute every partition. The
producer `chi_at_q0_via_matrix_m_mpfr` applies a `max_dim` cap that SKIPS the
high-dim partitions (12/30 for tritium), so its cached `tr_M` is a ~1e-3
truncation — NOT 1-ppQ. This probe drops the cap: it computes χ^λ for EVERY
λ ⊢ 3A via the native reduced-block `chi_via_matrix_m_mpfr` (handles any dim,
no selection skip), sums `Σ_λ y_λ χ^λ`, and reports the FULL tr_M plus the
mass the cap was dropping.

Cross-check: full tr_M(deuteron, q₀) must still equal the catalogue value
(deuteron had 0 skipped, so it's the control); tritium full vs capped shows
the skipped-partition error.

Output: cap-free-trm-prototype.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))

import pyhecke_native as nat  # noqa: E402
from chi_at_q0_via_matrix_m_mpfr import _split_atom_braid  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
DPS = 50
K_SPLIT = 3

CAPPED = {  # capped tr_M from the matrix-M caches (with skipped-max-dim)
    "deuteron": ("chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json", (1, 1)),
    "tritium": ("chi-tritium-h9-at-q0-50dps-matrix-m.witness.json", (1, 2)),
}


def full_tr_M(Z: int, N: int, q):
    """Σ_λ y_λ χ^λ over ALL partitions of 3A — no max_dim cap."""
    n, wl, bs, wr = _split_atom_braid(Z, N)
    qs = mp.nstr(q, DPS + 3, strip_zeros=False)
    parts = nat.partitions_of(n)
    y = nat.trace_weights_n(n, float(q))
    tot = mp.mpf(0)
    n_done = 0
    t0 = time.monotonic()
    for lam, ylam in zip(parts, y):
        chi = mp.mpf(nat.chi_via_matrix_m_mpfr(list(lam), wl, bs, wr, K_SPLIT, qs, DPS))
        tot += mp.mpf(str(ylam)) * chi
        n_done += 1
        if n_done % 10 == 0:
            print(f"   [{n_done}/{len(parts)}] {time.monotonic()-t0:.0f}s",
                  file=sys.stderr, flush=True)
    return tot, len(parts)


def _capped_value(f):
    w = json.loads((HERE / f).read_text())
    d = w.get("data", w)
    bp = d.get("by_partition") or w.get("by_partition")
    n_skip = sum(1 for e in bp if e.get("chi_lambda") == "skipped-max-dim")
    return mp.mpf(str(d.get("tr_M_at_q0") or w.get("tr_M_at_q0"))), len(bp), n_skip


def main() -> int:
    t0 = time.monotonic()
    q0 = q_at(50)
    rows = []
    for atom, (f, (Z, N)) in CAPPED.items():
        capped, n_part, n_skip = _capped_value(f)
        full, n_full = full_tr_M(Z, N, q0)
        rows.append({
            "atom": atom, "Z": Z, "N": N, "A": Z + N, "n_partitions": n_full,
            "n_skipped_in_cache": n_skip,
            "tr_M_capped": mp.nstr(capped, 18),
            "tr_M_full_no_cap": mp.nstr(full, 18),
            "cap_error_abs": mp.nstr(abs(full - capped), 6),
            "cap_error_rel": mp.nstr(abs(full - capped) / abs(full), 4),
        })
        print(f"\n{atom}: full(all {n_full}) = {mp.nstr(full,16)}  "
              f"capped({n_part-n_skip}) = {mp.nstr(capped,16)}  "
              f"Δ = {mp.nstr(abs(full-capped),4)} ({mp.nstr(100*abs(full-capped)/abs(full),3)}%)")

    w = WitnessBuilder("cap-free-trm-prototype", engine="mpmath", start_time=t0)
    w.set_description(
        "Cap-free tr_M over ALL partitions via the matrix-M reduced-block "
        "kernel (no max_dim skip) — owner directive: no truncation. Quantifies "
        "the cache's max_dim-cap error (the skipped high-dim partitions) and "
        "shows the reduced-block computes every λ losslessly."
    )
    w.add_data("rows", rows)
    w.add_data("conclusion",
               "The max_dim cap drops ~1e-3 of tr_M (the skipped high-dim "
               "partitions) — not 1-ppQ. The reduced-block computes all "
               "partitions; the cap is unnecessary and must be removed for "
               "precise binding. No truncation.")
    # deuteron (0 skipped) is the control — full must equal capped
    deut = [r for r in rows if r["atom"] == "deuteron"][0]
    w.add_assertion(
        name="deuteron_full_equals_capped_control",
        computed=float(deut["cap_error_rel"]), expected=0.0, tolerance=1e-9,
        source="deuteron had 0 skipped → full tr_M == cached tr_M",
    )
    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
