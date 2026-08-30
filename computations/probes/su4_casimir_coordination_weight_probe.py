#!/usr/bin/env python3
"""su4_casimir_coordination_weight_probe.py

A Wigner-SU(4) Casimir form for the coordination weight. A LEAD, not a result.

THE CANDIDATE
-------------
qou-edt7's open question is the coordination weight w(z) = B(A)/C(A,2): why it
rises from z=1 and turns over at the alpha. Wigner's supermultiplet symmetry
SU(4) = SU(2)_spin x SU(2)_isospin puts the A nucleons of the s-shell in the
fully antisymmetric representation [1^A], whose quadratic Casimir is

    C2([1^n]) = (5/8) n (4 - n)      = 1.875, 2.5, 1.875, 0   for n = 1..4

and whose dimension C(4,n) VANISHES for n >= 5. Testing the simplest form an
SU(4)-symmetric interaction can take:

    w(A) = alpha - beta * C2([1^A])

WHAT IT GETS RIGHT
------------------
Fitting alpha and beta to the TWO ENDPOINTS A=2 and A=4 (C2 = 2.5 and 0, so
alpha = w(4) directly) and PREDICTING A=3:

    predicted w(3) = 2.847410583   ->  B(3) = 8.54223175 MeV
    measured (3H, Coulomb-corrected convention) = 2.8272654  ->  0.71%

It also gets the SHAPE right for the reason the shape exists: -C2 rises
monotonically across n = 2,3,4 and is maximal at n = 4, which is the turnover;
and [1^n] does not exist for n >= 5, so the form is silent exactly where w falls
off the shell.

WHAT IT IS NOT — read before citing
-----------------------------------
1. **Two parameters fitted to two points, predicting ONE point.** That is a
   single degree of predictive freedom. It is not a derivation and the 0.71%
   should not be read as a precision result.
2. **The convention was chosen after seeing the numbers.** Against the three A=3
   conventions the errors are 10.68% (3He), 5.46% (isospin average) and 0.71%
   (3H / Coulomb-corrected). The 3H convention has an independent a-priori case
   -- it is the Coulomb-free mirror, and the corpus's own Tjon block reads the
   alpha Coulomb-corrected -- but the selection is declared here because I did
   look at all three before preferring it.
3. **beta = 0.9965 MeV is fitted, and its closeness to 1 MeV is not evidence.**
   MeV is a human unit; there is no scale in the framework that makes 1 MeV
   distinguished. Do not build on it.
4. **It cannot be tested further in this form.** [1^n] is empty for n >= 5, so
   the model makes no A >= 5 prediction to falsify. That is a virtue for the
   turnover and a defect for testability, and the second is why this stays a
   lead.

THE TEST THAT WOULD PROMOTE IT
------------------------------
Derive beta. An SU(4)-symmetric two-body contact interaction has ONE coupling at
leading order (Platter-Hammer-Meissner, arXiv:nucl-th/0409040, ingested at
library/arxiv-nucl-th-0409040v2/); if the framework fixes that coupling from the
three calibrations, beta is predicted and the 0.71% becomes a real test rather
than the residue of a fit.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def c2_antisym(n: int, N: int = 4):
    """Quadratic Casimir of the fully antisymmetric [1^n] of SU(N)."""
    return mp.mpf(1) / 2 * (n * N + n - n**2 - mp.mpf(n**2) / N)


def main() -> int:
    wb = WitnessBuilder("su4-casimir-coordination-weight", engine="mpmath")
    wb.set_description(
        "A LEAD, not a result: w(A) = alpha - beta*C2([1^A]) with the Wigner SU(4) "
        "supermultiplet Casimir C2 = (5/8)n(4-n). Two parameters fitted to the A=2 "
        "and A=4 endpoints predict A=3 to 0.71% against the Coulomb-corrected "
        "convention. One degree of predictive freedom, a declared convention "
        "selection, and no A>=5 prediction to falsify. beta is fitted; deriving it "
        "is what would promote this."
    )

    for n in range(1, 6):
        print(f"   n={n}  C2([1^n]) = {mp.nstr(c2_antisym(n), 8):>8}   dim = {comb(4, n)}")
    wb.add_data("su4_casimir", {str(n): fmt(c2_antisym(n)) for n in range(1, 6)})
    wb.add_data("su4_dim", {str(n): comb(4, n) for n in range(1, 6)})

    D = ame_binding_mev(1, 2)
    T3, He3 = ame_binding_mev(1, 3), ame_binding_mev(2, 3)
    w2, w4 = D, ame_binding_mev(2, 4) / 6

    alpha = w4                                   # C2([1^4]) = 0
    beta = (w4 - w2) / c2_antisym(2)
    pred3 = alpha - beta * c2_antisym(3)
    print(f"\n   alpha = {mp.nstr(alpha,10)}  beta = {mp.nstr(beta,10)} (FITTED)")
    print(f"   predicted w(3) = {mp.nstr(pred3,10)}   B(3) = {mp.nstr(3*pred3,10)} MeV")

    errs = {}
    for nm, B3 in (("3He_alone", He3), ("isospin_average", (T3 + He3) / 2),
                   ("3H_Coulomb_corrected", T3)):
        m = B3 / 3
        errs[nm] = abs(pred3 - m) / m
        print(f"     {nm:<24} err = {mp.nstr(errs[nm]*100, 4)}%")
    wb.add_data("prediction_vs_conventions", {k: fmt(v) for k, v in errs.items()})

    wb.add_assertion(
        name="su4_casimir_predicts_A3_within_1pct_coulomb_corrected",
        computed=fmt(errs["3H_Coulomb_corrected"]), expected="0", tolerance="0.01",
        unit="relative error on w(3)",
        source=("alpha,beta fitted to A=2 and A=4; A=3 predicted. ONE degree of "
                "predictive freedom. Convention preferred AFTER inspecting all "
                "three -- declared, not concealed."),
    )

    wb.add_data("scope", {
        "is_a_derivation": False,
        "fitted_parameters": 2, "points_fitted": 2, "points_predicted": 1,
        "convention_selected_post_hoc": True,
        "beta_close_to_1_MeV_is_not_evidence": "MeV is a human unit; no framework "
                                               "scale distinguishes it",
        "cannot_be_falsified_further": "[1^n] is empty for n >= 5, so no A >= 5 "
                                       "prediction exists",
        "what_would_promote_it": "derive beta from the three calibrations; the LO "
                                 "SU(4)-symmetric contact interaction has one "
                                 "coupling (nucl-th/0409040)",
    })
    wb.save()
    print("\nOK — recorded as a LEAD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
