#!/usr/bin/env python3
"""Why the two canonical tr_M(⁴He) producers disagree by 2.157x — measured.

Bean `qou-qu2w`. Two producers compute the H_3 nucleon traces the whole
closed-form mass/binding path is built on, and they disagree:

    habiro-coefficients-atomic.witness.json   tau_p 1.14576   tau_n 0.98774
    closed_form_tau_M.compute_tau_M_nucleon_H3      1.32159         1.25756

and (1.32159*1.25756)^2 / (1.14576*0.98774)^2 = 2.157, which is exactly the
gap between `habiro-coefficients-helium-4` (0.16097) and
`atomic-tr-m-helium4-canonical` (0.34716).

## It is NOT a convention question, and that is why it hid

  * The habiro atomic `tr_M_in_q` is RATIONAL in q with no half-powers, and
    the proton denominator factors as `4q^9 (q^2+1)^2` — the convention-D
    fingerprint. Both producers are convention D.
  * A=1 has NO p-n interface, so no `pn_convention` argument reaches this.
    `compute_tau_M_nucleon_H3` correctly takes none. That is precisely what
    concealed it: every audit keyed on `pn_convention` is blind here.
  * The ratio DIFFERS between proton (1.15346) and neutron (1.27316), so it
    is not a common normalisation factor either.

## Root cause: the legacy marshalling drops `d` on INTRA-nucleon crossings

`compute_tau_M_nucleon_H3` routes the nucleon chain through
`canonical_braid_marshalling.marshal_to_chi_lambda_braid`, whose own docstring
says it "emits signs and drops `d` entirely" and maps `averaged -> sign=+1`.

Each nucleon chain carries TWO `averaged` crossings — intra-nucleon, nothing
to do with a p-n interface:

    proton   {sigma: 6, averaged: 2, sigma_inv: 3}
    neutron  {sigma: 5, averaged: 2, sigma_inv: 4}

Flattening `averaged -> sigma` replaces that crossing's Markov factor
`z - h/2` by `z`, at two sites per nucleon.

That marshaller's stated defence — "Lossy, but equally lossy for both
variants, which is why the collapse is correct *here*" — is about `averaged`
vs `averaged_weighted`. It does NOT justify collapsing `averaged -> sigma`,
which is a different and larger loss.

## The three arms, and what each one guards

Rebuilt 2026-09-07 (bean `qou-o0pa`). All three run on the SAME canonical word,
so nothing here confounds `d`-dropping with intra ordering:

  * **d-preserving** -- `chi_all_lambda_any` over the word with `d` intact.
    Reproduces the habiro atomic target to ~1e-50.
  * **marshalled (current)** -- `compute_tau_M_nucleon_H3`, the PRODUCTION
    helper. It no longer marshals (`qou-qu2w` removed that), so its agreement
    with the d-preserving arm is a guard on production's ROUTING: it fires if
    anyone re-points production back through the lossy path.
  * **marshalled EXPLICIT** -- marshals on purpose, through
    `marshal_to_chi_lambda_braid` into `chi_lambda_braid`. This is what
    measures the loss the title names: 0.282 (p) and 0.126 (n) on the
    canonical word.

An earlier draft of this note called the probe "weaker than its title" and
"vacuous" once the production arm stopped marshalling. That OVERSTATED it in
one direction and understated the fix in the other. The production-agreement
check is a real regression guard -- it can fail, if production regresses -- it
simply cannot measure the size of the loss. The explicit arm restores that,
additively, without disturbing the guard.

Convention note, because getting it wrong is easy and silent:
`marshal_to_chi_lambda_braid` emits `[(sign, gen_1based)]` FOR
`hecke_characters.chi_lambda_braid`, NOT for the `chi_all_lambda*` family.
Feeding it to the wrong kernel raises `unsupported crossing c=-1.0`.

## What this probe proves

Running the SAME `Sum_lambda y_lambda * chi_lambda` over the SAME nucleon
chains, changing ONLY whether the crossing's `d` survives, reproduces the
habiro values to ~1e-50. So the two producers are not two conventions of one
object; one is computing the trace of a DIFFERENT Hecke element — the one
whose averaged crossings have been replaced by sigma.

The d-preserving path is `chi_general_word.chi_all_lambda_any` (the dispatcher;
it was `chi_monotone_transfer.chi_all_lambda` until 2026-09-07, when the chain
became the canonical NON-monotone word and the monotone-only kernel refused
it). The monotone transfer underneath is validated against `char_fast` at n=6
and four cached oracles to n=12, at 1e-50.

## What this probe does NOT do

It does not change `compute_tau_M_nucleon_H3`. That helper feeds 13 direct
importers and a 46-module `closed_form_tau_M` cone including
`mass_table_comprehensive` and `nucleus_sdp_assembly` — the canonical mass and
binding path. Re-pointing it moves every closed-form nucleon and atom trace in
the corpus, which is an owner decision, not an agent's.

Ref: `constit-factor-tau-M-proton-identity`
Ref: closed_form_tau_M.py (compute_tau_M_nucleon_H3)
Ref: canonical_braid_marshalling.py (marshal_to_chi_lambda_braid)
Ref: chi_monotone_transfer.py (chi_all_lambda, the d-preserving path)

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
import json  # noqa: E402
from collections import Counter  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(50)

import closed_form_tau_M as C  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
import canonical_braid_marshalling as MM  # noqa: E402
from hecke_characters import chi_lambda_braid  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from hecke_characters import partitions_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from canonical_braid_crossings import classify_crossing  # noqa: E402


def _habiro_atomic_targets(q_sym, q0_str):
    """tau_p / tau_n as the habiro atomic witness records them."""
    path = HERE.parent / "habiro" / "habiro-coefficients-atomic.witness.json"
    res = json.loads(path.read_text())["results"]
    out = {}
    for key, nuc in (("p (proton, A=1)", "p"), ("n (neutron, A=1)", "n")):
        expr = sp.sympify(res[key]["tr_M_in_q"], locals={"q": q_sym})
        out[nuc] = mp.mpf(
            str(sp.N(expr.subs(q_sym, sp.Float(q0_str, 50)), 50)))
    return out


def main() -> int:
    w = WitnessBuilder("nucleon-h3-marshalling-divergence",
                       engine="python+mpmath+sympy")
    w.set_description(
        "Root-causes the 2.157x disagreement between the two canonical "
        "tr_M(4He) producers (bean qou-qu2w). NOT a convention difference: "
        "both are convention D and A=1 has no p-n interface. "
        "compute_tau_M_nucleon_H3 marshals through marshal_to_chi_lambda_braid, "
        "which drops each nucleon's TWO intra-nucleon `averaged` crossings to "
        "plain sigma (z - h/2 -> z). Preserving `d` over the same chains "
        "reproduces the habiro atomic values to ~1e-50."
    )

    q_sym = sp.Symbol("q", positive=True, real=True)
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = C.hecke_h(q0)
    targets = _habiro_atomic_targets(q_sym, Q_50_DIGIT_STR)

    parts = [tuple(p) for p in partitions_of(3)]
    y = {p: y_lambda_wenzl_bridge_numeric(p, q0, 50) for p in parts}

    print("=" * 78)
    print("Nucleon H_3 trace: marshalled (d dropped) vs d-preserving")
    print("=" * 78)

    rows = []
    for nuc, (Z, N) in (("p", (1, 0)), ("n", (0, 1))):
        # `chain` comes from the ruling's own emitter, 2026-09-07 (bean
        # `qou-o0pa`). It used to be hand-built GROUPED out of the `hecke_core`
        # chains -- `[(c,d,0) for ... g0] + [(c,d,1) for ... g1]` -- while the
        # marshalled arm below was separately pinned to `grouped` to match. Both
        # halves of that arrangement were wrong once
        # `habiro-coefficients-atomic` was regenerated to the canonical ordering
        # in `a4909014a5`, and the probe failed its own assertions on `main`.
        #
        # The substitution is SAFE and that is measured, not assumed:
        # `atom_braid_word_3A` carries the SAME 11 crossings as
        # `g0 + g1` -- identical `(c, d)` multiset -- and therefore an identical
        # crossing census, which is what this probe's whole d-dropping argument
        # rests on:
        #
        #     p  same (c,d) multiset=True  census equal=True
        #        {'sigma': 6, 'averaged': 2, 'sigma_inv': 3}
        #     n  same (c,d) multiset=True  census equal=True
        #        {'sigma': 5, 'averaged': 2, 'sigma_inv': 4}
        #
        # Only the ORDER differs. Keeping the two arms on different orders made
        # the probe measure d-dropping CONFOUNDED with ordering -- the two
        # things it exists to separate.
        chain = list(atom_braid_word_3A(Z, N))
        census = Counter(classify_crossing(c, d, float(h)) for c, d, _ in chain)

        word = [(mp.mpf(str(c)), mp.mpf(str(d)), g) for c, d, g in chain]
        # The dispatcher, not `chi_monotone_transfer.chi_all_lambda`: the
        # canonical word is NON-monotone and the monotone-only transfer refuses
        # it outright ("non-monotone word: gen 0 after 1"). Same routing
        # `qou-cvky` applied to its 11 monotone-kernel callers. At H_3 the
        # general path is `d_lambda <= 2` and costs nothing.
        chi = chi_all_lambda_any(word, 3)
        preserving = mp.fsum([y[p] * chi.get(p, mp.mpf(0)) for p in parts])

        # `intra_order` UNPINNED, 2026-09-07 (bean `qou-o0pa`). The pin was
        # added 2026-09-06 reasoning that the borromean default "would swing
        # `marshalled` to 0.629/0.475 against a 1.146/0.988 target". That target
        # no longer exists: `habiro-coefficients-atomic.witness.json` was
        # regenerated to the canonical ordering in `a4909014a5`, the SAME
        # option-B commit the pin was reacting to. Measured against the live
        # target, the default matches to 50 digits and the pin misses by 82/108 %:
        #
        #     p  grouped    1.14575969245730087    rel 0.821
        #     p  borromean  0.629328402202921918   rel 6.37e-51
        #     n  grouped    0.987743688115809572   rel 1.08
        #     n  borromean  0.475133517155682213   rel 2.39e-50
        marshalled = C.compute_tau_M_nucleon_H3(nuc, q0, dps=50)
        target = targets[nuc]

        # THE EXPLICIT MARSHALLED ARM, restored 2026-09-07 (bean `qou-o0pa`).
        #
        # `marshalled` above calls the production helper, which no longer
        # marshals — `qou-qu2w` removed that — so its agreement with
        # `preserving` guards PRODUCTION's routing and cannot measure the loss
        # the title advertises. This arm marshals explicitly and does.
        #
        # The convention is the marshaller's own, checked in its source rather
        # than guessed: it emits `[(sign, gen_1based)]` FOR
        # `hecke_characters.chi_lambda_braid`, not for `chi_all_lambda*`.
        # Feeding it to the wrong kernel is what produced `unsupported crossing
        # c=-1.0` on a first attempt.
        mword = MM.marshal_to_chi_lambda_braid(chain, float(h))
        # float64-intentional: the marshaller takes float(h); this path measures that loss
        marshalled_explicit = mp.fsum(
            [y[pp] * mp.mpf(str(chi_lambda_braid(pp, mword, q0,
                                                 precision="mpfr_50dps")))
             for pp in parts])
        rel_lossy = abs(marshalled_explicit - target) / abs(target)

        rel_pres = abs(preserving - target) / abs(target)
        rel_marsh = abs(marshalled - target) / abs(target)

        print(f"\n  {nuc}: census = {dict(census)}")
        print(f"     marshalled EXPLICIT    {mp.nstr(marshalled_explicit, 18)}"  # float64-intentional: the lossy path, measured
              f"   rel vs habiro = {mp.nstr(rel_lossy, 3)}"
              f"   (ratio {mp.nstr(marshalled_explicit / preserving, 6)})")
        print(f"     d-preserving           {mp.nstr(preserving, 18)}"
              f"   rel vs habiro = {mp.nstr(rel_pres, 3)}")
        print(f"     habiro atomic (target) {mp.nstr(target, 18)}")
        print(f"     marshalled (current)   {mp.nstr(marshalled, 18)}"
              f"   rel vs habiro = {mp.nstr(rel_marsh, 3)}")

        rows.append({
            "nucleon": nuc,
            "census": dict(census),
            "n_averaged_intra_nucleon": census.get("averaged", 0),
            "d_preserving": str(preserving),
            "habiro_atomic_target": str(target),
            "marshalled_current": str(marshalled),
            "marshalled_explicit": str(marshalled_explicit),
            "rel_marshalled_explicit_vs_target": str(rel_lossy),
            "rel_d_preserving_vs_target": str(rel_pres),
            "rel_marshalled_vs_target": str(rel_marsh),
        })
        w.add_assertion(
            name=f"d_preserving_reproduces_habiro_{nuc}",
            computed=str(rel_pres),
            expected="0",
            tolerance="1e-45",
            source=("Same Sum y_l chi_l over the same nucleon chain; only "
                    "whether the crossing `d` survives differs. Reproducing "
                    "the habiro atomic value to this precision is what shows "
                    "the divergence is the marshalling, not a convention."),
        )

    pres = {r["nucleon"]: mp.mpf(r["d_preserving"]) for r in rows}
    marsh = {r["nucleon"]: mp.mpf(r["marshalled_current"]) for r in rows}
    he4_ratio = ((marsh["p"] * marsh["n"]) ** 2) / ((pres["p"] * pres["n"]) ** 2)
    print(f"\n  implied 4He ratio (Z=N=2): {mp.nstr(he4_ratio, 10)}")
    # Re-pointed 2026-09-06 (bean qou-y2o7). This asserted `== 2.157`, the
    # ratio between the BROKEN marshalled path and the correct d-preserving
    # one — i.e. it asserted the defect. `qou-qu2w` fixed that marshalling on
    # 2026-08-26, so the two paths have agreed and the ratio has been 1.0 ever
    # since; the assertion has been failing on success, and the committed
    # witness (2.1566, passed: true) predates the fix and has been an
    # unreproducible green for eleven days.
    #
    # The live check is now that the fix HOLDS. 2.157 is kept below as the
    # historical symptom, which is what it always was.
    # RESIDUAL against 0, not value against target: the verdict path
    # (qou_substrate/witness.py) compares float(computed) to float(expected),
    # so a value-vs-value form here could not resolve anything below the
    # float64 floor and the tolerance below it was unreachable by ~10^14.
    # A residual near zero IS representable as a float64 all the way down, so
    # the same tolerance is a real bound on it.
    # Gate: computations/audits/tolerance_below_arithmetic_floor_audit.py.
    w.add_assertion(
        name="qu2w_fix_holds_marshalled_equals_d_preserving",
        computed=mp.nstr(abs(he4_ratio - 1), 20),
        expected="0",
        tolerance="1e-30",
        source=("(tau_p*tau_n)^2 ratio between the two paths. Before the "
                "qou-qu2w fix this was 2.157, matching the independently "
                "observed 0.34716 / 0.16097 and closing the chain from root "
                "cause to reported symptom. It is 1.0 once the marshaller "
                "stops dropping `d`, and a drift away from 1.0 means that "
                "defect has returned."),
    )
    # The loss is REAL and this is what makes the probe test its own title
    # again: dropping `d` moves the trace by 28 % (p) and 13 % (n) on the
    # canonical word. If this ever fell to ~0 the marshaller would have stopped
    # being lossy, which would mean the `averaged -> sigma` collapse this probe
    # documents had silently changed.
    lossy = {r["nucleon"]: mp.mpf(r["marshalled_explicit"]) for r in rows}
    for nuc in ("p", "n"):
        w.add_assertion(
            name=f"explicit_marshalling_is_still_lossy_{nuc}",
            computed=str(abs(lossy[nuc] - pres[nuc]) / abs(pres[nuc])),
            expected="0.1",
            tolerance="0.2",
            source=("Marshalling explicitly through marshal_to_chi_lambda_braid "
                    "drops `d` on each nucleon's two `averaged` crossings. On "
                    "the canonical word that moves the trace by 0.282 (p) / "
                    "0.126 (n). A collapse toward 0 means the marshaller "
                    "stopped being lossy; a large jump means the crossing "
                    "census changed."),
        )
    w.add_data("historical_symptom_ratio_before_qu2w", "2.157")

    w.add_parameter("q_0", Q_50_DIGIT_STR)
    w.add_parameter("dps", 50)
    w.add_data("rows", rows)
    w.add_data("he4_implied_ratio", str(he4_ratio))
    w.add_data("root_cause", {
        "site": "closed_form_tau_M.compute_tau_M_nucleon_H3",
        "mechanism": ("routes the nucleon chain through "
                      "canonical_braid_marshalling.marshal_to_chi_lambda_braid, "
                      "which emits (sign, gen) and drops `d`; `averaged` maps "
                      "to sign=+1, replacing that crossing's Markov factor "
                      "z - h/2 by z at two sites per nucleon"),
        "not_a_convention_issue": ("both producers are convention D (the habiro "
                                   "tr_M_in_q is rational in q, proton "
                                   "denominator 4q^9(q^2+1)^2); A=1 has no p-n "
                                   "interface so no pn_convention argument "
                                   "reaches this site"),
        "why_it_hid": ("every audit keyed on `pn_convention` is structurally "
                       "blind here, and the ratio differs between p (1.15346) "
                       "and n (1.27316) so it does not look like a "
                       "normalisation factor either"),
        "available_fix": ("chi_monotone_transfer.chi_all_lambda preserves `d` "
                          "and is validated against char_fast at n=6 and four "
                          "cached oracles to n=12, all at 1e-50"),
        "blast_radius": ("13 direct importers of compute_tau_M_nucleon_H3; 46 "
                         "modules in the closed_form_tau_M cone, including "
                         "mass_table_comprehensive and nucleus_sdp_assembly — "
                         "the canonical mass and binding path"),
        "bean": "qou-qu2w",
    })
    w.add_caveat(
        "This probe MEASURES the divergence and does not resolve it. Deciding "
        "which path is canonical moves every closed-form nucleon and atom "
        "trace in the corpus and is an owner decision."
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
