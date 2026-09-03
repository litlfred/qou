#!/usr/bin/env python3
"""Durable mpmath-only c₀ runner — computes Whitehead exact-root anchors
one N at a time, rewriting the witness after EACH N so partial progress
survives container reclamation (the hi-tower died at N=8 twice).

N=6, N=8 are seeded from the completed mpmath runs already in the log
(9 sig figs — ample for c₀ to ~1e-2); N=10, N=12 are computed here.
mpmath-only; no float64 in the c₀ number.  Audit-only.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_c0_mpmath import (  # noqa: E402
    whitehead_exact, fig8_exact_logJ, fit_c0, VOL_WHITEHEAD, VOL_4_1,
)

mp.mp.dps = 60
OUT = Path(__file__).resolve().parent / "whitehead-c0-mpmath.witness.json"

# All N recomputed fresh via the fast O(N⁸) path at dps=60 (the earlier
# dps=40/δ=1e-35 seeds were only ~4 digits — too coarse to keep).
SEED = {}


def write_witness(vals, note):
    Nw = sorted(vals)
    logw = [mp.log(vals[N]) for N in Nw]
    # figure-eight reference (exact) for validation
    Nf = [6, 8, 10, 12, 14]
    logf = [fig8_exact_logJ(N) for N in Nf]
    c0_fig = float(fit_c0(Nf[1:], logf[1:], VOL_4_1, nterms=2))  # N>=8 window
    fits = {}
    c0s = []
    if len(Nw) >= 2:
        c0s.append(float(fit_c0(Nw, logw, VOL_WHITEHEAD, nterms=1)))
        fits["1-term-all"] = c0s[-1]
    if len(Nw) >= 3:
        c0s.append(float(fit_c0(Nw[1:], logw[1:], VOL_WHITEHEAD, nterms=1)))
        fits["1-term-Nge8"] = c0s[-1]
        c0s.append(float(fit_c0(Nw, logw, VOL_WHITEHEAD, nterms=2)))
        fits["2-term-all"] = c0s[-1]
    c0_mean = sum(c0s) / len(c0s) if c0s else float("nan")
    c0_spread = (max(c0s) - min(c0s)) / 2 if len(c0s) > 1 else float("nan")
    factor = float(mp.e ** (2 * (mp.mpf(str(c0_mean)) + mp.mpf("0.87")))) if c0s else float("nan")
    nearest = min([1, 2, 4], key=lambda f: abs(factor - f)) if c0s else None
    w = {
        "description": "Whitehead c₀/factor from mpmath EXACT-ROOT values only (no float64). Reconstruction of a lost session.",
        "computation": "whitehead_c0_run",
        "audit_only": True,
        "precision": "mpmath dps=40 exact-root; no float64 in the c0 determination",
        "whitehead_braid_word": "[1,-2,1,-2,1]",
        "vol_4G": str(VOL_WHITEHEAD),
        "p_fixed": 1.5,
        "figure_eight_reference_c0_Nge8": c0_fig,
        "figure_eight_target_minus_quarter_ln3": float(-mp.log(3) / 4),
        "whitehead_exact_values": {str(N): float(vals[N]) for N in Nw},
        "whitehead_c0_fits": fits,
        "whitehead_c0_mean": c0_mean,
        "whitehead_c0_spread": c0_spread,
        "factor": factor,
        "nearest_factor": nearest,
        "progress_note": note,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    w.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        w, script_path=__file__, engine=None, q0_anchor=False)
    OUT.write_text(json.dumps(w, indent=2))
    print(f"    witness updated ({note}): c0_mean={c0_mean:.4f} factor={factor:.2f} -> factor {nearest}", flush=True)


def main() -> int:
    vals = dict(SEED)
    for N in (6, 8, 10, 12):
        t = time.monotonic()
        print(f"  computing Whitehead mpmath exact N={N} …", flush=True)
        vals[N] = whitehead_exact(N)
        print(f"    N={N}: |J_red|={float(vals[N]):.8e}  ({time.monotonic()-t:.0f}s)", flush=True)
        write_witness(vals, f"through N={N}")
    print("  DONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
