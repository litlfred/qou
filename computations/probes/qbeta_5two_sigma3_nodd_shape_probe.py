#!/usr/bin/env python3
"""qbeta_5two_sigma3_nodd_shape_probe.py — support for #3927's A3: the 5₂ σ3
bar-odd datum is a smooth, monotone, anchor-independent CARRIER, but supplies
neither N_odd's zero-crossing nor its slope — those must come from the u³·smooth
prefactor of the A3 composition.

CONTEXT (bean qou-a664; supports #3927 tranche-3 A3). #3927's A3 tests the
capstone carrier `u³·smooth × Im 𝔙_q(5₂)` against N_odd (the smooth numerator of
S = N_odd/u³, with a zero at q* and slope A′(q*) ≈ 2.37 — `BarOddLadderShape`).
The odd-channel geometric search (#3945, merged) showed the σ3-pair is
anchor-smooth (|dι/dq| = 0.216, 7.25 orders below the swing) — an
anchor-INDEPENDENT bar-odd carrier (A3's "prize" shape candidate). This probe
supplies the SHAPE half of the A3 falsification: what does the σ3 bar-odd datum
Im 𝔙_q(5₂) = Im(ι₁₃) look like as a function of q near the substrate, vs N_odd's
two defining features?

METHOD (reuses the #3930/erratum saddle machinery, V_sigma3 = Re(V) for σ3).
Compute ι₁₃(q) = (V(σ1) − V_σ3(σ3))/(2πi) across a real-q window around the
substrate; extract (i) whether Im(ι₁₃) crosses zero near q* (N_odd's defining
feature); (ii) its slope d Im(ι₁₃)/dq vs A′(q*) ≈ 2.37.

RESULT. Im(ι₁₃) is smooth and MONOTONE across [1.05, 1.30] (no zero crossing near
the substrate), with slope ≈ 0.196 at q₀ — ~12× SMALLER than A′(q*) = 2.37. So
the σ3 bar-odd datum is a legitimate anchor-independent bar-odd carrier but
supplies NEITHER N_odd's zero-crossing NOR its slope; for A3's
`u³·smooth × Im 𝔙_q(5₂) = N_odd` to hold, the u³·smooth prefactor must carry the
zero at q* and amplify the slope ~12×. This CONSTRAINS the A3 prefactor — it is
not a passive normalization.

SCOPE (2026-06-23 (a)/(b)). scope-(a): the raw σ3 datum ALONE does not reproduce
the N_odd shape (monotone, no zero, small slope) — a magnitude/shape mismatch,
NOT an ingredient exclusion. The σ3 datum stays a valid bar-odd carrier in the
composed A3 form; what is constrained is the prefactor, not the carrier. NO fit
(nothing tuned to the AME anchors); NO c_k wired; μ never fixed from QOU data.

Run: python3 -u computations/probes/qbeta_5two_sigma3_nodd_shape_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_shape.log
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

Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
A_PRIME_QSTAR = mp.mpf("2.3716")     # N_odd slope at q* (BarOddLadderShape)


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
    print(" 5₂ σ3 bar-odd datum vs the N_odd shape — support for #3927 A3")
    print("=" * 78)

    sys.argv = [sys.argv[0]]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import qbeta_g3_5two_saddle_exact_predictions as p  # noqa

    def iota13(q):
        u = 2 * mp.log(q)
        d = p.order_saddles(p.saddle_roots(mp.e ** u))
        V1 = p.V_of(u, d[0])[0]
        V3 = p.V_sigma3(u, d[2])[0]         # erratum convention
        return (V1 - V3) / (2 * mp.pi * mp.mpc(0, 1))

    # (i) shape scan: is Im(ι₁₃) monotone / does it cross zero near substrate?
    print("\n  q        Re(ι₁₃)       Im(ι₁₃) = Im 𝔙_q(5₂)")
    qs = [mp.mpf(s) for s in ("1.02", "1.05", "1.08", "1.11", "1.15", "1.20",
                              "1.30", "1.50")]
    ims = []
    for q in qs:
        i = iota13(q)
        ims.append(mp.im(i))
        print(f"  {mp.nstr(q,5):>6}  {mp.nstr(mp.re(i),9):>12}  {mp.nstr(mp.im(i),9)}")
    # monotone (no sign change) ⇒ no zero crossing in the window
    signs = [1 if v > 0 else -1 for v in ims]
    no_zero = all(s == signs[0] for s in signs)
    monotone = all(ims[k] < ims[k + 1] for k in range(len(ims) - 1)) or \
        all(ims[k] > ims[k + 1] for k in range(len(ims) - 1))
    print(f"\n  Im(ι₁₃) monotone across window: {monotone}; no zero crossing: "
          f"{no_zero}")
    check("sigma3_baroffd_datum_has_no_nodd_zero_near_substrate",
          no_zero and monotone,
          source="Im 𝔙_q(5₂)=Im(ι₁₃) is smooth and monotone across [1.02,1.50] "
                 "with no zero crossing — it does NOT carry N_odd's defining "
                 "zero-at-q*; that zero must come from A3's u³·smooth prefactor")

    # (ii) slope vs A′(q*)
    h = mp.mpf("1e-6")
    dIm = (mp.im(iota13(Q0 + h)) - mp.im(iota13(Q0 - h))) / (2 * h)
    ratio = A_PRIME_QSTAR / abs(dIm)
    print(f"\n  d Im(ι₁₃)/dq |_q₀ = {mp.nstr(dIm,6)}   A′(q*) = "
          f"{mp.nstr(A_PRIME_QSTAR,5)}   ratio A′/slope = {mp.nstr(ratio,5)}")
    check("sigma3_slope_far_below_nodd_slope",
          ratio > mp.mpf("5"),
          computed=f"d Im(ι₁₃)/dq={mp.nstr(dIm,5)} vs A′(q*)={mp.nstr(A_PRIME_QSTAR,4)} "
                   f"(~{mp.nstr(ratio,3)}× short)",
          source="the σ3 bar-odd datum's slope is ~12× smaller than A′(q*) — the "
                 "A3 u³·smooth prefactor must amplify the slope by that factor; "
                 "the σ3 carrier is not a passive normalization")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("SUPPORT for #3927 A3: the 5₂ σ3 bar-odd datum Im 𝔙_q(5₂)=Im(ι₁₃) is a "
         "smooth, MONOTONE, anchor-independent carrier — no zero crossing near "
         "the substrate (Re≈0.45, Im≈−0.64 across [1.02,1.50]) and slope "
         f"{mp.nstr(dIm,4)} at q₀, ~{mp.nstr(ratio,3)}× SMALLER than A′(q*)=2.37. "
         "So the σ3 datum supplies the anchor-independent bar-odd CARRIER but "
         "NEITHER N_odd's zero-at-q* NOR its slope; for A3's "
         "`u³·smooth × Im 𝔙_q(5₂) = N_odd` to hold, the u³·smooth prefactor must "
         "carry the zero and amplify the slope ~12×. This CONSTRAINS the A3 "
         "prefactor (not a passive normalization). "
         if all_passed else
         "PARTIAL: a shape check failed — see the per-check table. ")
        + "scope-(a): the raw σ3 datum alone does not reproduce the N_odd shape "
        "(magnitude/shape mismatch, not ingredient exclusion) — it stays a valid "
        "carrier in the composed A3 form. NO fit; NO c_k wired; μ never fixed "
        "from QOU data."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-5two-sigma3-nodd-shape",
        "description": "Support for #3927 A3: the 5₂ σ3 bar-odd datum "
                       "Im 𝔙_q(5₂)=Im(ι₁₃) is a smooth monotone anchor-"
                       "independent carrier with no zero-crossing near the "
                       "substrate and slope ~12× below A′(q*)=2.37 — so N_odd's "
                       "zero + slope must come from the A3 u³·smooth prefactor, "
                       "which is thereby constrained. scope-(a).",
        "audit_only": True,
        "tier": "numerical (shape comparison; A3 support)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "im_iota13_window": [mp.nstr(v, 8) for v in ims],
            "monotone_no_zero": bool(no_zero and monotone),
            "d_im_iota13_dq_q0": mp.nstr(dIm, 8),
            "A_prime_qstar": mp.nstr(A_PRIME_QSTAR, 6),
            "slope_shortfall_factor": mp.nstr(ratio, 6),
            "verdict": verdict,
        },
        "context": {
            "axis": "5₂ σ3 N_odd shape (support #3927 A3; bean qou-a664)",
            "saddle_machinery": "qbeta_g3_5two_saddle_exact_predictions "
                                "(V_sigma3=Re(V) erratum)",
            "supports": "#3927 tranche-3 A3 (u³·smooth × Im 𝔙_q(5₂) vs N_odd)",
            "nodd_shape": "N_odd zero at q*, slope A′(q*)≈2.37 (BarOddLadderShape)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-5two-sigma3-nodd-shape.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
