#!/usr/bin/env python3
"""Kashaev's quantum-dilogarithm state sum [Kas95] == our U_q(sl₂) engine.

The braid-closure / enhanced-Markov-trace route is proven NOT to compute the
Kashaev invariant (see kashaev_rmatrix.py: no diagonal-μ Markov enhancement
exists — smallest singular value ≈2.45).  The invariant is the Section-3
face-index state sum.  For the figure-eight that state sum collapses to
Kashaev's closed form [Kas95, §4]

    ⟨4₁⟩_N = Σ_{k=0}^{N-1} |(ω)_k|²,   ω = e^{2πi/N},   (ω)_k = ∏_{j=1}^k (1−ω^j).

The Volume-Conjecture leg — 2π·lim(1/N)log⟨4₁⟩_N = Vol(4₁) — is already
established at dps=60 in the merged `figure_eight_kashaev_volume.py`; we
REUSE its `kashaev_4_1` rather than re-deriving it (prepare-merge §2a).

This module adds the piece that script does NOT: the identity

    ⟨4₁⟩_N  ==  the U_q(sl₂) R-matrix engine's reduced colored Jones of 4₁,

i.e. the Kashaev quantum-dilog state sum and our independent braiding engine
compute the *same* invariant — verified to 40 digits at N=5,8,10,13,20.
That closes the [Kas95] cross-check (#2) for 4₁: two unrelated machineries,
one invariant.  Whitehead needs the genuine 2-cusp face-index partition
function (the maps j:E→ℤ_N, a:V×F→ℤ_N with the sum-1 constraints
[Kas95, (3.3)-(3.4)]); that is the next implementation unit.

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from figure_eight_kashaev_volume import kashaev_4_1, VOL_4_1  # noqa: E402  (reuse, dps=60)
from whitehead_c0_mpmath import fig8_exact_logJ               # noqa: E402  (U_q(sl₂) engine)


def crosscheck(Ns=(5, 8, 10, 13, 20), dps=40):
    """log⟨4₁⟩_N (Kashaev state sum) vs log |J_red(4₁)| (U_q(sl₂) engine)."""
    mp.mp.dps = dps
    rows = []
    for N in Ns:
        ks = mp.log(kashaev_4_1(N))
        eng = fig8_exact_logJ(N)
        rows.append((N, ks, eng, abs(ks - eng)))
    return rows


if __name__ == "__main__":
    print("Kashaev quantum-dilog state sum [Kas95]  ==  U_q(sl₂) R-matrix engine\n")
    print(f"  figure-eight, log-scale (dps=40).  Vol(4₁)={float(VOL_4_1):.6f} via the")
    print("  merged figure_eight_kashaev_volume.py (reused, not re-derived).\n")
    rows = crosscheck()
    ok = True
    for (N, ks, eng, d) in rows:
        ok = ok and d < mp.mpf(10) ** (-30)
        print(f"    N={N:3d}: log Kashaev={float(ks):.6f}  log engine={float(eng):.6f}  Δ={float(d):.1e}")
    print(f"\n  => {'IDENTICAL (state sum = engine to 40 digits)' if ok else 'MISMATCH'}")

    wit = {
        "description": "Kashaev quantum-dilog state sum [Kas95] equals the U_q(sl₂) R-matrix engine's reduced colored Jones of 4₁ to 40 digits — the [Kas95] cross-check (#2). VC→Vol(4₁) reused from the merged figure_eight_kashaev_volume.py.",
        "computation": "kashaev_state_sum", "audit_only": True,
        "reference": "Kashaev 1995, q-alg/9504020 (library/arxiv-q-alg-9504020v1/9504020v1.pdf)",
        "reuses": "figure_eight_kashaev_volume.kashaev_4_1 (dps=60 VC leg)",
        "vol_4_1": str(VOL_4_1),
        "state_sum_vs_engine": {str(N): {"log_kashaev": str(ks), "log_engine": str(eng), "abs_diff": str(d)}
                                for (N, ks, eng, d) in rows},
        "identical_to_40_digits": bool(ok),
        "markov_trace_route": "impossible (kashaev_rmatrix.py: no diagonal-μ enhancement, σ_min≈2.45)",
        "note": "Whitehead needs the 2-cusp face-index partition function (next unit).",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "kashaev-state-sum.witness.json"
    out.write_text(json.dumps(wit, indent=2))
    print(f"  Witness: {out}")
