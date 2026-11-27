#!/usr/bin/env python3
"""alpha_em_perloop_integer_forcedness_probe.py

How forced is the per-loop-measure integer? — a scope-(a) MEASUREMENT (not a
derivation) of the strength of the `1/(8π) = 1/(π·dim H¹(Bring))` identification.

Context. The α_EM ladder closes as the fixed point of `1/α = T + α·H`,
`T = q[9]_q[10]_q + b₁/Area` (tree + zero-mode, both derived), `H = [2]_q/(π·D)`
with the per-loop-measure denominator `D`. The 07-14 derivability map pins every
ingredient EXCEPT `D`: the phase-4 "identification" `D = dim H¹(M_Bring) = 2g = 8`
is an admitted PATTERN MATCH (its own HONEST CAVEAT). The 9500σ falsification
(`D = Area/π = 12` → −1419 ppb) already shows the residual is hypersensitive to
`D`. This probe quantifies that sensitivity exactly and asks the sharp question:

  is `D = 8` *pinned* by CODATA to the topological integer (→ a precise
  coincidence a derivation must explain), or *loose* (→ weak numerology)?

Method (closed form). At the fixed point `1/α = C` (CODATA), the cubic
`α²H + αT − 1 = 0` gives `H* = C·(C − T)` exactly, hence the data-selected
denominator `D* = [2]_q / (π · H*)`. We report `D*`, its 1σ uncertainty from
`σ(1/α)`, and how many σ separate `D=7` and `D=9` from the fit.

ANTI-LAUNDERING (STRICT). `D*` is SOLVED FROM the data — it is the FIT, NOT a
derivation. A small `|D* − 8|` does NOT derive `1/(8π)`; it measures that the
empirical selection lands on the topological integer. The open derivation target
is unchanged: derive `per-loop measure = 1/(π · dim H¹)` from the RT/heat-kernel
zero-mode measure (the reassessment's rule: the value must be FORCED by the
physics, never reverse-engineered from CODATA). No c_k wired; no tier change.
"""
import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402

set_compute_dps()

CODATA_ALPHA_INV = mp.mpf("137.035999084")
SIGMA_ALPHA_INV = mp.mpf("0.000000021")          # CODATA 2018 σ on 1/α
# Both pins read BY NAME (bean qou-4bef, 2026-09-03); the muon literal this carried was the
# pin RETIRED 2026-08-22/28.
ANCHORS = {
    "proton": Q_MP,
    "muon": q_muon_at(50),
}


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
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                  cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def T_of(q):
    g = 4
    tree = q * qb(9, q) * qb(10, q)
    zero_mode = mp.mpf(2 * g) / (4 * mp.pi * (g - 1))     # b₁/Area = 2/(3π)
    return tree + zero_mode


def D_star(q, C):
    """Data-selected per-loop denominator D such that the fixed point hits C."""
    T = T_of(q)
    Hstar = C * (C - T)
    return qb(2, q) / (mp.pi * Hstar)


def main():
    print("Per-loop-measure integer forcedness (scope-(a) measurement, NOT a derivation)")
    print(f"  CODATA 1/α = {mp.nstr(CODATA_ALPHA_INV, 14)} ± {mp.nstr(SIGMA_ALPHA_INV, 2)}")
    rows = {}
    for name, q in ANCHORS.items():
        C = CODATA_ALPHA_INV
        D0 = D_star(q, C)
        Dp = D_star(q, C + SIGMA_ALPHA_INV)
        Dm = D_star(q, C - SIGMA_ALPHA_INV)
        sigD = abs(Dp - Dm) / 2
        # σ separation of the integer neighbours from the fit
        sep7 = abs(D0 - 7) / sigD
        sep8 = abs(D0 - 8) / sigD
        sep9 = abs(D0 - 9) / sigD
        rows[name] = {
            "D_star": mp.nstr(D0, 12),
            "sigma_D": mp.nstr(sigD, 4),
            "D_minus_8": mp.nstr(D0 - 8, 6),
            "sep_from_7_sigma": mp.nstr(sep7, 5),
            "sep_from_8_sigma": mp.nstr(sep8, 5),
            "sep_from_9_sigma": mp.nstr(sep9, 5),
        }
        print(f"\n  --- {name} (q0={mp.nstr(q, 14)}) ---")
        print(f"    D* (data-selected)     = {mp.nstr(D0, 12)}  ± {mp.nstr(sigD, 3)}")
        print(f"    D* − 8 (dim H¹)         = {mp.nstr(D0 - 8, 6)}")
        print(f"    integer 7 excluded at    {mp.nstr(sep7, 4)} σ")
        print(f"    integer 8 (dim H¹) at    {mp.nstr(sep8, 4)} σ  ← the identification")
        print(f"    integer 9 excluded at    {mp.nstr(sep9, 4)} σ")

    # Verdict: is 8 pinned (neighbours excluded ≫3σ) AND consistent (|D*−8| small)?
    pro = rows["proton"]
    d8 = abs(mp.mpf(pro["D_minus_8"]))
    sep_nb = min(float(pro["sep_from_7_sigma"]), float(pro["sep_from_9_sigma"]))
    pinned = sep_nb > 3.0
    consistent = float(pro["sep_from_8_sigma"]) < sep_nb          # 8 is the closest integer
    verdict = (
        f"The ladder pins the per-loop denominator to D* = {pro['D_star']} "
        f"(proton anchor), with integer neighbours 7 and 9 excluded at "
        f"≥{sep_nb:.1f}σ. "
        + ("D=8 is the UNIQUELY data-selected integer and it equals dim H¹(Bring)"
           "=2g=8 exactly — a PRECISE coincidence (not loose numerology), which "
           "sharpens (does not close) the derivation target: the residual "
           f"|D*−8| = {pro['D_minus_8']} is the (still-underived) 2-loop-and-higher "
           "tail, not a free knob."
           if pinned and consistent else
           "D=8 is NOT uniquely selected at this precision — the dim-H¹ match is "
           "looser than the 9500σ discriminant suggested; re-examine.")
        + " SCOPE (anti-laundering): D* is SOLVED FROM CODATA — this measures how "
        "forced the empirical value is, it is NOT a derivation of 1/(π·dim H¹). "
        "The open target (RT/heat-kernel zero-mode measure = 1/(π·dim H¹), value "
        "FORCED by the physics) is unchanged. No c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict)

    assertions = [
        {"name": "neighbours_excluded_gt3sigma", "passed": bool(pinned)},
        {"name": "eight_is_closest_integer", "passed": bool(consistent)},
        {"name": "D_star_within_1_of_8", "passed": bool(d8 < 1)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "alpha-em-perloop-integer-forcedness",
        "description": "Scope-(a) forcedness measurement of the α_EM per-loop-measure "
                       "denominator: solve D from the fixed-point cubic against CODATA, "
                       "test whether 8=dim H¹(Bring) is uniquely data-selected. NOT a "
                       "derivation of 1/(8π).",
        "audit_only": True,
        "tier": "numerical (forcedness measurement)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"anchors": rows, "verdict": verdict},
        "context": {
            "axis": "α_EM per-loop measure wall (1ppq path, #3612)",
            "identification_tested": "1/(8π) = 1/(π·dim H¹(M_Bring)), dim H¹=2g=8",
            "status": "D* solved from CODATA = the FIT; derivation of 1/(π·dim H¹) still open",
            "derivation_target": "RT/heat-kernel zero-mode measure on Jac(Bring)~E⁴",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "alpha-em-perloop-integer-forcedness.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. This producer reads BOTH pins on purpose
        # (it was wrongly declared q0-independent until 2026-09-03, bean qou-4bef).
        from qou_substrate.witness import WitnessBuilder as _WB, apply_q0_comparison
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        apply_q0_comparison(witness,
            muon=ANCHORS["muon"], proton=ANCHORS["proton"],
            reason="per-loop-measure integer forcedness measured at both pins on purpose; "
                   "the proton (default) leg carries the verdict")
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor="comparison")
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
