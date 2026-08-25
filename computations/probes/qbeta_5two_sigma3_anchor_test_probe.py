#!/usr/bin/env python3
"""qbeta_5two_sigma3_anchor_test_probe.py — the decisive 5₂-class test: the
chiral σ3-pair carries a nonzero intrinsic bar-odd PHASE but is ANCHOR-SMOOTH,
so it cannot carry the c₃ swing. The odd-channel geometric search closes.

CONTEXT (bean qou-9w95; capstone item 2). The 4₁ odd-phase null (#3923) pointed
the odd channel to non-amphichiral (5₂-class) geometry, and the 5₂ port (#3930,
`qbeta_g3_5two_saddle_exact_predictions.py`, Lean-proved `FiveTwoSaddleCurve`)
made it falsifiable: 5₂ is chiral (CS ≠ 0), and its **σ3-pairs carry a nonzero
intrinsic phase** at the substrate deformation (ι̃₁₃ −0.958 rad, ι̃₂₃ −2.184 rad,
using the erratum σ3 convention V_sigma3 = Re(V) per GGM §6.1) — the bar-odd
carrier the 4₁ null excluded (whose floor is 9.2e-9).

A nonzero phase is NECESSARY but not SUFFICIENT for the swing: the σ3-pair must
ALSO be anchor-dependent at the ~3.84×10⁶ scale (S swings 2.44 % while q₀ moves
~1.28e-8). This probe runs that test, reusing the #3930 saddle machinery: compute
ι₁₃, ι₂₃ = (V_i − V_j)/(2πi) at BOTH q₀ anchors and measure |dι/dq|.

RESULT. |dι₁₃/dq| ≈ 0.216 (O(1)) — ANCHOR-SMOOTH, ~7.25 orders below the
3.84×10⁶ the swing needs, exactly like the 5₂ σ1 quantum volume (#3902, 1.47) and
every other geometric object. So the chiral σ3-pair distinguishes chirality
(nonzero phase 0.958/2.184 rad, matching the erratum) but NOT the swing
(anchor-smooth). This CLOSES the odd-channel geometric
search: every geometric object — amphichiral 4₁ (branch-point generic, quantum
volume anchor-smooth, odd-phase null), chiral 5₂ σ1 (quantum volume
anchor-smooth), chiral 5₂ σ3 (nonzero phase, anchor-smooth) — fails the swing.
The swing is representational on every front, chiral included.

SCOPE (2026-06-23 (a)/(b) discipline). This is a **scope-(a)** result: the 5₂
σ3-pair, alone, does not reproduce the swing (anchor-smooth), constraining
magnitude not ingredient. The σ3-pair genuinely IS a non-amphichiral bar-odd
carrier (nonzero phase, a permanent structural contribution); its
anchor-smoothness says the swing does not live in its anchor-dependence — it does
not exclude the σ3-pair from a many-term closure. NO fit; NO c_k wired; μ never
fixed from QOU data.

Run: python3 -u computations/probes/qbeta_5two_sigma3_anchor_test_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_s3.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

Q0_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q0_MUON = mp.mpf("1.10997859555733471")
SWING_REQUIREMENT = mp.mpf("3.84e6")     # |dS/dq| the c₃ swing needs
FOURONE_NULL_FLOOR = mp.mpf("9.2e-9")    # #3923 4₁ odd-phase null floor


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" 5₂ σ3-pair anchor test — nonzero phase, but anchor-smooth?")
    print("=" * 78)

    # reuse the #3930 5₂ saddle machinery
    sys.argv = [sys.argv[0]]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import qbeta_g3_5two_saddle_exact_predictions as p  # noqa

    def iota(q, i, j):
        # σ1/σ2 use the full complex action V_of; σ3 (index 2) uses V_sigma3
        # (GGM §6.1 "keep only Re(V)" — the erratum convention, superseding the
        # #3937 full-complex V₃).
        u = 2 * mp.log(q)                       # u_sub = 2·ln q₀
        d = p.order_saddles(p.saddle_roots(mp.e ** u))
        Vi = p.V_sigma3(u, d[i])[0] if i == 2 else p.V_of(u, d[i])[0]
        Vj = p.V_sigma3(u, d[j])[0] if j == 2 else p.V_of(u, d[j])[0]
        return (Vi - Vj) / (2 * mp.pi * mp.mpc(0, 1))

    dq = Q0_PROTON - Q0_MUON
    print(f"\n  anchor gap dq = {mp.nstr(dq,6)}")
    slopes = {}
    for nm, (i, j) in (("13", (0, 2)), ("23", (1, 2))):
        iP = iota(Q0_PROTON, i, j)
        iM = iota(Q0_MUON, i, j)
        slope = abs((iP - iM) / dq)
        phase = abs(mp.arg(iP))
        slopes[nm] = (slope, phase, iP)
        print(f"\n  ι_{nm}(proton) = {mp.nstr(iP,10)}")
        print(f"  ι_{nm}: nonzero intrinsic phase |arg| = {mp.nstr(phase,6)} rad "
              f"(≫ 4₁ null floor {mp.nstr(FOURONE_NULL_FLOOR,3)})")
        print(f"  ι_{nm}: |dι/dq| = {mp.nstr(slope,8)}  vs swing requirement "
              f"{mp.nstr(SWING_REQUIREMENT,3)}  (ratio "
              f"{mp.nstr(slope/SWING_REQUIREMENT,4)})")

    # (1) the σ3-pair IS a non-amphichiral bar-odd carrier (nonzero phase)
    phase_ok = all(slopes[nm][1] > mp.mpf("0.1") for nm in slopes)
    check("sigma3_carries_nonzero_intrinsic_phase", phase_ok,
          computed=f"|arg ι_13|={mp.nstr(slopes['13'][1],5)}, "
                   f"|arg ι_23|={mp.nstr(slopes['23'][1],5)} rad",
          source="the chiral 5₂ σ3-pairs carry a genuinely nonzero intrinsic "
                 "phase (CS(5₂)≠0) — the bar-odd carrier the amphichiral 4₁ "
                 "excluded (regression of the #3930 falsifiable target)")

    # (2) but the σ3-pair is ANCHOR-SMOOTH — cannot carry the swing
    smooth_ok = all(slopes[nm][0] < mp.mpf("100") for nm in slopes)
    worst = max(slopes[nm][0] for nm in slopes)
    orders = mp.log10(SWING_REQUIREMENT / worst)
    print(f"\n  worst |dι/dq| = {mp.nstr(worst,6)} — {mp.nstr(orders,4)} orders "
          f"below the swing requirement")
    check("sigma3_anchor_smooth_cannot_carry_swing", smooth_ok,
          computed=f"max |dι/dq| = {mp.nstr(worst,5)} (O(1))",
          expected=f"≪ {mp.nstr(SWING_REQUIREMENT,3)} (~7 orders)",
          source="the 5₂ σ3-pair datum is anchor-SMOOTH (|dι/dq|=O(1)), ~7 "
                 "orders below the swing scale — like the 5₂ σ1 quantum volume "
                 "(#3902) and every geometric object; the chiral σ3-pair "
                 "distinguishes chirality (nonzero phase) but NOT the swing")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("CLOSED (odd-channel geometric search): the chiral 5₂ σ3-pair carries a "
         f"genuinely nonzero intrinsic phase (|arg ι_13|={mp.nstr(slopes['13'][1],4)} "
         "rad — the non-amphichiral bar-odd carrier the 4₁ null excluded) yet is "
         f"ANCHOR-SMOOTH (max |dι/dq|={mp.nstr(worst,4)}, O(1), ~7 orders below the "
         "3.84e6 swing scale). So the ONE geometric object with nonzero bar-odd "
         "phase still cannot carry the swing. Every geometric object now fails: "
         "amphichiral 4₁ (branch-point generic, quantum volume anchor-smooth, "
         "odd-phase null), chiral 5₂ σ1 (quantum volume anchor-smooth, #3902), and "
         "chiral 5₂ σ3 (nonzero phase, anchor-smooth, this probe). The c₃ swing is "
         "representational on EVERY front, chiral included — the 1/u³ inversion of "
         "a smooth N_odd, pinned by experimental Q_β. "
         if all_passed else
         "PARTIAL: a check failed — see the per-check table. ")
        + "scope-(a): the σ3-pair alone does not reproduce the swing "
        "(anchor-smooth), constraining magnitude not ingredient — it remains a "
        "permanent non-amphichiral bar-odd carrier, not excluded from a many-term "
        "closure. NO fit; NO c_k wired; μ never fixed from QOU data."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-5two-sigma3-anchor-test",
        "description": "The decisive 5₂-class test: the chiral σ3-pair carries a "
                       "nonzero intrinsic bar-odd phase (CS(5₂)≠0, #3930 target) "
                       "but is anchor-smooth (|dι/dq|=O(1), ~7 orders below the "
                       "swing) — so it cannot carry the c₃ swing. Closes the "
                       "odd-channel geometric search; swing representational on "
                       "every front. scope-(a).",
        "audit_only": True,
        "tier": "numerical (anchor-dependence; decisive geometric-search test)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "iota_13_slope": mp.nstr(slopes["13"][0], 8),
            "iota_13_phase_rad": mp.nstr(slopes["13"][1], 8),
            "iota_23_slope": mp.nstr(slopes["23"][0], 8),
            "iota_23_phase_rad": mp.nstr(slopes["23"][1], 8),
            "swing_requirement": mp.nstr(SWING_REQUIREMENT, 4),
            "orders_below_swing": mp.nstr(orders, 5),
            "verdict": verdict,
        },
        "context": {
            "axis": "5₂ σ3-pair anchor test (capstone item 2; bean qou-9w95)",
            "saddle_machinery": "qbeta_g3_5two_saddle_exact_predictions (#3930; "
                                "FiveTwoSaddleCurve.lean)",
            "compare": "5₂ σ1 quantum volume anchor-smooth (#3902); 4₁ odd-phase "
                       "null (#3923)",
            "verdict_scope": "(a) scope-limited negative — σ3-pair alone does not "
                             "carry the swing; not an ingredient exclusion",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-5two-sigma3-anchor-test.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
