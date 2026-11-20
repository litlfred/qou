#!/usr/bin/env python3
"""Meridian-holonomy q₀↦u deformation MAGNITUDE — the TRUE anchor-swing test.

Bean qou-b8mf (milestone qou-t5d0). Branch
`claude/qbeta-meridian-holonomy-c3-anchor-2026-07-25`, PR #4288.

DISTINCT ANGLE (orthogonal to #4283; measured research-overlap permitted per the
2026-07-18 owner relaxation). C1 (#4282, `QOU.QBeta.BarOddAntisymOffDiagonal`,
sorry-free) proved the bar-odd datum is the ι-odd antisymmetric off-diagonal
ω(β,p,q)=β·p−β⁻¹·q and its companion showed ω is ANCHOR-SMOOTH (4.56 ppm) while
c₃ swings 3.47%. C1 relocated the missing anchor-dependence to the
meridian-holonomy q₀↦u deformation (CuspShapeBarParity's open link). #4283 chases
the in-block module-map successors; THIS probe attacks the q₀↦u deformation's
MAGNITUDE channel directly.

THE TRUE ANCHOR COMPARISON (the honest test the C1/2026-07-11 audits did not do
cleanly — that audit matched |S(muon)| with |u|=barOdd(√q₀) and |S(proton)| with
|u|=barOdd(q₀), i.e. it substituted a DIFFERENT coordinate at the SAME anchor,
which is fit-adjacent). Here we hold the coordinate FIXED (the meridian-holonomy
bar-odd deformation shape barOdd(q)=q−q⁻¹, ≡ u+O(u³) with u=2·ln q₀) and evaluate
it at BOTH committed q₀ anchors, measuring the swing the deformation magnitude
actually produces.

Meridian holonomy = multiplication by q (meridian-holonomy-boost.md). The NZ
observable enters as S ∝ u² (leading Neumann–Zagier term CVol(u)=Vol−(τ/4)u²+…).
The deformation-magnitude's log-q sensitivity is barEven/barOdd, whose SQUARE the
boost hyperbola barEven²−barOdd²=4 pins EXACTLY (Lean, sorry-free):

    QOU.QBeta.MeridianHolonomyAnchorCarrier.sensitivity_sq:
        (barEven q / barOdd q)² = 1 + 4/(barOdd q)²

This probe MEASURES the order of the anchor swing that this magnitude channel
produces, and confirms the Lean amplification bound
barOdd_sq_le_of_amplification: reaching amplification ρ≥N forces
(barOdd q)² ≤ 4/(N²−1), i.e. q near the compact locus barOdd=0 (q=±1).

Consumes committed values only — muon q₀ from the q-pinning witness, proton q₀
from the committed qou-substrate package constant, the c₃ swing from the corpus
canonical framing (2026-05-31), and the A1 bar-odd home swing as a cross-check.
No state integral is re-run; NO wide scan; nothing inverts Q_β/CODATA; no c_k
wired.

Assertions (pre-registered, scope-(a)):
  A1  sensitivity_sq identity holds at both anchors (probe↔Lean tie, residual→0).
  A2  the deformation-magnitude anchor swing Δ(u²)/u² is O(ppm) (< 1e-5) —
      anchor-smooth, matching C1's ω (4.56 ppm); it equals 2·ρ_u·(Δq₀/q₀) to
      leading order.
  A3  (c₃ swing 3.47%)/(deformation-magnitude swing) > 1e4 — the decisive
      scope-(a) statement: the deformation MAGNITUDE cannot realise the c₃ swing.
  A4  the required amplification ρ_req = (c₃ swing)/(anchor spacing) ≥ 1e6, and
      barOdd(q₀) exceeds the compact-locus bound 2/√(ρ_req²−1) by ≥ 5 orders —
      the substrate is ~5 orders too FAR from the compact locus for a magnitude
      amplification.

VERDICT (pre-registered): scope-(a) NEGATIVE. The meridian-holonomy q₀↦u
deformation MAGNITUDE is anchor-smooth at the substrate (O(ppm) swing, ρ≈9.6),
so — like C1's ω and #4283's in-block maps — it cannot alone realise the c₃
percent swing. The swing lives only in the near-singular / non-perturbative PHASE
arg(u) (consistent with #3818's ξ-frame phase law). Bounds BOTH this route and
#4283's in-block maps under one exact criterion (amplification ⇒ proximity to the
compact locus). Does NOT close c₃; the phase remains the open
conj:algebraic-geometric-dilog-equivalence.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

from mpmath import mp, mpf, log, sqrt

mp.dps = 60

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
_OUT = _HERE / "qbeta-meridian-holonomy-anchor-swing.witness.json"


def _git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def _read_muon_q0() -> mpf:
    """Muon-anchored q₀ — the canonical computations-layer 50-digit value."""
    w = json.loads((_ROOT / "computations" / "q-pinning-50-digit.witness.json").read_text())
    # committed field: derived_50_digit.q  (== q0Value)
    for key in ("derived_50_digit",):
        if key in w.get("data", w) if isinstance(w, dict) else {}:
            pass
    # robust walk
    def find_q(o):
        if isinstance(o, dict):
            if "q0Value" in o:
                return o["q0Value"]
            for v in o.values():
                r = find_q(v)
                if r is not None:
                    return r
        return None
    q = find_q(w)
    return mpf(str(q))


def _read_proton_q0() -> mpf:
    """Proton-anchored q₀ — the committed qou-substrate package 50-digit constant."""
    import sys
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP
    return Q_MP


def bar_odd(q: mpf) -> mpf:
    return q - 1 / q


def bar_even(q: mpf) -> mpf:
    return q + 1 / q


def main() -> int:
    assertions = []

    q_mu = _read_muon_q0()
    q_pr = _read_proton_q0()

    # --- committed corpus references (NOT re-derived, NOT inverted) ----------
    # c₃ cross-anchor swing: 3.47 % (2026-05-31 canonical framing; AGENTS.md).
    C3_SWING = mpf("0.0347")
    # A1 bar-odd HOME swing (C1), as an independent cross-check of the ppm scale.
    A1 = json.loads(
        (_ROOT / "computations" / "probes" / "qbeta-5two-chirality-state-integral.witness.json").read_text()
    )
    odd_mu = mpf(str(A1["data"]["chirality_split"]["muon"]["odd_ImZhat"]))
    odd_pr = mpf(str(A1["data"]["chirality_split"]["proton"]["odd_ImZhat"]))
    a1_odd_home_swing = abs(odd_pr - odd_mu) / abs(odd_mu)

    # --- anchor spacing ------------------------------------------------------
    dq_rel = abs(q_pr - q_mu) / q_mu  # |Δq₀|/q₀ (≈ 11.5 ppb)

    # --- per-anchor deformation-magnitude data -------------------------------
    per_anchor = {}
    for name, q0 in (("muon", q_mu), ("proton", q_pr)):
        bo = bar_odd(q0)
        be = bar_even(q0)
        u = 2 * log(q0)  # NZ meridian coordinate; ≈ barOdd(q0) to O(u³)
        rho_u = be / bo  # d log|barOdd| / d log q  (magnitude sensitivity)
        # sensitivity_sq (Lean) identity residual:
        sens_lhs = rho_u ** 2
        sens_rhs = 1 + 4 / bo ** 2
        per_anchor[name] = {
            "q0": mp.nstr(q0, 30),
            "barOdd": mp.nstr(bo, 24),
            "barEven": mp.nstr(be, 24),
            "u_2lnq": mp.nstr(u, 24),
            "u_vs_barOdd_rel": mp.nstr(abs(u - bo) / abs(bo), 6),
            "rho_u_magnitude_sensitivity": mp.nstr(rho_u, 18),
            "rho_S_channel_2rho": mp.nstr(2 * rho_u, 18),
            "sensitivity_sq_residual": mp.nstr(abs(sens_lhs - sens_rhs), 6),
        }

    # --- A1: sensitivity_sq identity holds at both anchors -------------------
    max_sens_resid = max(
        abs((bar_even(q0) / bar_odd(q0)) ** 2 - (1 + 4 / bar_odd(q0) ** 2))
        for q0 in (q_mu, q_pr)
    )
    assertions.append({
        "name": "sensitivity_sq_identity_both_anchors",
        "computed": mp.nstr(max_sens_resid, 6),
        "expected": 0.0,
        "passed": max_sens_resid < mpf("1e-40"),
        # String, not the float literal. This probe hand-builds its assertion
        # dicts and json.dumps them, so it never constructs an `Assertion` and
        # `qou_substrate.witness._tolerance_literal` — which converts a declared
        # tolerance to its literal at `Assertion.to_dict` — never runs. These
        # are exactly the strings that helper returns for these two values.
        "tolerance": "1e-40",
        "source": "(barEven/barOdd)² = 1 + 4/barOdd² at both q₀ anchors — the "
        "boost-hyperbola identity, probe↔Lean "
        "MeridianHolonomyAnchorCarrier.sensitivity_sq tie",
    })

    # --- A2: deformation-magnitude anchor swing is O(ppm) --------------------
    # true anchor comparison, coordinate FIXED (u=2 ln q): swing of the S∝u² channel.
    u_mu = 2 * log(q_mu)
    u_pr = 2 * log(q_pr)
    S_channel_swing = abs(u_pr ** 2 - u_mu ** 2) / (u_mu ** 2)   # Δ(u²)/u²
    barOdd_swing = abs(bar_odd(q_pr) - bar_odd(q_mu)) / abs(bar_odd(q_mu))
    # leading-order prediction 2·ρ_u·(Δq₀/q₀):
    rho_u_mu = bar_even(q_mu) / bar_odd(q_mu)
    pred_S_swing = 2 * rho_u_mu * dq_rel
    assertions.append({
        "name": "deformation_magnitude_swing_is_ppm",
        "computed": mp.nstr(S_channel_swing, 8),
        "expected": "< 1e-5 (O(ppm)); ≈ 2·ρ_u·(Δq₀/q₀)",
        "passed": S_channel_swing < mpf("1e-5"),
        "tolerance": "1e-05",
        "source": "Δ(u²)/u² across the muon↔proton q₀ anchors, coordinate FIXED "
        "(u=2 ln q). Leading-order 2·ρ_u·(Δq₀/q₀)=" + mp.nstr(pred_S_swing, 8)
        + "; barOdd-shape swing=" + mp.nstr(barOdd_swing, 8)
        + "; cross-check A1 ω home swing=" + mp.nstr(a1_odd_home_swing, 8),
    })

    # --- A3: (c₃ swing)/(deformation-magnitude swing) > 1e4 ------------------
    ratio = C3_SWING / S_channel_swing
    assertions.append({
        "name": "c3_swing_over_deformation_magnitude_swing_gt_1e4",
        "computed": mp.nstr(ratio, 8),
        "expected": "> 1e4",
        "passed": ratio > mpf("1e4"),
        "tolerance": 1e4,
        "source": "(c₃ cross-anchor swing 3.47%)/(deformation-magnitude swing): "
        "decisive scope-(a) — the meridian-holonomy deformation MAGNITUDE is "
        "anchor-smooth and cannot alone realise the c₃ swing",
    })

    # --- A4: required amplification vs the compact-locus bound ----------------
    # ρ_req = (c₃ swing)/(anchor spacing).  Lean barOdd_sq_le_of_amplification:
    #   ρ≥N ⟹ (barOdd)² ≤ 4/(N²−1).  So a magnitude amplification ρ_req needs
    #   |barOdd| ≤ 2/√(ρ_req²−1).  Compare to the actual barOdd(q₀).
    rho_req = C3_SWING / dq_rel
    barOdd_max_for_req = 2 / sqrt(rho_req ** 2 - 1)
    barOdd_actual = abs(bar_odd(q_mu))
    orders_too_far = log(barOdd_actual / barOdd_max_for_req) / log(10)
    assertions.append({
        "name": "substrate_far_from_compact_locus",
        "computed": "ρ_req=" + mp.nstr(rho_req, 6)
        + ", barOdd_max_for_req=" + mp.nstr(barOdd_max_for_req, 6)
        + ", barOdd_actual=" + mp.nstr(barOdd_actual, 6)
        + ", orders_too_far=" + mp.nstr(orders_too_far, 6),
        "expected": "ρ_req ≥ 1e6 AND orders_too_far ≥ 5",
        "passed": (rho_req > mpf("1e6")) and (orders_too_far > mpf("5")),
        "tolerance": None,
        "source": "Lean barOdd_sq_le_of_amplification: reaching ρ_req forces "
        "|barOdd|≤2/√(ρ_req²−1). The substrate barOdd(q₀)≈0.209 exceeds that "
        "bound by ~5 orders ⇒ the meridian deformation magnitude is ~5 orders "
        "too far from the compact locus barOdd=0 (q=±1) to supply the swing.",
    })

    passed = sum(1 for a in assertions if a["passed"])
    witness = {
        "schema": "witness/v1",
        "id": "qbeta-meridian-holonomy-anchor-swing",
        "title": "Meridian-holonomy q₀↦u deformation MAGNITUDE is anchor-smooth "
        "(exact boost-hyperbola amplification bound; true anchor comparison)",
        "description": "Scope-(a) NEGATIVE: the meridian-holonomy deformation "
        "magnitude channel produces an O(ppm) anchor swing (ρ≈9.6=O(10)), ~1.5e5× "
        "too smooth for the 3.47% c₃ swing; reaching the needed amplification "
        "would require q₀ within ~3e-7 of 1 (compact locus), but the substrate is "
        "~0.11 away. Ties to Lean sensitivity_sq / barOdd_sq_le_of_amplification. "
        "No fit; nothing inverts Q_β/CODATA; no c_k wired.",
        "producer": "computations/qbeta/qbeta_meridian_holonomy_anchor_swing_probe.py",
        "scriptCommitSha": _git_sha(),
        "consumes": [
            "computations/q-pinning-50-digit.witness.json (muon q₀)",
            "tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR (proton q₀)",
            "computations/probes/qbeta-5two-chirality-state-integral.witness.json (A1 ω home swing cross-check)",
        ],
        "lean": [
            "QOU.QBeta.MeridianHolonomyAnchorCarrier.sensitivity_sq",
            "QOU.QBeta.MeridianHolonomyAnchorCarrier.barOdd_sq_le_of_amplification",
            "QOU.QBeta.MeridianHolonomyAnchorCarrier.amplification_le_of_barOdd_sq_ge",
        ],
        "anchor_spacing_rel": mp.nstr(dq_rel, 10),
        "c3_swing_reference": mp.nstr(C3_SWING, 6),
        "per_anchor": per_anchor,
        "assertions": assertions,
        "assertions_passed": passed,
        "assertions_total": len(assertions),
        "verdict": "scope-(a) NEGATIVE — meridian-holonomy deformation MAGNITUDE "
        "anchor-smooth; swing lives in the near-singular / non-perturbative phase "
        "arg(u); bounds both this route and #4283's in-block maps.",
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    _OUT.write_text(json.dumps(witness, indent=2) + "\n")

    print(f"[meridian-holonomy anchor-swing] {passed}/{len(assertions)} assertions passed")
    for a in assertions:
        mark = "OK " if a["passed"] else "XX "
        print(f"  {mark}{a['name']}: {a['computed']}")
    print(f"  anchor spacing |Δq₀|/q₀ = {mp.nstr(dq_rel, 8)}")
    print(f"  wrote {_OUT.relative_to(_ROOT)}")
    return 0 if passed == len(assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
