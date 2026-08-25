#!/usr/bin/env python3
"""Numerical witness for Part A of conj:dilogarithm-archimedean-limit.

Confirms the elementary result proved in
docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md:
for fixed x in (0,1), on the convergence side q -> 1^-,

    (1 - q) * log Phi_n(x; q)  ->  Li_2(x),

with log Phi_n(x; q) = - sum_{k=0}^{n-1} log(1 - x q^k), along the
Faddeev scaling q = e^{-eps}, n = ceil(C / eps) so that n*eps -> infty.

The proof predicts the error is dominated by the monotone Riemann-sum
bound  eps * (-log(1-x))  plus the exponential tail  (x/(1-x)) e^{-n eps}.
With C large the tail is negligible, so the error should fall ~linearly
in eps. This script checks exactly that and emits a witness JSON.
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json
import math
import os
import subprocess
import sys
from datetime import datetime, timezone

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

C = mp.mpf(30)  # n = ceil(C/eps); n*eps ~ 30 so tail ~ e^{-30} ~ 1e-13
XS = [mp.mpf("0.2"), mp.mpf("0.5"), mp.mpf("0.8")]
EPS = [mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-4")]


def rescaled_log_partial_product(x, eps):
    """(1 - q) * log Phi_n(x; q) with q = e^{-eps}, n = ceil(C/eps)."""
    q = mp.e ** (-eps)
    n = int(mp.ceil(C / eps))
    # log Phi_n = - sum_{k<n} log(1 - x q^k); accumulate stably.
    s = mp.mpf(0)
    qk = mp.mpf(1)  # q^0
    for _ in range(n):
        s += -mp.log(1 - x * qk)
        qk *= q
    return (1 - q) * s, n


def predicted_error_bound(x, eps):
    """eps * (-log(1-x))  +  (x/(1-x)) * e^{-C}  (Riemann-sum + tail)."""
    n_eps = C  # n*eps ~ C by construction
    return eps * (-mp.log(1 - x)) + (x / (1 - x)) * mp.e ** (-n_eps)


def git_sha_of(path):
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", path],
            cwd=os.path.dirname(os.path.abspath(__file__)),
        ).decode().strip()
    except Exception:
        return None


def file_hash(path):
    import hashlib
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except Exception:
        return None


def main():
    results = []
    all_ok = True
    for x in XS:
        li2 = mp.polylog(2, x)
        row = {"x": str(x), "Li2_x": mp.nstr(li2, 18), "sweep": []}
        prev_err = None
        for eps in EPS:
            val, n = rescaled_log_partial_product(x, eps)
            err = abs(val - li2)
            bound = predicted_error_bound(x, eps)
            within = err <= bound * 2  # generous: error within 2x the bound
            shrinks = prev_err is None or err < prev_err
            all_ok = all_ok and within and shrinks
            row["sweep"].append({
                "eps": mp.nstr(eps, 3),
                "q": mp.nstr(mp.e ** (-eps), 12),
                "n": n,
                "value": mp.nstr(val, 18),
                "abs_error": mp.nstr(err, 6),
                "predicted_bound": mp.nstr(bound, 6),
                "within_bound": bool(within),
                "error_shrinks": bool(shrinks),
            })
            prev_err = err
        results.append(row)

    script_path = os.path.abspath(__file__)
    witness = {
        "schema": "qou-witness/v1",
        "name": "dilog-archimedean-limit-partA",
        "description": (
            "Numerical confirmation of Part A of "
            "conj:dilogarithm-archimedean-limit: (1-q) log Phi_n(x;q) -> "
            "Li_2(x) for fixed x in (0,1), q -> 1^-, along Faddeev scaling. "
            "Error tracks the elementary monotone-Riemann-sum + tail bound."
        ),
        "computation": {
            "engine": "python+mpmath",
            "dps": mp.mp.dps,
            "C_n_eps": str(C),
            "script": "computations/dilog_archimedean_partA_witness.py",
        },
        "scriptCommitSha": git_sha_of(script_path),
        "scriptHash": file_hash(script_path),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "result": {"all_within_bound_and_monotone": bool(all_ok), "rows": results},
        "refs": [
            "docs/audits/2026-06-07-dilog-archimedean-limit-part-A-elementary.md",
            "content/quantum-observable-universe/mass-theory/dilogarithm-archimedean-limit.md",
        ],
    }
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "dilog-archimedean-limit-partA", witness,
        script_path=__file__, engine="mpmath", start_time=_T0,
        output_dir=os.path.dirname(script_path),
    ).save()
    print(f"all_within_bound_and_monotone = {all_ok}")
    for row in results:
        print(f"  x={row['x']}  Li2={row['Li2_x']}")
        for s in row["sweep"]:
            print(f"    eps={s['eps']}  n={s['n']:>7}  "
                  f"err={s['abs_error']}  bound={s['predicted_bound']}  "
                  f"ok={s['within_bound']} shrink={s['error_shrinks']}")
    print(f"witness -> {out}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
