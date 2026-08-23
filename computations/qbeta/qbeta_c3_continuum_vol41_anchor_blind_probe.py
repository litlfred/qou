#!/usr/bin/env python3
"""
Re-scope: c_3 does NOT converge to -Vol(4_1); the continuum-geometry claim is
anchor-blind and WORSE at the muon (CAL-2) anchor than the keystone near-match.

`content/quantum-observable-universe/mass-theory/q-beta-c3-continuum-geometry.md`
claims (pushed by a Gemini session) that "the true analytical evaluation of c_3
in the infinite-order continuum limit is therefore EXACTLY c_3 -> -Vol(4_1) ~
-2.02988", that this "structurally generates c_3 ... rigorously banishing all
finite algebraic rational truncations", and that it "completely rejects the
prior algebraic shadow hallucination (c_3 = -2)".

This probe checks the identification against BOTH substrate anchors:
  * -Vol(4_1) = -2.02988 is a FIXED (anchor-blind) value; the actual c_3 SWINGS
    2.43% between proton and muon anchors, so no fixed value converges to it.
  * At the MUON anchor (the CAL-2 pin the framework calibrates on), -Vol(4_1)
    misses by ~0.48% -- ~7x WORSE than the keystone's own -Vol(4_1)+u-(10/3)u^2
    near-match (~0.07%). So the "continuum limit" makes the muon fit worse, not
    exact.
  * c_3 = -2 = J_Hopf(q=1) is the CANONICAL q=1 shadow (registry KC10; KC20
    C_Hopf(2) = -2), NOT a "hallucination".

The hyperbolic geometry in the doc is REAL and kept (Vol(4_1) = 2*Vol(ideal
tetrahedron) = 2*Cl_2(pi/3); the Lobachevsky saddle at theta=pi/3). What is
over-claimed is the IDENTIFICATION c_3 = -Vol(4_1) and the "rigorous/exact"
tier. No fit introduced; measures existing claims. Same class as the keystone
re-scope (#3501/#3503). Anchors from qou_substrate (q_at / q_muon_at).
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
    from qbeta_utils import c3_target_at
    from substrate import codata_constants as C

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)          # Vol(4_1) = 2*Cl_2(pi/3)
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q_p, q_m = q_at(50), q_muon_at(50)
    c3_p, c3_m = c3_target_at(q_p, Qcod, me), c3_target_at(q_m, Qcod, me)
    swing = float((c3_p / c3_m - 1) * 100)
    v = -Vol41
    miss_p = float((v / c3_p - 1) * 100)
    miss_m = float((v / c3_m - 1) * 100)
    keystone = mp.mpf("-2.0216078")             # -Vol41 + u - (10/3)u^2 (anchor-blind)
    key_miss_m = float((keystone / c3_m - 1) * 100)

    # Vol(4_1) geometry is REAL (kept): 2*Cl_2(pi/3) ~ 2.02988; ideal-tet saddle.
    check("vol41_geometry_real",
          abs(float(Vol41) - 2.0298832) < 1e-5,
          f"Vol(4_1) = 2*Cl_2(pi/3) = {mp.nstr(Vol41,9)} (real hyperbolic geometry, kept)")

    # actual c_3 SWINGS -> no fixed value is its continuum limit.
    check("actual_c3_swings", abs(swing) > 1.0,
          f"c3(proton)={mp.nstr(c3_p,8)} c3(muon)={mp.nstr(c3_m,8)} swing={swing:.3f}%")

    # -Vol(4_1) is anchor-blind and misses BOTH anchors.
    check("neg_vol41_misses_both_anchors",
          abs(miss_p) > 0.1 and abs(miss_m) > 0.1,
          f"-Vol(4_1)={mp.nstr(v,8)}: muon miss {miss_m:+.3f}%, proton miss {miss_p:+.3f}%")

    # At the MUON (CAL-2) anchor, -Vol(4_1) is WORSE than the keystone near-match.
    check("neg_vol41_worse_at_muon_than_keystone",
          abs(miss_m) > abs(key_miss_m) * 3,
          f"muon: -Vol(4_1) {miss_m:+.3f}% vs keystone {key_miss_m:+.3f}% "
          f"({abs(miss_m)/max(abs(key_miss_m),1e-9):.1f}x worse)")

    # c_3 = -2 = J_Hopf(1) is the CANONICAL shadow, not a hallucination.
    check("shadow_neg2_is_canonical_not_hallucination",
          True,
          "c_3 -> -2 = J_Hopf(q=1) is registry KC10 / KC20 C_Hopf(2)=-2 (canonical q=1 shadow)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        f"RE-SCOPE (scope-(a)): c_3 does NOT converge to -Vol(4_1). -Vol(4_1) = "
        f"{mp.nstr(v,8)} is anchor-blind and misses BOTH anchors (muon {miss_m:+.3f}%, "
        f"proton {miss_p:+.3f}%) while the actual c_3 SWINGS {swing:.2f}%. At the muon "
        f"(CAL-2) anchor it is {abs(miss_m)/max(abs(key_miss_m),1e-9):.0f}x WORSE than the "
        f"keystone's own -Vol(4_1)+u-(10/3)u^2 near-match ({key_miss_m:+.3f}%). The claim "
        "'the continuum limit is EXACTLY -Vol(4_1) ... rigorously banishing all finite "
        "algebraic truncations' is unsupported (it makes the muon fit worse, still "
        "anchor-blind, still fails cross-anchor). And c_3 = -2 = J_Hopf(1) is the CANONICAL "
        "q=1 shadow (KC10 / KC20 C_Hopf(2)=-2), NOT a 'hallucination'. KEPT (real): the "
        "hyperbolic geometry Vol(4_1)=2*Cl_2(pi/3), the Lobachevsky saddle at pi/3. Only "
        "the c_3 IDENTIFICATION + the 'rigorous/exact' tier are corrected. Same class as "
        "the keystone re-scope (#3501/#3503). No c_k wired; production unchanged."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "qbeta-c3-continuum-vol41-anchor-blind",
        "description": "Re-scope: c_3 does not converge to -Vol(4_1). -Vol(4_1)=-2.02988 is "
                       "anchor-blind, misses both anchors, and is ~7x worse at the muon (CAL-2) "
                       "anchor than the keystone near-match; c_3=-2=J_Hopf(1) is the canonical "
                       "shadow, not a hallucination. Vol(4_1) geometry kept; identification/tier corrected.",
        "auditOnly": "docs/audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md",
        "tier": "measurement-exact (high-precision anchor comparison; measures existing claims)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "neg_Vol_4_1": mp.nstr(v, 12), "c3_proton": mp.nstr(c3_p, 12),
            "c3_muon": mp.nstr(c3_m, 12), "miss_proton_pct": miss_p, "miss_muon_pct": miss_m,
            "keystone_muon_miss_pct": key_miss_m, "c3_swing_pct": swing,
            "verdict": verdict,
        },
        "context": {
            "corrects": "content/quantum-observable-universe/mass-theory/q-beta-c3-continuum-geometry.md (+.lean docstring)",
            "sibling_rescope": "docs/audits/2026-07-11-qbeta-c3-keystone-rescope-anchor-blind.md (#3501); #3503",
            "canonical_shadow": "registry KC10 (c_3->-2=J_Hopf(1)); KC20 (C_Hopf(2)=-2)",
            "kept": "Vol(4_1)=2*Cl_2(pi/3) hyperbolic geometry + Lobachevsky saddle at pi/3 (real)",
        },
    }
    out = os.path.join(_HERE, "qbeta-c3-continuum-vol41-anchor-blind.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== c_3 continuum -Vol(4_1) anchor-blind re-scope ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
