"""multiterm_cost_deuteron_psd_gate_probe.py — Subgoal-1 option 3.

Tests the audit hypothesis (2026-06-02-subgoal-1-sdp-canonical-knot-run.md
+ conj-canonical-knot-id-sdp.md §"Partial closure"): "wiring T2-T6 of
thm:knot-mass-formula-unified into cost_for_candidate makes deuteron 6_2
the SDP structural winner".

## Result: the hypothesis is STRUCTURALLY REFUTED.

The R5-full cost is

    cost = w_alpha · alpha_gap  +  w_resid · rel_resid
           (w_alpha = 1.0,         w_resid = 0.25)

The multi-term mass formula (T2 brane-tower + T4 Frobenius co-Casimir)
only enters the binding prediction B_pred, hence only the SECONDARY
term rel_resid.  It CANNOT change alpha_gap — the PRIMARY PSD-feasibility
gate — which is intrinsic to the candidate braid's Hoefsmit
representation (Wedderburn-block eigenvalues at q_0).

Deuteron 6_2 has alpha_gap = 0.890510 (standard (2,1) block eigenvalue
-0.89 < 0 — NOT PSD-feasible).  Therefore:

  cost(6_2) >= w_alpha · 0.890510 = 0.890510   (even at rel_resid = 0)
  cost(winner, alpha_gap=0) <= w_resid = 0.25  (when rel_resid <= 1)

6_2 can NEVER be the joint-cost winner while alpha_gap = 0.89, for ANY
binding formula.  The blocker is 6_2's PSD-infeasibility itself, not the
cost weighting.

## What multi-term DOES change (for PSD-feasible candidates)

It shifts the effective |tr_M| target from B_AME/(m_e·rho) to
(B_AME - m_e·Sigma)/(m_e·rho) where Sigma = Sum_{lam |- 3A} 1/dim_q(lam).
For the deuteron (Sigma_6, m_e·Sigma = 1.636 MeV) this is a large shift —
but it only re-ranks WITHIN the PSD-feasible subset, which 6_2 is not in.

## Redirect

The deuteron canonical-knot SDP closure is blocked by 6_2's intrinsic
PSD-infeasibility, NOT by the single-term cost.  Productive directions:
  (a) 6_2 may not be the right canonical object — the structural
      decomposition (conj-canonical-knot-id-sdp.md §"Structural
      decomposition") factors T_w = K(binding) (x) prod T_w(nucleon),
      with the deuteron binding K = L_H (Hopf), NOT 6_2.
  (b) the PSD-feasibility certificate may need the JOINT multi-block
      constraint rather than the single (2,1)-block check.

Ref: docs/audits/2026-06-02-subgoal-1-sdp-canonical-knot-run.md
Ref: content/.../mass-theory/conj-canonical-knot-id-sdp.md
Ref: computations/subgoal-1-frobenius-co-casimir-validation.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from q_parameter import Q as Q_CANONICAL  # noqa: E402
from codata_constants import M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = M_E_MEV

# Deuteron data (R5-full witness historical_cross_check + Frobenius validation)
B_AME = AME_B_DEUTERON_MEV_VALIDATION
ALPHA_GAP_6_2 = mp.mpf("0.890510")    # standard (2,1)-block PSD violation
TRM_6_2 = mp.mpf("0.288326")
M_E_SIGMA_6 = mp.mpf("1.636287112")   # m_e·Σ_{λ⊢6} 1/dim_q (validated)

# Cost weights from cost_for_candidate (r5_full_canonical_knot_solver.py)
W_ALPHA = mp.mpf("1.0")
W_RESID = mp.mpf("0.25")


def main() -> int:
    print("Multi-term cost vs deuteron PSD-gate probe @ q_0")
    print(f"  cost = {W_ALPHA}·alpha_gap + {W_RESID}·rel_resid")
    print()

    # 6_2 best-case cost floor (rel_resid driven to 0)
    cost_6_2_floor = W_ALPHA * ALPHA_GAP_6_2
    winner_cost_max = W_RESID  # alpha_gap=0, rel_resid<=1

    print(f"  6_2 alpha_gap          = {mp.nstr(ALPHA_GAP_6_2, 8)} (NOT PSD-feasible)")
    print(f"  6_2 BEST-CASE cost     = {mp.nstr(cost_6_2_floor, 8)} (rel_resid=0)")
    print(f"  winner MAX cost        = {mp.nstr(winner_cost_max, 8)} (alpha_gap=0, rel_resid<=1)")
    print(f"  6_2 can win?           = {cost_6_2_floor < winner_cost_max}")
    print()

    can_6_2_win = cost_6_2_floor < winner_cost_max

    # Effective |tr_M| targets, single vs multi-term
    print("  Effective |tr_M| targets (single-term vs multi-term):")
    targets = {}
    for rho in (1, 2, 3, 4):
        t_single = B_AME / (m_e * rho)
        t_multi = (B_AME - M_E_SIGMA_6) / (m_e * rho)
        targets[rho] = (t_single, t_multi)
        flag = "  <- ~6_2 |tr_M|=0.288" if abs(t_multi - TRM_6_2) < mp.mpf("0.01") else ""
        print(f"    rho={rho}: single={mp.nstr(t_single,5):>8s}  multi={mp.nstr(t_multi,5):>8s}{flag}")
    print()
    print("  NOTE: multi-term ρ=4 target ≈ 6_2's |tr_M| is a COINCIDENCE at the")
    print("  wrong rho (deuteron is rho=1); and 6_2 is not PSD-feasible anyway.")

    # Witness
    w = WitnessBuilder("multiterm-cost-deuteron-psd-gate", engine="mpmath")
    w.set_description(
        "Refutes the audit hypothesis that wiring T2-T6 into the SDP "
        "cost makes deuteron 6_2 the winner. The cost is alpha_gap + "
        "0.25·rel_resid; multi-term only affects rel_resid (secondary). "
        "6_2's alpha_gap=0.89 (intrinsic PSD-infeasibility) floors its "
        "cost at 0.89 >> winner's max 0.25 — for ANY binding formula. "
        "The deuteron SDP blocker is 6_2 PSD-infeasibility, not the cost."
    )
    w.add_data("alpha_gap_6_2", mp.nstr(ALPHA_GAP_6_2, 20))
    w.add_data("cost_6_2_best_case", mp.nstr(cost_6_2_floor, 20))
    w.add_data("winner_cost_max", mp.nstr(winner_cost_max, 20))
    w.add_data("m_e_Sigma_6_MeV", mp.nstr(M_E_SIGMA_6, 20))
    w.add_assertion(
        name="multiterm_cost_cannot_rescue_6_2",
        computed=bool(not can_6_2_win),
        expected=True,
        tolerance=0,
        source="6_2 cost floor 0.89 > winner max 0.25, independent of binding formula",
    )
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("deuteron (²H)"))
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
