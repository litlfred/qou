#!/usr/bin/env python3
"""The Delta-element candidate set is SIX, not four -- two beans each say
"four" and their lists differ. Census at ONE pin, in ONE basis, with the three
tests the corpus actually applies.

## Why this probe exists

`qou-bg3w` and `qou-vtlj` both conclude "the corpus carries FOUR values for
Delta". Neither is wrong. But they are **different fours**:

    qou-vtlj                              qou-bg3w
    ------------------------------------  ------------------------------------
    short model         -0.1872072   <->  Delta_S              -0.187207
    blocks AS STATED    -0.2089           build_nucleon_nf     -0.1883216 (9x)
    blocks CONSTRUCTED  -0.2137638        build_atom_nf_exact  -0.2272041 (11 interleaved)
    hecke_core Delta_L  -0.2331977   <->  nucleon_gen_chains   -0.2332459 (11 gen-grouped)

They overlap in exactly two rows. The union is **six distinct values**, and
nothing in the corpus has ever measured them side by side. Worse, the two
apparently-matching bottom rows are the SAME element at DIFFERENT q: `qou-bg3w`
recorded -0.2332459 at `pyhecke.gram._Q_FRAC = 111/100`, which is 185 ppm off
the substrate pin, while `qou-vtlj` recorded -0.2331977 at q_0. Agreement to
four digits that is really a pin difference is exactly the trap this repo
records for stale figures, so every number here is at ONE pin: proton q_0.

## What is measured, per candidate

  T1  net(Delta) -- exact in h, and at the proton pin.
  T2  Is (D1) available? `2*alpha = net(Delta) - tr_M^z(Delta)` is affine in z
      iff the z^2 coefficient of tr_M vanishes. With
      `TR = [1, z, z, z^2, z^2, z(hz+1)]` that coefficient is
      `d[L+] + d[L-] + h*d[e^-]` -- a SUM. Testing `L+` alone is wrong and
      gives the right answer for the wrong reason on the gen-grouped element,
      where `L+` vanishes identically.
  T3  The e^- coordinate. `qbeta-counit-closed-form.md` asserts the coordinate
      sum and `tr_M|_{z=1}` coincide "on elements whose e^- coordinate
      vanishes, which both nucleon models happen to satisfy". That is a
      falsifiable claim about the elements, so it is checked rather than
      quoted.
  T4  Does the published closed form `eps(Delta) = h^2/2 - h` hold?

## Scope

Scope-(a) throughout. This selects nothing and wires nothing. It establishes
the candidate set, at one pin, with a per-candidate verdict on the tests the
corpus already uses -- so that an adjudication has one table to work from
instead of two disagreeing beans.
"""

from __future__ import annotations

import importlib.util
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

_SRC = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_counit_silver_ratio_adjudication_probe.py")
_spec = importlib.util.spec_from_file_location("_adj", _SRC)
_adj = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_adj)

hm = _adj.hm_sym
h = _adj.h

set_compute_dps(50)

ZERO, ONE = sp.Integer(0), sp.Integer(1)
q = sp.Symbol("q", positive=True)
z = sp.Symbol("z")

#: exact substrate pin, as a Rational -- no float64 anywhere in this file
Q0 = sp.Rational(Q_50_DIGIT_STR)
#: h(q_0) = q_0 - 1/q_0, exactly
H0 = Q0 - 1 / Q0

# 🛑 hm_sym's slot order REVERSES gram.py's canonical NF_BASIS at 3 and 4.
# Pinned by construction in `_assert_slots`, never by comment -- an earlier
# probe reused NF_NAMES positionally and reported L+ and L- swapped.
BASIS = ["gamma", "sigma_0", "sigma_1", "L-", "L+", "e^-"]
I_LMINUS, I_LPLUS, I_EMINUS = 3, 4, 5

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_data(name, bool(ok))
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def _assert_slots() -> None:
    ident = [ONE] + [ZERO] * 5
    s0s1 = hm(hm(ident, ONE, ZERO, 0), ONE, ZERO, 1)
    s1s0 = hm(hm(ident, ONE, ZERO, 1), ONE, ZERO, 0)
    assert s0s1[I_LPLUS] == 1 and s0s1[I_LMINUS] == 0, f"L+ slot: {s0s1}"
    assert s1s0[I_LMINUS] == 1 and s1s0[I_LPLUS] == 0, f"L- slot: {s1s0}"


def at_q0(e):
    """Exact h -> h(q_0) substitution, then a 40-dps readout. No float64."""
    return mp.mpf(str(sp.N(sp.sympify(e).subs(h, H0), 40)))


# ---------------------------------------------------------------- candidates

def nuc9(kind: str):
    """`pyhecke.atom.build_nucleon_nf`: B_3 + 3 quark pairs, NO gluon.
    Its own docstring: "No separate gluon dressing -- B_3 IS the gluon
    structure"."""
    nf = [ONE] + [ZERO] * 5
    for _ in range(3):
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h, 1)
    if kind == "p":
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h / 2, 0)
        nf = hm(nf, ONE, -h / 2, 1)
    else:
        nf = hm(nf, ONE, -h / 2, 0)
        nf = hm(nf, ONE, -h / 2, 0)
        nf = hm(nf, ONE, -h, 1)
    return nf


def nuc11_interleaved(kind: str):
    """`pyhecke.atom.build_atom_nf_exact`: 9-crossing core + 2 sigma_0 gluon."""
    nf = nuc9(kind)
    nf = hm(nf, ONE, ZERO, 0)
    nf = hm(nf, ONE, ZERO, 0)
    return nf


_GEN_CHAINS = {
    "p": ([0, 0, 0, 0, sp.Rational(-1, 2), 0, 0],
          [-1, -1, -1, sp.Rational(-1, 2)]),
    "n": ([0, 0, 0, sp.Rational(-1, 2), sp.Rational(-1, 2), 0, 0],
          [-1, -1, -1, -1]),
}


def nuc11_gen_grouped(kind: str):
    """`pyhecke.atom.nucleon_gen_chains`: all gen-0 crossings, then all gen-1.
    Same typed-crossing multiset as the interleaved model, different ORDER --
    and H_3(q) is not commutative across generators, so a different element."""
    g0, g1 = _GEN_CHAINS[kind]
    nf = [ONE] + [ZERO] * 5
    for d in g0:
        nf = hm(nf, ONE, d * h, 0)
    for d in g1:
        nf = hm(nf, ONE, d * h, 1)
    return nf


def nuc11_constructed(kind: str, gens=(0, 0, 1), hopf=(1, 0)):
    """The properties blocks' OWN recipe: B_3 = (sigma_0 (sigma_1 - h))^3,
    typed quark shifts, one Hopf link.

    🛑 `gens` and `hopf` are NOT corpus statements. The blocks give the typed
    SHIFTS (uu -> 0, ud -> -h/2, dd -> -h) but never say which generator each
    quark crossing sits on, and `qou-vtlj` scanned 8 assignments x 2 Hopf
    orientations for exactly that reason. Fixing one assignment and calling the
    result "the constructed Delta" would be choosing a number, so this probe
    enumerates and reports the RANGE instead -- see `constructed_variants`.
    """
    nf = [ONE] + [ZERO] * 5
    for _ in range(3):
        nf = hm(nf, ONE, ZERO, 0)
        nf = hm(nf, ONE, -h, 1)
    shifts = ([ZERO, -h / 2, -h / 2] if kind == "p" else [-h, -h / 2, -h / 2])
    for g, d in zip(gens, shifts):
        nf = hm(nf, ONE, d, g)
    for g in hopf:                     # L_- = sigma_1 sigma_0, or L_+
        nf = hm(nf, ONE, ZERO, g)
    return nf


def constructed_variants():
    """All 8 quark-generator assignments x 2 Hopf orientations = 16 readings of
    the blocks' recipe. Yields (label, net(Delta), net(n))."""
    import itertools
    for gens in itertools.product((0, 1), repeat=3):
        for hopf, hname in (((1, 0), "L-"), ((0, 1), "L+")):
            p = nuc11_constructed("p", gens, hopf)
            n = nuc11_constructed("n", gens, hopf)
            yield (f"gens={gens},hopf={hname}",
                   net(delta(n, p)), net(n))


def delta(n, p):
    return [sp.simplify(sp.expand(n[k] - p[k])) for k in range(6)]


def net(d):
    return sp.simplify(sp.expand(sum(d)))


def z2_coeff(d):
    """z^2 coefficient of tr_M, with TR = [1, z, z, z^2, z^2, z(h z + 1)].
    (D1) is affine in z -- hence available -- iff this vanishes."""
    return sp.simplify(sp.expand(d[I_LPLUS] + d[I_LMINUS] + h * d[I_EMINUS]))


def main() -> int:
    _assert_slots()

    w = WitnessBuilder("qbeta-delta-candidate-census", engine="sympy+mpmath")
    w.set_description(
        "Census of the Delta-element candidates at ONE pin (proton q_0) in ONE "
        "basis. qou-bg3w and qou-vtlj each report FOUR values; their lists "
        "differ, so the union is six. Per candidate: net, whether (D1) is "
        "affine in z, the e^- coordinate, and whether the published closed "
        "form eps(Delta) = h^2/2 - h holds. Selects nothing; scope-(a)."
    )

    print("\n=== Delta candidate census, proton pin ===")
    print(f"  q_0 = {mp.nstr(Q_MP, 20)}")
    print(f"  h_0 = {mp.nstr(at_q0(h), 20)}\n")

    short_net = h**2 / 2 - h
    print(f"  published closed form: eps(Delta) = h^2/2 - h "
          f"= {mp.nstr(at_q0(short_net), 12)}\n")

    models = [
        ("nuc9_build_nucleon_nf", nuc9, 9),
        ("nuc11_interleaved_build_atom_nf_exact", nuc11_interleaved, 11),
        ("nuc11_gen_grouped_nucleon_gen_chains", nuc11_gen_grouped, 11),
    ]

    rows = []
    for name, fn, cross in models:
        d = delta(fn("n"), fn("p"))
        nt, c2, em = net(d), z2_coeff(d), sp.simplify(d[I_EMINUS])
        rows.append((name, cross, nt, c2, em))
        print(f"  --- {name}  ({cross} crossings)")
        print(f"      net(Delta)  = {mp.nstr(at_q0(nt), 14)}   exact: {sp.simplify(nt)}")
        print(f"      [z^2] tr_M  = {mp.nstr(at_q0(c2), 14)}   exact: {sp.factor(c2)}")
        print(f"      e^- coord   = {mp.nstr(at_q0(em), 14)}")
        w.add_data(f"{name}/net_at_q0", str(at_q0(nt)))
        w.add_data(f"{name}/net_exact_in_h", str(sp.simplify(nt)))
        w.add_data(f"{name}/z2_coeff_exact_in_h", str(sp.factor(c2)))
        w.add_data(f"{name}/e_minus_at_q0", str(at_q0(em)))
        w.add_data(f"{name}/crossings", cross)
        print()

    # T4 -- does the published closed form hold on any CONSTRUCTED candidate?
    holds = [nm for nm, _c, nt, _z, _e in rows
             if sp.simplify(nt - short_net) == 0]
    check("closed_form_holds_on_no_constructed_candidate", not holds,
          f"eps(Delta) = h^2/2 - h holds on: {holds or 'none of the four'} "
          f"-- so the 27-site incumbent value comes from the 1-/2-crossing "
          f"SHORT model alone, not from any element built here", w)

    # T2 -- (D1) availability
    affine = [nm for nm, _c, _n, c2, _e in rows if sp.simplify(c2) == 0]
    check("D1_unavailable_for_every_long_model", not affine,
          f"(D1) affine in z for: {affine or 'none'} -- the z^2 coefficient "
          f"is nonzero on all four, so alpha = (z-1)h/2 is not the "
          f"counit-minus-trace gap on any of them", w)

    # T2b -- WHICH of L+/L- vanishes on the gen-grouped element.
    # qou-bg3w: "L+ vanishes exactly for this bean's Delta_L -- the exclusion
    # there rides on L-". qou-vtlj cont.7 gives the opposite, as a closed form:
    # L_plus = -(q^2-1)(q^4+1)/(4q^3), L_minus = 0. They cannot both hold.
    d_gg = delta(nuc11_gen_grouped("n"), nuc11_gen_grouped("p"))
    lplus_gg = sp.simplify(d_gg[I_LPLUS])
    lminus_gg = sp.simplify(d_gg[I_LMINUS])
    vtlj_lplus = -(q**2 - 1) * (q**4 + 1) / (4 * q**3)
    vtlj_num = mp.mpf(str(sp.N(vtlj_lplus.subs(q, Q0), 40)))
    mine_num = at_q0(lplus_gg)
    agree = abs(mine_num - vtlj_num) < mp.mpf("1e-30")
    check("bg3w_has_L_plus_and_L_minus_swapped",
          sp.simplify(lminus_gg) == 0 and sp.simplify(lplus_gg) != 0 and agree,
          f"L- = {lminus_gg} (vanishes) and L+ = {sp.factor(lplus_gg)} "
          f"= {mp.nstr(mine_num, 14)}, which reproduces qou-vtlj cont.7's "
          f"closed form -(q^2-1)(q^4+1)/(4q^3) = {mp.nstr(vtlj_num, 14)} to "
          f"30 dps. So qou-vtlj is right and qou-bg3w's attribution is "
          f"swapped: the (D1) exclusion rides on L+, not L-", w)

    check("z2_test_needs_the_sum_not_one_coordinate",
          sp.simplify(z2_coeff(d_gg) - (lplus_gg + lminus_gg
                                        + h * d_gg[I_EMINUS])) == 0,
          f"[z^2] = d[L+] + d[L-] + h*d[e^-]; on this element L- and e^- both "
          f"vanish so it collapses to L+ alone -- but that is a property of "
          f"this element, not of the test", w)

    # T3 -- the block's e^- claim
    nonzero_em = [nm for nm, _c, _n, _z, e in rows if sp.simplify(e) != 0]
    check("e_minus_nonzero_on_some_long_models",
          len(nonzero_em) > 0,
          f"e^- coordinate is nonzero on {len(nonzero_em)}/{len(rows)}: "
          f"{nonzero_em}. qbeta-counit-closed-form.md's 'both nucleon models "
          f"happen to satisfy' e^- = 0 does NOT hold across the candidate "
          f"set, so the coordinate-sum/tr_M|_{{z=1}} agreement it licenses is "
          f"element-specific and must not be carried to another candidate", w)

    # T5 -- the 9-crossing residual qou-bg3w attributes to float64 is the PIN
    d9 = delta(nuc9("n"), nuc9("p"))
    n9 = net(d9)
    q111 = sp.Rational(111, 100)
    n9_pin = at_q0(n9)
    n9_111 = mp.mpf(str(sp.N(sp.sympify(n9).subs(h, q111 - 1 / q111), 40)))
    check("bg3w_nuc9_residual_is_the_pin_not_float64",
          abs(n9_111 - mp.mpf("-0.1883216147")) < mp.mpf("1e-9")
          and abs(n9_pin - mp.mpf("-0.188290601")) < mp.mpf("1e-8"),
          f"qou-bg3w calls -0.1883216147 the EXACT net and -0.188290601 the "
          f"float64 coordinate sum, and attributes the gap to 'float64 h "
          f"versus exact _H_FRAC'. Measured: the same exact expression gives "
          f"{mp.nstr(n9_111, 14)} at q = 111/100 and {mp.nstr(n9_pin, 14)} at "
          f"the proton pin. The gap is 185 ppm of PIN, not float64 rounding "
          f"(which would be ~1e-16). Both of bg3w's numbers are exact; they "
          f"are at different q", w)

    # T6 -- the blocks' recipe does not determine a number
    variants = list(constructed_variants())
    nets = sorted(at_q0(v) for _l, v, _n in variants)
    target_n = mp.mpf("0.7975664")
    hits = [l for l, _v, nn in variants if abs(at_q0(nn) - target_n) < mp.mpf("1e-6")]
    check("constructed_recipe_is_assignment_dependent",
          len(set(str(x)[:10] for x in nets)) > 1,
          f"{len(variants)} readings of the blocks' recipe (8 quark-generator "
          f"assignments x 2 Hopf orientations) give net(Delta) spanning "
          f"[{mp.nstr(nets[0], 12)}, {mp.nstr(nets[-1], 12)}] -- "
          f"{len(set(str(x)[:10] for x in nets))} distinct values. The corpus "
          f"fixes the SHIFTS but not the generators, so 'the constructed "
          f"Delta' is not a single number without a selection rule. "
          f"Variants reproducing the blocks' stated net(n) = 0.7975664: "
          f"{hits or 'none in this parameterisation'}", w)
    w.add_data("constructed_net_range_at_q0",
               [str(nets[0]), str(nets[-1])])
    w.add_data("constructed_variant_count", len(variants))

    # T1 -- the two 'agreeing' bottom rows are one element at two pins
    d_gen = delta(nuc11_gen_grouped("n"), nuc11_gen_grouped("p"))
    net_gen = net(d_gen)
    at_pin = at_q0(net_gen)
    q_111 = sp.Rational(111, 100)
    at_111 = mp.mpf(str(sp.N(sp.sympify(net_gen).subs(h, q_111 - 1 / q_111), 40)))
    rel = abs(at_pin - at_111) / abs(at_pin)
    check("bg3w_and_vtlj_bottom_rows_are_one_element_at_two_pins",
          rel > mp.mpf("1e-5") and rel < mp.mpf("1e-2"),
          f"gen-grouped net = {mp.nstr(at_pin, 12)} at q_0 (vtlj's -0.2331977) "
          f"vs {mp.nstr(at_111, 12)} at q = 111/100 (bg3w's -0.2332459); "
          f"rel {mp.nstr(rel, 4)}. Same element, two pins -- NOT two elements", w)

    # T7 -- what the two neutron-reproducing variants actually give for Delta
    sel = [(l, at_q0(v)) for l, v, nn in variants
           if abs(at_q0(nn) - target_n) < mp.mpf("1e-6")]
    for lab, val in sel:
        print(f"  neutron-reproducing variant {lab}: net(Delta) = "
              f"{mp.nstr(val, 14)}")
        w.add_data(f"neutron_reproducing/{lab}", str(val))
    # 🛑 This check originally asserted the OPPOSITE -- that the two
    # neutron-reproducing readings would disagree on Delta, because Delta also
    # depends on the proton reading. They agree exactly, and the agreed value
    # independently reproduces qou-vtlj's -0.2137638. Recorded as measured.
    agree_sel = len(sel) >= 2 and len({str(v)[:12] for _l, v in sel}) == 1
    vtlj_constructed = mp.mpf("-0.2137638")
    check("neutron_reproducing_variants_agree_and_match_vtlj",
          agree_sel and abs(sel[0][1] - vtlj_constructed) < mp.mpf("1e-7"),
          f"{len(sel)} of 16 readings reproduce the blocks' stated "
          f"net(n) = 0.7975664, and both give the SAME net(Delta) = "
          f"{mp.nstr(sel[0][1], 14)}, independently reproducing qou-vtlj's "
          f"constructed value -0.2137638. So within this parameterisation the "
          f"neutron constraint DOES pin Delta -- the assignment freedom that "
          f"spans [-0.2507, -0.2047] collapses once the stated neutron net is "
          f"imposed. Note this pins Delta from the NEUTRON alone; qou-vtlj "
          f"separately found no reading reproduces the stated PROTON net, so "
          f"the pin rests on one of the block's two numbers", w)

    # candidate-set size -- the FULL union, not just the fixed models
    vals = {str(at_q0(nt))[:12] for _nm, _c, nt, _z, _e in rows}
    vals.add(str(at_q0(short_net))[:12])
    vals.add(str(mp.mpf("-0.2089"))[:12])          # blocks AS STATED
    vals |= {str(at_q0(v))[:12] for _l, v, _n in variants}
    check("candidate_set_exceeds_the_four_each_bean_reports",
          len(vals) > 4,
          f"{len(vals)} distinct net values at ONE pin: 3 constructed models, "
          f"the published closed form, the blocks' stated -0.2089, and "
          f"{len({str(at_q0(v))[:12] for _l, v, _n in variants})} distinct "
          f"values from the 16 readings of the blocks' own recipe. Both "
          f"qou-bg3w and qou-vtlj report 'FOUR', and their fours differ; "
          f"neither figure is the size of the candidate set", w)
    w.add_data("distinct_net_values_at_q0", sorted(vals))

    w.add_data("q0_anchor_note", "proton pin; every value in this witness is "
                                 "at Q_50_DIGIT_STR, none at q = 111/100")
    w.save()

    print(f"\n=== {'ALL PASS' if not FAILED else 'FAILURES: ' + ', '.join(FAILED)} ===")
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
