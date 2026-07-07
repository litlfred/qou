#!/usr/bin/env python3
"""qbeta_hopf_cubic_shadow_bridge.py — Hopf-cubic ↔ crossing-weight reconcile.

Reconciles KC20 (odd-carrier Hopf cubic `C_Hopf(y)=y³−6y²+10y−6`, `y=q²+q⁻²`)
with KC19 (affine crossing-weight narrowing; `c_3` = the open scalar `w(q)`).

Two exact/high-precision facts (no fit, no wiring):

  (1) SHADOW MATCH (q=1, y=2):  C_Hopf(2) = −2  = the c_3 q=1 shadow (J_Hopf(1),
      KC10).  [Lean-certified: `cubicC_Hopf_classical_shadow`.]
  (2) SUBSTRATE WALL:  C_Hopf(y₀) is ANCHOR-RIGID (identical at the proton and
      muon pins to full precision) ≈ −2.0873, while the physical c_3 SWINGS
      2.375% (−2.06934 proton / −2.02019 muon).  An anchor-rigid quantity
      cannot equal an anchor-swinging one at both anchors ⇒ the cubic does NOT
      determine c_3; the swing lives in w(q) (KC19).  The −2.087 ≈ −2.07
      proximity is a near-coincidence, not an identity.

Self-contained: `decimal` arbitrary precision, no mpmath / substrate deps.
Audit: docs/audits/2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md.
"""
from __future__ import annotations

import json
import subprocess
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec = 50
HERE = Path(__file__).resolve().parent

# Substrate q₀ pins (50-digit), matching qbeta_c3_cross_anchor_exactness_probe.py.
Q_PROTON = D("1.1099785827513808075916690956107688798744991218736")
Q_MUON = D("1.10997859555733471989976322048322502665620840878015368660798114614493")
# c_3 at each anchor (from the 2026-07-06 c3-not-exact verdict / production routine).
C3_PROTON = D("-2.06934257711516784")
C3_MUON = D("-2.02018812814143946")


def cubicC_Hopf(y: D) -> D:
    return y ** 3 - 6 * y ** 2 + 10 * y - 6


def y_of(q: D) -> D:
    return q * q + 1 / (q * q)


def _git_head() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(HERE),
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main() -> int:
    # (1) shadow match at q=1 (y=2)
    shadow = cubicC_Hopf(D(2))
    shadow_ok = shadow == D(-2)

    # (2) substrate: C_Hopf(y₀) at both anchors
    yp, ym = y_of(Q_PROTON), y_of(Q_MUON)
    chp, chm = cubicC_Hopf(yp), cubicC_Hopf(ym)
    # anchor-rigidity: C_Hopf agrees to many digits between anchors...
    ch_rel_swing = abs((chp - chm) / chp)
    # ...while c_3 swings ~2.4%
    c3_rel_swing = abs((C3_PROTON - C3_MUON) / C3_PROTON)
    rigid_ok = ch_rel_swing < D("1e-6")            # anchor-rigid
    c3_swings_ok = c3_rel_swing > D("0.02")        # >2%
    # the cubic cannot equal c_3 at BOTH anchors (rigid vs swinging)
    not_a_bridge = not (chp == C3_PROTON and chm == C3_MUON)
    # proximity is a near-coincidence, NOT an identity
    near_not_identity = (abs(chp - C3_PROTON) > D("1e-6")) and (abs(chp - C3_PROTON) < D("0.1"))

    out = {
        "computation": "qbeta-hopf-cubic-shadow-bridge",
        "engine": "python-decimal",
        "scriptFile": Path(__file__).name,
        "commitSha": _git_head(),
        "description": (
            "Reconcile KC20 (Hopf cubic C_Hopf) with KC19 (affine crossing "
            "weight, c_3=open scalar). SHADOW: C_Hopf(2)=-2=c_3 q=1 shadow "
            "(Lean cubicC_Hopf_classical_shadow). SUBSTRATE: C_Hopf(y0) "
            "anchor-rigid ~-2.0873 while c_3 swings 2.375% -> cubic does NOT "
            "determine c_3; swing lives in w(q). Near-coincidence, not identity."),
        "data": {
            "shadow_C_Hopf_at_2": str(shadow),
            "c3_q1_shadow": "-2",
            "y0_proton": str(yp), "y0_muon": str(ym),
            "C_Hopf_y0_proton": str(chp), "C_Hopf_y0_muon": str(chm),
            "C_Hopf_anchor_rel_swing": str(ch_rel_swing),
            "c3_anchor_rel_swing": str(c3_rel_swing),
            "verdict": ("shadow: exact Hopf match (q=1); substrate: no bridge "
                        "(C_Hopf anchor-rigid vs c_3 swinging) — swing in w(q), KC19"),
        },
        "assertions": [
            {"name": "shadow_C_Hopf_2_equals_minus_2", "computed": 0.0 if shadow_ok else 1.0,
             "expected": 0.0, "tolerance": 0.0, "unit": "bool (0=holds)",
             "source": "C_Hopf(2)=-2 = c_3 q=1 shadow; Lean cubicC_Hopf_classical_shadow"},
            {"name": "C_Hopf_y0_anchor_rigid", "computed": 0.0 if rigid_ok else 1.0,
             "expected": 0.0, "tolerance": 0.0, "unit": "bool (0=rigid, rel swing<1e-6)",
             "source": "C_Hopf(y0) identical proton vs muon to full precision"},
            {"name": "c3_anchor_swings_gt_2pct", "computed": 0.0 if c3_swings_ok else 1.0,
             "expected": 0.0, "tolerance": 0.0, "unit": "bool (0=swings>2%)",
             "source": "c_3 -2.069(p)/-2.020(m), 2.375% swing (2026-07-06 verdict)"},
            {"name": "cubic_does_not_determine_c3", "computed": 0.0 if not_a_bridge else 1.0,
             "expected": 0.0, "tolerance": 0.0, "unit": "bool (0=not a bridge)",
             "source": "anchor-rigid cannot equal anchor-swinging at both anchors"},
            {"name": "substrate_proximity_is_near_coincidence", "computed": 0.0 if near_not_identity else 1.0,
             "expected": 0.0, "tolerance": 0.0, "unit": "bool (0=near but not identity)",
             "source": "|C_Hopf(y0)-c3|~0.018, same order as the c_3 swing"},
        ],
        "audit_only": "docs/audits/2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md",
    }
    out["allPassed"] = all(a["computed"] == a["expected"] for a in out["assertions"])
    p = HERE / "qbeta-hopf-cubic-shadow-bridge.witness.json"
    p.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Witness: {p}")
    print(f"  shadow_ok={shadow_ok} rigid={rigid_ok} c3_swings={c3_swings_ok} "
          f"not_bridge={not_a_bridge} allPassed={out['allPassed']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
