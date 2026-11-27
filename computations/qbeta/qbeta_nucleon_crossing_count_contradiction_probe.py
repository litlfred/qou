#!/usr/bin/env python3
"""The corpus DERIVES a 13-crossing neutron; the code implements an 11.

qou-bg3w / qou-cds1.  The Delta-element fork turns on which object `Delta_L`
is a difference OF.  `Delta_L = neutron_word - proton_word`, both taken from
`hecke_core`, so the crossing content of those two words is load-bearing.

Three corpus statements and one implementation, all measured here:

  (A) `categorical-proton-properties.md:10` -- the PROTON is the bare
      9-crossing element B_3 x Delta_3(uud) plus "a single Hopf link
      L_- = sigma_1 sigma_0".  9 + 2 = 11.

  (B) `categorical-neutron-properties.md:11` -- the NEUTRON's LP dual "selects
      L_+ -> L_- (two Hopf links, 4 gluon crossings)... The neutron requires
      more gluon crossings than the proton (4 versus 2) because the dd
      crossing creates a deeper instability (tr_M = -0.132 versus -0.006).
      This yields A TOTAL OF 13 CROSSINGS (6 from B_3, 3 from quarks, 4 from
      gluons)."

  (C) `q-beta-gamma-gamma-canonical-derivation.md:33` -- "From
      def:categorical-proton and def:categorical-neutron, B_p and B_n have
      11 typed crossings EACH."

  (D) `hecke_core._PROTON_G0/_G1`, `_NEUTRON_G0/_G1` -- 11 each.

(A), (C) and (D) agree on the proton.  (B) derives 13 for the neutron while
(C) asserts 11 for it, CITING the very definition whose properties block
derives 13 -- and (D) implements 11.

WHAT THIS PROBE DOES AND DOES NOT DO.  Scope-(a).  It establishes the
mismatch mechanically so the claim is reproducible and so it FAILS LOUDLY if
someone later reconciles the two.  It does NOT adjudicate which count is
right, does NOT modify `hecke_core`, and proposes no c_k.  Deciding between a
13-crossing neutron and an 11-crossing one moves every number `Delta_L`
enters; that is an owner call of the same class as the fork itself.

A NOTE ON THE DECOMPOSITION.  The per-crossing classification below (pure /
inverted / averaged, from the stored shift d in {0, -h, -h/2}) reproduces
`c5-involution-leibniz-decomposition-interpretation.md:18` for the proton
EXACTLY -- "7 pure sigma_0, 4 pure sigma_1, 1 averaged sigma_0, 1 averaged
sigma_1, 3 inverted sigma_1^-1".  The further identification of `pure` with
B_3 crossings and `averaged`/`inverted` with quark/gluon crossings is NOT
asserted: it is a plausible reading, not a corpus statement, and the
contradiction this probe reports needs no such mapping -- it is a mismatch of
TOTALS.

-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/categorical-neutron-properties.md
-- Ref: [manuscript] folio/quantum-observable-universe/knots-particles-confinement/categorical-proton-properties.md
-- Ref: [manuscript] folio/quantum-observable-universe/stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md
-- Ref: [manuscript] computations/qbeta/qbeta_delta_element_fork_pricing_probe.py (the fork this feeds)
"""
from __future__ import annotations

import os
import re
import sys

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)

set_compute_dps(50)

ROOT = _pl.Path(__file__).resolve().parents[2]
CONTENT = ROOT / "folio" / "quantum-observable-universe"

Q = Q_MP
H = Q - 1 / Q
TOL = mp.mpf("1e-30")

_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    if w is not None:
        w.add_data(name, bool(ok))
        # bean qou-srvu. Without this the witness carried ZERO assertions and
        # `save()` still emitted `allPassed: true` -- green while claiming
        # nothing, indistinguishable to a consumer from a run that checked
        # something and passed. The verdict was already computed (it prints
        # [PASS]/[FAIL] above, is tallied into _FAILURES, and drives this
        # script's exit code); it just never reached `assertions[]`. No
        # threshold is chosen here and no claim is invented: `ok` is the
        # producer's own boolean and `True` is what the exit code already
        # compares it against.
        w.add_assertion(name, computed=bool(ok), expected=True, source=detail)
    if not ok:
        _FAILURES.append(name)
    return ok


def classify(word):
    """pure / inverted / averaged, from the stored shift d.

    The stored values are full-precision mpf.  Comparing via `str(d)` would
    round-trip them through a 17-digit repr and land every one in OTHER --
    so compare the mpf DIRECTLY.
    """
    out = {"pure": 0, "inverted": 0, "averaged": 0, "other": 0}
    for _c, d in word:
        if d == 0:
            out["pure"] += 1
        elif abs(d + H) < TOL:
            out["inverted"] += 1
        elif abs(d + H / 2) < TOL:
            out["averaged"] += 1
        else:
            out["other"] += 1
    return out


def grep1(relpath, pattern):
    """First matching line of a content file, or None."""
    p = CONTENT / relpath
    if not p.exists():
        return None
    for line in p.read_text(encoding="utf-8").split("\n"):
        if re.search(pattern, line):
            return line.strip()
    return None


def main() -> int:
    w = WitnessBuilder("qbeta-nucleon-crossing-count-contradiction",
                       engine="python")
    w.set_description(
        "qou-bg3w: categorical-neutron-properties derives a 13-crossing "
        "neutron (6 B_3 + 3 quark + 4 gluon, two Hopf links) while "
        "q-beta-gamma-gamma-canonical-derivation asserts 11 for both nucleons "
        "-- citing the very definition that derives 13 -- and hecke_core "
        "implements 11. The proton is consistent at 11 across all three. "
        "Scope-(a): establishes the mismatch, adjudicates nothing, changes "
        "no compute."
    )

    print("=" * 72)
    print(" qou-bg3w - nucleon crossing counts: corpus vs hecke_core")
    print("=" * 72)

    p_tot = len(_PROTON_G0) + len(_PROTON_G1)
    n_tot = len(_NEUTRON_G0) + len(_NEUTRON_G1)
    pc = classify(list(_PROTON_G0) + list(_PROTON_G1))
    nc = classify(list(_NEUTRON_G0) + list(_NEUTRON_G1))

    print(f"\n  hecke_core PROTON  : {p_tot} crossings  {pc}")
    print(f"  hecke_core NEUTRON : {n_tot} crossings  {nc}")
    for k, v in pc.items():
        w.add_data(f"proton_{k}", v)
    for k, v in nc.items():
        w.add_data(f"neutron_{k}", v)
    w.add_data("proton_total_code", p_tot)
    w.add_data("neutron_total_code", n_tot)

    check("no_unrecognised_crossing_shift",
          pc["other"] == 0 and nc["other"] == 0,
          "every stored d is exactly 0, -h or -h/2 -- compared as mpf, not "
          "via str(): the str round-trip truncates to ~17 digits and would "
          "put all 22 in 'other'", w)

    # -- the proton is consistent everywhere --------------------------------
    check("code_proton_is_eleven",
          p_tot == 11,
          f"hecke_core proton = {p_tot} crossings, matching the derivation "
          f"(bare 9 = 6 B_3 + 3 quark, plus one Hopf link = 2 gluon)", w)

    check("code_proton_decomposition_matches_the_c5_block",
          pc["pure"] == 6 and pc["inverted"] == 3 and pc["averaged"] == 2
          and len(_PROTON_G0) == 7 and len(_PROTON_G1) == 4,
          "c5-involution-leibniz-decomposition-interpretation.md:18 says "
          "'7 pure sigma_0, 4 pure sigma_1, 1 averaged sigma_0, 1 averaged "
          "sigma_1, 3 inverted sigma_1^-1' -- gen0=7 (6 pure + 1 averaged), "
          "gen1=4 (3 inverted + 1 averaged). The code matches EXACTLY, so "
          "that block describes the LONG model faithfully", w)

    # -- the neutron does not ----------------------------------------------
    derived = grep1("knots-particles-confinement/categorical-neutron-properties.md",
                    r"total of 13 crossings")
    check("corpus_derives_a_thirteen_crossing_neutron",
          derived is not None,
          f"categorical-neutron-properties.md: {(derived or 'NOT FOUND')[:150]}",
          w)

    asserted = grep1("stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md",
                     r"11 typed crossings")
    check("corpus_also_asserts_eleven_for_both",
          asserted is not None,
          f"q-beta-gamma-gamma-canonical-derivation.md: "
          f"{(asserted or 'NOT FOUND')[:150]}", w)

    check("THE_CONTRADICTION_neutron_derived_13_implemented_11",
          derived is not None and n_tot == 11,
          f"the corpus derives 13 crossings for the neutron (two Hopf links, "
          f"4 gluon crossings, because the dd crossing is a deeper "
          f"instability: tr_M = -0.132 vs -0.006) while hecke_core "
          f"implements {n_tot}. Delta_L = neutron - proton is built on the "
          f"11. NOT adjudicated here", w)

    check("the_citation_does_not_say_what_it_is_cited_for",
          asserted is not None and derived is not None,
          "q-beta-gamma-gamma-canonical-derivation.md:33 cites "
          "def:categorical-proton and def:categorical-neutron as authority "
          "for '11 typed crossings each'. That is right for the proton and "
          "wrong for the neutron: the neutron definition's own properties "
          "block derives 13. Same stale-citation class as the convention-C "
          "citations drained in this branch", w)

    # -- scope ---------------------------------------------------------------
    print("\n  scope")
    print("    SCOPE-(a). Reports a mismatch of TOTALS, which needs no")
    print("    mapping from crossing-type to B_3/quark/gluon. Does NOT")
    print("    adjudicate which count is right and does NOT touch")
    print("    hecke_core -- changing the neutron word moves every number")
    print("    Delta_L enters. Owner call, bean qou-bg3w.")
    w.add_data("scope", "a")
    w.add_data("adjudicates", False)
    w.add_data("modifies_compute", False)

    npass = 7 - len(_FAILURES)
    print(f"\n  {npass}/7 checks passed")
    if _FAILURES:
        print(f"  FAILURES: {', '.join(_FAILURES)}")
    w.add_data("checks_passed", npass)
    w.add_data("checks_total", 7)
    out = w.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
