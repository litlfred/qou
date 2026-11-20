#!/usr/bin/env python3
"""Which bar-even `E` closes the bar-odd p-n repair -- and what fails to pick one.

# The question, and why the answer reshapes it

`pnWeighted_barEven_iff` (PR #5769) gives the criterion: the weighted p-n
interface factor `f_pn = z - (1/2 - eps)*h` is q-bar-even iff the offset
`eps` is bar-ODD. The canonical bring_color_weighted offset `eps = delta/4`
is not, because `bar delta = -q^2 * delta` -- bar-odd only up to weight.

Absorbing that weight gives the obvious repair class

    eps = q * delta * E / 4,    E bar-even

which is bar-odd for EVERY such E (`weightForm_barOdd`, sorry-free). So the
criterion selects nothing inside the class, and the question became "which E?".

This probe asks what else could narrow it. The finding is that nothing in the
corpus does, and that the frame is narrower than it looks:

  * Requiring E regular at q = 1 forces `eps = O((q-1)^3)`, because delta
    itself vanishes to third order. Every regular-E repair therefore keeps
    f_pn within O((q-1)^3) of the strict average -- the same size as the
    canonical convention it replaces.

  * The one OTHER structurally-derived bar-even p-n factor is the GEOMETRIC
    mean of the bar orbit, `sqrt(f_pp * f_nn) = z/q^2`. Its offset is
    O(q - 1): a hundred times larger than the canonical one and of the
    opposite sign. By the previous point no regular E reaches it; the
    required E carries a double pole at q = 1.

So "which bar-even E?" cannot be answered from the criterion, and the two
candidates the bond structure actually supplies are not both inside the frame.

# What is checked here

Four candidate narrowing constraints, each measured rather than asserted:

    C1  confluence f_pn(1) = f_pp(1)          -> holds for every regular E
    C2  convex bond weights |eps| <= 1/2      -> bounds |E(q0)| by ~1e3
    C3  Markov bond form f_pn = z + d         -> holds for every eps
    C4  cubic order of vanishing at q = 1     -> holds for every regular E

All four are vacuous as selectors. C2 is a bound and C1/C3/C4 are satisfied
identically, so none of them distinguishes one bar-even E from another.

# What is NOT done here

No E is selected. An offset fitted to an isotope anchor would be a fit, not a
derivation, and the anti-fit discipline applies unchanged (AGENTS.md
"Axiomatization is NOT a Proof", the Delta_lambda "no seventh fit-based
ansatz" rule). The productive question this leaves is the prior one -- whether
the p-n bond interpolates its neighbours ARITHMETICALLY (the Markov trace is
linear in the bond element) or GEOMETRICALLY (the closed form is a product
over bonds). That has a structural route and is left open.

Lean: `QOU.MassTheory.PnOffset` (12 declarations, sorry-free).
Bean qou-cblw section 3. Owner authorisation 2026-08-26 ("1y").
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE.parent, _HERE.parent / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from closed_form_tau_M import markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

DPS = 60


def _bar_even_candidates():
    """Bar-even E's, each with its bar image computed independently.

    `regular` records whether E is finite at q = 1 -- the property that C4
    turns into a constraint on the reachable offsets.
    """
    return [
        ("E = 1", lambda q: mp.mpf(1), True),
        ("E = [2]_q / 2", lambda q: (q + 1 / q) / 2, True),
        ("E = 2 / [2]_q", lambda q: 2 / (q + 1 / q), True),
        ("E = ([2]_q / 2)^2", lambda q: ((q + 1 / q) / 2) ** 2, True),
        ("E = -6q^3/((q-1)^2 (q^2+1)^2)  [reaches the geometric mean]",
         lambda q: -6 * q ** 3 / ((q - 1) ** 2 * (q ** 2 + 1) ** 2), False),
    ]


def _eps_weight_form(q, E):
    return q * flavor_split_leading(q) * E(q) / 4


def _f_pn(q, eps):
    return markov_z(q) - (mp.mpf(1) / 2 - eps) * hecke_h(q)


def main() -> int:
    _started = time.monotonic()
    mp.dps = DPS
    # `q_parameter.Q` is a float64 and would cap every figure below at 17
    # significant digits; the 50-digit anchor is what the corpus computes at.
    q = Q_MP
    z, h, delta = markov_z(q), hecke_h(q), flavor_split_leading(q)

    w = WitnessBuilder("pn-offset-bar-odd-class", engine="mpmath",
                       output_dir=_HERE, start_time=_started)
    w.set_description(
        "The bar-odd repair class eps = q*delta*E/4 (E bar-even) is closed "
        "under every bar-even E, and four candidate narrowing constraints "
        "-- confluence, convex weights, the Markov bond form, and the cubic "
        "order of vanishing -- are each vacuous as selectors. Regular E "
        "confines the offset to O((q-1)^3); the geometric mean of the bar "
        "orbit, z/q^2, is O(q-1) and needs a double pole, so it is outside "
        "the class. No E is selected: that would be a fit."
    )
    w.set_content_block("prop:pn-averaging-uniqueness")
    w.add_parameter("q0Anchor", "proton")
    w.add_parameter("q0", mp.nstr(q, 50))
    w.add_parameter("dps", str(DPS))

    print(f"q0    = {mp.nstr(q, 30)}")
    print(f"z     = {mp.nstr(z, 30)}")
    print(f"h     = {mp.nstr(h, 30)}")
    print(f"delta = {mp.nstr(delta, 30)}\n")

    # --- anchors: the two reference constants of the source sweep -----------
    # Recomputed here from the definitions, independently of the producers the
    # sweep keyed on. Agreement is a cross-check of the sweep's anchors.
    f_strict = _f_pn(q, mp.mpf(0))
    f_canon = _f_pn(q, delta / 4)
    w.add_assertion("f_pn_strict_averaged", mp.nstr(f_strict, 15),
                    "0.508157887748646",
                    source="the sweep's BLIND_KEY, recomputed from z and h "
                           "rather than read from a producer")
    w.add_assertion("f_pn_bring_color_weighted", mp.nstr(f_canon, 15),
                    "0.508229789376739",
                    source="the sweep's CANON_KEY, likewise")

    # --- the class is closed under every bar-even E ------------------------
    print("--- bar-oddness of eps = q*delta*E/4, for each bar-even E ---")
    worst_odd = mp.mpf(0)
    for name, E, regular in _bar_even_candidates():
        assert abs(E(1 / q) - E(q)) < mp.mpf("1e-45"), f"{name} is not bar-even"
        eps = _eps_weight_form(q, E)
        # bar(eps) computed by substituting q -> 1/q throughout, NOT by
        # applying the identity being tested.
        eps_bar = (1 / q) * flavor_split_leading(1 / q) * E(1 / q) / 4
        defect = abs(eps_bar + eps)
        worst_odd = max(worst_odd, defect)
        print(f"  {name:56s} eps={mp.nstr(eps, 12):>16}  |bar(eps)+eps|={mp.nstr(defect, 3)}")
    w.add_assertion("weight_form_bar_odd_worst_defect", mp.nstr(worst_odd, 6), "0",
                    tolerance="1e-45",
                    source="every bar-even E gives a bar-odd offset; the "
                           "criterion selects nothing inside the class")

    # --- C1  confluence at q = 1 -------------------------------------------
    print("\n--- C1: confluence f_pn(1) = f_pp(1) ---")
    # AT q = 1, not near it. h(1) = 0 and delta(1) = 0, so f_pn(1) = z(1)
    # for every regular E. An earlier revision measured the gap at
    # q = 1 + 1e-25 and asserted it against zero; that gap is
    # -(1/2 - eps)*h ~ -(q-1), i.e. 1e-25, so the test was measuring the
    # offset it had introduced, not a confluence failure.
    one = mp.mpf(1)
    worst_conf = mp.mpf(0)
    for name, E, regular in _bar_even_candidates():
        if not regular:
            continue
        gap = abs(_f_pn(one, _eps_weight_form(one, E)) - markov_z(one))
        worst_conf = max(worst_conf, gap)
        print(f"  {name:56s} |f_pn - f_pp| at q=1 exactly: {mp.nstr(gap, 3)}")
    # And the approach is linear in (q-1), with slope -1/2 * h'(1) = -1:
    qn = mp.mpf(1) + mp.mpf("1e-25")
    slope = (_f_pn(qn, _eps_weight_form(qn, lambda _q: mp.mpf(1))) - markov_z(qn)) / (qn - 1)
    print(f"  approach slope d(f_pn - f_pp)/d(q-1) at E=1: {mp.nstr(slope, 8)}")
    w.add_assertion("C1_confluence_worst_gap", mp.nstr(worst_conf, 6), "0",
                    tolerance="1e-50",
                    source="C1 holds identically at q = 1 for every regular E -- "
                           "vacuous as a selector")
    w.add_assertion("C1_approach_slope", mp.nstr(slope, 8), "-1.0",
                    tolerance="1e-6",
                    source="f_pn - f_pp = -(1/2 - eps)h and h ~ 2(q-1), so the "
                           "gap vanishes linearly with slope -1; recorded because "
                           "mistaking this slope for a confluence failure is what "
                           "the earlier revision of this check did")

    # --- C2  convex bond weights |eps| <= 1/2 ------------------------------
    print("\n--- C2: convex weights |eps| <= 1/2 ---")
    scale = q * delta / 4                      # eps = scale * E(q0)
    e_bound = (mp.mpf(1) / 2) / scale
    print(f"  eps = {mp.nstr(scale, 12)} * E(q0)  =>  |E(q0)| <= {mp.nstr(e_bound, 8)}")
    for name, E, regular in _bar_even_candidates():
        print(f"  {name:56s} |E(q0)| = {mp.nstr(abs(E(q)), 8)}")
    # Assert the IDENTITY that defines the bound, not a number typed by hand.
    # An earlier revision asserted "1453.6" against a measured 1309.7495 -- a
    # guessed expected value, which is the failure mode the anti-fit discipline
    # exists to catch even when the quantity is this innocuous.
    w.add_assertion("C2_bound_times_scale_is_one_half",
                    mp.nstr(e_bound * scale, 6), "0.5", tolerance="1e-50",
                    source="|eps| <= 1/2 with eps = scale*E(q0) means the bound on "
                           "|E(q0)| is exactly (1/2)/scale = 2/(q0*delta)")
    w.add_assertion("C2_excludes_no_candidate",
                    str(all(abs(E(q)) < e_bound for _n, E, _r in _bar_even_candidates())),
                    "True",
                    source=f"the bound is |E(q0)| <= {mp.nstr(e_bound, 8)}; the "
                           "largest candidate here is 136, so C2 excludes none of "
                           "them -- it is a sanity bound, not a selector")

    # --- C3  Markov bond form ----------------------------------------------
    print("\n--- C3: Markov bond form f_pn = z + d, d = -(1/2 - eps)h ---")
    worst_bond = mp.mpf(0)
    for eps_test in [mp.mpf(0), delta / 4, mp.mpf("-0.3"), mp.mpf("0.47")]:
        d = -(mp.mpf(1) / 2 - eps_test) * h
        worst_bond = max(worst_bond, abs(_f_pn(q, eps_test) - (z + d)))
    print(f"  worst |f_pn - (z + d)| over four arbitrary eps: {mp.nstr(worst_bond, 3)}")
    w.add_assertion("C3_bond_form_worst_residual", mp.nstr(worst_bond, 6), "0",
                    tolerance="1e-50",
                    source="every eps yields a valid bond constant -- C3 is an "
                           "identity, not a constraint")

    # --- C4  cubic order of vanishing --------------------------------------
    # eps/(q-1)^3 tends to a finite limit for regular E and diverges otherwise.
    print("\n--- C4: order of vanishing of eps at q = 1 ---")
    ratios = {}
    for name, E, regular in _bar_even_candidates():
        vals = []
        for k in (10, 15, 20):
            qk = mp.mpf(1) + mp.mpf(10) ** (-k)
            vals.append(_eps_weight_form(qk, E) / (qk - 1) ** 3)
        spread = abs(vals[-1] - vals[0])
        ratios[name] = (mp.nstr(vals[-1], 10), regular)
        verdict = "finite (cubic)" if regular else "DIVERGES (pole)"
        print(f"  {name:56s} eps/(q-1)^3 -> {mp.nstr(vals[-1], 10):>18}  {verdict}"
              f"  spread={mp.nstr(spread, 3)}")
    # The regular ones all converge to delta's own leading coefficient times E(1).
    lim_E1 = mp.mpf(ratios["E = 1"][0])
    w.add_assertion("C4_cubic_limit_for_E_eq_1", mp.nstr(lim_E1, 8), "0.3333333",
                    tolerance="1e-5",
                    source="delta = (q-1)^3 (q+1)(q^2+1)/(3q^4), so eps/(q-1)^3 "
                           "-> 4/12 = 1/3 at E = 1; finite, hence O((q-1)^3)")
    div = mp.mpf(ratios["E = -6q^3/((q-1)^2 (q^2+1)^2)  [reaches the geometric mean]"][0])
    w.add_assertion("C4_geometric_E_diverges", str(abs(div) > mp.mpf("1e30")), "True",
                    source="the geometric-mean E has a double pole, so its offset "
                           "is O(q-1), not O((q-1)^3): outside the regular class")

    # --- the geometric-mean candidate --------------------------------------
    print("\n--- the second derived bar-even factor: geometric mean of the bar orbit ---")
    f_pp, f_nn = z, z - h
    geom = mp.sqrt(f_pp * f_nn)
    eps_geom = -(q ** 2 - 1) / (2 * (q ** 2 + 1))
    print(f"  f_pp = z            = {mp.nstr(f_pp, 20)}")
    print(f"  f_nn = z - h        = {mp.nstr(f_nn, 20)}")
    print(f"  arithmetic mean     = {mp.nstr((f_pp + f_nn) / 2, 20)}   (eps = 0)")
    print(f"  geometric mean      = {mp.nstr(geom, 20)}   (eps = {mp.nstr(eps_geom, 12)})")
    print(f"  z/q^2               = {mp.nstr(z / q ** 2, 20)}")
    w.add_assertion("geometric_mean_eq_z_over_q2", mp.nstr(abs(geom - z / q ** 2), 6),
                    "0", tolerance="1e-50",
                    source="sqrt(z * bar z) = z/q^2 because bar z = z/q^4")
    w.add_assertion("geometric_mean_realised_by_eps",
                    mp.nstr(abs(_f_pn(q, eps_geom) - geom), 6), "0",
                    tolerance="1e-50",
                    source="the geometric mean is an admissible convex bond")
    w.add_assertion("geometric_eps_bar_odd",
                    mp.nstr(abs(-((1 / q) ** 2 - 1) / (2 * ((1 / q) ** 2 + 1)) + eps_geom), 6),
                    "0", tolerance="1e-50",
                    source="so it satisfies the criterion, like the strict average")
    # Both means are convex combinations, so both are physically admissible bonds.
    w_pp_geom = mp.mpf(1) / 2 + eps_geom
    w.add_assertion("geometric_weights_are_convex",
                    str(mp.mpf(0) <= w_pp_geom <= mp.mpf(1)), "True",
                    source=f"weights (p-p, n-n) = ({mp.nstr(w_pp_geom, 8)}, "
                           f"{mp.nstr(1 - w_pp_geom, 8)}) -- a genuine bond, not "
                           "a formal solution")

    ratio = abs(eps_geom / (delta / 4))
    print(f"\n  |eps_geometric / eps_canonical| = {mp.nstr(ratio, 8)}  "
          f"(signs: geometric {'-' if eps_geom < 0 else '+'}, canonical +)")
    w.add_assertion("geometric_over_canonical_magnitude", mp.nstr(ratio, 8), "151.14",
                    tolerance="1e-1",
                    source="the two derived candidates differ by two orders of "
                           "magnitude AND in sign -- they are not variants of "
                           "one convention")

    # --- the arithmetic-vs-geometric fork (bean qou-s24v) -------------------
    # The case FOR the geometric mean was: the closed form is a product over
    # bonds, so the multiplicative midpoint is the natural interpolation. That
    # argument does not survive contact with the bond ELEMENTS.
    print("\n--- arithmetic vs geometric: the product-over-bonds argument ---")
    prod_factors = f_pp * f_nn
    # The two like-flavour bonds are sigma (d = 0) and sigma - h*1 = sigma^-1
    # (d = -h). They are MUTUALLY INVERSE, so their product in the algebra is
    # the identity, whose Markov-trace expectation is tau(1) = 1 -- the same
    # normalisation the relation f_k = z + d_k already assumes.
    trace_of_bond_product = mp.mpf(1)
    print(f"  f_pp * f_nn                 = {mp.nstr(prod_factors, 20)}   (product of TRACES)")
    print(f"  tau(sigma * sigma^-1)       = {mp.nstr(trace_of_bond_product, 20)}   (TRACE of the product)")
    print(f"  gap                         = {mp.nstr(trace_of_bond_product - prod_factors, 20)}")
    w.add_assertion("product_of_factors_eq_closed_form",
                    mp.nstr(abs(prod_factors - (q / (q ** 2 + 1)) ** 2), 6), "0",
                    tolerance="1e-50",
                    source="f_pp*f_nn = (q/(q^2+1))^2, which is (z/q^2)^2 -- the "
                           "reason the geometric mean is z/q^2")
    w.add_assertion("markov_trace_not_multiplicative_on_these_bonds",
                    str(abs(prod_factors - trace_of_bond_product) > mp.mpf("0.7")),
                    "True",
                    source="the product of the factors misses tau(1)=1 by more "
                           "than 3/4; it could not do otherwise, since a bond "
                           "and its inverse would need reciprocal traces")
    # 1/4 - f_pp*f_nn is a SQUARE, so the bound holds at every q, not just q0.
    sq = ((q ** 2 - 1) / (2 * (q ** 2 + 1))) ** 2
    w.add_assertion("quarter_minus_product_is_a_square",
                    mp.nstr(abs((mp.mpf(1) / 4 - prod_factors) - sq), 6), "0",
                    tolerance="1e-50",
                    source="1/4 - f_pp*f_nn = ((q^2-1)/(2(q^2+1)))^2, so the "
                           "product is <= 1/4 for EVERY q, equality only at q=1 "
                           "(Lean: quarter_sub_fPP_mul_fNN)")
    # The arithmetic mean has no such gap: the trace is LINEAR.
    arith = (f_pp + f_nn) / 2
    w.add_assertion("arithmetic_mean_is_trace_of_skein_symmetriser",
                    mp.nstr(abs(arith - (z - h / 2)), 6), "0", tolerance="1e-50",
                    source="(f_pp+f_nn)/2 = z - h/2 = tau((sigma+sigma^-1)/2); the "
                           "trace is linear, so the arithmetic mean of the factors "
                           "IS the trace of a canonical element, and the geometric "
                           "mean is the trace of nothing")

    # --- the honest verdict -------------------------------------------------
    # Was `add_assertion("an_E_is_selected", "False", "False")` (bean
    # `qou-26f2`) — the verdict of the whole probe, and the only claim in it
    # standing on no computation. Two literals would have read "no E selected"
    # even on a run where C2's bound had tightened to a single survivor, which
    # is exactly the event that turns this negative into a selection, and a
    # selection into a fit. C1, C3 and C4 are identities holding across the
    # class (the assertions above measure that), so C2 is the only constraint
    # with per-candidate teeth; count what it leaves standing.
    survivors = [n for n, E, _r in _bar_even_candidates() if abs(E(q)) < e_bound]
    n_candidates = len(list(_bar_even_candidates()))
    an_E_is_selected = (len(survivors) == 1)
    w.add_assertion("an_E_is_selected",
                    str(an_E_is_selected), "False",
                    source="none of C1-C4 narrows the class; selecting an E from "
                           "an isotope anchor would be a fit, and is not done. "
                           f"C2 is the only constraint that can exclude a "
                           f"candidate and it leaves {len(survivors)} of "
                           f"{n_candidates} standing, so the class is not "
                           f"narrowed to one")

    path = w.save(extra={"data": {
        "q0": mp.nstr(q, 25),
        "delta": mp.nstr(delta, 25),
        "eps_canonical_delta_over_4": mp.nstr(delta / 4, 25),
        "eps_geometric": mp.nstr(eps_geom, 25),
        "f_pn_strict_averaged": mp.nstr(f_strict, 30),
        "f_pn_bring_color_weighted": mp.nstr(f_canon, 30),
        "f_pn_geometric_mean": mp.nstr(geom, 30),
        "constraints_checked": ["confluence", "convex_weights",
                                "markov_bond_form", "cubic_vanishing_order"],
        "constraints_that_narrow_E": [],
        "regular_E_confines_offset_to": "O((q-1)^3)",
        "geometric_mean_reachable_in_class": False,
        "geometric_mean_required_E_pole_order": 2,
        "arithmetic_vs_geometric": "RESOLVED in favour of arithmetic as the structurally-backed choice (qou-s24v): the product-over-bonds argument for the geometric mean is unsound. f_pp and f_nn are the traces of sigma and sigma^-1, which are MUTUALLY INVERSE, so tau of their product is tau(1) = 1 while the product of their traces is <= 1/4 at every q. The closed form multiplies TRACES; there is no multiplicative structure at the factor level to take a midpoint in. The arithmetic mean, by contrast, IS the trace of the skein symmetriser (sigma+sigma^-1)/2, because the trace is linear. This does NOT establish eps = 0 physically; the colour-tube delta/4 sits on top either way.",
        "product_of_factors_at_q0": mp.nstr(f_pp * f_nn, 25),
        "trace_of_bond_product": "1",
        "lean": "QOU.MassTheory.PnOffset",
    }})
    print(f"\nwitness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
