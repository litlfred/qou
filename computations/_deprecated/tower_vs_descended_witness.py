#!/usr/bin/env python3
"""
P2.1a small-optimization witness — descended-only vs full-tower

Calls the existing tower_mass_symbolic_eval in crt_markov.py for
several atoms (D, ⁴He, ¹²C, ⁴⁰Ca) and reports the four mass-tower
components per `prop:mass-endomorphism-tower`:

    𝔪 = |Π V̂_i|                      (descended, level 0)
       + Σ_i Φ_q(|V̂_i|)                (single-generator tower)
       + z² Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|) (adjacent-pair tower)

V̂_i = w_sym · V_sym + w_std · V_s + w_alt · V_alt is the full
Wedderburn-traced volume at H_3 weights.

This complements `deuteron_error.py` (which is intentionally
descended-only as a level-3 pair-coupling test) by exposing the
tower contribution for atoms beyond D, where the descended term
alone leaves ~0.04–0.91% mass error per AUDIT-crt-k-level.md.

Caveat: H_3 weights are used (not H_{3A}). The H_{3A} replacement
is workplan task P2.2 (CRT polynomial reconstruction at higher k).

Witness: docs/audits/2026-05-01-p2-1a-tower-vs-descended.witness.json
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from crt_markov import (
    markov_trace_symbolic_eval,
    tower_mass_symbolic_eval,
)
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))

# Test atoms — light enough that tower_mass_symbolic_eval converges
# without polynomial explosion at H_3 weights.
ATOMS = [
    ("D", 1, 1, True, 1, 1, 1),
    ("3He", 2, 1, True, 1, 1, 1),
    ("4He", 2, 2, True, 1, 1, 1),
    ("12C", 6, 6, True, 1, 1, 1),
    ("16O", 8, 8, True, 1, 1, 1),
    ("40Ca", 20, 20, True, 1, 1, 1),
]


def report_atom(name, Z, N, include_inter, m_pp, m_pn, m_nn):
    """Return descended-only and full-tower for one atom."""
    desc_only = abs(markov_trace_symbolic_eval(
        Z, N, include_inter, m_pp, m_pn, m_nn, q0, precision=50))

    full = tower_mass_symbolic_eval(
        Z, N, include_inter, m_pp, m_pn, m_nn, q0, precision=50)

    desc = full["desc"]
    single = full["single"]
    cross = full["cross"]
    total = full["total"]

    # Tower contribution as fraction of descended term
    if desc != 0 and not mpmath.isinf(total):
        single_pct = float(single / desc) * 100 if not mpmath.isinf(single) else float("inf")
        cross_pct = float(cross / desc) * 100 if not mpmath.isinf(cross) else float("inf")
        total_over_desc = float(total / desc) if not mpmath.isinf(total) else float("inf")
    else:
        single_pct = cross_pct = total_over_desc = float("nan")

    return {
        "atom": name,
        "Z": Z, "N": N, "A": Z + N,
        "descended_only": str(desc_only),
        "tower": {
            "desc": str(desc),
            "single": str(single) if not mpmath.isinf(single) else "inf",
            "cross": str(cross) if not mpmath.isinf(cross) else "inf",
            "total": str(total) if not mpmath.isinf(total) else "inf",
        },
        "tower_contribution_pct_of_desc": {
            "single": single_pct,
            "cross": cross_pct,
            "total_ratio": total_over_desc,
        },
    }


print("=" * 78)
print("Descended-only vs full-tower mass — H_3 Wedderburn weights")
print("=" * 78)
print(f"q_0 = {q0}")
print()
print(f"  {'atom':>6} {'A':>4} {'descended':>22} {'+single%':>10} {'+cross%':>9} {'total/desc':>11}")
print("  " + "-" * 76)

results = []
for name, Z, N, include_inter, m_pp, m_pn, m_nn in ATOMS:
    try:
        r = report_atom(name, Z, N, include_inter, m_pp, m_pn, m_nn)
    except Exception as e:
        r = {
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "error": str(e),
        }
    results.append(r)
    if "error" in r:
        print(f"  {name:>6} {r['A']:>4} ERROR: {r['error'][:50]}")
    else:
        single_pct = r["tower_contribution_pct_of_desc"]["single"]
        cross_pct = r["tower_contribution_pct_of_desc"]["cross"]
        total_over_desc = r["tower_contribution_pct_of_desc"]["total_ratio"]
        desc_str = r["tower"]["desc"][:22]
        print(
            f"  {name:>6} {r['A']:>4} {desc_str:>22} "
            f"{single_pct:>9.3f}% {cross_pct:>8.3f}% {total_over_desc:>11.4f}"
        )

# Witness JSON
witness = {
    "audit": "P2.1a — descended-only vs full-tower (H_3 weights)",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "wedderburn_weights": "H_3 (not H_{3A} — see workplan P2.2 for H_{3A} replacement)",
    "atoms": results,
    "interpretation": (
        "Per AUDIT-crt-k-level.md: live compute uses descended-only "
        "by default; the tower contribution (single + cross terms) is "
        "the missing piece. This witness exposes the tower for several "
        "atoms so callers can see the magnitude of the gap. The H_3 "
        "weights are an approximation; H_{3A} weights via CRT polynomial "
        "reconstruction is the deeper task (workplan P2.2)."
    ),
}

out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-p2-1a-tower-vs-descended.witness.json"
out_path.write_text(json.dumps(witness, indent=2))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
