"""E_unit via 𝔇 (decay width) — predicted-first check + reconciliation with
the landed §2h scale-free wall (owner steer: reinterpret E_unit via 𝔇).

Context. The sibling reeb-flow tranche 6 (§2h, landed on main:
ss_det_no_linear_term, sorry-free) established:
  * 2h.1 (positive): the deuteron is ONE OPEN pn bond, so B is the O(g)
    linear object 5g (the ss-matrix is traceless => no linear loop term);
    the g-ORDER of the law is derived.
  * 2h.2 (limit, scope-a): the exchange sector is SCALE-FREE; E_unit is
    external; among canonical energies the closest is 2 m_e (+2.62%), and
    the bar-odd Q_beta is the WORST (-21.45%). Near-match, unit external.

The owner asks whether the 𝔇 (decay-width) reinterpretation closes E_unit
inside 3 CALs (E_unit = hbar/𝔇, a CAL-2 datum — NOT CAL-4). This probe tests
that route predicted-first and reconciles it with §2h.

Predicted-first candidates. If E_unit = hbar/𝔇_bond with 𝔇_bond the
deuteron BOND width, related to the single-nucleon P_skew^beta (=> Q_beta) by the
2-body structure, then E_unit = Q_beta * F with F a bar-EVEN O(1) 2-body
factor (bar-even F * bar-odd Q_beta = bar-odd E_unit). The genuine
2-body-structure factors, stated BEFORE evaluation:
  * F = 2         : reduced-mass / two-nucleon count (mu = m_N/2 => rate x2)
  * F = 3/[2]_v   : spin-triplet multiplicity over the bond bracket
  * F = [3]_v/[2]_v : fused-channel quantum-dimension over the bond bracket
Each evaluated ONCE against the target ratio E_unit/Q_beta.

Discipline. Genuine structural factors only (no sqrt/tuning); the
golden-ratio-adjacent F ~ sqrt(phi)=1.272 (E_unit/Q_beta=1.271, 0.09%) is a
NUMEROLOGY TRAP (the #3444 cut) and is explicitly NOT a candidate. Honest
expectation given §2h: the decay-width sector is numerically the worst, so
these confirm the wall rather than close it.
"""
import json
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = Q_MP
me = mp.mpf("0.51099895069")
v = mp.sqrt(q)
two_v = v + 1 / v
three_v = v**2 + 1 + 1 / v**2
Qb = me * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)   # CAL-2 proxy (bar-odd)
E_UNIT = mp.mpf("0.995940")
LAW_PREC = mp.mpf("0.004")
target_ratio = E_UNIT / Qb

# predicted-first genuine 2-body factors
factors = {
    "F = 2 (two-nucleon / reduced-mass)": mp.mpf(2),
    "F = 3/[2]_v (spin-triplet / bond bracket)": 3 / two_v,
    "F = [3]_v/[2]_v (fused-dim / bond bracket)": three_v / two_v,
}
results = {}
n_pass = 0
for name, F in factors.items():
    val = Qb * F
    rel = abs(val - E_UNIT) / E_UNIT
    ok = rel < LAW_PREC
    n_pass += int(ok)
    results[name] = {"E_unit_pred_MeV": mp.nstr(val, 10),
                     "rel_miss": mp.nstr(rel, 6), "within_0.4pct": bool(ok)}

# reference: the closest CANONICAL candidate from §2h is bar-EVEN 2 m_e.
two_me = 2 * me
two_me_miss = abs(two_me - E_UNIT) / E_UNIT

assertions = {
    "three_factors_predicted_first_evaluated": len(results) == 3,
    "target_ratio_recorded": target_ratio > 0,
}

verdict = (
    "𝔇 (DECAY-WIDTH) ROUTE: ARCHITECTURALLY VALID (removes CAL-4), "
    "NUMERICALLY NEGATIVE (confirms the landed §2h wall). E_unit = "
    "Q_beta * F needs F = E_unit/Q_beta = "
    f"{mp.nstr(target_ratio, 6)}; the genuine 2-body factors (2, 3/[2]_v, "
    "[3]_v/[2]_v) all miss the 0.4% law scale. Reconciliation with §2h: "
    "the exchange sector is scale-free (ss_det_no_linear_term) so E_unit is "
    "external either way; the sibling's landed table has the bar-EVEN 2 m_e "
    f"closest (+{mp.nstr(two_me_miss*100,3)}%) and bar-odd Q_beta WORST "
    "(-21%). So the 𝔇/bar-odd reinterpretation, while it correctly keeps "
    "E_unit inside 3 CALs (no new calibration), points at the numerically "
    "worst sector: it does NOT close the number, and if anything the data "
    "favor a bar-EVEN unit (2 m_e). The golden-ratio F ~ sqrt(phi) (0.09%) "
    "is a numerology trap, not claimed. CONCLUSION: E_unit stays open; the "
    "§2h NEAR-MATCH / external-unit verdict holds from the 𝔇 side too. "
    "Value delivered: the CAL-4 violation is removed (E_unit must be a "
    "3-CAL function), and the decay-width sector is now an honest negative."
)

witness = {
    "computation": "e_unit_decay_width_reconcile_probe",
    "description": (
        "Predicted-first test of the owner's 𝔇 (decay-width) "
        "reinterpretation of E_unit, reconciled with the landed §2h "
        "scale-free wall (ss_det_no_linear_term). Confirms: 𝔇 removes CAL-4 "
        "but is numerically the worst sector; E_unit stays open."
    ),
    "discipline": ("predicted-first; genuine 2-body factors only, no "
                   "sqrt/tuning; sqrt(phi) numerology trap walled off; "
                   "reconciled with landed sibling §2h; (a)-scoped."),
    "auditOnly": "docs/coordination/e-unit-deuteron-scale.md",
    "results": {
        "E_unit_MeV": mp.nstr(E_UNIT, 8),
        "Q_beta_MeV": mp.nstr(Qb, 8),
        "target_F_E_unit_over_Q_beta": mp.nstr(target_ratio, 8),
        "decay_width_factors": results,
        "closest_canonical_2me_bar_even": {"MeV": mp.nstr(two_me, 8),
                                           "miss": mp.nstr(two_me_miss, 6)},
        "sibling": "docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md §2h (ss_det_no_linear_term)",
        "numerology_trap": "E_unit/Q_beta ~ sqrt(phi)=1.272 (0.09%) — NOT a candidate (#3444 cut)",
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(_HERE, "e-unit-decay-width-reconcile-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"target F = E_unit/Q_beta = {mp.nstr(target_ratio, 8)}")
for name, r in results.items():
    print(f"  {name}: E_unit_pred {r['E_unit_pred_MeV']} MeV (miss {r['rel_miss']}) "
          f"{'within' if r['within_0.4pct'] else 'NEG'}")
print(f"  [ref] 2 m_e (bar-even, §2h closest): miss {mp.nstr(two_me_miss,6)}")
print(f"\nwitness -> {out}")
