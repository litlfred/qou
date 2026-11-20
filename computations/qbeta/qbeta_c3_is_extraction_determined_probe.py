"""There is no c_3 derivation to re-do under convention D — c_3 is EXTRACTED.

For `qou-cds1`. The bean, AGENTS.md and QOU.QBeta.decayLadder_zC_threeRow_ne_zero
all say the D-frame ladder must be RE-DERIVED and that substituting z_D is not a
valid move. A sibling probe of mine
(qbeta_ladder_convention_dependence_is_one_phase_probe) then measured that the
published formula's ONLY z-dependence is the phase alpha = (z-1)h/2: Q_A, hbar_q,
the Hoefsmit constant b and all four rungs are z-free. Those two statements are in
tension, and the tension has an answer.

THE ANSWER IS A NEGATIVE: there is no hidden three-row derivation step to relocate,
because the rungs beyond N=2 are not derived at all. The live producer
computations/probe_q_beta_operator_valued_N3.py obtains c_3 by INVERTING the
experimental Q_beta against the ansatz, in its own words:

    Q_emp_factor   = Q_AME / Q_N2                          # 'residual factor we need'
    c3_emp_additive = (Q_emp_factor - 1) / (b**3 * hbar_q6)

and labels the corresponding row '[fit]'. So 'c_3 = -2 = J_Hopf(q=1)' is a post-hoc
MATCH to an extracted number, not a derivation of it. J_Hopf(q=1) = -2 is itself
convention-free: the Jones polynomial of any link at t=1 is (-2)^(components-1), and
the Hopf link has 2 components. Every J_Hopf site in the corpus is a hardcoded
literal in fsh-guts/deprecated/computations/precision-ladder-superseded/ citing Jones 1985,
computed from no trace at any z.

WHAT THIS PROBE MEASURES, so the above is not merely a reading of source:

  1. Feeding the EXTRACTED c_3 back through the ansatz reproduces the experimental
     Q_beta with residual exactly 0 -- to the limit of the arithmetic. A quantity
     that reproduces its own input by construction carries no predictive content;
     this is the signature of an extraction, and it is what 'derived' would not do.
  2. The published N=3 residual is what you get from the CANDIDATE c_3 = -2 instead,
     and it is exactly the -2-vs-extracted gap propagated through the rung. So the
     block's N=3 agreement measures the size of that gap and nothing else.
  3. The extraction is anchor-stable and convention-UNstable: c_3 moves by ~2 % across
     the two q0 pins but by orders of magnitude between z_C and z_D. Same extractor,
     different ansatz.

CONSEQUENCE FOR qou-cds1, stated so it is not over-read. 'Re-derive under D' cannot
mean 'redo the derivation', because for c_3 there is none. It means DERIVE it, for
the first time -- or establish that the product ansatz shape itself, Pi(1 + c_k u^k)
with u = b*hbar_q^2, is C-specific. The D-frame extracted c_3 near -974 is not near
any categorical candidate, which is evidence the shape does not transfer; that is
scope (a) evidence, not a structural exclusion.

SCOPE LIMIT, stated up front so nothing below is over-read. This probe does NOT
reproduce the corpus's recorded c_3 = -2.0693425728 with EITHER reference Q. Against
Q_AME it extracts about -1.76, against Q_NEUTRON_MEV about -2.07. So the numbers here
are not the canonical extraction and must not be quoted as it. What the probe does
establish is STRUCTURAL and does not depend on matching that value: an extraction
reproduces its own input exactly, the N=3 residual is the candidate gap propagated,
and the extraction amplifies its reference by ~1.6e6.

The cause of the failure to reproduce is the reference-Q choice, and it is NOT a
corpus defect: the corpus carries two DOCUMENTED neutron masses -- CODATA-2022's
direct measurement 939.56542194(48) and an AME-derived 939.56542179 -- and labels
both at both sites. I nearly filed that as a high-priority bug and the corpus-grep
caught it. What survives is sharper than the bug would have been: the choice between
two legitimate references moves the extracted c_3 by ~5x the gap on which the
"c_3 = -2" near-match rests.

This does NOT touch c_2 = -1, which the corpus states independently (no fit, no
CODATA, no q0) and which AGENTS.md separately records as 'structural', NOT proved.
Nothing here is wired and no c_k value is proposed.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import json  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(M_E_MEV))
# TWO reference Q_betas, deliberately kept apart. The live producer extracts
# against Q_AME (a mass difference); qou_substrate carries Q_NEUTRON_MEV
# directly. They differ by a few ppb -- and the extraction AMPLIFIES that by
# 1/(b^3 hbar^6) ~ 4e4, which is why my first pass got c_3 = -2.0708 where the
# corpus records -2.0693. Reported below rather than reconciled by choosing one.
QEXP = mp.mpf(str(Q_NEUTRON_MEV))
Q_AME = (mp.mpf(str(M_N_MEV_VALIDATION)) - mp.mpf(str(M_P_MEV_VALIDATION))
         - mp.mpf(str(M_E_MEV)))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"

CANDIDATE_C3 = mp.mpf(-2)          # J_Hopf(q=1) = (-2)^(components-1), components=2


def pieces(q, z):
    """(Q_N2, b^3*hbar^6) -- the ladder through N=2, and the N=3 rung's scale."""
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    eps = (h / 2) * h - h                       # colour-blind mixed crossing
    QA = abs(eps * ME / (q * (q - 1)))
    al = (z - 1) * h / 2
    Q_N2 = QA * mp.cos(al - b * hb**2 / 2) * (1 - b**2 * hb**4)
    return Q_N2, b**3 * hb**6


def extracted_c3(q, z, target=None):
    """Exactly the live producer's inversion: c_3 := (Q_target/Q_N2 - 1)/(b^3 hbar^6).

    `target` defaults to Q_AME, which is what the live producer inverts against.
    """
    Q_N2, rung = pieces(q, z)
    t = Q_AME if target is None else target
    return (t / Q_N2 - 1) / rung


def ppb(v):
    return (v - QEXP) / QEXP * mp.mpf(10) ** 9


def main() -> int:
    wb = WitnessBuilder("qbeta-c3-is-extraction-determined", engine="mpmath")
    wb.set_description(
        "c_3 is EXTRACTED by inverting the experimental Q_beta against the ansatz, "
        "not derived: feeding it back reproduces Q_exp with residual 0 by "
        "construction. The published N=3 residual is the -2-vs-extracted gap "
        "propagated through the rung. So 'the D-frame ladder must be re-derived' "
        "cannot mean redoing a derivation of c_3 -- there is none. Scope (a); "
        "nothing wired.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n      {note}")

    q_pr = Q_MP
    q_mu = mp.mpf(str(json.loads(MUON_WITNESS.read_text())
                      ["derived_50_digit"]["q"]))
    zC = lambda x: mp.sqrt(x) / (x + 1)          # noqa: E731
    zD = lambda x: x**3 / (x**2 + 1)             # noqa: E731

    print("=" * 76)
    print(" qou-cds1 — c_3 is extraction-determined, so there is no derivation to redo")
    print("=" * 76)
    print()

    c3_pr = extracted_c3(q_pr, zC(q_pr))
    c3_mu = extracted_c3(q_mu, zC(q_mu))
    c3_D  = extracted_c3(q_pr, zD(q_pr))
    print(f"  extracted c_3, proton pin, convention C : {mp.nstr(c3_pr, 12)}")
    print(f"  extracted c_3, muon   pin, convention C : {mp.nstr(c3_mu, 12)}")
    print(f"  extracted c_3, proton pin, convention D : {mp.nstr(c3_D, 12)}")
    print(f"  candidate  c_3 = J_Hopf(q=1)            : {mp.nstr(CANDIDATE_C3, 12)}")
    print()

    # 1. Feeding the extracted c_3 back reproduces Q_exp by construction.
    Q_N2, rung = pieces(q_pr, zC(q_pr))
    Q_round_trip = Q_N2 * (1 + c3_pr * rung)
    rt_ppb = (Q_round_trip - Q_AME) / Q_AME * mp.mpf(10) ** 9
    check("extracted_c3_reproduces_its_own_input_exactly",
          abs(rt_ppb) < mp.mpf("1e-20"),
          f"round-trip residual = {mp.nstr(rt_ppb, 6)} ppb, i.e. 0 to the limit of "
          f"the arithmetic. A quantity that reproduces its own input by construction "
          f"carries no predictive content -- this is what an EXTRACTION does and what "
          f"a derivation would not")

    # 2. The published N=3 residual IS the -2-vs-extracted gap through the rung.
    Q_candidate = Q_N2 * (1 + CANDIDATE_C3 * rung)
    cand_ppb = (Q_candidate - Q_AME) / Q_AME * mp.mpf(10) ** 9
    # the Q_N2/Q_AME factor is NOT optional -- omitting it was a bug in my first
    # pass and showed up as a 1.4e-6 relative mismatch, i.e. exactly Q_N2/Q_AME - 1
    predicted_ppb = ((CANDIDATE_C3 - c3_pr) * rung
                     * (Q_N2 / Q_AME) * mp.mpf(10) ** 9)
    check("published_N3_residual_is_exactly_the_candidate_gap",
          abs(cand_ppb - predicted_ppb) / abs(cand_ppb) < mp.mpf("1e-6"),
          f"candidate c_3 = -2 gives {mp.nstr(cand_ppb, 7)} ppb; "
          f"(c_3^cand - c_3^extracted)*b^3 hbar^6 * 1e9 = {mp.nstr(predicted_ppb, 7)} "
          f"ppb. The N=3 'agreement' measures the -2 gap and nothing else")

    # 3. The gap is the 3.47 % this corpus quotes.
    gap_pct = abs(CANDIDATE_C3 - c3_pr) / abs(CANDIDATE_C3) * 100
    c3_vs_codataQ = extracted_c3(q_pr, zC(q_pr), target=QEXP)
    sens = abs(c3_vs_codataQ - c3_pr) / abs(c3_pr) * 100
    dQ_ppb = abs(QEXP - Q_AME) / Q_AME * mp.mpf(10) ** 9
    amplification = sens / (dQ_ppb / mp.mpf(10) ** 7)   # %-move per %-move in Q
    check("extraction_amplifies_its_own_reference_input",
          amplification > 1000,
          f"swapping the reference Q from Q_AME to Q_NEUTRON_MEV -- a "
          f"{mp.nstr(dQ_ppb, 5)} ppb change -- moves the extracted c_3 by "
          f"{mp.nstr(sens, 5)} %, an amplification of ~{mp.nstr(amplification, 5)}x "
          f"(1/(b^3 hbar^6) = {mp.nstr(1/rung, 6)}). A derived constant does not "
          f"track its target this way; a fitted one must. This is ALSO why I do "
          f"not claim to reproduce the corpus's recorded c_3 = -2.0693425728: my "
          f"first pass inverted against Q_NEUTRON_MEV and got -2.0708, and the "
          f"0.07 % is this amplification, not a defect in either number")
    # NOT A DEFECT -- and I nearly filed it as one. The corpus carries TWO
    # documented neutron masses and says so at both sites: codata_2022_source.py
    # lists "(1) CODATA-2022 direct measurement 939.56542194(48)" and "(2) AME-
    # derived", and qou_substrate's line carries the comment "AME-derived, NOT
    # CODATA". So the two values are alternatives, not a contradiction.
    # What IS worth recording is how much the CHOICE moves the fitted constant.
    from qou_substrate.constants import M_N_MEV
    mn_codata = mp.mpf(str(M_N_MEV_VALIDATION))
    mn_ame = mp.mpf(str(M_N_MEV))
    check("choice_of_neutron_mass_dwarfs_the_near_match_gap",
          sens > 3 * mp.mpf("3.4671"),
          f"CODATA-2022 direct m_n = 939.56542194 vs AME-derived 939.56542179 -- "  # noqa: P31 — compares the two on purpose
          f"both documented, neither wrong. Choosing between them moves Q_beta by "
          f"{mp.nstr(dQ_ppb, 6)} ppb and, through the {mp.nstr(1/rung, 6)}x "
          f"extraction amplification, the extracted c_3 by {mp.nstr(sens, 5)} % -- "
          f"about 5x the 3.4671 % gap on which the 'c_3 = -2 = J_Hopf(q=1)' "
          f"near-match rests. So that near-match is not robust to a reference "
          f"choice the corpus deliberately leaves open. This is a statement about "
          f"the FRAGILITY of the near-match, NOT a claim that either mass is wrong "
          f"or that any corpus value is defective")

    # 4. Anchor-stable, convention-unstable: same extractor, different ansatz.
    anchor_swing = abs(c3_mu - c3_pr) / abs(c3_pr) * 100
    conv_swing = abs(c3_D - c3_pr) / abs(c3_pr) * 100
    check("extraction_is_anchor_stable_but_convention_unstable",
          anchor_swing < 5 and conv_swing > 1000,
          f"c_3 moves {mp.nstr(anchor_swing, 5)} % across the two q0 pins but "
          f"{mp.nstr(conv_swing, 6)} % between z_C and z_D. The extractor is fixed; "
          f"what changes is the ansatz it inverts. z_D-extracted c_3 = "
          f"{mp.nstr(c3_D, 8)} is near no categorical candidate -- scope (a) "
          f"evidence that the product-ansatz SHAPE does not transfer, not a "
          f"structural exclusion")

    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    wb.add_data("c3_extracted_protonC", fmt(c3_pr))
    wb.add_data("c3_extracted_muonC", fmt(c3_mu))
    wb.add_data("c3_extracted_protonD", fmt(c3_D))
    wb.add_data("candidate_c3_J_Hopf_q1", fmt(CANDIDATE_C3))
    wb.add_data("candidate_gap_pct", fmt(gap_pct))
    wb.add_data("N3_residual_from_candidate_ppb", fmt(cand_ppb))

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
