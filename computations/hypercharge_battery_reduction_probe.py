#!/usr/bin/env python3
"""Reduce the eightfold-way hypercharge battery to its irreducible content.

Context
-------
``folio/quantum-observable-universe/eightfold-way/eightfold-open-problems.md``
item 2 states hypercharge ``Y`` is open: the writhe map is *falsified* as a
``Y`` assignment (proton and neutron share ``Y = +1`` while their writhes
differ), so a **second crossing invariant independent of the writhe** is
required.  Any candidate must pass two batteries
(``flavor-charge-assignments.md``):

  B1  Gell-Mann--Nishijima ``Q = I3 + Y/2`` on the nucleon doublet.
  B2  First-generation spectrum: ``Y`` of ``(u, d, e-, nu_e)`` must be
      ``{+1/3, +1/3, -1, -1}`` left-handed and ``{+4/3, -2/3, -2, 0}``
      right-handed.

This probe asks what B1/B2 *actually constrain*, in exact rational
arithmetic.  It derives nothing new about the framework; it measures the
information content of the stated tests, so the search is narrowed before
it is run (AGENTS.md formalize-first probe discipline).

Result (all exact, no floats, no fitted parameter)
--------------------------------------------------
  R1  The RH half of B2 is an **identity**, not a test.  RH fermions are
      weak singlets (``I3 = 0``), so GMN forces ``Y = 2Q`` termwise.  Given
      the framework's independently derived ``Q``, the RH targets are
      *entailed*; they can discriminate no candidate.  Same logical status
      as the GMO identity proved vacuous in ``GellMannOkuboIdentity.lean``.

  R2  The LH half of B2 is exactly ``Y = B - L`` termwise -- baryon number
      minus lepton number, the standard anomaly-free combination.

  R3  On the nucleon doublet (B1) ``L = 0``, so there ``Y = B``.

Consequence for the open item
-----------------------------
B2 does not impose two independent conditions; it imposes one.  The whole
hypercharge battery reduces to *derive ``B - L`` on the left-handed sector*,
of which the nucleon-doublet case is the ``L = 0`` restriction ``Y = B``.

This is a scope-(a) statement about the **battery**, not about any
candidate: it says what must be derived, not that any particular invariant
derives it.  A candidate supplying ``B`` alone (e.g. the Milnor triple
linking ``mu-bar_123`` proposed in PR #4597, where ``mu-bar_123 = B``)
closes B1 and the quark rows of B2-LH but leaves the ``L`` half open --
lepton number is not a baryon-sector invariant.  Nothing here endorses that
candidate; it fixes the target it would have to hit.
"""

from __future__ import annotations

import json
from fractions import Fraction as F

# --- Standard Model first-generation quantum numbers (reference data) ------
# (Q, I3_L, B, L).  Q and B/L are handedness-independent; I3 is 0 for the
# right-handed weak singlets.  These are definitions/observed assignments,
# used here as the *targets* the battery states -- not framework outputs.
FERMIONS = {
    "u":     dict(Q=F(2, 3),  I3_L=F(1, 2),  B=F(1, 3), L=F(0)),
    "d":     dict(Q=F(-1, 3), I3_L=F(-1, 2), B=F(1, 3), L=F(0)),
    "nu_e":  dict(Q=F(0),     I3_L=F(1, 2),  B=F(0),    L=F(1)),
    "e-":    dict(Q=F(-1),    I3_L=F(-1, 2), B=F(0),    L=F(1)),
}

# Battery-2 targets exactly as stated in flavor-charge-assignments.md.
# The chapter lists them in the order (u, d, e-, nu_e).
TARGET_LH = {"u": F(1, 3), "d": F(1, 3), "e-": F(-1), "nu_e": F(-1)}
TARGET_RH = {"u": F(4, 3), "d": F(-2, 3), "e-": F(-2), "nu_e": F(0)}

# Nucleon doublet (battery 1).  B = 1, L = 0 for both.
NUCLEONS = {
    "p": dict(Q=F(1), I3=F(1, 2),  B=F(1), L=F(0)),
    "n": dict(Q=F(0), I3=F(-1, 2), B=F(1), L=F(0)),
}


def gmn_Y(Q: F, I3: F) -> F:
    """Hypercharge forced by Gell-Mann--Nishijima Q = I3 + Y/2."""
    return 2 * (Q - I3)


def main() -> dict:
    results: dict[str, object] = {}
    ok = True

    # R1 -- RH half of B2 is an identity: I3 = 0 => Y = 2Q.
    rh_rows = []
    rh_all = True
    for name, d in FERMIONS.items():
        y_forced = gmn_Y(d["Q"], F(0))          # RH: weak singlet, I3 = 0
        match = y_forced == TARGET_RH[name]
        rh_all &= match
        rh_rows.append(dict(fermion=name, Q=str(d["Q"]),
                            Y_forced_by_GMN=str(y_forced),
                            Y_target=str(TARGET_RH[name]), match=match))
    results["R1_rh_is_identity"] = dict(
        claim="RH battery targets are entailed by Q via GMN at I3=0 (Y=2Q); "
              "they test nothing beyond the already-derived Q",
        all_match=rh_all, rows=rh_rows)
    ok &= rh_all

    # R2 -- LH half of B2 is exactly B - L.
    lh_rows = []
    lh_all = True
    for name, d in FERMIONS.items():
        y_gmn = gmn_Y(d["Q"], d["I3_L"])
        b_minus_l = d["B"] - d["L"]
        match = (y_gmn == TARGET_LH[name] == b_minus_l)
        lh_all &= match
        lh_rows.append(dict(fermion=name, Y_from_GMN=str(y_gmn),
                            Y_target=str(TARGET_LH[name]),
                            B_minus_L=str(b_minus_l), match=match))
    results["R2_lh_is_B_minus_L"] = dict(
        claim="LH battery targets equal B - L termwise (and agree with GMN)",
        all_match=lh_all, rows=lh_rows)
    ok &= lh_all

    # R3 -- nucleon doublet: Y = B (since L = 0), and both share Y = +1
    #       while writhes differ (the falsification the chapter records).
    nuc_rows = []
    nuc_all = True
    for name, d in NUCLEONS.items():
        y_gmn = gmn_Y(d["Q"], d["I3"])
        b_minus_l = d["B"] - d["L"]
        match = (y_gmn == F(1) == b_minus_l == d["B"])
        nuc_all &= match
        nuc_rows.append(dict(hadron=name, Y_from_GMN=str(y_gmn),
                             B=str(d["B"]), B_minus_L=str(b_minus_l),
                             match=match))
    results["R3_nucleon_Y_equals_B"] = dict(
        claim="On the nucleon doublet L=0, so Y = B - L = B = +1 for both",
        all_match=nuc_all, rows=nuc_rows)
    ok &= nuc_all

    # Consequence: independent content of the battery.
    results["reduction"] = dict(
        rh_independent_conditions=0,
        lh_independent_conditions=1,
        statement="B2 imposes ONE condition, not two: derive B - L on the LH "
                  "sector. B1 (nucleon doublet) is its L=0 restriction Y = B.",
        scope="(a) -- a statement about the battery's information content, "
              "not an exclusion of any candidate invariant.",
        candidate_note="An invariant supplying B alone (e.g. mu-bar_123 = B, "
                       "PR #4597) closes B1 and the quark rows of B2-LH; the "
                       "lepton-number half stays open. Not an endorsement.")

    results["all_checks_passed"] = bool(ok)
    return results


if __name__ == "__main__":
    res = main()
    print(json.dumps(res, indent=2))
    print("\nALL EXACT CHECKS PASSED" if res["all_checks_passed"]
          else "\nCHECK FAILED")
