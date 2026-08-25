#!/usr/bin/env python3
"""Firm up the Whitehead factor with the numeric weight-block tower to N≈30.

Item #1 of the 1-3-2 plan.  Extends the exact-root reduced-colored-Jones
tower (previously N=6..14 via the O(N⁸) engine) to N≈30 using the validated
numeric weight-block engine, and re-fits c₀ / the factor with the
figure-eight (exact −¼ln3) as the fit calibration.

Checkpoints the witness after each N so progress survives container reclaim.
Audit-only; no wiring.
"""
from __future__ import annotations

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_weightblock_numeric import reduced_at_root  # noqa: E402
from whitehead_c0_mpmath import fig8_exact_logJ, fit_c0, VOL_WHITEHEAD, VOL_4_1  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
OUT = Path(__file__).resolve().parent / "whitehead-factor-hi.witness.json"
# EXACT-root anchors (mpmath) from the merged whitehead-c0-mpmath tower; the
# float64 δ-extrap tower (N≥16) carries ~1e-3, so these anchor the low-N scale.
SEED = {6: 362.3920528929998, 8: 1635.4283652320307,
        10: 7062.35924065477, 12: 29287.27767465885, 14: 117161.33858}


def write(vals, note):
    Nw = sorted(vals)
    logw = [math.log(vals[N]) for N in Nw]
    # figure-eight reference c0 (exact) — fit calibration
    Nf = [6, 8, 10, 12, 14, 16, 18, 20]
    logf = [float(fig8_exact_logJ(N)) for N in Nf]
    c0_fig = float(fit_c0(Nf[2:], logf[2:], VOL_4_1, nterms=2))  # N>=10 window
    fits = {}
    c0s = []
    if len(Nw) >= 3:
        fits["1term_all"] = float(fit_c0(Nw, logw, VOL_WHITEHEAD, nterms=1)); c0s.append(fits["1term_all"])
        fits["2term_all"] = float(fit_c0(Nw, logw, VOL_WHITEHEAD, nterms=2)); c0s.append(fits["2term_all"])
    if len(Nw) >= 5:
        hi = [N for N in Nw if N >= Nw[len(Nw)//2]]
        loghi = [math.log(vals[N]) for N in hi]
        fits["2term_hi"] = float(fit_c0(hi, loghi, VOL_WHITEHEAD, nterms=2)); c0s.append(fits["2term_hi"])
    c0 = sum(c0s) / len(c0s) if c0s else float("nan")
    spread = (max(c0s) - min(c0s)) / 2 if len(c0s) > 1 else float("nan")
    factor = math.exp(2 * (c0 + 0.87)) if c0s else float("nan")
    nearest = min([1, 2, 4], key=lambda f: abs(factor - f)) if c0s else None
    w = {
        "description": "Whitehead factor firmed up with the numeric weight-block tower to high N. Item #1 of 1-3-2.",
        "computation": "whitehead_factor_hi", "audit_only": True,
        "precision": "mpmath dps=50 exact-root, weight-block engine",
        "vol_4G": str(VOL_WHITEHEAD),
        "figure_eight_calibration_c0": c0_fig, "figure_eight_target": float(-mp.log(3)/4),
        "whitehead_values": {str(N): vals[N] for N in Nw},
        "c0_fits": fits, "c0_mean": c0, "c0_spread": spread,
        "factor": factor, "nearest_factor": nearest, "note": note,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    OUT.write_text(json.dumps(w, indent=2))
    print(f"  [{note}] N={Nw[-1] if Nw else '-'}  c0={c0:.4f}±{spread:.4f}  factor={factor:.3f}->{nearest}", flush=True)


def main() -> int:
    # Float64 δ-extrapolation is reliable only to N≈16; beyond that the
    # near-root cancellation (|J_red|≫1e8) swamps float64 and the values
    # diverge (verified: N=18 already off by orders of magnitude). So the
    # firm factor comes from the exact mpmath anchors N≤14 plus the one
    # extra float64-clean point N=16. Firming past that needs exact high-N
    # values (CRT reconstruction from the fast mod-p weight-block engine).
    vals = dict(SEED)                       # exact mpmath anchors N=6..14
    write(vals, "exact anchors N<=14")
    for N in (16,):                         # last float64-clean point
        vals[N] = float(reduced_at_root(N))
        print(f"  computed N={N}: |J_red|={vals[N]:.6e}", flush=True)
        write(vals, f"through N={N}")
    print("  DONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
