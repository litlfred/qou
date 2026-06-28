"""multiterm_cost_he3_l6a4_probe.py — Subgoal-1 He3 canonical knot probe.

Tests the hypothesis: "wiring the multi-term mass formula (T4 Frobenius offset)
into the cost function makes He3's historical canonical knot L6a4 the SDP winner".

## Result: the hypothesis is STRUCTURALLY REFUTED.

For He3, B_AME = 7.718 MeV.
L6a4 is PSD-feasible (alpha_gap = 0.0), with rho = 3 and |tr_M| = 0.998367.
Its descended mass term is: B_desc = rho * m_e * |tr_M| = 3 * 0.511 * 0.998 = 1.530 MeV.

The multi-term offset used in the PSD gate probe is the Frobenius co-Casimir T4:
T4 = m_e * Sigma_{lam |- 3A} 1/dim_q(lam) = 1.300 MeV (for A=3).

With this offset, L6a4's predicted binding is:
B_pred = B_desc + T4 = 1.530 + 1.300 = 2.830 MeV.

This leaves a huge gap to B_AME (7.718 MeV). The relative residual is:
rel_resid = |7.718 - 2.830| / 7.718 = 0.63.
The solver cost (alpha_gap + 0.25 * rel_resid) is 0.158.

Meanwhile, other braids (like [1, 1, 1, 1, 1, 1, 2, 2] with rho=4, |tr_M|=1.617)
produce B_pred = 4.60 MeV, giving a lower rel_resid = 0.40 and a lower cost (0.101).

Thus, L6a4 cannot be the winner. The T4-only offset is insufficient to close the
binding gap for He3. The missing terms (T2, T3, T5, T6) are required, but their
Kashaev-specialized forms diverge or produce unphysical values (like T6 = -21375 MeV).

## Redirect
The He3 canonical-knot SDP closure is blocked because the multi-term formula
additive components (at q_0) do not sum to B_AME. The solver correctly rejects
L6a4 because its T1+T4 binding prediction is 4.88 MeV short of reality.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge
import mpmath as mp

from _precision import set_compute_dps
from witness_base import WitnessBuilder
from q_parameter import Q as Q_CANONICAL
from codata_constants import M_E_MEV, AME_B_HE3_MEV_VALIDATION

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = M_E_MEV

# He3 data
B_AME = AME_B_HE3_MEV_VALIDATION
ALPHA_GAP_L6A4 = mp.mpf("0.0")
TRM_L6A4 = mp.mpf("0.998367")
RHO_L6A4 = 3
# T4 for A=3:
M_E_SIGMA_9 = mp.mpf("1.2999219630934102")

# Cost weights
W_ALPHA = mp.mpf("1.0")
W_RESID = mp.mpf("0.25")

def main() -> int:
    print("Multi-term cost vs He3 L6a4 probe")
    print(f"  cost = {W_ALPHA}·alpha_gap + {W_RESID}·rel_resid")
    print()

    b_desc = RHO_L6A4 * m_e * TRM_L6A4
    b_pred = b_desc + M_E_SIGMA_9
    rel_resid = abs(B_AME - b_pred) / B_AME
    cost_l6a4 = W_ALPHA * ALPHA_GAP_L6A4 + W_RESID * rel_resid

    print(f"  L6a4 B_desc (T1)       = {mp.nstr(b_desc, 6)} MeV")
    print(f"  L6a4 B_pred (T1+T4)    = {mp.nstr(b_pred, 6)} MeV")
    print(f"  B_AME                  = {mp.nstr(B_AME, 6)} MeV")
    print(f"  rel_resid              = {mp.nstr(rel_resid, 6)}")
    print(f"  L6a4 cost              = {mp.nstr(cost_l6a4, 6)}")
    print()
    
    # Alternate winner
    rho_alt, trm_alt = 4, mp.mpf("1.617533")
    b_desc_alt = rho_alt * m_e * trm_alt
    b_pred_alt = b_desc_alt + M_E_SIGMA_9
    rel_resid_alt = abs(B_AME - b_pred_alt) / B_AME
    cost_alt = W_ALPHA * mp.mpf("0.0") + W_RESID * rel_resid_alt
    
    print(f"  Alt winner B_pred      = {mp.nstr(b_pred_alt, 6)} MeV")
    print(f"  Alt rel_resid          = {mp.nstr(rel_resid_alt, 6)}")
    print(f"  Alt cost               = {mp.nstr(cost_alt, 6)}")
    print(f"  Alt wins?              = {cost_alt < cost_l6a4}")

    w = WitnessBuilder("multiterm-cost-he3-l6a4-probe", engine="mpmath")
    w.set_description(
        "Refutes the hypothesis that wiring the T4 Frobenius offset into the SDP "
        "cost makes He3's historical L6a4 the winner. L6a4's T1+T4 binding prediction "
        "is 2.83 MeV, far short of the 7.718 MeV B_AME. Other candidates hit 4.6 MeV "
        "and win on relative residual."
    )
    w.add_data("b_pred_l6a4", mp.nstr(b_pred, 12))
    w.add_data("cost_l6a4", mp.nstr(cost_l6a4, 12))
    w.add_data("cost_alt_winner", mp.nstr(cost_alt, 12))
    w.add_assertion(
        name="multiterm_t4_cannot_rescue_l6a4",
        computed=bool(cost_alt < cost_l6a4),
        expected=True,
        tolerance=0,
        source="T1+T4 offset leaves a 4.88 MeV gap, so L6a4 loses to higher-|tr_M| braids.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
