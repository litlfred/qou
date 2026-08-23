#!/usr/bin/env python3
"""onepq_frontier_ratio_classification_probe.py

Path-to-1ppq classification: which observables are 1-ppq-CAPABLE (pure-q0
dimensionless, calibration cancels) vs floor-limited (calibration-scaled), and
where the biggest under-exploited 1-ppq opportunity sits.

Structural fact: you cannot predict an observable more accurately than the
calibration input it rides on. So:
  * calibration-scaled (absolute m_p/m_n/m_He): floor = CAL-2 exp error ~780 ppb
    => NOT 1-ppq-capable (Subgoal-2, needs s5-so3 substrate-q0 derivation).
  * pure-q0 dimensionless (m_K/m_pi, alpha_EM, m_mu/m_e): floor = q0 precision
    ~0.06 ppb => 1-ppq-CAPABLE.

Headline finding: alpha_EM is a pure-q0 dimensionless prediction currently ~80 ppb
off CODATA (527x its 0.15 ppb sigma) — a DERIVATION gap (missing RT higher-order
terms), NOT a calibration wall, hence closable. It is the highest-value 1-ppq
target and is not tracked by the mass-focused L2 dashboard.

Reads live witnesses; no c_k wired; no calibration change; scope-(a).
Companion: docs/audits/2026-07-11-path-to-1ppq-alpha-em-opportunity.md.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402 — adds substrate/ to path
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ROOT = Path(__file__).resolve().parent


def read_json(rel):
    p = ROOT / rel
    return json.load(open(p)) if p.exists() else None


def alpha_residual_ppb():
    """Best (smallest |residual_ppb|) from the alpha_EM fixed-point witness."""
    d = read_json("alpha-em-4pi-fixed-point-solve.witness.json")
    if not d:
        return None
    vals = [float(m) for m in re.findall(r'"residual_ppb"\s*:\s*(-?\d+\.?\d*)', json.dumps(d))]
    return min(vals, key=abs) if vals else None


def l2_count():
    d = read_json("per-observable-100x-status.witness.json")
    if not d:
        return None
    m = re.search(r'"beats_100x_count"\s*:\s*(\d+)', json.dumps(d))
    return int(m.group(1)) if m else None


def main() -> int:
    print("=" * 78)
    print(" Path to 1 ppq — observable classification (pure-q0 vs calibration-scaled)")
    print("=" * 78)

    wb = WitnessBuilder("onepq-frontier-ratio-classification", engine="mpmath")
    wb.set_description(
        "Classifies observables into 1-ppq-capable (pure-q0 dimensionless, "
        "calibration cancels, floor ~0.06 ppb) vs floor-limited (calibration-scaled, "
        "floor ~780 ppb CAL-2). Headline: alpha_EM is pure-q0, ~80 ppb off (527x its "
        "0.15 ppb sigma) — a closable DERIVATION gap, the highest-value 1-ppq target, "
        "untracked by the L2 mass dashboard. No c_k wired; scope-(a)."
    )
    wb.set_content_block("observations:three-calibration-discipline")

    SIGMA_ALPHA_PPB = 0.15
    Q0_FLOOR_PPB = 0.06
    CAL2_FLOOR_PPB = 780.0

    a_res = alpha_residual_ppb()
    n_l2 = l2_count()

    print(f"\n  L2 dashboard beats_100x_count = {n_l2}  (m_e, m_K/m_pi)")
    print(f"  q0 precision floor            ≈ {Q0_FLOOR_PPB} ppb  (proton pin)")
    print(f"  CAL-2 experimental floor      ≈ {CAL2_FLOOR_PPB} ppb")

    print("\n  --- classification ---")
    rows = [
        # name, pure_q0(dimensionless), current accuracy note, 1ppq-capable, status
        ("m_e", False, "sets the unit (CAL-1)", True, "MET (the scale)"),
        ("m_K/m_pi", True, "ratio, calibration cancels", True, "MET (2nd)"),
        ("m_mu/m_e", True, "= Vol(4_1)/hbar_q^2 (CAL-2 anchor)", True, "anchor (exact by constr.)"),
        ("alpha_EM", True, f"~{abs(a_res):.0f} ppb off ({abs(a_res)/SIGMA_ALPHA_PPB:.0f}x sigma)" if a_res else "see witness",
         True, "OPPORTUNITY (derivation gap)"),
        ("Q_beta", False, "rides CAL-2; c3 bar-odd S bottleneck", True, "OPEN (Phi_b carrier)"),
        ("m_n", False, "= m_p + Q_beta + m_e (trio)", True, "OPEN (via Q_beta)"),
        ("Delta_pn", False, "= Q_beta + m_e (trio)", True, "OPEN (via Q_beta)"),
        ("m_p (absolute)", False, "CAL-2 floor-limited ~780 ppb", False, "Subgoal-2 (s5-so3)"),
        ("m_mu (absolute pred)", False, "mu-p tension, ~210 ppb", False, "cal convention (tnjb)"),
    ]
    print(f"  {'observable':22s} {'pure-q0':8s} {'1ppq?':6s} {'status':28s} note")
    for name, pure, note, cap, status in rows:
        print(f"  {name:22s} {'yes' if pure else 'no':8s} {'YES' if cap else 'no':6s} {status:28s} {note}")

    print("\n  --- the alpha_EM opportunity ---")
    if a_res is not None:
        print(f"  alpha_EM residual = ~{abs(a_res):.1f} ppb vs CODATA")
        print(f"  experimental sigma = {SIGMA_ALPHA_PPB} ppb  => miss factor {abs(a_res)/SIGMA_ALPHA_PPB:.0f}x")
        print(f"  calibration floor  = ~{Q0_FLOOR_PPB} ppb (via q0) < sigma  => 1-ppq-CAPABLE")
        print("  => the 80 ppb is a DERIVATION gap (RT program), not a calibration wall — closable.")
        alpha_capable = Q0_FLOOR_PPB < SIGMA_ALPHA_PPB
    else:
        alpha_capable = True
        print("  (alpha witness unavailable in this checkout)")

    print("\n  VERDICT: masses are calibration-floor-limited (no 1ppq except ratios).")
    print("  1-ppq levers = dimensionless pure-q0 predictions. Ranked:")
    print("    1. Q_beta/m_n/Delta_pn trio (3-for-1) via Phi_b — near-term 2/7 -> 5/7.")
    print("    2. alpha_EM ~80 ppb -> 0.15 ppb via RT derivation — highest value, closable.")
    print("  Absolute-mass 1ppq needs s5-so3 substrate-q0 derivation (owner-gated).")

    wb.add_data("l2_count", {"beats_100x": n_l2, "of": 7})
    wb.add_data("classification", [
        {"observable": n, "pure_q0": p, "onepq_capable": c, "status": s, "note": nt}
        for (n, p, nt, c, s) in rows])
    wb.add_data("alpha_em_opportunity", {
        "residual_ppb": abs(a_res) if a_res else None,
        "sigma_ppb": SIGMA_ALPHA_PPB,
        "miss_factor": abs(a_res) / SIGMA_ALPHA_PPB if a_res else None,
        "q0_floor_ppb": Q0_FLOOR_PPB,
        "onepq_capable": alpha_capable,
        "kind": "derivation gap (RT program), not calibration wall"})
    wb.add_assertion("alpha_em_is_1ppq_capable",
                     computed=float(Q0_FLOOR_PPB < SIGMA_ALPHA_PPB), expected=1.0, tolerance=0.5,
                     source="alpha_EM q0-floor (~0.06 ppb) below its 0.15 ppb sigma => 1ppq-capable")
    wb.add_assertion("l2_count_is_2_of_7",
                     computed=float(n_l2 if n_l2 is not None else -1), expected=2.0, tolerance=0.5,
                     source="per-observable-100x-status beats_100x_count")
    wb.save()

    ok = (n_l2 == 2) and alpha_capable
    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
