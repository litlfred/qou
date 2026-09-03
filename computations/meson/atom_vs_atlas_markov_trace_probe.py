#!/usr/bin/env python3
"""Do the atom element and its atlas knot share a Markov trace? Exactly: no.

Bean qou-qpj9. Turns an ARGUMENT into a MEASUREMENT.

THE QUESTION
============
per_atom_hyperbolic_volume_witness.py used to justify substituting an atlas
knot for the atom object with "Same Markov class, different topological
realization". That sentence was corrected as a category error -- the atom
object is not a braid (it lies in H_n(q) outside im(rho)), so it has no Markov
class to share.

A category error is an argument. It invites the charitable reply: "granted the
phrasing is loose, but surely the two agree on the invariant that matters."
The Markov trace IS that invariant -- it is what rho(K) in the mass law is, it
is defined on BOTH objects (on the atom element by linearity, on the knot braid
as a braid), and it is a Markov invariant, so genuinely Markov-equivalent
objects MUST agree on it.

So the charitable reading is testable, and this tests it.

WHY IT IS A CLEAN TEST
======================
  * SAME ALGEBRA. A = 1 gives 3A = 3 strands, and the Borromean braid
    (s1 s2^-1)^3 is a 3-braid. Both live in H_3 -- no stabilisation, no
    normalisation mismatch.
  * SAME CONVENTION. Both sides go through markov_peel / markov_trace_canonical,
    which are convention D (z = q^3/(q^2+1)). Deliberately NOT via
    from_scratch/wenzl_y_axiomatic.py, whose z = 1/(q^1/2 + q^-1/2) is
    convention C -- comparing across it would manufacture a disagreement that
    is about the convention, not the objects.
  * SYMBOLIC IN q. No anchor, no dps, no float. The verdict is an algebraic
    identity or it is not, so "agrees to N digits" cannot arise.

WHAT IT DOES NOT SHOW
=====================
NOT that the framework is wrong. The division of labour is sound and was
checked separately (docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md):
Vol comes from the atlas KNOT, rho = tr_M comes from the atom ELEMENT, and
nothing reads a topological quantity off the element. This result CONFIRMS that
split is real rather than redundant -- the two objects are genuinely different
and are genuinely used for different factors.

Nor is the shared knot for p and n a defect. Their atlas entry is the same
Borromean link on purpose: Vol is shared and the p-n mass difference comes from
rho, which this probe confirms differs.

EXPLORATORY / audit-only. Symbolic sympy throughout; no float anywhere, so the
precision gates are vacuous by construction.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from markov_peel import crossing_element, tr_M_atomic  # noqa: E402
from hecke_symbolic import SymbolicHeckeElement  # noqa: E402
from markov_trace_canonical import tr_M_element  # noqa: E402

BORROMEAN = [(0, "sigma"), (1, "sigma_inv")] * 3     # (s1 s2^-1)^3


def braid_elem(word):
    e = SymbolicHeckeElement.identity()
    for g, t in word:
        e = e * crossing_element(g, t)
    return e


def main() -> None:
    tr_bor = sp.simplify(tr_M_element(braid_elem(BORROMEAN), 3))
    tr_p = sp.simplify(tr_M_atomic(1, 0))
    tr_n = sp.simplify(tr_M_atomic(0, 1))

    d_p = sp.simplify(sp.together(tr_p - tr_bor))
    d_n = sp.simplify(sp.together(tr_n - tr_bor))
    d_pn = sp.simplify(sp.together(tr_p - tr_n))

    rows = [
        {"pair": "proton element vs Borromean braid", "difference": str(sp.factor(d_p)),
         "is_zero": d_p == 0},
        {"pair": "neutron element vs Borromean braid", "difference": str(sp.factor(d_n)),
         "is_zero": d_n == 0},
        {"pair": "proton element vs neutron element", "difference": str(sp.factor(d_pn)),
         "is_zero": d_pn == 0},
    ]

    # 1. THE RESULT: the charitable reading of "Same Markov class" is false.
    assert d_p != 0, ("proton element and Borromean braid DO share a trace -- "
                      "then the substitution has a warrant after all and the "
                      "audit must be rewritten, not merely re-scoped")
    assert d_n != 0, "neutron element and Borromean braid share a trace"
    # 2. p and n are distinguished by rho, which is what makes sharing a knot OK
    assert d_pn != 0, ("proton and neutron elements have the SAME trace -- then "
                       "the p-n mass difference cannot come from rho, and the "
                       "shared Borromean entry would be a real defect")
    # 3. CONVENTION GUARD -- test the ANSWER, not the source.
    #
    # AGENTS.md: "when the result is exact and symbolic, test the ANSWER, not
    # the source ... the Markov peel's denominator factors as 192*q^23*(q^2+1)^3
    # -- one (q^2+1) per peel, because z = q^3/(q^2+1). Convention C leaves
    # half-integer powers and cannot produce it." A value cannot be stale,
    # mislabelled, re-spelled, or inherited from a stale record and still
    # factor correctly. An earlier draft of this file grepped a module
    # docstring instead and asserted against prose that lives on the FUNCTION;
    # that guard was about itself.
    q = sp.Symbol("q", positive=True)
    den = sp.denom(sp.together(tr_bor))
    has_qsq_plus_1 = sp.simplify(sp.rem(sp.Poly(den, q), sp.Poly(q**2 + 1, q))) == 0
    half_powers = [e for e in sp.together(tr_bor).atoms(sp.Pow)
                   if e.base == q and e.exp.is_Rational and e.exp.q != 1]
    assert has_qsq_plus_1, (
        f"denominator {den} carries no (q^2+1) factor -- not the convention-D "
        "peel signature; the two sides may not be comparable")
    assert not half_powers, (
        f"half-integer powers of q present ({half_powers}) -- that is the "
        "convention-C signature, so this comparison would measure the "
        "convention rather than the objects")

    wb = WitnessBuilder("atom-vs-atlas-markov-trace", engine="sympy-symbolic")
    wb.set_description(
        "Tests the charitable reading of the corrected 'Same Markov class' "
        "claim: do the atom H_n(q) element and its atlas knot agree on the "
        "Markov trace, the invariant rho(K) in the mass law actually is? "
        "Symbolically in q, both objects in H_3, both through convention-D "
        "machinery. They do not. Markov-equivalent objects must agree on a "
        "Markov invariant, so this measures what the category-error argument "
        "only argued.")
    wb.add_data("differences", rows)
    wb.add_data("traces", {
        "borromean_braid": str(sp.factor(tr_bor)),
        "proton_element": str(tr_p),
        "neutron_element": str(tr_n),
    })
    wb.add_data("method_guards", {
        "same_algebra": ("A=1 gives 3A=3 strands and (s1 s2^-1)^3 is a 3-braid; "
                         "both in H_3, so no stabilisation or normalisation "
                         "mismatch"),
        "same_convention": ("both sides via markov_peel / "
                            "markov_trace_canonical, convention D "
                            "(z = q^3/(q^2+1)). Deliberately NOT via "
                            "from_scratch/wenzl_y_axiomatic.py, whose "
                            "z = 1/(q^1/2 + q^-1/2) is convention C -- that "
                            "comparison would measure the convention, not the "
                            "objects."),
        "symbolic": ("sympy in q throughout; no anchor, no dps, no float, so "
                     "'agrees to N digits' cannot arise"),
    })
    wb.add_data("what_this_does_not_show", {
        "not_a_defect_in_the_framework": ("the division of labour is sound and "
                                          "was checked separately -- Vol from "
                                          "the atlas KNOT, rho = tr_M from the "
                                          "atom ELEMENT, nothing reading a "
                                          "topological quantity off the "
                                          "element. This CONFIRMS that split is "
                                          "real rather than redundant."),
        "shared_knot_for_p_and_n_is_deliberate": ("both atlas to the same "
                                                  "Borromean link on purpose: "
                                                  "Vol is shared and the p-n "
                                                  "difference comes from rho, "
                                                  "which assertion 2 confirms "
                                                  "differs."),
    })
    wb.set_audit_only(
        "docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md")

    wb.add_assertion(
        name="atom_element_and_atlas_knot_do_not_share_a_markov_trace",
        computed=sum(1 for r in rows[:2] if not r["is_zero"]), expected=2,
        tolerance=0, unit="count",
        source=("Exact, symbolic in q, both in H_3, both convention D. A "
                "Markov invariant must agree on Markov-equivalent objects, so "
                "this settles the charitable reading of 'Same Markov class'."))
    wb.add_assertion(
        name="proton_and_neutron_elements_are_distinguished_by_rho",
        computed=0 if rows[2]["is_zero"] else 1, expected=1, tolerance=0,
        unit="bool",
        source=("They share an atlas knot, so Vol is shared; the p-n "
                "difference has to come from rho. It does."))
    out = wb.save()

    print(f"tr_M(Borromean braid) = {sp.factor(tr_bor)}\n")
    for r in rows:
        print(f"  {r['pair']:<38} zero? {r['is_zero']}")
        print(f"      {r['difference'][:100]}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
