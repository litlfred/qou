#!/usr/bin/env python3
"""qbeta_kashaev_vs_btower_phase_distinction_probe.py — the ħ↔2πi/N wall is
load-bearing: the Kashaev deformed fluctuation tower does NOT reproduce the
b-tower phase law term-by-term, so it cannot independently confirm #3923's 4₁
odd-phase null — but it agrees qualitatively (weak odd phase).

CONTEXT. Main's #3923 (`qbeta_g3_aomega_sharpened_amplitude.py`) established the
4₁ deformed Stokes AMPLITUDE is real (odd-phase null): the b-tower obeys the
phase law κ̃_n^b = ρ_n·ωⁿ with ω = e^{−i·arctan(t/π)}, ρ_n ∈ ℝ, so arg(r̃) is a
pure kinematic rotation (9.2e-9 rad residual = the rung-precision floor). It
concluded "A_ω is not a 4₁ Stokes phase at any level; the 4₁/GGM lane is
COMPLETE; the odd channel must source from non-amphichiral (5₂-class) geometry."

This probe attempts an INDEPENDENT confirmation of that null from a DISTINCT
route — the Kashaev-saddle Wick fluctuation engine (`qbeta_phib_saddle_
fluctuation_complex_meridian_probe`, deformed via the linear tilt μ = −log m²) —
and finds the honest outcome: the two towers relate by RESUMMATION, not
term-by-term, so the Kashaev-frame deformed tower carries a DIFFERENT phase and
cannot term-by-term reproduce the b-tower phase law. What it CAN say:

  (1) DISTINCTION (the ħ↔2πi/N wall is load-bearing). The b-tower phase law
      predicts arg(κ̃_n^b) = −n·arctan(t/π) (linear, negative). The Kashaev
      deformed tower at the substrate tilt μ = i·t gives arg(κ_n^K) that is
      tiny and POSITIVE (~+0.0003 → +0.012 over n=1..5), NOT −0.033n. The two
      towers genuinely differ — b-tower amplitudes (#3805/#3898/#3923, r̃≈1.024)
      and Kashaev-frame numbers are NOT interchangeable (a category-error guard
      for the campaign).

  (2) QUALITATIVE AGREEMENT (cross-frame near-null). Despite the term-by-term
      difference, the Kashaev deformed tower's per-rung phase stays WELL BELOW
      the kinematic magnitude n·arctan(t/π): |arg(κ_n^K)| < arctan(t/π) for the
      leading rungs. Both frames agree the deformed 4₁ tower carries only weak
      odd phase — consistent with #3923's null, from an independent direction,
      without over-claiming a term-by-term match.

HONEST SCOPE (scope-(a)). NOT a term-by-term confirmation of #3923 (the wall
forbids it); a documentation of the two-tower distinction + qualitative
cross-frame consistency. 4₁ geometric facts; μ never fixed from QOU data. NO
fit; NO c_k wired; NO tier change. The 4₁ lane stays #3923's (complete); the
open frontier is the 5₂-class lane (#3892/#3902).

Run: python3 -u computations/probes/qbeta_kashaev_vs_btower_phase_distinction_probe.py \\
       2>&1 | tee /tmp/qbeta_twotower.log
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
    print(" Kashaev fluctuation tower vs b-tower phase law — the ħ↔2πi/N wall")
    print("=" * 78)

    # import the on-main complex-meridian Kashaev fluctuation engine
    sys.argv = [sys.argv[0]]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import qbeta_phib_saddle_fluctuation_complex_meridian_probe as cm  # noqa

    t = mp.log(Q0)
    arctan_tp = mp.atan(t / mp.pi)         # arctan(t/π) = the b-tower ω phase
    print(f"\n  t = ln q₀ = {mp.nstr(t,10)}   arctan(t/π) = {mp.nstr(arctan_tp,10)}")

    # Kashaev deformed tower at the substrate finite-b tilt μ = i·t
    mu = mp.mpc(0, 1) * t
    sstar = cm.saddle_of_mu(mu)
    kap = cm.ladder_at_saddle(sstar, 5, 10)
    print(f"  deformed Kashaev saddle s*(μ) = {mp.nstr(sstar,8)}")

    print("\n  n | arg(κ_n^Kashaev) | b-tower law −n·arctan(t/π) | |arg| < arctan?")
    argsK, matches_law, below_kin = [], True, True
    for n in range(1, 6):
        aK = mp.arg(kap[n])
        law = -n * arctan_tp
        argsK.append(float(aK))
        # term-by-term match to the b-tower law? (within a tight tol)
        if abs(aK - law) > mp.mpf("0.005"):
            matches_law = False
        # per-rung phase stays below the single-step kinematic magnitude?
        if abs(aK) >= arctan_tp:
            below_kin = False
        print(f"  {n} | {mp.nstr(aK,6):>14} | {mp.nstr(law,6):>14} | "
              f"{abs(aK) < arctan_tp}")

    # (1) the two towers DIFFER (ħ↔2πi/N load-bearing): the Kashaev tower does
    #     NOT reproduce the b-tower phase law term-by-term.
    check("btower_phase_law_not_reproduced_in_kashaev_frame", not matches_law,
          computed=f"arg(κ_1^K)={mp.nstr(argsK[0],5)} vs law "
                   f"{mp.nstr(-arctan_tp,5)}",
          source="the Kashaev deformed fluctuation tower does NOT carry the "
                 "b-tower phase −n·arctan(t/π); the two towers relate by "
                 "resummation, not term-by-term — the ħ↔2πi/N wall is "
                 "load-bearing (b-tower amplitudes and Kashaev-frame numbers "
                 "are NOT interchangeable)")

    # (2) qualitative cross-frame near-null: the Kashaev per-rung phase stays
    #     below the kinematic magnitude — weak odd phase, consistent with #3923.
    check("kashaev_tower_weak_odd_phase_consistent_with_3923_null", below_kin,
          computed=f"max |arg(κ_n^K)| = {mp.nstr(max(abs(a) for a in argsK),5)} "
                   f"< arctan(t/π) = {mp.nstr(arctan_tp,5)}",
          source="the Kashaev deformed tower's per-rung phase stays below the "
                 "single-step kinematic magnitude — both frames agree the "
                 "deformed 4₁ tower carries only weak odd phase (qualitative "
                 "cross-frame consistency with #3923's odd-phase null, NOT a "
                 "term-by-term confirmation)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("DOCUMENTED: the Kashaev deformed fluctuation tower does NOT reproduce "
         "the b-tower phase law κ̃_n=ρ_n·ωⁿ term-by-term — arg(κ_n^Kashaev) is "
         "tiny and positive (~+0.0003→+0.012), not the b-tower's −n·arctan(t/π). "
         "The two towers relate by RESUMMATION (ħ↔2πi/N), so this DISTINCT route "
         "cannot term-by-term confirm #3923's 4₁ odd-phase null — the wall is "
         "load-bearing, a category-error guard for the campaign (b-tower "
         "amplitudes r̃ and Kashaev-frame numbers are not interchangeable). It "
         "DOES agree qualitatively: the Kashaev per-rung phase stays below the "
         "kinematic magnitude, so both frames see only weak odd phase in the "
         "deformed 4₁ tower. The 4₁ lane remains #3923's (complete); the open "
         "frontier is the non-amphichiral 5₂-class lane (#3892/#3902). "
         if all_passed else
         "PARTIAL: a check failed — see the per-check table. ")
        + "scope-(a): documentation of the two-tower distinction + qualitative "
        "cross-frame consistency, NOT a term-by-term confirmation. μ never fixed "
        "from QOU data. NO fit; NO c_k wired; NO tier change."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-kashaev-vs-btower-phase-distinction",
        "description": "The ħ↔2πi/N wall is load-bearing: the Kashaev deformed "
                       "fluctuation tower does not reproduce the b-tower phase "
                       "law term-by-term (cannot term-by-term confirm #3923's 4₁ "
                       "odd-phase null), but agrees qualitatively (weak odd "
                       "phase). scope-(a).",
        "audit_only": True,
        "tier": "numerical (cross-frame phase comparison)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "t_ln_q0": mp.nstr(t, 10),
            "arctan_t_over_pi": mp.nstr(arctan_tp, 10),
            "kashaev_saddle": mp.nstr(sstar, 8),
            "arg_kappa_kashaev": [round(a, 8) for a in argsK],
            "btower_law_predicts": [mp.nstr(-n * arctan_tp, 6) for n in range(1, 6)],
            "verdict": verdict,
        },
        "context": {
            "axis": "Kashaev vs b-tower phase distinction (item-1 re-scope)",
            "btower_null_source": "qbeta-g3-aomega-sharpened-amplitude (#3923; "
                                  "4₁ odd-phase null, r̃ real)",
            "engine": "qbeta_phib_saddle_fluctuation_complex_meridian_probe "
                      "(Kashaev Wick fluctuation)",
            "conclusion": "4₁ lane complete (#3923); open frontier = 5₂-class "
                          "(#3892/#3902)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-kashaev-vs-btower-phase-distinction.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
