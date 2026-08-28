#!/usr/bin/env python3
"""Extend the Whitehead exact-root tower to N=14 (best-effort N=16) to pin
the growth exponent p — the blocker for the exact-prefactor derivation.

Context: the reported factor-2 (c₀=−0.53) assumes p=3/2, the figure-eight
KNOT exponent.  The Whitehead is a 2-cusp LINK; a control fit shows the
figure-eight recovers p≈3/2 from N=6..16 while the Whitehead's N=6..12 fit
reads a different exponent — so p is not pinned and the exact prefactor
(hence the exact factor) is contingent on it.  More N constrains p.

Reuses N=6,8,10,12 from whitehead-c0-mpmath.witness.json; computes N=14
(≈48 min) then N=16, checkpointing after each so a reclaim keeps N=14.
mpmath-only, dps=60, fast O(N⁸) path.  Audit-only.
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
from whitehead_c0_mpmath import whitehead_exact, VOL_WHITEHEAD  # noqa: E402

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
SRC = HERE / "whitehead-c0-mpmath.witness.json"
OUT = HERE / "whitehead-p-exponent.witness.json"


def pfit(vals):
    """Fit log|J| = (V/2π)N + p·logN + c₀ + d/N (+e/N²); return (p, c₀)."""
    import numpy as np
    Ns = sorted(vals)
    A = VOL_WHITEHEAD / (2 * math.pi)
    # cast mpmath values to float — np.linalg.lstsq rejects object dtype
    y = np.array([float(mp.log(vals[N])) - A * N for N in Ns], dtype=float)
    nt = 2 if len(Ns) >= 4 else 1
    cols = [[math.log(N) for N in Ns], [1.0] * len(Ns)] + \
           [[1.0 / N**j for N in Ns] for j in range(1, nt + 1)]
    M = np.array(cols, dtype=float).T
    c, *_ = np.linalg.lstsq(M, y, rcond=None)
    return c[0], c[1]


def write(vals, note):
    p, c0 = pfit(vals) if len(vals) >= 3 else (float("nan"), float("nan"))
    w = {
        "description": "Whitehead growth-exponent p extension (N up to 14/16) — pins whether the refined-VC exponent is the knot 3/2 or a distinct 2-cusp-link value; gates the exact-prefactor derivation.",
        "computation": "whitehead_p_extend",
        "audit_only": True,
        "precision": "mpmath dps=60 exact-root, fast O(N^8)",
        "whitehead_exact_values": {str(N): float(vals[N]) for N in sorted(vals)},
        "p_free_fit": p,
        "c0_at_p_free": c0,
        "note": note,
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
    print(f"    [{note}] N={sorted(vals)} p_free={p:.4f} c0={c0:.4f}", flush=True)


def main() -> int:
    vals = {int(k): mp.mpf(str(v))
            for k, v in json.loads(SRC.read_text())["whitehead_exact_values"].items()}
    print(f"seed N={sorted(vals)} from merged witness", flush=True)
    for N in (14, 16):
        t = time.monotonic()
        print(f"  computing exact N={N} …", flush=True)
        vals[N] = whitehead_exact(N)
        print(f"    N={N}: |J_red|={float(vals[N]):.8e} ({time.monotonic()-t:.0f}s)", flush=True)
        write(vals, f"through N={N}")
    print("  DONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
