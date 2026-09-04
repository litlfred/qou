#!/usr/bin/env python3
"""A=3 beyond-Hecke magnitude probe: does a Vassiliev/Kontsevich weight-system correction
supply the triton Delta_lambda magnitude factor r* = mu3/c3 ~ 1.585?  Exact (sympy) + mpmath;
0 fit; nothing wired.  Forward-only: no anchor (mu3, c3, q0) is inverted.

CONTEXT.  The A=3 3-body magnitude factor r* = mu3 (+0.4708, AdditiveResidualSimplex #4320)
/ c3 (+0.297, Hecke H_9 near-miss #4364) ~ 1.585 is bracketed out of every Hecke-level
ingredient (level #4364/#4376; geometric W_lambda #4392; coordination-edge #4472).  This
probe tests the last un-excluded candidate: a finite-type (Vassiliev) weight-system
correction of the proved Borromean deficit, at the Brunnian-deficit degree 2(A-1)=4 or the
length-A Milnor degree A-1=2 (DD-1 grading crux, MilnorVassilievGrading.lean).

THE OBJECT (proved, from milnor_weight_parity_convergence_probe.py):
  1 - tau_Borr(h) = h^4 (3 + h^2) / (h^2 + 4),   h = q - 1/q.
  Leading finite-type (Vassiliev degree 2(A-1)=4) weight = the h->0 symbol = (3/4) h^4.

DECISIVE STRUCTURAL FACT (exact, all h): the leading Vassiliev weight (3/4)h^4 is <= the full
deficit, since (3/4)(h^2+4) = (3/4)h^2 + 3 <= h^2 + 3.  (3+h^2)/(h^2+4) increases in h^2 from
3/4 (h=0) toward 1, so the leading term is the SMALLEST term of a positive convergent series.
=> weight/Hecke <= 1 < 3/2 < r*.  The finite-type filtration re-expands the SAME Markov trace
the Hecke level already sums; no truncation exceeds the Hecke value.  So a Vassiliev
weight-system correction CANNOT supply the 1.585x magnitude factor.

Length-A Milnor reading (A-1=2): genuine mu-bar(123) is realized as an INTEGER Vassiliev
invariant = +-1 (BrunnianVassilievBridge.muBar_realized, val: K -> Z); corpus-measured Milnor
ratio is the integer -2 = J_Hopf(q=1).  An integer weight != r* in (3/2, 2).

Numerology dismissal: r* ~ log2 3 = 1.58496 is a coincidence; log2 3 is irrational.

VERDICT (scope-(b) structural exclusion of the bare-weight claim): the Vassiliev weight does
NOT supply 1.585x.  Does NOT exclude Vassiliev structure from a larger closure (untested).

Lean: QOU/MassTheory/VassilievMagnitudeA3.lean (leadingWeight_le_borrDeficit,
vassiliev_weight_cannot_supply_magnitude, no_integer_weight_eq_rStar, two_pow_ne_three_pow)
-- sorry-free, lean-direct exit 0.

EXPLORATORY -- audit + witness only; no fit, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 70

# q0 (PROTON pin; label corrected, bean qou-9ugp); forward inputs never inverted
# q0 RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This was the literal
# 1.10997859555733471..., the SUPERSEDED muon pin A -- it stopped being the
# muon anchor when PR #5500 re-derived that anchor to CODATA-2022. A frozen
# literal cannot follow an anchor move, so the witness kept recording A under
# the label "muon" and the anchor gate scored it Q0_FLIP; re-running could not
# clear it, because the producer was the source of the stale number. It now
# resolves the PROTON pin per the owner directive of 2026-08-15 ("we want
# proton unless for an explicit reason ... otherwise pin proton").
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402 -- q0 RESOLVED, not frozen (qou-1c4y)

Q0 = mp.mpf(_Q0_RESOLVED)
H0 = Q0 - 1 / Q0
MU3 = mp.mpf("0.4708")     # additive-residual moment mu3 (#4320)
C3 = mp.mpf("0.297")       # Hecke H_9 near-miss (#4364, atom-dressed)
R_STAR = MU3 / C3          # ~ 1.585
LOG2_3 = mp.log(3) / mp.log(2)


def main() -> int:
    h = sp.symbols("h", positive=True)
    deficit = h ** 4 * (3 + h ** 2) / (h ** 2 + 4)     # 1 - tau_Borr, proved (A=3)

    ser = sp.expand(sp.series(deficit, h, 0, 9).removeO())
    lead_coeff_h4 = sp.nsimplify(ser.coeff(h, 4))      # leading Vassiliev (deg-4) coefficient
    leading_weight = sp.Rational(3, 4) * h ** 4

    f = sp.lambdify(h, deficit, "mpmath")
    w = sp.lambdify(h, leading_weight, "mpmath")
    deficit_q0 = f(H0)                                 # full deficit = Hecke Markov value (undressed)
    weight_q0 = w(H0)
    weight_over_hecke = weight_q0 / deficit_q0         # <= 1 structurally
    hecke_over_weight = deficit_q0 / weight_q0         # the finite-type "correction" (~1.004)

    # exact all-h bound: (3+h^2)/(h^2+4) - 3/4 == (h^2/4)/(h^2+4) >= 0  =>  weight <= deficit
    bound_is_exact = sp.simplify((3 + h ** 2) / (h ** 2 + 4) - sp.Rational(3, 4)
                                 - (h ** 2 / 4) / (h ** 2 + 4)) == 0

    A_leading = bool(lead_coeff_h4 == sp.Rational(3, 4))
    A_bound = bool(bound_is_exact)
    A_ratio_le1 = bool(weight_over_hecke <= 1)
    A_corr_tiny = bool(hecke_over_weight < mp.mpf("1.05") < R_STAR)   # correction << r*
    A_rstar_open = bool(mp.mpf("1.5") < R_STAR < mp.mpf("2"))
    A_int_ne = bool(all(mp.fabs(k - R_STAR) > mp.mpf("0.01")
                        for k in (mp.mpf(-2), mp.mpf(-1), mp.mpf(1), mp.mpf(2))))
    A_log_coinc = bool(mp.fabs(R_STAR - LOG2_3) < mp.mpf("1e-3"))
    all_passed = all([A_leading, A_bound, A_ratio_le1, A_corr_tiny,
                      A_rstar_open, A_int_ne, A_log_coinc])

    payload = {
        "computation": "vassiliev-magnitude-a3",
        "description": ("Does a Vassiliev/Kontsevich weight-system correction supply the A=3 "
                        "Delta_lambda magnitude factor r*=mu3/c3~1.585? The proved Borromean "
                        "deficit 1-tau=h^4(3+h^2)/(h^2+4); its leading finite-type (Vassiliev "
                        "deg 2(A-1)=4) weight (3/4)h^4 is <= the full deficit for ALL h (exact "
                        "bound (h^2/4)/(h^2+4)>=0), so weight/Hecke<=1<3/2<r*. The finite-type "
                        "filtration re-expands the SAME Markov trace the Hecke level sums, so no "
                        "truncation exceeds the Hecke near-miss 0.297. Length-A Milnor mu-bar is "
                        "the integer +-1 (bridge class, val:K->Z); measured ratio -2; no integer "
                        "weight = r* in (3/2,2). r*~log2 3 is an irrational coincidence. VERDICT "
                        "REFUTE(scope-b): the Vassiliev weight does NOT supply 1.585x. Does not "
                        "exclude Vassiliev from a larger closure (untested). 0 fit; nothing wired."),
        "audit_only": True,
        "tier": "scope-(b) structural exclusion of the bare-weight magnitude claim (exact all-h "
                "bound + integrality); no fit",
        "result": {
            "leading_weight_coeff_h4": str(lead_coeff_h4),
            "leading_le_full_deficit_all_h": A_bound,
            "q0_muon": mp.nstr(Q0, 50),
            "h0": mp.nstr(H0, 50),
            "full_deficit_at_q0": mp.nstr(deficit_q0, 40),
            "leading_weight_at_q0": mp.nstr(weight_q0, 40),
            "weight_over_hecke": mp.nstr(weight_over_hecke, 40),
            "hecke_over_weight_correction": mp.nstr(hecke_over_weight, 40),
            "r_star_target": mp.nstr(R_STAR, 40),
            "log2_3": mp.nstr(LOG2_3, 40),
            "milnor_integer_reading": "mu-bar=+-1 (bridge), measured ratio -2; both integers != r*",
            "free_parameters": 0,
        },
        "context": {
            "axis": "Delta_lambda / A=3 3-body MAGNITUDE (beyond-Hecke) via Vassiliev weight",
            "lean": "QOU/MassTheory/VassilievMagnitudeA3.lean",
            "builds_on": "#4364 Hecke near-miss c3=0.297; #4480 mu-bar ratio -2; DD-1 grading crux; "
                         "#4479 Vassiliev finite-type scaffold",
            "distinct_angle": "A=3 beyond-Hecke MAGNITUDE (weight<=Hecke bound); siblings own the "
                              "exact-order mu-bar_A coefficient (#4480) and the A=4 magnitude (#4472)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "vassiliev-magnitude-a3", payload,
        script_path=__file__, engine="sympy+mpmath",
        output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.add_assertion("leading_weight_is_three_quarters_h4", computed=str(A_leading), expected="True")
    wb.add_assertion("leading_le_full_deficit_all_h", computed=str(A_bound), expected="True")
    wb.add_assertion("weight_over_hecke_le_one", computed=str(A_ratio_le1), expected="True")
    wb.add_assertion("finite_type_correction_far_below_r_star", computed=str(A_corr_tiny), expected="True")
    wb.add_assertion("r_star_in_open_3half_2", computed=str(A_rstar_open), expected="True")
    wb.add_assertion("integer_weights_ne_r_star", computed=str(A_int_ne), expected="True")
    wb.add_assertion("r_star_approx_log2_3_coincidence", computed=str(A_log_coinc), expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== A=3 Vassiliev-weight magnitude probe ===")
    print(f"q0 (muon)          = {mp.nstr(Q0, 20)}   h0 = q0-1/q0 = {mp.nstr(H0, 12)}")
    print(f"leading weight     = (3/4) h^4   (Vassiliev degree 2(A-1)=4)   coeff_h4 = {lead_coeff_h4}")
    print(f"full deficit @q0   = {mp.nstr(deficit_q0, 12)}   (= Hecke Markov-trace value, undressed)")
    print(f"leading weight @q0 = {mp.nstr(weight_q0, 12)}")
    print(f"weight / Hecke     = {mp.nstr(weight_over_hecke, 12)}   (<= 1 for all h : {A_ratio_le1})")
    print(f"Hecke / weight     = {mp.nstr(hecke_over_weight, 12)}   (finite-type 'correction' ~ 1.004)")
    print(f"r* = mu3/c3        = {mp.nstr(R_STAR, 8)}   log2(3) = {mp.nstr(LOG2_3, 8)}   (coincidence)")
    print(f"VERDICT REFUTE(scope-b): weight/Hecke <= 1 << r*; correction {mp.nstr(hecke_over_weight,6)} "
          f"!= {mp.nstr(R_STAR,6)}; integer mu-bar (+-1 / -2) != r*")
    print(f"allPassed = {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
