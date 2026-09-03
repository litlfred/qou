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

## What this probe proves

Running the SAME `Sum_lambda y_lambda * chi_lambda` over the SAME nucleon
chains, changing ONLY whether the crossing's `d` survives, reproduces the
habiro values to ~1e-50. So the two producers are not two conventions of one
object; one is computing the trace of a DIFFERENT Hecke element — the one
whose averaged crossings have been replaced by sigma.

The d-preserving path is `chi_monotone_transfer.chi_all_lambda`, itself
validated against `char_fast` at n=6 and four cached oracles to n=12, at 1e-50.

## What this probe does NOT do

It does not change `compute_tau_M_nucleon_H3`. That helper feeds 13 direct
importers and a 46-module `closed_form_tau_M` cone including
`mass_table_comprehensive` and `nucleus_sdp_assembly` — the canonical mass and
binding path. Re-pointing it moves every closed-form nucleon and atom trace in
the corpus, which is an owner decision, not an agent's.

Ref: prop:constit-factor-tau-M-proton-identity
Ref: closed_form_tau_M.py (compute_tau_M_nucleon_H3)
Ref: canonical_braid_marshalling.py (marshal_to_chi_lambda_braid)
Ref: chi_monotone_transfer.py (chi_all_lambda, the d-preserving path)
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
import chi_monotone_transfer as T  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from hecke_characters import partitions_of  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
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
    for nuc, (g0, g1) in (("p", (_PROTON_G0, _PROTON_G1)),
                          ("n", (_NEUTRON_G0, _NEUTRON_G1))):
        chain = [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]
        census = Counter(classify_crossing(c, d, float(h)) for c, d, _ in chain)

        word = [(mp.mpf(str(c)), mp.mpf(str(d)), g) for c, d, g in chain]
        chi = T.chi_all_lambda(word, 3)
        preserving = mp.fsum([y[p] * chi.get(p, mp.mpf(0)) for p in parts])

        marshalled = C.compute_tau_M_nucleon_H3(nuc, q0, dps=50)
        target = targets[nuc]

        rel_pres = abs(preserving - target) / abs(target)
        rel_marsh = abs(marshalled - target) / abs(target)

        print(f"\n  {nuc}: census = {dict(census)}")
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
    w.add_assertion(
        name="he4_ratio_matches_the_observed_2p157",
        computed=str(he4_ratio),
        expected="2.157",
        tolerance="1e-3",
        source=("(tau_p*tau_n)^2 ratio between the two paths. Matching the "
                "independently-observed 0.34716 / 0.16097 = 2.157 closes the "
                "chain from root cause to the reported symptom."),
    )

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
