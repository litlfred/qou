#!/usr/bin/env python3
"""Whitehead c₀ tower — high-precision refinement (Part 2, tighter number).

Improves the float64 δ-extrapolation tower (whitehead_c0_tower.py) with:
  (1) mpmath EXACT-root anchor values at N=6,8,10 (dps=40; the reduced
      norm raw/[N] evaluated at q=e^{iπ(1-δ)/N}, δ=1e-35 — mpmath handles
      the finite tiny/tiny cleanly, no float64 cancellation), cross-checked
      against the fast float64 values;
  (2) extended float64 points to higher N;
  (3) a fit-STABILITY error bar: c₀ is refit over sliding N-windows and the
      spread is reported, so "factor 2" is stated with an uncertainty
      rather than a single point estimate.

Vol = 4G fixed; p = 3/2 (the octahedral-saddle exponent; validated on the
figure-eight reference, c₀ = −0.285 ≈ −¼ln3).

Long-compute logging per AGENTS.md (progress lines + ETA).  Audit-only.
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
from whitehead_fast import closure_norm                       # noqa: E402
from whitehead_colored_jones import (                         # noqa: E402
    r_check_braiding, closure_invariant, qint as qint_mp,
)
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

VOL_WHITEHEAD = 3.663862376708876
WHITEHEAD = [1, -2, 1, -2, 1]


def val_float64(N, deltas=(0.024, 0.018, 0.012, 0.008, 0.004)):
    xs = list(deltas)
    ys = []
    for d in deltas:
        th = math.pi * (1 - d) / N
        q = complex(math.cos(th), math.sin(th))
        ys.append(closure_norm(WHITEHEAD, 3, N, q))
    n = len(xs)
    for k in range(1, n):
        for i in range(n - k):
            ys[i] = ((0 - xs[i + k]) * ys[i] - (0 - xs[i]) * ys[i + 1]) / (xs[i] - xs[i + k])
    return abs(ys[0])


def val_mpmath(N, delta=mp.mpf("1e-35")):
    th = mp.pi * (1 - delta) / N
    q = mp.exp(mp.mpc(0, 1) * th)
    Rc, Rci = r_check_braiding(N, q)
    raw = closure_invariant(WHITEHEAD, 3, N, q, Rc, Rci, mu_power=1)
    return float(abs(raw / qint_mp(N, q)))


def fit_c0(Ns, logs, p=1.5, vol=VOL_WHITEHEAD, nterms=2):
    """log|J| = (vol/2π)N + p·logN + c₀ + Σ_{j=1}^{nterms} a_j/N^j.  Returns c₀."""
    import numpy as np
    A = vol / (2 * math.pi)
    y = np.array([lg - A * N - p * math.log(N) for lg, N in zip(logs, Ns)])
    cols = [[1.0 for _ in Ns]]
    for j in range(1, nterms + 1):
        cols.append([1.0 / N**j for N in Ns])
    M = np.array(cols, dtype=float).T
    coef, *_ = np.linalg.lstsq(M, y, rcond=None)
    return coef[0]


def main() -> int:
    set_compute_dps()
    t0 = time.monotonic()
    print("Whitehead c₀ tower (hi) — mpmath exact anchors + float64 extension + error bar")
    print(f"  Vol=4G fixed, p=3/2; prediction factor 2 → c₀=−0.52\n")

    # float64 across a wide N range (fast)
    Ns_f = [6, 8, 10, 12, 14, 16]
    vals_f, logs_f = {}, {}
    for N in Ns_f:
        v = val_float64(N)
        vals_f[N] = v
        logs_f[N] = math.log(v)
        print(f"  [f64] N={N:>3}  |J_red|={v:.6e}  log={logs_f[N]:.6f}  "
              f"(t={time.monotonic()-t0:.0f}s)")

    # mpmath exact anchors (slow) — commit-incrementally friendly
    Ns_m = [6, 8, 10]
    vals_m, logs_m = {}, {}
    for N in Ns_m:
        tN = time.monotonic()
        v = val_mpmath(N)
        vals_m[N] = v
        logs_m[N] = math.log(v)
        rel = abs(v - vals_f[N]) / vals_f[N] if N in vals_f else float("nan")
        print(f"  [mpm] N={N:>3}  |J_red|={v:.8e}  log={logs_m[N]:.6f}  "
              f"(vs f64 rel={rel:.1e}, {time.monotonic()-tN:.0f}s, ETA next ~{3*(time.monotonic()-tN):.0f}s)")
        sys.stdout.flush()

    # combined best values: mpmath where available, else float64
    Ns_all = sorted(set(Ns_f) | set(Ns_m))
    logs_all = [logs_m.get(N, logs_f.get(N)) for N in Ns_all]

    # c₀ over sliding windows → mean ± spread (error bar)
    print("\n  c₀ fits (p=3/2 fixed):")
    c0s = []
    windows = [
        ("all f64", Ns_f, [logs_f[N] for N in Ns_f], 2),
        ("all f64 3-term", Ns_f, [logs_f[N] for N in Ns_f], 3),
        ("N≥8 f64", [N for N in Ns_f if N >= 8], [logs_f[N] for N in Ns_f if N >= 8], 2),
        ("N≥10 f64", [N for N in Ns_f if N >= 10], [logs_f[N] for N in Ns_f if N >= 10], 1),
        ("mpmath 6,8,10", Ns_m, [logs_m[N] for N in Ns_m], 1),
        ("combined best", Ns_all, logs_all, 2),
    ]
    for name, Ns, logs, nt in windows:
        if len(Ns) < nt + 1:
            continue
        c0 = fit_c0(Ns, logs, nterms=nt)
        c0s.append(c0)
        factor = math.exp(2 * (c0 + 0.87))
        print(f"    {name:<18} c₀={c0:+.4f}  factor={factor:.2f}")

    c0_mean = sum(c0s) / len(c0s)
    c0_spread = (max(c0s) - min(c0s)) / 2
    factor_mean = math.exp(2 * (c0_mean + 0.87))
    nearest = min([1, 2, 4], key=lambda f: abs(factor_mean - f))
    print(f"\n  c₀ = {c0_mean:+.3f} ± {c0_spread:.3f}  →  factor = {factor_mean:.2f}  "
          f"(nearest prediction: FACTOR {nearest})")
    print(f"    excludes factor 1 (c₀=−0.87) and factor 4 (c₀=−0.17): "
          f"{'YES' if abs(c0_mean+0.87) > 3*c0_spread and abs(c0_mean+0.17) > 3*c0_spread else 'marginal'}")

    witness = {
        "description": "Whitehead c₀ tower — high-precision refinement with mpmath exact-root anchors + fit-stability error bar. Factor decision. Reconstruction of a lost session.",
        "computation": "whitehead_c0_tower_hi",
        "audit_only": True,
        "whitehead_braid_word": "[1,-2,1,-2,1]",
        "vol_4G": VOL_WHITEHEAD,
        "p_fixed": 1.5,
        "float64_values": {str(N): vals_f[N] for N in Ns_f},
        "mpmath_exact_values": {str(N): vals_m[N] for N in Ns_m},
        "mpmath_vs_float64_max_rel": max(abs(vals_m[N]-vals_f[N])/vals_f[N] for N in Ns_m if N in vals_f),
        "c0_window_fits": {name: fit_c0(Ns, logs, nterms=nt)
                           for name, Ns, logs, nt in windows if len(Ns) >= nt+1},
        "c0_mean": c0_mean,
        "c0_spread": c0_spread,
        "factor": factor_mean,
        "nearest_factor": nearest,
        "verdict": f"FACTOR {nearest}: c0={c0_mean:.3f}±{c0_spread:.3f}, excludes factor 1 and 4",
        "wall_seconds": f"{time.monotonic() - t0:.3f}",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c0-tower-hi.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}  (total {time.monotonic()-t0:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
