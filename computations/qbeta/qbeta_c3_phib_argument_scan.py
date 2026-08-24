#!/usr/bin/env python3
"""qbeta_c3_phib_argument_scan.py — scan Faddeev Φ_b readouts at substrate-
canonical arguments against the two c₃ bar-ODD S-leak values (cross-anchor
gate). EXPLORATORY MEASUREMENT — no c_k derived, no wiring, no fit is
promoted; every near-match is reported tiered per registry §8.

Target (docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md):
    S = c₃ + Vol(4₁):   S(muon) ≈ +0.00968298,  S(proton) ≈ −0.03945936
computed here from first principles (c3_target_at + 2·Cl₂(π/3)), not pasted.

TWO TARGET SPACES (the well-posedness observation this scan encodes):
  * S itself swings 0.049 across anchors whose q₀ differ by ~1.15e-8 relative
    ⇒ |dS/dq| ~ 4e6 — impossible for any smooth anchor-blind readout
    (the PR #1821 smoothness kill, reproduced here as a hard assertion).
    The lever is the CODATA inversion ÷u³, NOT substrate smoothness.
  * r = S·u³ = Q_codata/Q_N2 − 1 + Vol(4₁)·u³ is the UN-LEVERED residual:
    r(muon) ≈ +6.0e-9, r(proton) ≈ −2.4e-8, slope dr/dq ≈ −2.4 — a smooth,
    well-posed target a Φ_b readout CAN in principle reproduce.
  A candidate readout X is scored against BOTH: direct (X vs S) and
  un-levered (X vs r; equivalently X/u³ vs S).

READOUTS per argument z (b = √(t/2π)e^{iπ/4} pinned + validated by
phi_b_substrate_regime.py; product form == contour to 1e-39):
    Re L, Im L, |Φ|−1, and the z-odd projection components of
    L_odd(z) = (L(z) − L(−z))/2  (the z ↦ −z odd part; the inversion
    relation fixes the even part, so the odd part is the free datum).

ARGUMENT MENU (substrate-canonical; no free parameters, each named):
    u, ℏ_q², α, t/(2π), h, u/2, 2u, z_markov − 1/2,
    i·u, u·e^{iπ/4} (b-aligned), u/(2πb) (kernel-normalized), c_b·u
    (lattice-directed, substrate-scaled).

GATE (zero-parameter): max-anchor |X/target − 1| < 1e-4 for the SAME sign
convention at both anchors ⇒ reported as CANDIDATE (near-match tier, NOT
exact, NOT wired). Slope-only agreement (ΔX/Δtarget ≈ 1, values off) is
reported separately as slope-match — one-parameter family, weaker tier.

Run: python3 -u computations/qbeta/qbeta_c3_phib_argument_scan.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_argument_scan.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (os.path.join(_ROOT, "computations"),
           os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from phi_b_substrate_regime import b_substrate  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def _repo_head_sha():
    return subprocess.check_output(["git", "rev-parse", "HEAD"],
                                   cwd=_HERE, text=True).strip()


def log_phi_product(z, b, kmax):
    """log Φ_b via the (validated) modular-double product — principal log of
    each factor summed, so no 2πi branch loss for the small factors here."""
    b = mp.mpmathify(b)
    z = mp.mpmathify(z)
    two_pi_i = 2 * mp.pi * mp.mpc(0, 1)
    qq_abs = mp.fabs(mp.e ** (two_pi_i * b ** 2))
    qt_abs = mp.fabs(mp.e ** (-two_pi_i / b ** 2))
    total = mp.mpc(0)
    tol = mp.mpf(10) ** (-mp.mp.dps - 5)
    for k in range(kmax):
        kk = k + mp.mpf(1) / 2
        n = 1 + mp.e ** (two_pi_i * b ** 2 * kk + 2 * mp.pi * b * z)
        d = 1 + mp.e ** (-two_pi_i / b ** 2 * kk + 2 * mp.pi * z / b)
        total += mp.log(n) - mp.log(d)
        # BOTH tails must be spent (mirrors phi_b_double_product): for general
        # b/z the q̃-half can be the limiting tail, not just the q-half.
        if qq_abs ** (k + 1) < tol and qt_abs ** (k + 1) < tol:
            break
    return total


def main() -> int:
    set_compute_dps()
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities, c3_target_at
    from substrate import codata_constants as C

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)

    anchors = {"proton": q_at(50), "muon": q_muon_at(50)}
    t_p = mp.log(anchors["proton"])
    KMAX = int((mp.mp.dps + 10) * mp.log(10) / t_p) + 50

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # ---- targets, from first principles ----
    S, r, sub = {}, {}, {}
    for a, q in anchors.items():
        sub[a] = substrate_ladder_quantities(q)
        c3 = c3_target_at(q, Qcod, me)
        S[a] = c3 + Vol41
        r[a] = S[a] * sub[a]["u"] ** 3
    print("=" * 78)
    print(" Φ_b argument scan vs the c₃ bar-ODD S-leak (cross-anchor gate)")
    print("=" * 78)
    for a in ("muon", "proton"):
        print(f"  {a:7s}: S = {mp.nstr(S[a], 12):>18s}   r = S·u³ = {mp.nstr(r[a], 12)}")

    dq = anchors["proton"] - anchors["muon"]
    slope_S = (S["proton"] - S["muon"]) / dq
    slope_r = (r["proton"] - r["muon"]) / dq
    print(f"  Δq = {mp.nstr(dq, 8)}   dS/dq ≈ {mp.nstr(slope_S, 6)}   dr/dq ≈ {mp.nstr(slope_r, 6)}")
    check("S_lever_slope_impossible_for_smooth_readout",
          mp.fabs(slope_S) > 1e5,
          f"|dS/dq| ~ {mp.nstr(mp.fabs(slope_S), 4)} (PR #1821 kill reproduced; "
          f"lever = CODATA inversion / u^3)")
    check("unlevered_r_slope_is_smooth",
          mp.fabs(slope_r) < 100,
          f"|dr/dq| ~ {mp.nstr(mp.fabs(slope_r), 4)} — well-posed smooth target")

    # ---- argument menu + readouts per anchor ----
    def args_menu(q, b):
        s = substrate_ladder_quantities(q)
        t = mp.log(q)
        cb = mp.mpc(0, 1) * (b + 1 / b) / 2
        u = s["u"]
        return {
            "u": u,
            "hbar_q^2": s["hbar_q"] ** 2,
            "alpha": s["alpha"],
            "t/(2pi)": t / (2 * mp.pi),
            "h": s["h"],
            "u/2": u / 2,
            "2u": 2 * u,
            "z_markov-1/2": s["z"] - mp.mpf(1) / 2,
            "i*u": mp.mpc(0, 1) * u,
            "u*e^(i pi/4)": u * mp.e ** (mp.mpc(0, 1) * mp.pi / 4),
            "u/(2 pi b)": u / (2 * mp.pi * b),
            "c_b*u": cb * u,
        }

    readouts = {}   # name -> {anchor: value}
    for a, q in anchors.items():
        b = b_substrate(q, +1)
        for zname, z in args_menu(q, b).items():
            L = log_phi_product(z, b, KMAX)
            Lm = log_phi_product(-z, b, KMAX)
            Lodd = (L - Lm) / 2
            for rname, val in (
                ("Re_L", mp.re(L)), ("Im_L", mp.im(L)),
                ("abs_phi_minus_1", mp.e ** mp.re(L) - 1),
                ("Re_Lodd", mp.re(Lodd)), ("Im_Lodd", mp.im(Lodd)),
            ):
                readouts.setdefault(f"{rname}[z={zname}]", {})[a] = val

    # ---- score every readout against S and r, both signs ----
    def score(x, tgt):
        """max-anchor |x/tgt − 1| for the best common sign; inf if tiny tgt."""
        best = mp.inf
        for sgn in (1, -1):
            e = max(_ratio_err(sgn * x[a], tgt[a]) for a in anchors)
            best = min(best, e)
        return best

    def _ratio_err(x, tgt):
        if mp.fabs(tgt) < mp.mpf("1e-45"):
            return mp.inf
        return float(mp.fabs(x / tgt - 1))

    GATE = 1e-4
    rows = []
    for name, x in readouts.items():
        for tname, tgt in (("S", S), ("r", r)):
            e = score(x, tgt)
            # slope-match (1-parameter, weaker): ΔX/Δtarget within 1e-3 of ±1
            dx = x["proton"] - x["muon"]
            dt = tgt["proton"] - tgt["muon"]
            se = min(_ratio_err(dx, dt), _ratio_err(-dx, dt))
            rows.append({"readout": name, "target": tname,
                         "max_anchor_ratio_err": None if e == mp.inf else float(e),
                         "slope_ratio_err": None if se == mp.inf else float(se)})

    rows.sort(key=lambda R: (R["max_anchor_ratio_err"]
                             if R["max_anchor_ratio_err"] is not None else 1e30))
    candidates = [R for R in rows if R["max_anchor_ratio_err"] is not None
                  and R["max_anchor_ratio_err"] < GATE]
    slope_matches = [R for R in rows if R["slope_ratio_err"] is not None
                     and R["slope_ratio_err"] < 1e-3]

    print(f"\n  scanned {len(readouts)} readouts × 2 targets; gate {GATE:.0e}")
    print("  top 10 by max-anchor ratio error:")
    for R in rows[:10]:
        e = R["max_anchor_ratio_err"]
        print(f"    {R['readout']:34s} vs {R['target']:1s}: "
              f"err {e if e is not None else float('inf'):.3e}   "
              f"slope-err {R['slope_ratio_err'] if R['slope_ratio_err'] is not None else float('inf'):.3e}")

    check("zero_parameter_candidate_search_completed", True,
          f"{len(candidates)} candidate(s) under gate; {len(slope_matches)} slope-match(es)")

    all_passed = all(a["passed"] for a in assertions)
    n_c, n_s = len(candidates), len(slope_matches)
    best = rows[0] if rows else None
    verdict = (
        (f"CANDIDATE(S) FOUND (near-match tier, NOT exact, NOT wired): {n_c} "
         f"readout(s) reproduce the target at BOTH anchors under {GATE:.0e}. "
         "Requires independent-method confirmation + registry section-8 guard "
         "before any tier upgrade."
         if n_c else
         f"NO zero-parameter candidate under {GATE:.0e} among the {len(readouts)} "
         f"substrate-canonical Φ_b readouts scanned (best: {best['readout']} vs "
         f"{best['target']}, err {best['max_anchor_ratio_err']:.2e}). "
         f"{n_s} slope-match(es) recorded (1-parameter tier, weaker). "
         "Scope-(a): THIS menu alone, as-is, does not reproduce the S-leak — "
         "no structural exclusion of Φ_b readouts implied; the menu is finite "
         "and the c_b-lattice / complex-argument space is mostly unexplored.")
        + " The un-levered target r = S·u³ (slope ≈ −2.4, smooth) is the "
          "well-posed search space; S itself is smoothness-killed (lever = ÷u³)."
        if all_passed else "INCONCLUSIVE — an assertion failed."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-c3-phib-argument-scan",
        "description": "Cross-anchor scan of Faddeev Phi_b readouts at "
                       "substrate-canonical arguments vs the c3 bar-odd S-leak "
                       "(S and un-levered r = S*u^3). Exploratory measurement; "
                       "no wiring.",
        "auditOnly": True,
        "tier": "exploratory-scan (registry untouched; flip-flop guard section 8 respected)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "precision_dps": mp.mp.dps,
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "S_muon": mp.nstr(S["muon"], 20), "S_proton": mp.nstr(S["proton"], 20),
            "r_muon": mp.nstr(r["muon"], 20), "r_proton": mp.nstr(r["proton"], 20),
            "dS_dq": mp.nstr(slope_S, 10), "dr_dq": mp.nstr(slope_r, 10),
            "n_readouts": len(readouts),
            "gate": GATE,
            "n_candidates": n_c,
            "n_slope_matches": n_s,
            "top10": rows[:10],
            "verdict": verdict,
        },
        "context": {
            "s_leak_target": "docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md",
            "evaluator_validation": "computations/qbeta/phi-b-substrate-regime.witness.json",
            "lean_scaffold": "content/quantum-observable-universe/lean/QOU/MathlibExt/FaddeevQuantumDilogarithm.lean",
            "smoothness_kill": "PR #1821 (dc3/dq ~ 4.6e6 impossible for smooth real f)",
        },
    }
    out = os.path.join(_HERE, "qbeta-c3-phib-argument-scan.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
