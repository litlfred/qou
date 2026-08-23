#!/usr/bin/env python3
"""q0_anchor_gate_test.py — regression test: the y_λ cache must not cross calibration layers.

WHAT BROKE, AND WHY THIS TEST EXISTS.  `wedderburn_jones_markov.y_lambda_at(n, q)` used to
serve its cached `y-lambda-at-q0.witness.json` whenever `|q − q_parameter.Q| < 1e-12`.  But the
cache is built at the **IDEAL / canonical-3-CAL muon** pin while `q_parameter.Q` is the
**EXPERIMENTAL / Physical-Observations proton** pin — 11.54 ppb apart, which is the μ–p
substrate tension itself.  The gate was therefore satisfied *trivially* by any caller passing
`q_parameter.Q`, and the ideal-layer cache was handed to an experimental-layer caller **with no
signal that a calibration-layer boundary had been crossed**.

That silently mixed layers inside single computed quantities (found in the μ₃ Fréchet probe;
see `deltalambda/mu3_anchor_consistency_probe.py`).  The fix gates on the witness's **own
recorded** `q_0` instead, so a proton-anchored caller falls through to the live closed form at
the anchor it actually asked for.

Per AGENTS.md §"q₀ anchor convention" (owner directive 2026-08-07), **all agents and all
production code default to the experimental (proton) anchor**.  This test pins that behaviour.

Run: `python3 computations/q0_anchor_gate_test.py`  (exit 0 = pass)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent),
                str(Path(__file__).resolve().parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from q_parameter import Q_MP as Q0  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1]
                       / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor  # noqa: E402

mp.mp.dps = 50

Q_PROTON = mp.mpf(str(Q0))
# READ the muon anchor; do not retype it. This file is a test ABOUT crossing
# the calibration layers, and it used to name its muon leg with a 61-character
# literal that tracked the anchor for 51 digits and then diverged --
# `…878015405145269` against the anchor's `…878015368660798114`. A test that
# transcribes the thing it is testing cannot follow a re-pin, which is the
# whole defect it exists to catch. The proton leg already reads (`Q_MP`); this
# makes the muon leg symmetric with it.
Q_MUON = mp.mpf(_q0_value_for_anchor("muon"))
N = 9
TOL = mp.mpf("1e-20")


def _maxrel(got, ref):
    return max(abs(mp.mpf(str(got[l])) - ref[l]) / max(abs(ref[l]), mp.mpf("1e-40"))
               for l in ref)


def main() -> int:
    live_p = y_lambda_at_q0_mpmath(N, Q_PROTON)
    live_m = y_lambda_at_q0_mpmath(N, Q_MUON)
    sep = abs(Q_PROTON - Q_MUON) / Q_MUON
    fails = []

    print("=" * 78)
    print(" q₀ anchor gate — regression test")
    print("=" * 78)
    print(f" proton q₀ = {mp.nstr(Q_PROTON, 20)}")
    print(f" muon   q₀ = {mp.nstr(Q_MUON, 20)}")
    print(f" separation = {float(sep)*1e9:.2f} ppb (the μ–p substrate tension)")
    if float(sep) < 1e-10:
        fails.append("the two pins are no longer distinguishable — test is vacuous")

    # 1. the default path: a caller passing the package constant must get PROTON
    got = y_lambda_at(N, Q_PROTON)
    rp, rm = _maxrel(got, live_p), _maxrel(got, live_m)
    ok1 = rp < TOL and rp < rm
    print(f"\n 1. caller passes q_parameter.Q (the default path for ~145 callers)")
    print(f"      vs live PROTON {mp.nstr(rp,6)} | vs live MUON {mp.nstr(rm,6)}"
          f"  -> {'PROTON  PASS' if ok1 else 'MUON  FAIL'}")
    if not ok1:
        fails.append("y_lambda_at(n, q_parameter.Q) served the muon cache — layer crossing "
                     "has regressed")

    # 2. the cache must still be served to a caller who asks for ITS anchor
    got2 = y_lambda_at(N, Q_MUON)
    rp2, rm2 = _maxrel(got2, live_p), _maxrel(got2, live_m)
    ok2 = rm2 < TOL and rm2 < rp2
    print(f" 2. caller passes the muon q₀ (cache must still be reachable)")
    print(f"      vs live PROTON {mp.nstr(rp2,6)} | vs live MUON {mp.nstr(rm2,6)}"
          f"  -> {'MUON  PASS' if ok2 else 'PROTON  FAIL'}")
    if not ok2:
        fails.append("the muon cache is no longer served to a muon-anchored caller — the "
                     "fast path was lost, not just re-gated")

    # 3. signs are anchor-independent (YLambdaSignThreshold.wenzl_sign must not depend on pin)
    ok3 = all(mp.sign(live_p[l]) == mp.sign(live_m[l]) for l in live_m)
    print(f" 3. all {len(live_m)} signs agree across anchors"
          f"  -> {'PASS' if ok3 else 'FAIL'}")
    if not ok3:
        fails.append("sign(y_λ) now differs between anchors — QOU.MassTheory."
                     "YLambdaSignThreshold.wenzl_sign is anchor-dependent after all")

    print("\n" + "=" * 78)
    if fails:
        for f in fails:
            print(f" FAIL: {f}")
    else:
        print(" PASS — the cache is keyed on its own recorded q₀; no layer crossing.")
    print("=" * 78)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
