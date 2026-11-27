#!/usr/bin/env python3
"""The "~7x uniform shortfall" in the extensive term is an ENERGY-SCALE artifact.

WHAT THIS OVERTURNS
-------------------
Three probes of mine reported that the framework's extensive (volume-term)
coefficient is short of the empirical binding by a uniform factor of about seven:

* `braid_nucleus_map_exponent_probe` (bean `qou-imcd`) — "shortfall vs B/A
  plateau 6.906x";
* `markov_normalisation_convention_span_probe` (bean `qou-78pt`) — "deficit
  6.0x-15.0x", concluding **A1 REFUTED**;
* `extensive_counter_family_probe` — "family max 5.663 MeV/nucleon, still 1.50x
  short", and for A1's own counter "6.0-8.0x".

All three multiplied a dimensionless log by **`m_e = 0.511 MeV`**. They gave no
reason for that choice, and it is the wrong one: the corpus's own binding
machinery uses the **hadronic energy unit**

    E_0 = m_e / (q_0 (q_0 - 1)) = 4.18598... MeV

declared in `computations/b_over_a_evaluator.py` and used as `alpha` in the
`B_sym` linear-chain derivation (`docs/audits/2026-06-16-b-sym-linear-chain-
closed-form.md`, "alpha = E_0 = m_e/(q_0(q_0-1)) (CAL-1)"). It is larger than
`m_e` by

    E_0 / m_e = 1 / (q_0 (q_0 - 1)) = 8.1917611722...

and 8.19 is, to within the log ratio, the entire reported shortfall. **The
deficit was never a measurement. It was a units choice.**

THE UNRECONCILED NUMBER, RECONCILED
-----------------------------------
`markov_normalisation_convention_span_probe` recorded an open discrepancy: the
ROAST (`docs/audits/2026-08-07-l2-attack-options-ROAST.md` §A1) reports "the N=2
reading gives ~2.91 MeV/strand" where every member of my family gave 0.355-0.472.
I wrote that the ROAST "does not show its construction and this probe does not
reconstruct it".

It does show its construction, one sentence earlier: *"if a nucleon is one strand
the extensive coefficient is `E_0 log N`"*. At `N = 2`,

    2.91 / E_0 = 0.695176...   vs   ln 2 = 0.693147...   [assertion 1]

to 0.3 %, while at `m_e` the figure is UNREACHABLE — it would need a
normaliser with `log = 5.695`, against a family spanning 0.694-0.923
[assertion 1b].

The ROAST was using `E_0`; I was using `m_e`; the ratio 8.19 is the whole
discrepancy. Nothing about the ROAST's arithmetic was unreconstructable.

WHAT THE CORRECTED NUMBERS ARE
------------------------------
At `E_0`, with the corpus's 3 strands per nucleon, the normaliser family gives

    8.721 ... 11.596 MeV/nucleon

against a `B/A` plateau of 8.5 and `a_V ~ 15.8`. So **every member of the family
now exceeds the plateau** [assertion 3], and against `a_V` the deficit is
**1.36x-1.81x**, not 6x-15x.

CONSEQUENCE FOR `qou-78pt`: A1 IS NOT REFUTED, AND THE ROAST WAS RIGHT
---------------------------------------------------------------------
`qou-78pt` concluded A1 was refuted rather than unfalsifiable, on the argument
that the convention family spans only 1.33x while the deficit is 6-15x — "two
orders of magnitude too small to be the thing that closes the gap". At `E_0` the
deficit against `a_V` is 1.36x-1.81x and the span is 1.33x. **The span is now the
same size as the gap**, which is exactly the condition under which choosing a
member becomes a fit. That is the ROAST's original charge, and it stands:

    "Choosing the member that lands on a_V ~ 15.6 IS a fit, and it is a fit with
     a free continuous parameter dressed as a structural insight."

My refutation of A1 worked only because I had shrunk the family by 8.19x with an
unjustified scale. Withdrawn.

WHAT THIS PROBE DOES *NOT* CLAIM
--------------------------------
That `E_0` is the correct scale. It is the corpus's, the ROAST's, and the `B_sym`
chain's; `m_e` was mine and is the outlier. But neither is derived *for this
quantity* — the Markov normaliser is a dimensionless partition function and
nothing in the framework says which energy converts its logarithm to MeV. The
finding is that **the shortfall figure is not stable under a choice the corpus
has not pinned, and moves by 8.19x between two scales both in current use**, so
no "Nx short" claim about the extensive term means anything until that is fixed.
That is the ROAST's convention complaint, one level up, and I walked into it.

Usage:
    python3 computations/probes/extensive_term_energy_scale_reconciliation_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from b_over_a_evaluator import E_0_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

M_E_MEV = mp.mpf("0.51099895069")
STRANDS_PER_NUCLEON = 3
B_OVER_A_PLATEAU = mp.mpf("8.5")
SEMF_A_V = mp.mpf("15.8")

# The ROAST's published figure, quoted from the document, not recomputed.
ROAST_MEV_PER_STRAND = mp.mpf("2.91")


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    w = WitnessBuilder("extensive-term-energy-scale-reconciliation-probe")
    w.set_description(
        "The ~7x uniform shortfall three of my probes reported for the extensive term is "
        "the ratio E_0/m_e = 1/(q_0(q_0-1)) = 8.19, not a physical deficit. Reconstructs "
        "the ROAST's previously-unreconciled 2.91 MeV/strand as E_0 ln 2, and withdraws "
        "qou-78pt's refutation of A1."
    )

    # `E_0` rebuilt at 40 dps. NOT asserted against the imported `E_0_MEV`: that
    # module computes the same closed form from the same `q_0`, so the comparison
    # would be tautological in the sense of bean `qou-l81w`. Both are recorded as
    # data below instead, which is what a provenance check should look like.
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0_closed = _qbeta_e0.order_zero_scaled(M_E_MEV, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    # ---- assertion 1: dividing the ROAST's figure by E_0 gives ln 2 ---------
    # INDEPENDENT side: 2.91 is published in an audit written before this probe
    # existed. Stated as a ratio rather than as `E_0 ln 2 == 2.91`, because
    # E_0 ln 2 = 2.90150 and the quote is "~2.91" — 0.3 % apart, which is inside
    # the "~" but outside the quote's own 3-figure rounding. The ratio form says
    # exactly what is established: the figure is E_0-scaled, and what it divides
    # to is a normaliser logarithm.
    e0_ln2 = e0_closed * mp.log(2)
    w.add_assertion(
        "roast_figure_divided_by_E0_is_ln2",
        computed=mp.nstr(ROAST_MEV_PER_STRAND / e0_closed, 8),
        expected=mp.nstr(mp.log(2), 8),
        tolerance="3e-3",
        source="the '~2.91 MeV/strand' published in "
               "docs/audits/2026-08-07-l2-attack-options-ROAST.md line 85, divided by "
               "E_0 = m_e/(q_0(q_0-1)), vs ln 2 — the ROAST's own preceding sentence gives "
               "the construction 'the extensive coefficient is E_0 log N', at N = 2",
    )

    # ---- the family, at both scales ----------------------------------------
    family = {
        "[2]_q = q + 1/q": q + 1 / q,
        "[2]_Q = 1 + q^2": 1 + q ** 2,
        "kauffman q^(1/2)+q^(-1/2)": mp.sqrt(q) + 1 / mp.sqrt(q),
        "1 + q^4": 1 + q ** 4,
    }
    rows, at_e0 = [], []
    for name, delta in family.items():
        lg = mp.log(delta)
        per_nuc_me = lg * M_E_MEV * STRANDS_PER_NUCLEON
        per_nuc_e0 = lg * e0_closed * STRANDS_PER_NUCLEON
        at_e0.append(per_nuc_e0)
        rows.append({
            "normaliser": name,
            "log_loop_value": mp.nstr(lg, 12),
            "MeV_per_nucleon_at_m_e": mp.nstr(per_nuc_me, 10),
            "MeV_per_nucleon_at_E_0": mp.nstr(per_nuc_e0, 10),
        })
    lo_e0, hi_e0 = min(at_e0), max(at_e0)

    # ---- assertion 1b: at m_e the ROAST's figure is UNREACHABLE -------------
    # This is what makes the reconciliation decisive rather than suggestive.
    # Dividing 2.91 by m_e gives 5.6947, and every loop value the framework
    # offers has a logarithm in [0.6945, 0.9234]. So no normaliser whatsoever
    # produces the ROAST's number at the m_e scale — the scale must be E_0, and
    # my probes' silent choice of m_e is what made the figure look unreachable.
    logs = [mp.log(d) for d in family.values()]
    roast_over_me = ROAST_MEV_PER_STRAND / M_E_MEV
    unreachable_at_me = roast_over_me < min(logs) or roast_over_me > max(logs)
    w.add_assertion(
        "roast_figure_is_unreachable_at_the_m_e_scale",
        computed="1" if unreachable_at_me else "0",
        expected="1",
        source=f"2.91/m_e = {mp.nstr(roast_over_me, 8)} against the full range of normaliser "
               f"logarithms the framework offers, [{mp.nstr(min(logs), 8)}, "
               f"{mp.nstr(max(logs), 8)}] — no member comes within a factor of six",
    )

    # ---- assertion 2: the historical shortfall is exactly the scale ratio ----
    # The `expected` side is read out of a witness JSON committed BEFORE this
    # probe existed, not recomputed here. This checks that the published 6.9056x
    # is accounted for by the scale choice ALONE — i.e. that no second error is
    # hiding underneath it.
    prior = json.loads(
        (HERE / "braid-nucleus-map-exponent-probe.witness.json").read_text()
    )
    prior_shortfall = mp.mpf(prior["data"]["plateau_shortfall"]["shortfall_vs_plateau"])
    strands_at_e0 = STRANDS_PER_NUCLEON * mp.log(1 + q ** 2) * e0_closed
    shortfall_at_e0 = B_OVER_A_PLATEAU / strands_at_e0
    w.add_assertion(
        "prior_published_shortfall_is_accounted_for_by_the_scale_ratio_alone",
        computed=mp.nstr(prior_shortfall / shortfall_at_e0, 12),
        expected=mp.nstr(e0_closed / M_E_MEV, 12),
        tolerance="1e-7",
        source="the '6.9056498' recorded in computations/probes/"
               "braid-nucleus-map-exponent-probe.witness.json — produced by a different "
               "script and read from disk here, not recomputed — divided by the same "
               "shortfall recomputed at E_0, vs "
               "E_0/m_e = 1/(q_0(q_0-1)). Equality means the scale choice is the WHOLE of "
               "the discrepancy and nothing else went wrong.",
    )

    # ---- assertion 3: at E_0 the whole family clears the plateau ------------
    # INDEPENDENT side: the empirical B/A plateau is nuclear data, not a corpus
    # quantity. At m_e the same family sat a factor of 6-8 BELOW it, which is
    # what made qou-78pt read as a refutation.
    w.add_assertion(
        "at_E0_every_family_member_exceeds_B_over_A_plateau",
        computed="1" if lo_e0 > B_OVER_A_PLATEAU else "0",
        expected="1",
        source=f"family minimum at E_0 is {mp.nstr(lo_e0, 8)} MeV/nucleon vs the empirical "
               f"B/A plateau {B_OVER_A_PLATEAU} MeV/nucleon (independent: nuclear data). "
               f"At m_e the same minimum was {mp.nstr(lo_e0 * M_E_MEV / e0_closed, 8)}.",
    )

    w.add_parameter("q0", mp.nstr(q, 30))
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("E_0_MeV", mp.nstr(e0_closed, 25))
    w.add_parameter("strands_per_nucleon", STRANDS_PER_NUCLEON)

    w.add_data("scale_ratio", {
        "E_0_over_m_e": mp.nstr(e0_closed / M_E_MEV, 20),
        "closed_form": "1 / (q_0 (q_0 - 1))",
        "E_0_rebuilt_here_40dps": mp.nstr(e0_closed, 25),
        "E_0_as_imported_from_b_over_a_evaluator": mp.nstr(E_0_MEV, 25),
        "name_collision_WARNING": (
            "`E0_MEV` in computations/atom_mass_derived.py is a DIFFERENT constant: "
            "m_p / tr_M(proton) = 1662.7295... MeV, larger by a factor 397.21. Two "
            "unrelated quantities share the name E_0 in this corpus. The one relevant "
            "here is b_over_a_evaluator's hadronic energy unit; atom_mass_derived's "
            "belongs to the absolute-mass chain excised on 2026-08-11 (bean qou-exam)."
        ),
        "where_E_0_is_used": [
            "computations/b_over_a_evaluator.py — 'Hadronic energy unit', the scale of "
            "every B/A prediction in that module",
            "docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md — 'alpha = E_0 = "
            "m_e/(q_0(q_0-1)) (CAL-1)', the B_sym linear-chain per-bond constants",
            "docs/audits/2026-08-07-l2-attack-options-ROAST.md §A1 — 'E_0 log N'",
        ],
        "where_m_e_was_used": [
            "computations/probes/braid_nucleus_map_exponent_probe.py",
            "computations/probes/markov_normalisation_convention_span_probe.py",
            "computations/probes/extensive_counter_family_probe.py",
        ],
        "note": "All three m_e users are mine, written this session, and none of them gave "
                "a reason for the choice. E_0 is the corpus's; m_e is the outlier.",
    })

    w.add_data("two_E0_scaled_candidates_for_the_ROAST_figure", {
        "E_0 * ln 2": mp.nstr(e0_ln2, 10),
        "b_pp from the B_sym linear chain": "2.91 (docs/audits/2026-06-16-b-sym-linear-"
                                            "chain-closed-form.md, 'b_pp = 2.91, b_pn = 3.89, "
                                            "b_nn = 5.18', with the SAME alpha = E_0)",
        "residual_of_the_first": mp.nstr(abs(e0_ln2 - ROAST_MEV_PER_STRAND), 6)
                                 + " MeV (0.29 %)",
        "which_one_the_ROAST_used": (
            "NOT DETERMINED. Its own sentence gives 'E_0 log N', which is the first; but "
            "the first evaluates to 2.9015 and the ROAST wrote 2.91, which is the second "
            "to all three figures. The documents do not distinguish them and this probe "
            "does not guess. It does not matter for the finding: both are E_0-scaled, and "
            "the energy scale is the entire discrepancy."
        ),
        "per_bond_vs_per_strand": (
            "Worth flagging either way: b_pp is a PER-BOND constant in a chain with (A-1) "
            "bonds, and the ROAST labels its figure 'MeV/strand' and multiplies by 3 "
            "strands/nucleon. If the ROAST did take b_pp, the label is wrong and the "
            "multiplication is too."
        ),
    })

    w.add_data("family_at_both_scales", rows)
    w.add_data("corrected_deficits", {
        "family_range_at_E_0_MeV_per_nucleon":
            f"{mp.nstr(lo_e0, 8)} .. {mp.nstr(hi_e0, 8)}",
        "vs_B_over_A_plateau":
            f"{mp.nstr(lo_e0 / B_OVER_A_PLATEAU, 6)}x .. {mp.nstr(hi_e0 / B_OVER_A_PLATEAU, 6)}x OVER",
        "vs_a_V":
            f"{mp.nstr(SEMF_A_V / hi_e0, 6)}x .. {mp.nstr(SEMF_A_V / lo_e0, 6)}x short",
        "previously_reported_at_m_e": "6.0x .. 15.0x short",
        "span_of_the_convention_family": mp.nstr(hi_e0 / lo_e0, 6),
    })

    w.add_data("withdrawn", {
        "qou-78pt verdict": (
            "WITHDRAWN. 'A1 REFUTED, not unfitted' rested on the family span (1.33x) being "
            "two orders of magnitude smaller than the deficit (6-15x). At E_0 the deficit "
            "against a_V is 1.36-1.81x and the span is 1.33x -- the same size. That is "
            "precisely the condition under which picking a member is a fit, which is what "
            "the ROAST charged in the first place. A1 returns to UNFALSIFIABLE AS WRITTEN."
        ),
        "qou-imcd shortfall figure": (
            "The exponent test itself is unaffected -- it is scale-free, since a constant "
            "multiplier cannot change a log-log slope, and log Z(3A) is still exactly "
            "linear in A. Only the reported '6.906x' residual is withdrawn."
        ),
        "extensive_counter_family_probe": (
            "Its counter measurements (bonds A-1, averaged 2A+1, strands 3A, letters 12A-1, "
            "all exactly linear) stand. Every MeV figure in it is at m_e and must be "
            "multiplied by 8.1917611722."
        ),
    })

    w.add_data("what_is_NOT_claimed", (
        "That E_0 is the correct scale for this quantity. The Markov normaliser is a "
        "dimensionless partition function and nothing in the framework derives which energy "
        "converts its logarithm to MeV; E_0 itself is CAL-1, a calibration. The finding is "
        "that the shortfall moves by 8.19x between two scales both in current corpus use, so "
        "no 'Nx short' claim about the extensive term is meaningful until the scale is pinned "
        "from the axioms -- the same demand the ROAST made of the normalisation convention, "
        "one level up."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  E_0 = m_e/(q0(q0-1))              : {mp.nstr(e0_closed, 12)} MeV")
    print(f"  E_0 / m_e                         : {mp.nstr(e0_closed / M_E_MEV, 12)}")
    print(f"  E_0 * ln 2   (ROAST says ~2.91)   : {mp.nstr(e0_ln2, 8)} MeV/strand  -- RECONCILED")
    print(f"  family at E_0 (3 strands/nucleon) : {mp.nstr(lo_e0, 6)} .. {mp.nstr(hi_e0, 6)} MeV/nucleon")
    print(f"  vs B/A plateau 8.5                : {mp.nstr(lo_e0 / B_OVER_A_PLATEAU, 5)}x .. "
          f"{mp.nstr(hi_e0 / B_OVER_A_PLATEAU, 5)}x OVER  (was 6-8x short at m_e)")
    print(f"  vs a_V 15.8                       : {mp.nstr(SEMF_A_V / hi_e0, 5)}x .. "
          f"{mp.nstr(SEMF_A_V / lo_e0, 5)}x short (was 11-15x at m_e)")
    print(f"  family span                       : {mp.nstr(hi_e0 / lo_e0, 5)}x  "
          f"-- now the SAME SIZE as the deficit, so qou-78pt's refutation is withdrawn")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
