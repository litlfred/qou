#!/usr/bin/env python3
"""
qbeta_delta_element_fork_pricing_probe.py — qou-cds1: TWO nucleon-word models
are both called `Delta`, the corpus's two closed forms hold only for the
smaller one, and the D-frame trace baseline is priced across the two.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: .beans/qou-avt6--proved-no-typed-crossing-word-difference-has-couni.md
# Ref: folio/quantum-observable-universe/nuclear-interactions/qbeta-counit-closed-form.md
# Ref: folio/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.md
# Ref: folio/quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md
# Ref: computations/qbeta/qbeta_d_frame_trace_baseline_probe.py
# Ref: computations/qbeta/qbeta_phase_block_resolution_probe.py

THE TWO MODELS.  `qbeta-counit-closed-form.md` opens *"Let Delta = NF(n) -
NF(p) be the single-wrap normal-form difference of the neutron and proton
typed-crossing elements in H_3(q)"* and asserts two closed forms,

    eps(Delta) = h^2/2 - h            tr_M(Delta) = h^2/2 - h*z .

Two different elements in the corpus answer to that description:

  Delta_S  the SHORT model.  `deuteron-binding-dressing-proton-net.md` gives
           the single-wrap net coefficients as net(p) = 1 - h/2 and
           net(n) = 1 - 3h/2 + h^2/2 = (1 - h/2)(1 - h).  Since a typed
           crossing (sigma_g + d) has net 1 + d, and net is multiplicative
           across DISTINCT generators, these are the net coefficients of a
           ONE-crossing proton (d = -h/2) and a TWO-crossing neutron
           (d = -h/2, d = -h).  Reduced, Delta_S = (h^2/2, -h/2, -h/2, 0, 0, 0)
           in the basis [gamma, sigma0, sigma1, L+, L-, e-] -- the NF vector.

  Delta_L  the LONG model.  `q-beta-c3-hopf-three-fold-markov.md` states the
           construction uses *"proton uud / neutron udd, both 11 typed
           crossings"*, and `hecke_core._PROTON_G0/_G1`, `_NEUTRON_G0/_G1` are
           exactly 11 each.  This is the model the production compute runs on.

WHAT THIS PROBE ESTABLISHES.  Both are legitimate typed-crossing differences;
they are not the same element; and BOTH of the corpus block's closed forms
hold for Delta_S and FAIL for Delta_L:

  * net(Delta_L) = -h/2 - h^2/2 - h(q^4+1)/(4q^2), not h^2/2 - h;
  * tr_M^z(Delta_L) is QUADRATIC in z (Delta_L is supported on L+, where the
    Ocneanu trace is z^2), so it is not h^2/2 - h*z for any z.

The mechanism is exact and elementary: net is multiplicative across distinct
generators but NOT within one, because T_0^2 = h*T_0 + 1 reduces and
net(T_0^2) = 1 + h while net(T_0)^2 = 1.  Adding same-generator crossings
therefore moves net, which is why an 11-crossing word cannot carry the
1-crossing coefficient 1 - h/2.

TWO CONSEQUENCES FOR qou-cds1.

 1. THE PRICING IS MIXED.  `qbeta_d_frame_trace_baseline_probe` takes its
    counit baseline from Delta_S (`eps = h**2/2 - h`, hard-coded) and its
    Markov trace from Delta_L (`chi_all_lambda` of the 11-crossing words).
    Its headline "-15.451 %, 92.1x the entire five-rung ladder" -- the figure
    qou-cds1 carries as "the EXPECTATION set on the re-derivation" -- is one
    number from each model.  Priced consistently on Delta_S it is 257x.

 2. THE PHASE IDENTITY IS SHORT-MODEL-SPECIFIC, and this is the part that
    matters more than the number.  The identity qou-cds1 records as the
    derivation of the ladder phase -- (D1), *"alpha is neither free nor
    fitted: it IS the discrepancy"* --

        2*alpha(z) = net(Delta) - tr_M^z(Delta),   alpha = (z-1)h/2

    is AFFINE in z.  It is affine because Delta_S is supported only on
    {gamma, sigma0, sigma1}, where net - tr_M^z takes the values 0, 1-z, 1-z.
    On Delta_L the same difference is quadratic.  So the ladder phase being a
    linear function of the Markov parameter -- the property that makes the C->D
    move look like a substitution in the first place -- is a fact about the
    short model, not about the nucleon words the corpus names.

RELATION TO qou-avt6.  That bean proves (scope-(b), norm form on Z[sqrt2])
that no typed-crossing word difference has AUGMENTATION h^2/2 - h.  This is
the complementary reading: `epsNPq` is the COORDINATE SUM, not the
augmentation (qou-99qc), and under the coordinate sum the element does exist
-- it is Delta_S.  What fails is the identification of Delta_S with the
11-crossing construction.  The two results do not overlap and neither implies
the other.

SCOPE -- (a), and deliberately narrow.  This REFUTES NOTHING.  It does not
decide which model is canonical, does not claim either closed form is wrong on
its own model, does not propose a c_k or any value, and wires nothing.  It
reports that two named objects differ, which corpus statements hold of which,
and what each side prices at on its own.
"""
from __future__ import annotations

import sys
from pathlib import Path

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported. Without
# this the module is unresolvable and the probe cannot run standalone.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, BASIS_NAMES, L, ONE, basis_vec, vec, net, counit,
    length, reg_char,
)

set_compute_dps(50)

Z = sp.Symbol("z")
Z_C = sp.sqrt(q) / (q + 1)
Z_D = q**3 / (q**2 + 1)
LABELS = ["(3)", "(2,1)", "(1,1,1)"]

# q_0 as an EXACT rational; every substitution below is exact arithmetic.
Q0 = sp.Rational(Q_50_DIGIT_STR)


# -- characters, exactly as qbeta_phase_block_resolution_probe defines them --
def chi3(v):
    return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))


def chi111(v):
    return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))


def chi21(v):
    return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)


CHI = [chi3, chi21, chi111]

# -- the Ocneanu trace on the standard basis, from the Markov rule alone -----
#    tr(1) = 1,  tr(x T_2 y) = z tr(x y);  T_0^2 = h T_0 + 1 gives the last.
TR_BASIS = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]


def tr_M(v):
    return sp.simplify(sum(v[i] * TR_BASIS[i] for i in range(N)))


def num(e):
    """Exact substitution q -> q_0 (rational), then a 60-dps mpf readout.

    NO float64: the substitution is exact rational arithmetic and the handoff
    to mpmath goes through the decimal string sympy prints at 60 significant
    digits, never through a Python float.
    """
    return mp.mpf(str(sp.N(sp.simplify(sp.sympify(e)).subs(q, Q0), 60)))


_H_NUM = Q_MP - 1 / Q_MP


def _d_sym(d):
    """Lift a stored crossing-template mpf to the exact symbol it encodes."""
    dv = mp.mpf(str(d))
    for sym, val in ((sp.Integer(0), mp.mpf(0)),
                     (-h, -_H_NUM),
                     (-h / 2, -_H_NUM / 2)):
        if abs(dv - val) < mp.mpf("1e-40"):
            return sym
    raise ValueError(f"unrecognised crossing template d = {d}")


def _crossings(g0, g1):
    """(gen, d) list for a typed-crossing word: gen-0 factors, then gen-1.

    GROUPED, deliberately, and now said out loud (bean `qou-t29k`). Nothing in
    this probe forces it: `_mult` multiplies `L[g] + d*ONE` in whatever order it
    is handed, and the shared regular-representation helpers imported from
    `qbeta_net_trace_invariance_probe` are frame-agnostic. So unlike the four
    monotone-kernel siblings (`qou-11l4`), the frame here is a choice.

    It is the right choice, MEASURED rather than inherited. Driving both fork
    probes with the same symbols reordered into the borromean word:

        qbeta_delta_bar_parity_probe            16/16 -> 15/16
        qbeta_delta_element_fork_pricing_probe  15/15 -> 13/15

    Every substantive fork conclusion is INVARIANT: the two models are
    different elements, the corpus counit and trace closed forms fail on the
    long model and hold on the short one, chi^(2,1) vanishes on the short model
    only, the phase identity fails on the long model, the bar-parity split, the
    fork surviving descent, neither element in the two-row quotient. **The
    Delta fork does not depend on the intra-nucleon ordering.**

    What is frame-bound is narrow and identified. Two `calibration_*` legs
    check against COMMITTED grouped-era witnesses and published values, so they
    are frame-bound by construction -- the same reason
    `qbeta_delta_vs_deltaTbeta_settled_probe` chose grouped deliberately
    (2026-09-06, `qou-y2o7`). And one real content difference, `qou-epmq`:
    `Delta_L`'s `e_minus` coordinate is 0 grouped but
    `-(q^2-1)^2 Phi_12(q)^2 / (2 q^6)` canonical, so `net` and `tr_M(z=1)` stop
    coinciding on the long model.

    Switching to canonical would therefore break the calibration without
    changing a single finding. Named via `grouped_word_from_chains` so the
    frame is visible at the site rather than only in a bean.
    """
    from pyhecke.atom import grouped_word_from_chains
    for c, _d in list(g0) + list(g1):
        assert c == 1, "typed crossing with c != 1 is outside this reading"
    return [(off, d) for _c, d, off in grouped_word_from_chains(
        [(c, _d_sym(d)) for c, d in g0],
        [(c, _d_sym(d)) for c, d in g1])]


def _mult(word_ops):
    """Left-multiplication operator for a product of (gen, d) crossings."""
    M = ONE
    for g, d in word_ops:
        M = M * (L[g] + d * ONE)
    return M


def main() -> int:
    w = WitnessBuilder("qbeta-delta-element-fork-pricing", engine="sympy+mpmath")
    w.set_description(
        "qou-cds1: two nucleon-word models (a 1-/2-crossing SHORT model and "
        "the 11-crossing LONG model in hecke_core) are both called Delta. "
        "Both closed forms in qbeta-counit-closed-form hold for the short one "
        "and fail for the long one; the D-frame trace baseline's '92x the "
        "ladder' takes its counit from the short model and its trace from the "
        "long one; and the ladder phase's linearity in z is short-model "
        "specific. Scope-(a): reports which statement holds of which element, "
        "decides nothing, wires nothing.")
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n        {note}")

    print("=" * 78)
    print(" qou-cds1 - two nucleon-word models, and what each side prices at")
    print("=" * 78)

    # ---- Delta_S: the short model / corpus NF vector -----------------------
    delta_s = vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)
    corp_net_p = sp.simplify(1 - h / 2)
    corp_net_n = sp.simplify(1 - 3 * h / 2 + h**2 / 2)

    check("short_model_net_coefficients_factor_as_one_and_two_crossings",
          sp.simplify(corp_net_n - corp_net_p * (1 - h)) == 0,
          "net(n) = 1 - 3h/2 + h^2/2 = (1 - h/2)(1 - h) exactly, and a typed "
          "crossing (sigma+d) has net 1+d: a 1-crossing proton and a "
          "2-crossing neutron")

    check("short_model_carries_the_corpus_counit",
          sp.simplify(net(delta_s) - (h**2 / 2 - h)) == 0
          and sp.simplify((corp_net_n - corp_net_p) - (h**2 / 2 - h)) == 0,
          "net(Delta_S) = h^2/2 - h = epsNPq, the number Q_A and the whole "
          "published ladder are built from")

    # ---- Delta_L: the 11-crossing typed words, reduced ---------------------
    n_p = len(_PROTON_G0) + len(_PROTON_G1)
    n_n = len(_NEUTRON_G0) + len(_NEUTRON_G1)
    check("long_model_is_the_eleven_crossing_construction",
          n_p == 11 and n_n == 11,
          f"hecke_core proton {n_p} crossings, neutron {n_n} - matching "
          f"q-beta-c3-hopf-three-fold-markov's 'both 11 typed crossings'")

    proton_w = sp.expand(_mult(_crossings(_PROTON_G0, _PROTON_G1))
                         * basis_vec(0))
    neutron_w = sp.expand(_mult(_crossings(_NEUTRON_G0, _NEUTRON_G1))
                          * basis_vec(0))
    delta_l = sp.Matrix([sp.simplify(sp.factor(x))
                         for x in (neutron_w - proton_w)])

    print("\n  Delta_L coordinates in the standard basis:")
    for i in range(N):
        print(f"    {BASIS_NAMES[i]:<9} {sp.simplify(delta_l[i])}")

    print(f"\n  net(proton):   short {mp.nstr(num(corp_net_p), 16)}"
          f"   long {mp.nstr(num(net(proton_w)), 16)}")
    print(f"  net(neutron):  short {mp.nstr(num(corp_net_n), 16)}"
          f"   long {mp.nstr(num(net(neutron_w)), 16)}")

    check("the_two_models_are_DIFFERENT_elements",
          not sp.simplify(delta_l - delta_s).is_zero_matrix,
          "Delta_L != Delta_S in H_3(q) - measured by reduction in the "
          "6-dimensional regular representation, not inferred")

    check("per_nucleon_net_coefficients_do_not_match_either",
          sp.simplify(net(proton_w) - corp_net_p) != 0
          and sp.simplify(net(neutron_w) - corp_net_n) != 0,
          "the corpus's single-wrap net(p), net(n) are not the coordinate "
          "sums of the 11-crossing words")

    check("mechanism_net_is_not_multiplicative_within_one_generator",
          sp.simplify(net(sp.expand(L[0] * L[0] * basis_vec(0)))
                      - (1 + h)) == 0,
          "net(T_0^2) = 1 + h while net(T_0)^2 = 1, because T_0^2 = h T_0 + 1 "
          "reduces - so same-generator crossings move net and an 11-crossing "
          "word cannot carry a 1-crossing coefficient")

    # ---- both corpus closed forms fail on the long model ------------------
    check("corpus_counit_closed_form_FAILS_on_the_long_model",
          sp.simplify(net(delta_l) - (h**2 / 2 - h)) != 0,
          f"net(Delta_L) = {mp.nstr(num(net(delta_l)), 14)} vs the block's "
          f"h^2/2 - h = {mp.nstr(num(h**2 / 2 - h), 14)}")

    gap_s = sp.simplify(sp.expand(net(delta_s) - tr_M(delta_s)))
    gap_l = sp.simplify(sp.expand(net(delta_l) - tr_M(delta_l)))
    two_alpha = sp.simplify(h * (Z - 1))
    tr_s = sp.simplify(sp.expand(tr_M(delta_s)))
    tr_l = sp.simplify(sp.expand(tr_M(delta_l)))
    deg_l = sp.degree(sp.Poly(sp.expand(tr_l), Z), Z)

    check("corpus_trace_closed_form_holds_on_the_short_model",
          sp.simplify(tr_s - (h**2 / 2 - h * Z)) == 0,
          "tr_M^z(Delta_S) = h^2/2 - h z, identically in q and z")

    check("corpus_trace_closed_form_FAILS_on_the_long_model",
          sp.simplify(tr_l - (h**2 / 2 - h * Z)) != 0 and deg_l == 2,
          f"tr_M^z(Delta_L) is degree {deg_l} in z - Delta_L is supported on "
          f"L+, where the Ocneanu trace is z^2")

    # ---- characters, both models -----------------------------------------
    chi_s = [sp.simplify(sp.factor(f(delta_s))) for f in CHI]
    chi_l = [sp.simplify(sp.factor(f(delta_l))) for f in CHI]

    print("\n  block          chi(Delta_S)            chi(Delta_L)")
    for k in range(3):
        print(f"    {LABELS[k]:<10} {mp.nstr(num(chi_s[k]), 16):>22}"
              f" {mp.nstr(num(chi_l[k]), 16):>22}")
        w.add_data(f"chi_{LABELS[k]}_short", fmt(num(chi_s[k])))
        w.add_data(f"chi_{LABELS[k]}_long", fmt(num(chi_l[k])))

    check("chi_two_one_vanishes_on_the_short_model_only",
          sp.simplify(chi_s[1]) == 0 and sp.simplify(chi_l[1]) != 0,
          f"chi^(2,1)(Delta_S) = 0 (reproducing "
          f"qbeta_phase_block_resolution_probe) but chi^(2,1)(Delta_L) = "
          f"{mp.nstr(num(chi_l[1]), 12)} - 'the phase is blind to the 2-dim "
          f"block' is a short-model statement")

    COMMITTED = {
        "(3)": mp.mpf("-0.260387641790120802073285342788008683395823953848006260161245"),
        "(2,1)": mp.mpf("-0.106814457651578049623631258921144907521837554045064212540761"),
        "(1,1,1)": mp.mpf("-0.171538643776599505671840531694425115158778702109050313959100"),
    }
    worst = max(abs(num(chi_l[k]) - COMMITTED[LABELS[k]]) for k in range(3))
    check("calibration_long_model_reproduces_the_committed_trace_witness",
          worst < mp.mpf("1e-45"),
          f"max |diff| = {mp.nstr(worst, 6)} against all three chi in "
          f"qbeta-d-frame-trace-baseline.witness.json - Delta_L IS the element "
          f"that probe traces")

    # ---- the phase identity is short-model-specific -----------------------
    check("phase_identity_holds_on_the_short_model_for_every_z",
          sp.simplify(gap_s - two_alpha) == 0,
          "net(Delta_S) - tr_M^z(Delta_S) = h(z-1) = 2*alpha, identically in "
          "q and z - qou-cds1's (D1)")

    check("phase_identity_FAILS_on_the_long_model",
          sp.simplify(gap_l - two_alpha) != 0
          and sp.degree(sp.Poly(sp.expand(gap_l), Z), Z) == 2,
          "net - tr_M^z is quadratic in z on Delta_L, so alpha = (z-1)h/2 is "
          "not the counit-minus-trace gap there - the ladder phase's "
          "linearity in the Markov parameter is short-model specific")

    # ---- pricing, each model consistently ---------------------------------
    me = mp.mpf(str(M_E_MEV))
    Qexp = mp.mpf(str(Q_NEUTRON_MEV))
    qn = Q_MP
    E0 = me / (qn * (qn - 1))

    def price(sym_val):
        Qb = abs(num(sym_val) * E0)
        return Qb, (Qb - Qexp) / Qexp

    prices = {}
    for tag, dl in (("short", delta_s), ("long", delta_l)):
        for lbl, val in (("net", net(dl)),
                         ("augmentation", counit(dl)),
                         ("tr_M_zC", tr_M(dl).subs(Z, Z_C)),
                         ("tr_M_zD", tr_M(dl).subs(Z, Z_D))):
            prices[f"{tag}/{lbl}"] = price(val)

    print("\n  Q_beta from each functional, on each model (MeV, err vs CODATA):")
    print(f"    {'model/functional':<26} {'Q_beta':>18} {'err %':>14}")
    for k, (Qb, err) in prices.items():
        print(f"    {k:<26} {mp.nstr(Qb, 12):>18} {mp.nstr(err * 100, 6):>14}")
        w.add_data(f"Qbeta_{k.replace('/', '_')}", fmt(Qb))
        w.add_data(f"err_{k.replace('/', '_')}", fmt(err))

    ladder_move = abs(prices["short/net"][1])
    ratio_mixed = abs(prices["long/tr_M_zD"][1]) / ladder_move
    ratio_short = abs(prices["short/tr_M_zD"][1]) / ladder_move

    print(f"\n  published, MIXED (counit short / trace long) : "
          f"{mp.nstr(ratio_mixed, 8)}x")
    print(f"  consistent on the SHORT model                : "
          f"{mp.nstr(ratio_short, 8)}x")

    check("calibration_reproduces_the_published_mixed_ratio",
          abs(ratio_mixed
              - mp.mpf("92.1058337158958078293820971505915498676663"))
          < mp.mpf("1e-30"),
          f"{mp.nstr(ratio_mixed, 10)}x reproduces the committed "
          f"gap_over_ladder_ratio exactly - confirming it is net(Delta_S) "
          f"against tr_M(Delta_L)")

    check("the_consistent_short_model_price_is_LARGER",
          ratio_short > ratio_mixed,
          f"{mp.nstr(ratio_short, 8)}x vs {mp.nstr(ratio_mixed, 8)}x - the D "
          f"trace against the counit Q_A is actually built from. The mixed "
          f"figure UNDERSTATES the gap by "
          f"{mp.nstr(ratio_short / ratio_mixed, 4)}x")

    for k, v in (("gap_over_ladder_mixed_published", ratio_mixed),
                 ("gap_over_ladder_short_consistent", ratio_short),
                 ("understatement_factor", ratio_short / ratio_mixed)):
        w.add_data(k, fmt(v))
    w.add_data("delta_L_coords", "; ".join(
        f"{BASIS_NAMES[i]}={sp.simplify(delta_l[i])}" for i in range(N)))
    w.add_data("net_proton_long", fmt(num(net(proton_w))))
    w.add_data("net_neutron_long", fmt(num(net(neutron_w))))
    w.add_data("net_proton_short_corpus", fmt(num(corp_net_p)))
    w.add_data("net_neutron_short_corpus", fmt(num(corp_net_n)))
    w.add_data("trM_z_on_long_model", str(sp.factor(tr_l)))
    w.add_data("net_minus_trM_on_long_model", str(sp.factor(gap_l)))

    print(f"\n  {sum(ok)}/{len(ok)} checks passed")
    out = w.save()
    print(f"  witness: {out}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
