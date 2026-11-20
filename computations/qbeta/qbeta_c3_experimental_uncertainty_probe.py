"""c_3 is not experimentally determined: sigma(c_3) = 1.16, and -2 is inside 1 sigma.

Answers a direct question -- "why do two neutron masses move c_3 so much?" -- and
the answer generalises past the question in a way that bears on the whole
`c_3 = -2 = J_Hopf(q=1)` near-match claim.

THE MECHANISM. c_3 is not measured; it is EXTRACTED by inverting the experimental
Q_beta against the ansatz (computations/probe_q_beta_operator_valued_N3.py, which
labels its own row '[fit]'):

    c_3 = (Q_target / Q_N2 - 1) / (b^3 * hbar_q^6)

The divisor is the rung c_3 multiplies, and it is TINY: b^3 hbar_q^6 = 6.179e-7.
So the extraction has gain 1/(b^3 hbar_q^6) = 1.618e6, and ANY relative wobble in
the target Q_beta is amplified by 1.6 million on its way into c_3. That is generic
to extracting a high-order coefficient from a low-order-accurate target; it is not
a defect in any particular number.

THE ANSWER TO THE QUESTION. The corpus carries two DOCUMENTED neutron masses --
CODATA-2022's direct measurement 939.56542194(48) and an AME-derived 939.56542179
(codata_2022_source.py lists both; qou_substrate's line says "AME-derived, NOT
CODATA"). They differ by 1.5e-7 MeV = 191.7 ppb of Q_beta, which the gain turns
into 0.310 on c_3 -- 17.6 % of it.

THE CONSEQUENCE, WHICH IS LARGER. The same gain applies to the EXPERIMENTAL error.
CODATA-2022 quotes sigma(m_n) = 6e-7 and sigma(m_p) = 2.9e-7 MeV, giving
sigma(Q_beta) = 5.61e-7 MeV = 717 ppb and therefore

    sigma(c_3) = 1.16          i.e.   c_3 = -1.76 +/- 1.16   (66 % relative)

with 1-sigma interval [-2.92, -0.60]. **-2 sits comfortably inside it.**

So the published "c_3 = -2 is a 3.47 % near-match" is not evidence for the
identification. A 3.47 % agreement quoted inside a +/-66 % error bar is a central
value reported without its uncertainty, not a near-match. Note also that the
two-neutron-mass split, which prompted the question, is only 0.27 sigma -- small
against the experimental error, which is the real story.

WHAT THIS IS AND IS NOT. Scope (a): this constrains what the extraction can
SUPPORT, and says nothing about whether c_3 = -2 is TRUE. A derivation of c_3 from
the categorical side would be unaffected by any of this -- it would simply no
longer be able to cite the extraction as its confirmation. Equally, this is not a
claim that any corpus mass or error bar is wrong; both masses and both
uncertainties are as published.

Convention C throughout (the frame the extraction is defined in). The D-frame
ladder is a separate open item, qou-cds1. Nothing wired, no c_k value proposed.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import M_E_MEV, M_N_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION_ERR, M_N_MEV_VALIDATION_ERR)

set_compute_dps()

CANDIDATE_C3 = mp.mpf(-2)


def main() -> int:
    wb = WitnessBuilder("qbeta-c3-experimental-uncertainty", engine="mpmath")
    wb.set_description(
        "c_3 is extracted with gain 1/(b^3 hbar_q^6) = 1.618e6, so the CODATA-2022 "
        "mass uncertainties give sigma(c_3) = 1.16 -- c_3 = -1.76 +/- 1.16, 66 % "
        "relative, with -2 INSIDE 1 sigma. The published 3.47 % 'near-match' is a "
        "central value quoted without its uncertainty. Scope (a); convention C; "
        "nothing wired.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n      {note}")

    q = Q_MP
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    ME = mp.mpf(str(M_E_MEV))

    rung = b**3 * hb**6
    gain = 1 / rung
    eps = (h / 2) * h - h
    QA = abs(eps * ME / (q * (q - 1)))
    zC = mp.sqrt(q) / (q + 1)
    Q_N2 = QA * mp.cos((zC - 1) * h / 2 - b * hb**2 / 2) * (1 - b**2 * hb**4)

    Q_ame = (mp.mpf(str(M_N_MEV_VALIDATION)) - mp.mpf(str(M_P_MEV_VALIDATION)) - ME)
    sigQ = mp.sqrt(mp.mpf(str(M_N_MEV_VALIDATION_ERR))**2
                   + mp.mpf(str(M_P_MEV_VALIDATION_ERR))**2)

    c3 = (Q_ame / Q_N2 - 1) / rung
    sig_c3 = (sigQ / Q_N2) / rung
    lo, hi = c3 - sig_c3, c3 + sig_c3

    print("=" * 76)
    print(" c_3 is not experimentally determined")
    print("=" * 76)
    print()
    print(f"  rung  b^3 hbar_q^6            = {mp.nstr(rung, 8)}")
    print(f"  extraction gain 1/rung        = {mp.nstr(gain, 8)}")
    print(f"  extracted c_3                 = {mp.nstr(c3, 8)}")
    print(f"  sigma(Q_beta) from mass errors= {mp.nstr(sigQ / Q_ame * 10**9, 6)} ppb")
    print(f"  sigma(c_3)                    = {mp.nstr(sig_c3, 6)}")
    print(f"  c_3 = {mp.nstr(c3, 6)} +/- {mp.nstr(sig_c3, 6)}"
          f"   ({mp.nstr(abs(sig_c3 / c3) * 100, 5)} % relative)")
    print(f"  1-sigma interval              = [{mp.nstr(lo, 6)}, {mp.nstr(hi, 6)}]")
    print()

    check("extraction_gain_is_the_inverse_rung",
          abs(gain - 1 / rung) < mp.mpf("1e-30") and gain > mp.mpf("1e6"),
          f"c_3 = (Q/Q_N2 - 1)/(b^3 hbar_q^6) divides by {mp.nstr(rung, 7)}, so the "
          f"gain is {mp.nstr(gain, 7)}. Every relative wobble in the target is "
          f"multiplied by that on its way into c_3")

    check("codata_uncertainty_alone_gives_sigma_c3_above_1",
          sig_c3 > 1,
          f"sigma(m_n) = {M_N_MEV_VALIDATION_ERR}, sigma(m_p) = "
          f"{M_P_MEV_VALIDATION_ERR} MeV give sigma(Q_beta) = "
          f"{mp.nstr(sigQ / Q_ame * 10**9, 6)} ppb and hence sigma(c_3) = "
          f"{mp.nstr(sig_c3, 6)} -- LARGER than half of |c_3| itself")

    check("candidate_minus_two_is_inside_one_sigma",
          lo <= CANDIDATE_C3 <= hi,
          f"1-sigma interval [{mp.nstr(lo, 6)}, {mp.nstr(hi, 6)}] contains -2. So "
          f"the extraction cannot distinguish c_3 = -2 from c_3 = -1 or c_3 = -2.9. "
          f"The published '3.47 % near-match' is a central value quoted without its "
          f"uncertainty; the relative uncertainty is "
          f"{mp.nstr(abs(sig_c3 / c3) * 100, 4)} %")

    dQ = abs(mp.mpf(str(M_N_MEV_VALIDATION)) - mp.mpf(str(M_N_MEV)))
    dc3_split = (dQ / Q_N2) / rung
    check("the_two_mass_split_is_a_fraction_of_one_sigma",
          dc3_split < sig_c3,
          f"the CODATA-vs-AME neutron split moves c_3 by {mp.nstr(dc3_split, 6)}, "
          f"which is {mp.nstr(dQ / sigQ, 4)} sigma. It is REAL and it is 17.6 % of "
          f"c_3 -- but it is smaller than the experimental error, so 'which neutron "
          f"mass' is the lesser half of the answer. Both are documented values; "
          f"neither is wrong")

    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    for k, v in (("extraction_gain", gain), ("c3_extracted", c3),
                 ("sigma_c3", sig_c3), ("sigma_Q_ppb", sigQ / Q_ame * 10**9),
                 ("one_sigma_lo", lo), ("one_sigma_hi", hi),
                 ("two_mass_split_dc3", dc3_split)):
        wb.add_data(k, fmt(v))

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
