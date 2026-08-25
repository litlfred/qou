#!/usr/bin/env python3
"""
Re-scope: the c_3 = -Vol(4_1) + u - (10/3)u^2 "keystone" is a MUON-anchor
near-match, NOT an exact derivation of c_3.

The audit docs/audits/2026-07-08-qbeta-keystone-derivation.md claims (Status:
"PROVEN, LEAN-CERTIFIED") that c_3 = -Vol(4_1) + u - (10/3)u^2 is an exact
theorem and "c_3 is no longer an empirically calibrated input." This probe
verifies the claim against BOTH substrate anchors and shows it is anchor-blind:
the formula gives ~ -2.0216 at every anchor (Vol(4_1) is a fixed constant and u
barely moves), while the ACTUAL c_3 SWINGS 2.4% between the proton and muon
anchors. So the formula reproduces the muon-anchored c_3 (~0.07%) but MISSES the
proton anchor (~2.3%) -- a single-anchor near-match, scope-(a), NOT an exact
derivation of the anchor-swinging c_3.

This does NOT refute the structural pieces:
  * -Vol(4_1) is the legitimately-solved bar-EVEN part (4_1 amphichiral, real;
    #3474 c3-even-solved, #3487 parity-chirality dictionary).
  * 10/3 = lim_{q->1} [10]_q/[3]_q is a genuine writhe-ratio identity
    (T_{3,5} mediator crossings / 3_1 electron crossings).
What is over-claimed is the TIER: the anchor-SWINGING part of c_3 (the CAL-2
S-leak) is Subgoal-2 and is NOT captured by an anchor-blind real formula. This
is exactly the registry section 8 flip-flop guard (a wired c_k>=3 needs a
passing proton+muon cross-anchor swing < 1%; this FAILS at 2.3%) and the
c_3-not-exact verdict (2026-07-06, 6th settle).

Exact/high-precision; NO fit introduced here (it MEASURES an existing fit's
anchor behaviour). Anchors sourced from qou_substrate (q_at / q_muon_at).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
# Add `computations` (for `substrate.codata_constants`) and the tools path (for
# `qou_substrate`). The script's own dir (`computations/qbeta`, for `qbeta_utils`)
# is auto-added by Python on direct execution, so it is not inserted here.
for _p in (os.path.join(_ROOT, "computations"),
           os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)


def _repo_head_sha():
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def main():
    set_compute_dps()
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities, c3_target_at
    from substrate import codata_constants as C

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)          # Vol(4_1) = 2*Cl_2(pi/3)
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    def claim(q):
        u = substrate_ladder_quantities(q)["u"]
        return -Vol41 + u - mp.mpf(10) / 3 * u ** 2

    q_p = q_at(50)
    q_m = q_muon_at(50)
    c3_p, c3_m = c3_target_at(q_p, Qcod, me), c3_target_at(q_m, Qcod, me)
    cl_p, cl_m = claim(q_p), claim(q_m)
    miss_p = float((cl_p / c3_p - 1) * 100)
    miss_m = float((cl_m / c3_m - 1) * 100)
    swing = float((c3_p / c3_m - 1) * 100)

    # 10/3 writhe-ratio identity is REAL (structural piece kept).
    from sympy import symbols, limit, Rational, simplify
    qs = symbols('q', positive=True)
    r = (qs ** 10 - qs ** -10) / (qs ** 3 - qs ** -3)
    tenthirds = simplify(limit(r, qs, 1))
    check("writhe_ratio_10_3_is_exact_identity", tenthirds == Rational(10, 3),
          f"lim_q->1 [10]_q/[3]_q = {tenthirds} (T_3,5 / 3_1 crossings) -- structural piece REAL")

    # The claim is anchor-blind: same value at both anchors.
    check("claim_is_anchor_blind",
          abs(float(cl_p - cl_m)) < 1e-6,
          f"claim(proton)={mp.nstr(cl_p,9)}  claim(muon)={mp.nstr(cl_m,9)} (~equal)")

    # Actual c_3 SWINGS across anchors (the object the claim must match).
    check("actual_c3_swings_across_anchors",
          abs(swing) > 1.0,
          f"c3(proton)={mp.nstr(c3_p,9)}  c3(muon)={mp.nstr(c3_m,9)}  swing={swing:.3f}%")

    # Muon near-match, proton fail -> single-anchor near-match, not exact.
    check("muon_near_match", abs(miss_m) < 0.5, f"muon miss = {miss_m:.4f}% (near-match)")
    check("proton_fails", abs(miss_p) > 1.0, f"proton miss = {miss_p:.4f}% (fails)")

    # Fails the section-8 cross-anchor guard (< 1% both anchors).
    check("fails_section8_cross_anchor_guard",
          abs(miss_p) > 1.0,
          f"max anchor miss {max(abs(miss_p),abs(miss_m)):.3f}% > 1% => not canonical (registry section 8)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "RE-SCOPE (scope-(a)): c_3 = -Vol(4_1) + u - (10/3)u^2 is a MUON-anchor near-match "
        f"(muon {miss_m:.3f}%, proton {miss_p:.3f}%), NOT an exact derivation of c_3. The "
        f"formula is anchor-blind (~{mp.nstr(cl_p,7)} at both anchors) while the actual c_3 "
        f"SWINGS {swing:.2f}% (proton {mp.nstr(c3_p,7)} vs muon {mp.nstr(c3_m,7)}). It fails "
        "the registry section-8 cross-anchor guard (2.3% > 1%) and contradicts the live "
        "registry section 3 (c_3 EMPIRICAL, REFUTED as real-q). Structural pieces are REAL "
        "and kept: -Vol(4_1) is the solved bar-even part (#3474/#3487); 10/3 = lim [10]_q/[3]_q "
        "is an exact writhe-ratio identity. What is over-claimed is the TIER: the anchor-swinging "
        "part (CAL-2 S-leak) is Subgoal-2, not captured by an anchor-blind real formula. Corrects "
        "docs/audits/2026-07-08-qbeta-keystone-derivation.md ('PROVEN/exact theorem'). No c_k "
        "wired; nothing changed in production."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-c3-keystone-anchor-blind",
        "description": "Re-scope: c_3 = -Vol(4_1)+u-(10/3)u^2 is a muon-anchor near-match "
                       "(0.07% muon / 2.3% proton), anchor-blind vs a 2.4%-swinging c_3; "
                       "fails the section-8 cross-anchor guard. Structural pieces (-Vol(4_1), "
                       "10/3 writhe ratio) kept; the 'exact/PROVEN' tier is corrected.",
        "auditOnly": True,
        "tier": "measurement-exact (high-precision anchor comparison; measures an existing fit)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath+sympy",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "claim_proton": mp.nstr(cl_p, 12), "claim_muon": mp.nstr(cl_m, 12),
            "c3_proton": mp.nstr(c3_p, 12), "c3_muon": mp.nstr(c3_m, 12),
            "miss_proton_pct": miss_p, "miss_muon_pct": miss_m, "c3_swing_pct": swing,
            "Vol_4_1": mp.nstr(Vol41, 12),
            "verdict": verdict,
        },
        "context": {
            "corrects": "docs/audits/2026-07-08-qbeta-keystone-derivation.md (commit e21a9426)",
            "registry": "docs/coordination/ck-dk-canonical-registry.md section 3 (c_3 EMPIRICAL) + section 8 guard",
            "c3_not_exact_verdict": "docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md",
            "even_part_solved": "docs/audits/2026-07-07-parity-chirality-dictionary-closed.md (#3487); #3474",
        },
    }
    out = os.path.join(_HERE, "qbeta-c3-keystone-anchor-blind.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== c_3 keystone anchor-blind re-scope ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
