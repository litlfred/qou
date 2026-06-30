#!/usr/bin/env python3
"""b0vf — complete the ⁴He H₁₂ per-λ χ witness at the muon q₀ pin.

Computes all 77 partitions of S₁₂ for the colour-weighted averaged
atomic braid word β_atomic(2,2) via the {σ, drop} branch decomposition
(see `_b0vf_chi_branch_decomp.py`) and the canonical Rust seminormal
kernel `pyhecke_native.chi_lambda_all_partitions_mpfr` (correct at
q≠1).  This reproduces EXACTLY the convention of the pure-Python
Hoefsmit producer `chi_at_q0_via_hoefsmit_mpfr.py` (validated on the
deuteron to 5e-50 and on the 27 already-cached ⁴He partitions), but in
minutes instead of the multi-week dim≈5600 mpmath grind.

GATES (must all pass or NO write):
  1. the 27 already-cached partitions reproduce to < 1e-40 rel,
  2. Σ_λ y_λ χ_λ over all 77 matches the independent markov-peel
     scalar tr_M(⁴He) = 0.055358426266783106… to < 1e-30 rel.

Output: rewrites `chi-helium-4-h12-at-q0-50dps.witness.json` in place,
preserving the existing schema (adds producer provenance; flips
partial→False; drops the known_incomplete_note).  Same muon q₀ pin as
the input — NOT a cross-pin migration.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import _b0vf_chi_branch_decomp as bd  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402

WITNESS = HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"
MARKOV_PEEL = mp.mpf("0.055358426266783106469852047498437740316331036735298")


def main() -> int:
    mp.mp.dps = 60
    pw = json.loads(WITNESS.read_text())
    q_str = pw["q_0_50dps"]
    n = 12
    print(f"⁴He H12 completion @ muon q0={q_str[:20]}… (dps=50)", flush=True)

    t0 = time.time()
    chi_total, _ = bd.chi_by_branch(2, 2, q_str, dps=50, verbose=True)
    elapsed = time.time() - t0
    print(f"computed {len(chi_total)} partitions in {elapsed:.1f}s", flush=True)
    assert len(chi_total) == 77, f"expected 77, got {len(chi_total)}"

    # GATE 1 — 27 cached partitions
    stored = {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
              for e in pw["by_partition"]}
    worst = mp.mpf(0)
    for lam, cs in stored.items():
        rel = abs(chi_total[lam] - cs) / (abs(cs) if cs != 0 else mp.mpf(1))
        worst = max(worst, rel)
    print(f"GATE 1 — 27 cached partitions worst rel-err = {mp.nstr(worst,4)}",
          flush=True)
    assert worst < mp.mpf(10) ** (-40), "GATE 1 FAILED (cached mismatch)"

    # GATE 2 — full Σ y_λ χ_λ vs markov-peel
    y = _load_y_lambda(n, None)
    parts = sorted(chi_total.keys(), key=lambda p: (len(p), p), reverse=False)
    s = mp.mpf(0)
    by_partition = []
    for lam in parts:
        chi = chi_total[lam]
        y_lam = mp.mpf(str(y[lam]))
        contrib = y_lam * chi
        s += contrib
        by_partition.append({
            "partition": list(lam),
            "y_lambda": mp.nstr(y_lam, 50),
            "chi_lambda": mp.nstr(chi, 50),
            "contribution": mp.nstr(contrib, 50),
        })
    rel_mp = abs(s - MARKOV_PEEL) / abs(MARKOV_PEEL)
    print(f"GATE 2 — Σ y_λ χ_λ (77/77) = {mp.nstr(s,30)}", flush=True)
    print(f"         markov-peel        = {mp.nstr(MARKOV_PEEL,30)}", flush=True)
    print(f"         rel gap            = {mp.nstr(rel_mp,4)}", flush=True)
    assert rel_mp < mp.mpf(10) ** (-30), "GATE 2 FAILED (markov-peel mismatch)"

    # Both gates passed — rewrite witness in place.
    payload = {
        "computation": "chi-helium-4-h12-at-q0-50dps",
        "description": (
            "Numerical χ^λ_q(β_atomic(2, 2)) = helium-4 per partition λ ⊢ 12, "
            "evaluated at q = q_0 at 50 dps. Colour-weighted averaged-crossing "
            "convention (identical to chi_at_q0_via_hoefsmit_mpfr.py). Completed "
            "77/77 via the {σ, drop} branch decomposition of the single colour-"
            "weighted crossing + the canonical Rust seminormal kernel "
            "pyhecke_native.chi_lambda_all_partitions_mpfr (correct at q≠1). "
            "Validated: the 27 previously-cached Hoefsmit partitions reproduce "
            "to <1e-40, and Σ_λ y_λ χ_λ matches the independent markov-peel "
            "scalar tr_M to the rel gap reported in _provenance."
        ),
        "q_0_50dps": q_str,
        "dps": 50,
        "n_strands": n,
        "atom": "helium-4",
        "Z": 2, "N": 2,
        "n_partitions": len(by_partition),
        "n_partitions_total": 77,
        "partial": False,
        "convention": "colour-weighted-averaged-crossing",
        "producer": "branch-decomp + chi_lambda_all_partitions_mpfr",
        "compute_time_sec": round(elapsed, 2),
        "tr_M_at_q0": mp.nstr(s, 50),
        "by_partition": by_partition,
        "_provenance": {
            "engine": "pyhecke_native",
            "rust_fn": "chi_lambda_all_partitions_mpfr",
            "method": "branch_decomposition_colour_weighted_crossing",
            "n_branches": 2,
            "gate1_cached27_worst_rel": mp.nstr(worst, 4),
            "gate2_markov_peel_rel_gap": mp.nstr(rel_mp, 4),
            "markov_peel_scalar": mp.nstr(MARKOV_PEEL, 50),
            "bean": "b0vf",
        },
    }
    WITNESS.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"WROTE {WITNESS.name} — 77/77, partial=False", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
