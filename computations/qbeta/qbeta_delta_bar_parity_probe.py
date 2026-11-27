#!/usr/bin/env python3
"""Does a canonical criterion pick the Delta ELEMENT, as one picks the functional?

qou-bg3w / qou-cds1.  `ConventionDAdmissibleRoots.lean` (sorry-free) settles the
FUNCTIONAL side of the Delta fork: the (1^3)-block Ocneanu weight numerator
factors as

    N(q,z) = (q^2+1)z^2 - (2q^3+q)z + q^4 = (z - q)*((q^2+1)z - q^3),

so tr_M^z descends to the two-row (Wenzl) quotient iff z is a root, i.e. iff
z in {q, z_D}.  EXACTLY TWO admissible parameters; z_C and z = 1 are both
excluded, by the SAME criterion.

SCOPING NOTE (2026-08-29).  An earlier revision of this line wrote "z = 1
(`net`)", i.e. treated `net` AS tr_M at z = 1.  That is FALSE in general:
tr_M(z=1) weights the basis by [1,1,1,1,1,h+1] while `net` is the plain
coordinate sum [1,1,1,1,1,1], so they differ by h times the `e_minus`
coordinate.  They coincide for BOTH Delta models only because both happen to
have that coordinate zero -- checked below, not assumed.

And the corpus has a STRONGER, element-independent reason to exclude `net`
which does not go through z at all: `net` is the functional sigma -> 1, and
sigma^2 = h*sigma + 1 forces 1 = h + 1, i.e. h = 0.  So `net` is not an
algebra map, while the augmentation sigma -> q is one (q^2 = hq + 1 exactly
when h = q - 1/q).  That argument is `qbeta_epsnpq_functional_mismatch_probe`,
which could not be RUN until PR #5943 fixed its import bootstrap.

That leaves the ELEMENT side open: two objects are both called Delta,

  Delta_S   the SHORT model, NF vector (h^2/2, -h/2, -h/2, 0, 0, 0);
  Delta_L   the LONG model, the 11 typed crossings of `hecke_core._PROTON_G0/G1`
            and `_NEUTRON_G0/G1`.

This probe asks two questions and reports one NEGATIVE and one POSITIVE.

  Q1 (the obvious move, and it FAILS).  Does the descent criterion pick an
     element the way it picks a functional -- i.e. does either Delta have
     vanishing (1^3) component, so that it lives in the two-row quotient?
     Measured: NEITHER does.  The criterion is about the functional only.

  Q2 (a DIFFERENT canonical criterion, and it SEPARATES them).  The bar
     involution of Kazhdan-Lusztig -- the ring homomorphism with
     bar(q) = q^-1, bar(T_s) = T_s^-1 -- is the most canonical involution on
     H_n(q), and the framework already asserts the Q_beta channel is the
     BAR-ODD sinh partner of the bar-even cosh meson scale (AGENTS.md,
     canonical derivation chain).  Measured: Delta_S is EXACTLY bar-odd,
     bar(Delta_S) = -Delta_S, identically in q; Delta_L is neither bar-odd nor
     bar-even.

SCOPE.  This is a scope-(a) measurement of a structural property, NOT an
adjudication of the fork and NOT a wiring.  It reports that one canonical
involution separates the two candidates and which way it points; whether
bar-oddness is the RIGHT selection principle for the decay element is an
owner call (bean qou-bg3w).  No c_k is proposed, no fit is performed, nothing
downstream is re-pointed.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/QBeta/ConventionDAdmissibleRoots.lean
-- Ref: [manuscript] computations/qbeta/qbeta_d1_admissible_anchor_probe.py (the functional side)
-- Ref: [manuscript] computations/qbeta/qbeta_delta_element_fork_pricing_probe.py (the two models)
-- Ref: [kazhdan1979] Kazhdan, Lusztig, "Representations of Coxeter groups and Hecke algebras", Invent. Math. 53 (1979) 165-184.
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors", Invent. Math. 92 (1988) 349-383.
"""
from __future__ import annotations

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (_HERE, os.path.join(_HERE, ".."), os.path.join(_HERE, "..", "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp                                        # noqa: E402
import sympy as sp                                         # noqa: E402

from _precision import set_compute_dps, fmt                # noqa: E402
from witness_base import WitnessBuilder                    # noqa: E402
from q_parameter import Q_50_DIGIT_STR                     # noqa: E402
from hecke_core import (                                   # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from qbeta_net_trace_invariance_probe import (             # noqa: E402
    q, h, N, BASIS, BASIS_NAMES, L, ONE, basis_vec, vec, length, reg_char,
)

set_compute_dps(50)

Z = sp.Symbol("z")
Z_D = q**3 / (q**2 + 1)
LABELS = ["(3)", "(2,1)", "(1,1,1)"]

#: q_0 as an EXACT rational -- every substitution below is exact arithmetic.
Q0 = sp.Rational(Q_50_DIGIT_STR)

#: reduced words for the standard basis, in the SAME order as BASIS.
#: BASIS[3] = S0.S1 so T = T_0 T_1; BASIS[5] = (S0.S1).S0 so T = T_0 T_1 T_0.
REDUCED_WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]


# --- characters, exactly as the fork-pricing probe defines them -------------
def chi3(v):
    return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))


def chi111(v):
    return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))


def chi21(v):
    return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)


CHI = [chi3, chi21, chi111]

#: Ocneanu trace on the standard basis, from the Markov rule alone.
TR_BASIS = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]


def tr_M(v):
    return sp.simplify(sum(v[i] * TR_BASIS[i] for i in range(N)))


def num(e):
    """Exact substitution q -> q_0 (rational), then a 60-dps mpf readout.

    NO float64 anywhere: the substitution is exact rational arithmetic and the
    handoff to mpmath goes through the 60-significant-digit decimal string
    sympy prints, never through a Python float.
    """
    return mp.mpf(str(sp.N(sp.simplify(sp.sympify(e)).subs(q, Q0), 60)))


# --- the bar involution ----------------------------------------------------
#     bar is a RING homomorphism (not an anti-homomorphism) with
#       bar(q) = 1/q      and      bar(T_s) = T_s^{-1} = T_s - h,
#     the second from the Hecke relation T_s^2 = h T_s + 1.
INV_GEN = {g: L[g] - h * ONE for g in (0, 1)}


def _bar_basis_op(i):
    """Left-multiplication operator for bar(T_w), w = BASIS[i]."""
    M = ONE
    for g in REDUCED_WORDS[i]:
        M = M * INV_GEN[g]
    return M


_BAR_BASIS_VEC = [sp.expand(_bar_basis_op(i) * basis_vec(0)) for i in range(N)]


def barq(e):
    """The scalar half of the involution: q -> 1/q."""
    return sp.simplify(sp.together(sp.sympify(e).subs(q, 1 / q)))


def bar(v):
    """bar(x) for x given as a coefficient vector over BASIS."""
    out = sp.zeros(N, 1)
    for i in range(N):
        c = barq(v[i])
        if c == 0:
            continue
        out += c * _BAR_BASIS_VEC[i]
    return sp.Matrix([sp.simplify(sp.factor(sp.together(x))) for x in out])


# --- the two Delta models --------------------------------------------------
_H_NUM = mp.mpf(Q_50_DIGIT_STR) - 1 / mp.mpf(Q_50_DIGIT_STR)


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
    M = ONE
    for g, d in word_ops:
        M = M * (L[g] + d * ONE)
    return M


_CHECKS: list[str] = []
_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    _CHECKS.append(name)
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


def main() -> int:
    w = WitnessBuilder("qbeta-delta-bar-parity", engine="sympy+mpmath")
    w.set_description(
        "qou-bg3w: the admissible-root criterion picks the FUNCTIONAL but not "
        "the ELEMENT (neither Delta has vanishing (1^3) component). A "
        "different canonical criterion -- the Kazhdan-Lusztig bar involution "
        "bar(q)=1/q, bar(T_s)=T_s^-1 -- DOES separate them: Delta_S is exactly "
        "bar-odd, identically in q; Delta_L is neither bar-odd nor bar-even. "
        "Scope-(a): a structural measurement, not an adjudication of the fork."
    )

    print("=" * 72)
    print(" qou-bg3w - does a canonical criterion pick the Delta ELEMENT?")
    print("=" * 72)

    delta_s = vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)

    proton_w = sp.expand(_mult(_crossings(_PROTON_G0, _PROTON_G1))
                         * basis_vec(0))
    neutron_w = sp.expand(_mult(_crossings(_NEUTRON_G0, _NEUTRON_G1))
                          * basis_vec(0))
    delta_l = sp.Matrix([sp.simplify(sp.factor(x))
                         for x in (neutron_w - proton_w)])

    # ---- 0. the bar map is well-formed ------------------------------------
    print("\n  0. the bar involution is well-formed")

    check("bar_sends_the_generator_to_its_inverse",
          sp.simplify(sp.Matrix(_BAR_BASIS_VEC[1]) - (L[0] - h * ONE)
                      * basis_vec(0)) == sp.zeros(N, 1),
          "bar(T_0) = T_0 - h = T_0^{-1}, from T_0^2 = h T_0 + 1", w)

    invol_ok = all(
        sp.simplify(bar(bar(basis_vec(i))) - basis_vec(i)) == sp.zeros(N, 1)
        for i in range(N))
    check("bar_is_an_involution_on_every_basis_element",
          invol_ok,
          "bar(bar(T_w)) = T_w for all six w - the map is an involution, so "
          "'bar-odd' and 'bar-even' are well-defined eigenspaces", w)

    # a reduced-word-independence spot check: T_0 T_1 T_0 = T_1 T_0 T_1
    braid_lhs = INV_GEN[0] * INV_GEN[1] * INV_GEN[0] * basis_vec(0)
    braid_rhs = INV_GEN[1] * INV_GEN[0] * INV_GEN[1] * basis_vec(0)
    check("bar_is_independent_of_the_reduced_word",
          sp.simplify(sp.expand(braid_lhs - braid_rhs)) == sp.zeros(N, 1),
          "bar(T_0)bar(T_1)bar(T_0) = bar(T_1)bar(T_0)bar(T_1): the inverses "
          "satisfy the braid relation, so bar(T_w) is well-defined", w)

    # ---- 1. Q1 - the descent criterion does NOT pick an element -----------
    print("\n  1. Q1 - does the descent criterion pick an ELEMENT?  NO.")

    chi_s = [sp.simplify(sp.factor(f(delta_s))) for f in CHI]
    chi_l = [sp.simplify(sp.factor(f(delta_l))) for f in CHI]

    print("\n     block          chi(Delta_S)            chi(Delta_L)")
    for k in range(3):
        print(f"       {LABELS[k]:<10} {mp.nstr(num(chi_s[k]), 16):>22}"
              f" {mp.nstr(num(chi_l[k]), 16):>22}")
        w.add_data(f"chi_{LABELS[k]}_short", fmt(num(chi_s[k])))
        w.add_data(f"chi_{LABELS[k]}_long", fmt(num(chi_l[k])))

    check("neither_element_lies_in_the_two_row_quotient",
          sp.simplify(chi_s[2]) != 0 and sp.simplify(chi_l[2]) != 0,
          f"chi^(1,1,1)(Delta_S) = {sp.factor(chi_s[2])} != 0 and "
          f"chi^(1,1,1)(Delta_L) = {mp.nstr(num(chi_l[2]), 12)} != 0 - the "
          f"element analogue of the admissible-root criterion selects NEITHER, "
          f"so the criterion is about the functional alone", w)

    # the fork is NOT an artefact of the inadmissible block
    check("the_fork_survives_descent",
          sp.simplify(chi_s[0] - chi_l[0]) != 0
          or sp.simplify(chi_s[1] - chi_l[1]) != 0,
          "Delta_S and Delta_L differ ALREADY in the two-row part "
          f"(chi^(2,1) = {sp.factor(chi_s[1])} vs "
          f"{mp.nstr(num(chi_l[1]), 12)}), so no admissible functional "
          "identifies them: the fork cannot be deferred to the z-side", w)

    # and no rescaling repairs it either
    check("no_rescaling_identifies_the_two_models",
          sp.simplify(chi_s[1]) == 0 and sp.simplify(chi_l[1]) != 0,
          "chi^(2,1)(Delta_S) = 0 while chi^(2,1)(Delta_L) != 0, so no scalar "
          "multiple of one is the other - the fork is not a normalisation", w)

    # net is NOT tr_M at z=1 in general -- only for elements with no e_minus
    net_gap = sp.simplify(sp.expand(
        sum(delta_s[i] * TR_BASIS[i].subs(Z, 1) for i in range(N)) - sum(delta_s)))
    net_gap_l = sp.simplify(sp.expand(
        sum(delta_l[i] * TR_BASIS[i].subs(Z, 1) for i in range(N)) - sum(delta_l)))
    c5 = sp.symbols("c5")
    generic_gap = sp.simplify(h * c5)
    check("net_equals_tr_at_z_one_ONLY_when_e_minus_vanishes",
          net_gap == 0 and net_gap_l == 0
          and sp.simplify(delta_s[5]) == 0 and sp.simplify(delta_l[5]) == 0
          and generic_gap != 0,
          "in GENERAL tr_M(z=1) - net = h * (e_minus coordinate), since "
          "tr_M(z=1) weights the basis [1,1,1,1,1,h+1] and net weights it "
          "[1,1,1,1,1,1]. Both Delta models have e_minus = 0, so they "
          "coincide HERE -- but the identity is not general and must not be "
          "quoted as one", w)

    # ---- 2. Q2 - the bar involution DOES separate them --------------------
    print("\n  2. Q2 - the Kazhdan-Lusztig bar involution.  It SEPARATES them.")

    bar_s = bar(delta_s)
    bar_l = bar(delta_l)

    s_odd = sp.simplify(sp.expand(bar_s + delta_s)) == sp.zeros(N, 1)
    s_even = sp.simplify(sp.expand(bar_s - delta_s)) == sp.zeros(N, 1)
    l_odd = sp.simplify(sp.expand(bar_l + delta_l)) == sp.zeros(N, 1)
    l_even = sp.simplify(sp.expand(bar_l - delta_l)) == sp.zeros(N, 1)

    print("\n     bar(Delta_S) coordinates:")
    for i in range(N):
        print(f"       {BASIS_NAMES[i]:<9} {sp.simplify(bar_s[i])}")

    check("short_model_is_exactly_bar_odd",
          s_odd and not s_even,
          "bar(Delta_S) = -Delta_S identically in q. Term by term: "
          "bar(h) = -h so bar(h^2/2) = h^2/2 and bar(-h/2) = h/2, while "
          "bar(T_s) = T_s - h; the two h^2/2 contributions cancel to -h^2/2 "
          "and the generator terms flip sign", w)

    check("long_model_is_neither_bar_odd_nor_bar_even",
          not l_odd and not l_even,
          "bar(Delta_L) is neither -Delta_L nor +Delta_L - the 11-crossing "
          "word has no definite bar parity", w)

    w.add_data("short_bar_parity", "odd")
    w.add_data("long_bar_parity", "indefinite")

    # what the bar-odd part of the long model looks like, for the record
    l_odd_part = sp.Matrix([sp.simplify(sp.factor(x))
                            for x in (delta_l - bar_l) / 2])
    l_even_part = sp.Matrix([sp.simplify(sp.factor(x))
                             for x in (delta_l + bar_l) / 2])
    check("long_model_has_a_nonzero_bar_even_part",
          sp.simplify(sp.expand(l_even_part)) != sp.zeros(N, 1),
          "Delta_L = (bar-odd part) + (bar-even part) with the even part "
          f"nonzero; its counit is {mp.nstr(num(sum(l_even_part)), 12)} - it "
          "is the even part that spoils the parity", w)

    # is the long model's bar-odd part proportional to the short model?
    ratios = []
    for i in range(N):
        a, b = sp.simplify(l_odd_part[i]), sp.simplify(delta_s[i])
        if b != 0:
            ratios.append(sp.simplify(a / b))
    prop = len(ratios) > 0 and all(
        sp.simplify(r - ratios[0]) == 0 for r in ratios)
    nonzero_off = any(sp.simplify(l_odd_part[i]) != 0
                      for i in range(N) if sp.simplify(delta_s[i]) == 0)
    check("long_models_bar_odd_part_is_not_the_short_model",
          not (prop and not nonzero_off),
          "the bar-odd part of Delta_L is NOT a scalar multiple of Delta_S - "
          "so the short model is not recoverable from the long one by "
          "projecting onto the bar-odd eigenspace", w)

    # ---- 2b. WHAT bar-oddness forces on the symmetric family -------------
    print("\n  2b. what bar-oddness FORCES (not merely what it verifies)")

    # The corpus's NF vector has the shape c*1 + d*(sigma_0 + sigma_1) -- the
    # diagram automorphism sigma_0 <-> sigma_1 acts trivially on it.  For that
    # two-parameter family,
    #       bar(x) = (cbar - 2h*dbar) + dbar*(sigma_0 + sigma_1),
    # so bar(x) = -x  <=>  dbar = -d  AND  c + cbar = -2*h*d.
    def sym_family(c, d):
        return vec(c, d, d, 0, 0, 0)

    # bar is tested on a GENERIC Laurent pair, not on free symbols: `barq`
    # substitutes q -> 1/q, so a symbol independent of q would be its own
    # conjugate and the check would be vacuous.
    c_gen = q**3 + 1 / q + 5
    d_gen = q**2 - 1 / q**5 + 2
    lhs = bar(sym_family(c_gen, d_gen))
    rhs = sym_family(barq(c_gen) - 2 * h * barq(d_gen), barq(d_gen))
    check("bar_reduces_the_symmetric_family_to_two_scalar_equations",
          sp.simplify(sp.expand(lhs - rhs)) == sp.zeros(N, 1),
          "on x = c + d(sigma_0+sigma_1), bar(x) = (cbar - 2h*dbar) + "
          "dbar*(sigma_0+sigma_1) - verified on a generic Laurent pair - so "
          "bar(x) = -x reduces to exactly two equations: dbar = -d, and "
          "c + cbar = -2hd", w)

    # Fix the scale by taking the corpus's d = -h/2 (bar-odd, as required).
    d0 = -h / 2
    check("the_corpus_crossing_coefficient_is_bar_odd",
          sp.simplify(barq(d0) + d0) == 0,
          "d = -h/2 satisfies dbar = -d, so the corpus's 1-crossing "
          "coefficient already sits in the bar-odd eigenspace", w)

    # Then c + cbar = h^2, which pins the BAR-EVEN PART of c to h^2/2 and
    # leaves the bar-odd part of c entirely free.  Demonstrated both ways.
    c_plus_odd = h**2 / 2 + h            # h is bar-odd: should STAY bar-odd
    c_plus_even = h**2 / 2 + h**2        # h^2 is bar-even: should BREAK it
    still_odd = sp.simplify(sp.expand(
        bar(sym_family(c_plus_odd, d0)) + sym_family(c_plus_odd, d0)))
    now_broken = sp.simplify(sp.expand(
        bar(sym_family(c_plus_even, d0)) + sym_family(c_plus_even, d0)))
    check("bar_oddness_forces_the_bar_even_part_of_c_to_h2_over_2",
          still_odd == sp.zeros(N, 1) and now_broken != sp.zeros(N, 1),
          "with d = -h/2 the condition is c + cbar = h^2, so the BAR-EVEN part "
          "of c is forced to be exactly h^2/2 while its bar-odd part is free: "
          "adding the bar-odd h keeps the element bar-odd, adding the bar-even "
          "h^2 destroys it. h^2/2 is DERIVED from the involution, not fitted", w)

    # and h^2/2 is the number the ladder is actually built from
    check("the_forced_coefficient_is_the_one_the_ladder_uses",
          sp.simplify(sum(delta_s) - (h**2 / 2 - h)) == 0,
          "net(Delta_S) = h^2/2 - h = epsNPq, the counit the published ladder "
          "is built from - so the forced h^2/2 is not an incidental "
          "coefficient but the one the corpus consumes", w)

    # ---- 3. the traces at the two admissible parameters -------------------
    print("\n  3. what each model prices at the two admissible parameters")

    for lbl, zz in (("z = q", q), ("z = z_D", Z_D)):
        ts = sp.simplify(tr_M(delta_s).subs(Z, zz))
        tl = sp.simplify(tr_M(delta_l).subs(Z, zz))
        print(f"     {lbl:<10} tr(Delta_S) = {mp.nstr(num(ts), 16):>20}"
              f"   tr(Delta_L) = {mp.nstr(num(tl), 16):>20}")
        key = "q" if lbl == "z = q" else "zD"
        w.add_data(f"tr_short_at_{key}", fmt(num(ts)))
        w.add_data(f"tr_long_at_{key}", fmt(num(tl)))

    tq_s = sp.simplify(tr_M(delta_s).subs(Z, q))
    tq_l = sp.simplify(tr_M(delta_l).subs(Z, q))
    td_s = sp.simplify(tr_M(delta_s).subs(Z, Z_D))
    td_l = sp.simplify(tr_M(delta_l).subs(Z, Z_D))
    check("the_two_models_are_separated_at_both_admissible_parameters",
          sp.simplify(tq_s - tq_l) != 0 and sp.simplify(td_s - td_l) != 0,
          "tr_M differs between the models at z = q AND at z = z_D, "
          "confirming from the functional side what chi^(2,1) shows from the "
          "block side: no admissible functional identifies them", w)

    # ---- 4. honest scope --------------------------------------------------
    print("\n  4. scope")
    print("     SCOPE-(a). This measures that ONE canonical involution has a")
    print("     definite value on Delta_S and no definite value on Delta_L.")
    print("     It does NOT establish that bar-oddness is the correct")
    print("     selection principle for the decay element, and it wires")
    print("     nothing. Whether the Q_beta channel's stated bar-odd character")
    print("     is a REQUIREMENT on the element or only on the observable is")
    print("     the open question - bean qou-bg3w, an owner call.")

    w.add_data("scope", "a")
    w.add_data("adjudicates_the_fork", False)
    w.add_data("wires_anything", False)

    ntotal = len(_CHECKS)
    npass = ntotal - len(_FAILURES)
    print(f"\n  {npass}/{ntotal} checks passed")
    if _FAILURES:
        print(f"  FAILURES: {', '.join(_FAILURES)}")
    w.add_data("checks_passed", npass)
    w.add_data("checks_total", ntotal)
    out = w.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
