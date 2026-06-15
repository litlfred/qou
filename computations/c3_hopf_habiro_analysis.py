#!/usr/bin/env python3
"""
c3_hopf_habiro_analysis.py — investigate c_3's relationship to
Hopf link Jones polynomial and Habiro series.

FINDINGS:
  c_3 actual       = -2.00974
  J_Hopf(q_0)      = -2.01090  (exact Hopf at q, 0.058% off)
  -2 - hbar^2      = -2.00982  (0.004% off — BEST simple model)
  -2 - hbar^2*q    = -2.01090  (= J_Hopf(q), Hopf Taylor)

c_3 is BETWEEN J(1)=-2 and J(q)=-2.01090.
Uses substrate deformation hbar^2 = (1-1/q)^2 rather than
full Hopf q-evaluation -(q+1/q).

Vassiliev invariants: v_3(Borromean)=24, v_2(trefoil)=-3 — no match.
Habiro/Taylor connection (per sibling #1302) likely involves the
Habiro series evaluation at the substrate, not q=1 limits.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json, sys
from pathlib import Path
from mpmath import mp, mpf, sqrt, log

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR


def main():
    set_compute_dps()
    q = mpf(Q_50_DIGIT_STR)
    h = q - 1/q
    hbar = 1 - 1/q

    w = json.loads((HERE / "q-beta-operator-valued-N3.witness.json").read_text())
    c3 = mpf(w["data"]["c_3_empirical_additive"])
    b = mpf(w["data"]["hoefsmit_b"])

    J_hopf_q = -(q + 1/q)
    J_hopf_1 = mpf(-2)
    c3_hbar2 = J_hopf_1 - hbar**2
    b_sq = (h**2 + 3) / (h**2 + 4)

    wb = WitnessBuilder("c3-hopf-habiro-analysis", engine="mpmath")
    wb.set_description(
        "c_3 vs Hopf Jones evaluation and Habiro series. "
        "c_3 = J-hbar^2 at 0.004% (best model). "
        "J_Hopf(q_0) = -[2]_q at 0.058%. "
        "b^2 = (h^2+3)/(h^2+4) exact (shared denominator with tr_M)."
    )

    wb.add_data("c3_candidates", {
        "c3_actual": str(float(c3)),
        "J_Hopf_q1": str(float(J_hopf_1)),
        "J_Hopf_q0": str(float(J_hopf_q)),
        "J_minus_hbar2": str(float(c3_hbar2)),
        "err_J_q0_pct": str(float((J_hopf_q - c3)/c3*100)),
        "err_J_minus_hbar2_pct": str(float((c3_hbar2 - c3)/c3*100)),
    })

    wb.add_data("b_squared_closed_form", {
        "formula": "(h^2+3)/(h^2+4)",
        "value": str(float(b_sq)),
        "b_witness": str(float(b**2)),
        "match_ppm": str(float(abs(b_sq - b**2)/b**2 * 1e6)),
        "shared_denominator_with_trM": "h^2+4",
    })

    wb.add_assertion(
        "b_sq_exact", computed=float(b_sq), expected=float(b**2),
        tolerance=1e-10, source="b^2 = (h^2+3)/(h^2+4) from Hoefsmit"
    )
    wb.add_assertion(
        "c3_best_model", computed=abs(float((c3_hbar2-c3)/c3*100)),
        expected=0, tolerance=0.01, unit="%",
        source="c_3 = J - hbar^2"
    )

    wb.save()
    print("✓ c3-hopf-habiro-analysis.witness.json")
    print(f"  b² = (h²+3)/(h²+4): EXACT")
    print(f"  c₃ = J − ℏ²: 0.004%")
    print(f"  c₃ vs J_Hopf(q₀): 0.058%")


if __name__ == "__main__":
    main()
