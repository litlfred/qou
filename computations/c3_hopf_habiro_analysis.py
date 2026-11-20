#!/usr/bin/env python3
"""
c3_hopf_habiro_analysis.py — investigate c_3's relationship to
Hopf link Jones polynomial and Habiro series.

FINDINGS (refreshed 2026-06-28 after upstream N=3 operator-valued drift —
c_3_empirical_additive moved -2.0097 -> -2.0216 in
q-beta-operator-valued-N3.witness.json):
  c_3 actual       = -2.02162
  J_Hopf(q_0)      = -2.01090  (exact Hopf at q, 0.530% off)
  -2 - hbar^2      = -2.00982  (0.584% off — best simple model)
  -2 - hbar^2*q    = -2.01090  (= J_Hopf(q), Hopf Taylor)

TIERED FRAMING (AGENTS.md c_k banner): c_3 = J_Hopf(q=1) = -2 is a
NEAR-MATCH (classical-limit identification), NOT Taylor-exact. Only
c_2 = -1 is proved Taylor-exact. The residual below (now ~0.58%, was
0.004% against the pre-drift upstream input) is the size of the
near-match gap at the current upstream input, not evidence of exactness.

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
from witness_base import WitnessBuilder, record_upstream

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_50_DIGIT_STR, Q_MP


def main():
    set_compute_dps()
    q = Q_MP
    h = q - 1/q
    hbar = 1 - 1/q

    w = record_upstream(HERE / "q-beta-operator-valued-N3.witness.json", _UPSTREAM_RECORDS)
    c3 = mpf(w["data"]["c_3_empirical_additive"])
    b = mpf(w["data"]["hoefsmit_b"])

    J_hopf_q = -(q + 1/q)
    J_hopf_1 = mpf(-2)
    c3_hbar2 = J_hopf_1 - hbar**2
    b_sq = (h**2 + 3) / (h**2 + 4)

    wb = WitnessBuilder("c3-hopf-habiro-analysis", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    # Wire to the c_3 ↔ Hopf-link categorical prop. NOTE the tiered framing
    # (AGENTS.md c_k banner): this prop is the *near-match* identification
    # c_3 = J_Hopf(q=1) = -2 (classical limit), NOT a Taylor-exact claim.
    # The witness measures the near-match residual (c_3 actual = -2.0097 vs
    # -2; c_3 = J - hbar^2 closes it to 0.004%), so it supports the
    # near-match prop, never c_3-as-Taylor-exact.
    wb.set_content_block("prop:q-beta-c3-hopf-three-fold-markov")
    wb.set_description(
        "c_3 vs Hopf Jones evaluation and Habiro series. NEAR-MATCH tier "
        "(c_3 = J_Hopf(q=1) = -2 is a classical-limit identification, NOT "
        "Taylor-exact; only c_2 = -1 is proved-exact). "
        "c_3 = J-hbar^2 at ~0.58% (best model; was 0.004% before the upstream "
        "N=3 operator-valued c_3 drifted -2.0097 -> -2.0216). "
        "J_Hopf(q_0) = -[2]_q at ~0.53%. "
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
        "b_sq_exact", computed=b_sq, expected=b**2,
        tolerance=1e-10, source="b^2 = (h^2+3)/(h^2+4) from Hoefsmit"
    )
    wb.add_assertion(
        "c3_best_model", computed=abs(float((c3_hbar2-c3)/c3*100)),
        expected=0, tolerance=0.01, unit="%",
        source="c_3 = J - hbar^2"
    )

    wb.save()
    err_best = abs(float((c3_hbar2 - c3) / c3 * 100))
    err_jq0 = abs(float((J_hopf_q - c3) / c3 * 100))
    print("✓ c3-hopf-habiro-analysis.witness.json")
    print(f"  c₃ actual (upstream N=3): {float(c3):.6f}")
    print(f"  b² = (h²+3)/(h²+4): EXACT")
    print(f"  c₃ = J − ℏ² (NEAR-MATCH, best model): {err_best:.4f}%")
    print(f"  c₃ vs J_Hopf(q₀): {err_jq0:.4f}%")


if __name__ == "__main__":
    main()
