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

🛑 THE NARRATIVE ABOVE IS HISTORY, AND THIS FILE WAS RED ON MAIN.  Corrected 2026-08-29.

Two things have changed under the file since it was written.

**The cache is gone, not re-gated.**  `y_lambda_at` reads no witness at all now: the gated
cache load moved into `_y_lambda_at_convention_C_HISTORICAL`, which is dead code (convention C,
excised 2026-08-09), and the live body computes `y_lambda_su_n(n, mpf(str(q_val)), 2)` from
whatever `q` it is handed.  So checks 1 and 2 are a **cross-implementation agreement test**
between `wedderburn_jones_markov.y_lambda_at` and `schur_principal_mpmath.y_lambda_at_q0_mpmath`
at each pin — worth keeping, and still what would catch a re-introduced cache, but not the
cache-gating test their old messages claimed.  The μ₃ Fréchet straddle the paragraph above
describes was real; only the mechanism is obsolete.

**Check 3 was failing, and its message accused a Lean declaration.**  It compared `mp.sign(y_λ)`
across the two anchors over ALL partitions and reported
*"QOU.MassTheory.YLambdaSignThreshold.wenzl_sign is anchor-dependent after all"*.  Measured at
n=9: all 25 disagreements are exactly the ℓ≥3 partitions, and in every one BOTH values are below
the noise floor — proton residues of 1e-73 to 1e-147 against a muon leg of exactly 0.0.  The 5
two-row blocks, the ones carrying weight, agree.  Under convention D the Wenzl level is r = 2 so
`y_λ = 0` for `ℓ(λ) > 2`, and that vanishing is a polynomial identity reached by CANCELLATION at
finite precision: whether the residue lands on 0.0 or on 1e-75 depends on how q₀ is spelled.  The
two legs differ in their dust and in nothing else.  Check 3 now compares signs only where there
is weight, and reports the annihilated stratum separately.

Never compare against zero here.  A gate that reads round-off as a signed quantity does not
merely fail — it manufactures a refutation of a proved statement.

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
from _precision import set_compute_dps  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1]
                       / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor  # noqa: E402

set_compute_dps()

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

    # 1. the default path: a caller passing the package constant must get PROTON.
    #
    # NOTE what this now tests. `y_lambda_at` no longer reads any cache — the
    # gated cache load moved into `_y_lambda_at_convention_C_HISTORICAL`, which
    # is dead (convention C, excised 2026-08-09), and the live body computes
    # `y_lambda_su_n(n, mpf(str(q_val)), 2)` from whatever q it is handed. So
    # checks 1 and 2 are a CROSS-IMPLEMENTATION agreement test between
    # `wedderburn_jones_markov.y_lambda_at` and
    # `schur_principal_mpmath.y_lambda_at_q0_mpmath` at each pin — still worth
    # having, and still the thing that would catch a re-introduced cache, but
    # not the cache-gating test the old messages described.
    got = y_lambda_at(N, Q_PROTON)
    rp, rm = _maxrel(got, live_p), _maxrel(got, live_m)
    ok1 = rp < TOL and rp < rm
    print(f"\n 1. caller passes q_parameter.Q (the default path for ~145 callers)")
    print(f"      vs live PROTON {mp.nstr(rp,6)} | vs live MUON {mp.nstr(rm,6)}"
          f"  -> {'PROTON  PASS' if ok1 else 'MUON  FAIL'}")
    if not ok1:
        fails.append("y_lambda_at(n, q_parameter.Q) returned MUON values — a "
                     "proton-anchored caller is getting the ideal layer, so either a "
                     "pin-keyed cache has been re-introduced or the two "
                     "implementations have diverged")

    # 2. a caller who asks for the muon anchor must get muon values
    got2 = y_lambda_at(N, Q_MUON)
    rp2, rm2 = _maxrel(got2, live_p), _maxrel(got2, live_m)
    ok2 = rm2 < TOL and rm2 < rp2
    print(f" 2. caller passes the muon q₀ (the ideal layer must stay reachable)")
    print(f"      vs live PROTON {mp.nstr(rp2,6)} | vs live MUON {mp.nstr(rm2,6)}"
          f"  -> {'MUON  PASS' if ok2 else 'PROTON  FAIL'}")
    if not ok2:
        fails.append("a muon-anchored caller did not get muon values — the ideal "
                     "layer is no longer reachable through this accessor")

    # 3. signs are anchor-independent (YLambdaSignThreshold.wenzl_sign must not depend on pin)
    # SIGNS ARE COMPARED ONLY WHERE THERE IS A SIGN TO COMPARE.
    #
    # This check was RED on main and its message accused
    # `QOU.MassTheory.YLambdaSignThreshold.wenzl_sign` of being anchor-dependent.
    # It is not. Measured at n=9: all 25 disagreements are exactly the ℓ≥3
    # partitions, and in every one BOTH values are below the noise floor — the
    # proton leg carries residues of 1e-73 to 1e-147, the muon leg is exactly
    # 0.0. `mp.sign()` of round-off against `mp.sign(0)` is not a sign
    # disagreement. The 5 two-row partitions, which are the ones carrying
    # weight, agree.
    #
    # The underlying fact is convention D's, not a regression: the Wenzl level
    # is r = 2, so y_λ = 0 for ℓ(λ) > 2, and the vanishing is a polynomial
    # identity reached by CANCELLATION at finite precision. Whether the residue
    # lands on exactly 0.0 or on 1e-75 depends on how q0 is spelled, so the two
    # legs differ in their dust and in nothing else.
    #
    # Related and already adjudicated: bean qou-ulxr found that under D the sign
    # threshold lands exactly ON the content lattice, so `wenzl_sign`'s `hnd`
    # hypothesis fails and the parity on that stratum is UNDEFINED rather than
    # merely zero. That is one more reason not to read a sign off it.
    floor3 = max(abs(v) for v in live_p.values()) * mp.mpf(10) ** (-(mp.mp.dps - 8))
    carrying = [l for l in live_m
                if abs(live_p[l]) >= floor3 or abs(live_m[l]) >= floor3]
    annihilated = [l for l in live_m if l not in carrying]
    ok3 = all(mp.sign(live_p[l]) == mp.sign(live_m[l]) for l in carrying)
    print(f" 3. signs agree across anchors on the {len(carrying)} blocks carrying"
          f" weight  -> {'PASS' if ok3 else 'FAIL'}")
    print(f"      ({len(annihilated)} blocks are below the floor"
          f" {mp.nstr(floor3, 4)} at BOTH anchors — convention D annihilates"
          f" ℓ(λ)>2; no sign to compare)")
    if not ok3:
        bad = [l for l in carrying
               if mp.sign(live_p[l]) != mp.sign(live_m[l])]
        fails.append(f"sign(y_λ) differs between anchors on blocks that CARRY "
                     f"weight: {bad} — this is above the noise floor and is a "
                     f"real anchor-dependence, unlike the annihilated stratum")
    if not carrying:
        fails.append("every block is below the floor — check 3 is vacuous, which "
                     "means the floor or the weights are wrong, not that signs agree")

    print("\n" + "=" * 78)
    if fails:
        for f in fails:
            print(f" FAIL: {f}")
    else:
        print(" PASS — each accessor returns values at the anchor it was handed;")
        print("        no layer crossing, and signs agree wherever there is weight.")
    print("=" * 78)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
