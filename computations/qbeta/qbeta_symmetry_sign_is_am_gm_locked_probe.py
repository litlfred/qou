#!/usr/bin/env python3
"""The symmetry energy's wrong sign is AM-GM, and the threshold is 1/(q^2+1).

A bond sum is additive in `L = -ln b`, so whether mixing protons and neutrons
binds MORE or LESS turns on `b_pn` against the GEOMETRIC mean of `b_pp`, `b_nn`.
The corpus builds `b_pn` as an ARITHMETIC (convex) one. Arithmetic beats
geometric, so the sign comes out backwards -- structurally, not numerically.
Bean `qou-i01a`; unifies `qou-q7ga`, `qou-y2np` and the sibling's
`pn-bond-cannot-be-extremal`.

*** THE EXACT DECOMPOSITION (assignment-free, no mixing model) ***

For any graph and any proton/neutron assignment, with `E = E_pp + E_pn + E_nn`,

    Sigma = (L_pp+L_nn)/2 . E  +  (L_pp-L_nn)/2 . (E_pp - E_nn)  +  delta . E_pn
    delta = L_pn - (L_pp+L_nn)/2

Holding `E` and the imbalance `E_pp - E_nn` fixed, `Sigma` is AFFINE in `E_pn`
with slope `delta`. A symmetric nucleus maximises `E_pn`; an asymmetric one
minimises it. So the law binds symmetric nuclei MORE -- the SEMF sign -- exactly
when `delta > 0`. No layout, graph or scale enters.

*** THE THRESHOLD ***

The corpus pins `b_pp = q^2/[2]_q` and `b_nn = q^-2/[2]_q` (`qou-xf14`), so

    geometric mean  sqrt(b_pp b_nn) = 1/[2]_q                       EXACT
    arithmetic mean (b_pp+b_nn)/2   = [2]_q/2 - 1/[2]_q             EXACT
    AM - GM                         = ([2]_q^2 - 4)/(2[2]_q) = h^2/(2[2]_q)

with `h = q - 1/q` the Hecke parameter itself. And `pn-bond-cannot-be-extremal`
(merged 2026-09-04) proves `b_pn = w.b_pp + (1-w).b_nn` for a convex `w`. Then

    delta <= 0   <=>   w >= 1/(q^2 + 1)

`1/(q^2+1)` is `1/2` at `q = 1` and STRICTLY BELOW `1/2` for `q > 1`. So an
equal-weight p-n bond is wrong-signed for every `q > 1`: **the deformation moves
the threshold down while the construction holds the weight at a half.** That is
`qou-q7ga`'s "the q-deformation is net-negative on binding" with a mechanism.

The corpus's own weight is `w = 1/2 + delta_flavour/4 = 0.500344`, which is
**11.7 % above** the threshold `0.448018`. To get the SEMF sign the p-n bond
would have to be weighted about a tenth further toward the n-n end.

*** AND THE BAR BRANCH IS THIS FAMILY'S ENDPOINTS ***

`delta(w=0) = +2 ln q` and `delta(w=1) = -2 ln q`, which is exactly `qou-y2np`'s
`+/- 2 ln q_0 = +/- 0.2086814` bar branch. The swap it identified is the `w=0`
end of this convex family, and the sign flips at `w = 1/(q^2+1)` in between. So
`qou-y2np`'s "one bit" is one point on a continuum, and the continuum has a
derived crossing.

*** AND w ITSELF IS DERIVED — FROM THE CONVENTION, AND NOTHING ELSE ***

`f_pn = z - h(1/2 - d/4)` (bring_color_weighted) reproduces the corpus's
degree-10 closed form for `b_pn` to **0.0 at 40 dps**, and solving
`f_pn = w.f_pp + (1-w).f_nn` gives `(1-w)h = h(1/2 - d/4)` identically. So `w` is
not a free parameter: "derive w" reduces entirely to deriving the flat `1/2` in
`sigma_avg = (sigma + sigma^-1)/2`.

And that flat half is the WHOLE miss:

    w - w* = (q^2-1)/(2(q^2+1)) + d/4
             ^^^^^^^^^^^^^^^^^^   ^^^
             0.0519819            0.000344      ratio 151.1

The one derived ingredient in `w` (the flavour split) is 151x too small to
matter. The miss is an undeformed average sitting in a deformed algebra.

*** WHICH MEANS COULD WORK: EXACTLY THOSE BELOW THE GEOMETRIC ***

`M_p . M_-p = b_pp.b_nn = GM^2` for every `p`, so `delta(-p) = -delta(p)`: the
convention at `p = +1` has the harmonic mean at `p = -1` as its EXACT mirror,
`-0.0216177` against `+0.0216177`. Since `M_p` increases in `p` and `M_0` is
geometric, the SEMF sign needs `p < 0` -- strictly below the geometric mean,
where no average with `p >= 0` can go. All three classical means have clean
forms: `AM = [2]_{q^2}/(2[2]_q)`, `GM = 1/[2]_q`, `HM = 2/([2]_q[2]_{q^2})`.

⚠ Their weights `1/2`, `q^-1/[2]_q`, `q^-2/[2]_{q^2}` LOOK like a ladder
`q^-k/[2]_{q^k}`. **They are not** -- 0.55089 vs 0.55198 at `p = 2`, and it
fails at every non-classical `p` tested. Recorded so nobody re-derives it.

*** WHAT THIS DOES NOT CLAIM ***

The POWER. Turning `E_pn` into the SEMF's `(N-Z)^2/A` needs a well-mixed
assignment (`E_pn ~ 2E.ZN/A^2`), which is a mean-field MODEL, not a theorem --
and the corpus's canonical layout is segregated, with `E_pn = 1` and no symmetry
term at all. The sign result above needs none of that; the power does. Labelled
here, not smuggled.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 40
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
TWO_Q = Q0 + 1/Q0
H = Q0 - 1/Q0
B_PP = Q0**2/TWO_Q
B_NN = Q0**-2/TWO_Q
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
TOL = mp.mpf(10)**(-30)


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def delta_of(w, bpp=B_PP, bnn=B_NN):
    """`L_pn - (L_pp+L_nn)/2` for a convex p-n weight `w`."""
    return -mp.log(w*bpp + (1 - w)*bnn) + (mp.log(bpp) + mp.log(bnn))/2


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("1. THE TWO MEANS, IN CLOSED FORM")
    print("=" * 78)
    gm, am = mp.sqrt(B_PP*B_NN), (B_PP + B_NN)/2
    print(f"    b_pp = q^2/[2]_q        = {mp.nstr(B_PP, 16)}")
    print(f"    b_pn (corpus)           = {mp.nstr(B_PN, 16)}")
    print(f"    b_nn = q^-2/[2]_q       = {mp.nstr(B_NN, 16)}")
    print(f"    GM = sqrt(b_pp b_nn)    = {mp.nstr(gm, 16)}   1/[2]_q = {mp.nstr(1/TWO_Q, 16)}")
    print(f"    AM = (b_pp+b_nn)/2      = {mp.nstr(am, 16)}   [2]_q/2 - 1/[2]_q = "
          f"{mp.nstr(TWO_Q/2 - 1/TWO_Q, 16)}")
    print(f"    AM - GM                 = {mp.nstr(am - gm, 16)}   h^2/(2[2]_q) = "
          f"{mp.nstr(H**2/(2*TWO_Q), 16)}")

    ok &= chk("geometric_mean_is_exactly_one_over_two_q", abs(gm - 1/TWO_Q) < TOL, True,
              note="b_pp b_nn = 1/[2]_q^2 identically; re-verified from "
                   "qbeta_loop_value_pinned_probe.py, not new here")
    ok &= chk("arithmetic_mean_is_two_q_over_two_minus_its_inverse",
              abs(am - (TWO_Q/2 - 1/TWO_Q)) < TOL, True,
              note="(q^2+q^-2)/(2[2]_q) = ([2]_q^2-2)/(2[2]_q)")
    ok &= chk("am_minus_gm_is_h_squared_over_twice_two_q",
              abs((am - gm) - H**2/(2*TWO_Q)) < TOL, True,
              note="[2]_q^2 - 4 = (q - 1/q)^2 = h^2, so the AM-GM gap IS the "
                   "Hecke parameter squared over 2[2]_q -- the deformation is "
                   "literally the gap")

    print()
    print("=" * 78)
    print("2. THE CORPUS b_pn IS A CONVEX COMBINATION, AND WHICH ONE")
    print("=" * 78)
    w = (B_PN - B_NN)/(B_PP - B_NN)
    flav = ((Q0 - 1)**2*(1 - Q0**-4)/3)*(1 + ((Q0 - 1)/Q0)**3)
    print(f"    recovered w = (b_pn - b_nn)/(b_pp - b_nn) = {mp.nstr(w, 16)}")
    print(f"    1/2 + delta_flavour/4                     = {mp.nstr(mp.mpf(1)/2 + flav/4, 16)}")
    print(f"    residual                                  = {mp.nstr(w - (mp.mpf(1)/2 + flav/4), 6)}")
    ok &= chk("bpn_is_a_convex_combination_of_the_like_species_bonds",
              bool(0 < w < 1), True,
              note=f"w = {mp.nstr(w, 12)}. This is the load-bearing input from "
                   "the sibling's pn-bond-cannot-be-extremal (merged "
                   "2026-09-04); verified here numerically rather than assumed")
    ok &= chk("and_it_is_the_half_plus_quarter_flavour_split_weight",
              abs(w - (mp.mpf(1)/2 + flav/4)) < mp.mpf("1e-6"), True,
              note=f"residual {mp.nstr(w - (mp.mpf(1)/2 + flav/4), 4)} -- agrees "
                   "to 6 decimals, not exactly, because the sibling's delta is a "
                   "particular flavour-split convention. Reported, not rounded away")

    print()
    print("=" * 78)
    print("3. THE SIGN THRESHOLD IS 1/(q^2+1), AND THE CORPUS SITS ABOVE IT")
    print("=" * 78)
    thr = 1/(Q0**2 + 1)
    print(f"    threshold 1/(q^2+1) = {mp.nstr(thr, 16)}")
    print(f"    corpus w            = {mp.nstr(w, 16)}   ({mp.nstr(w/thr, 8)}x the threshold)")
    print()
    print(f"    {'w':>10}{'delta(w)':>18}   sign of the symmetry term")
    sweep = []
    for wv in [mp.mpf(x)/10 for x in range(0, 11)]:
        d = delta_of(wv)
        sweep.append({"w": mp.nstr(wv, 4), "delta": mp.nstr(d, 12)})
        print(f"    {mp.nstr(wv, 4):>10}{mp.nstr(d, 12):>18}   "
              f"{'SEMF (binds symmetric more)' if d > 0 else 'WRONG'}")
    print(f"    {mp.nstr(thr, 8):>10}{mp.nstr(delta_of(thr), 6):>18}   crossing")

    ok &= chk("delta_vanishes_exactly_at_the_threshold",
              abs(delta_of(thr)) < TOL, True,
              note="w b_pp + (1-w) b_nn = 1/[2]_q  <=>  w q^2 + (1-w) q^-2 = 1 "
                   "<=>  w = (q^2-1)/(q^4-1) = 1/(q^2+1)")
    ok &= chk("the_corpus_weight_is_above_the_threshold_so_the_sign_is_wrong",
              bool(w > thr and delta_of(w) < 0), True,
              note=f"w/threshold = {mp.nstr(w/thr, 8)}; the p-n bond would have "
                   "to be weighted ~11.7 % further toward the n-n end to get "
                   "the SEMF sign")

    print()
    print("=" * 78)
    print("4. WHY IT IS THE DEFORMATION: THE THRESHOLD MOVES, THE WEIGHT DOES NOT")
    print("=" * 78)
    print(f"    {'q':>10}{'1/(q^2+1)':>16}{'delta(w=1/2)':>18}")
    qsweep = []
    for qv in ("1.0", "1.02", "1.05", "1.1099785827513808", "1.2", "1.5"):
        qq = mp.mpf(qv)
        t2 = qq + 1/qq
        d_half = delta_of(mp.mpf(1)/2, qq**2/t2, qq**-2/t2)
        qsweep.append({"q": qv, "threshold": mp.nstr(1/(qq**2 + 1), 12),
                       "delta_at_half": mp.nstr(d_half, 12)})
        print(f"    {qv:>10}{mp.nstr(1/(qq**2+1), 12):>16}{mp.nstr(d_half, 12):>18}")
    ok &= chk("equal_weight_is_wrong_signed_for_every_q_above_one",
              all(mp.mpf(r["delta_at_half"]) <= 0 for r in qsweep), True,
              note="delta(1/2) <= 0  <=>  1/2 >= 1/(q^2+1)  <=>  q >= 1. At "
                   "q = 1 it is exactly zero (b_pp = b_nn, AM = GM). Every "
                   "q > 1 breaks it, so no re-derivation of q rescues the sign")

    print()
    print("=" * 78)
    print("5. THE BAR BRANCH IS THIS FAMILY'S ENDPOINTS")
    print("=" * 78)
    d0, d1 = delta_of(mp.mpf(0)), delta_of(mp.mpf(1))
    print(f"    delta(w=0) = {mp.nstr(d0, 14)}      +2 ln q_0 = {mp.nstr(2*mp.log(Q0), 14)}")
    print(f"    delta(w=1) = {mp.nstr(d1, 14)}      -2 ln q_0 = {mp.nstr(-2*mp.log(Q0), 14)}")
    ok &= chk("the_endpoints_are_qou_y2np_s_plus_minus_two_ln_q",
              bool(abs(d0 - 2*mp.log(Q0)) < TOL and abs(d1 + 2*mp.log(Q0)) < TOL), True,
              note="qou-y2np's bar branch is the w=0 / w=1 pair of this convex "
                   "family. Its 'one bit' is two points on a continuum whose "
                   "crossing 1/(q^2+1) is derived -- which is the finer object")

    print()
    print("=" * 78)
    print("6. DERIVING w — IT IS FORCED BY THE AVERAGING CONVENTION")
    print("=" * 78)
    Z_M = Q0**3/(Q0**2 + 1)          # H is the module-level Hecke h
    flav_lead = (Q0 - 1)**2*(1 - Q0**-4)/3
    f_pn_conv = Z_M - H*(mp.mpf(1)/2 - flav_lead/4)
    print("    f_pp = z              (positive crossing, Markov axiom)")
    print("    f_nn = z - h          (negative crossing, Hecke skein)")
    print("    f_pn = z - h(1/2 - d/4)   (bring_color_weighted, default 2026-06-01)")
    print()
    print(f"    f_pn from the convention = {mp.nstr(f_pn_conv, 18)}")
    print(f"    b_pn corpus closed form  = {mp.nstr(B_PN, 18)}")
    print(f"    difference               = {mp.nstr(f_pn_conv - B_PN, 5)}")
    ok &= chk("the_convention_reproduces_the_corpus_closed_form_exactly",
              abs(f_pn_conv - B_PN) < TOL, True,
              note="the degree-10 numerator over 12q^5(q^2+1) IS z - h(1/2-d/4). "
                   "So w is not a free parameter anywhere in the corpus")
    ok &= chk("w_is_forced_to_one_half_plus_flavour_over_four",
              abs(w - (mp.mpf(1)/2 + flav_lead/4)) < TOL, True,
              note="solving z - h(1/2-d/4) = w.z + (1-w)(z-h) gives (1-w)h = "
                   "h(1/2-d/4) identically. Lean: weight_of_convention. So "
                   "'derive w' reduces entirely to deriving the flat 1/2")

    print()
    print("=" * 78)
    print("7. AND THE FLAT HALF IS THE WHOLE MISS")
    print("=" * 78)
    deform = (Q0**2 - 1)/(2*(Q0**2 + 1))
    print(f"    w - w*                      = {mp.nstr(w - thr, 18)}")
    print(f"    (q^2-1)/(2(q^2+1)) + d/4    = {mp.nstr(deform + flav_lead/4, 18)}")
    print(f"      deformation part          = {mp.nstr(deform, 14)}")
    print(f"      flavour part d/4          = {mp.nstr(flav_lead/4, 14)}")
    print(f"      ratio                     = {mp.nstr(deform/(flav_lead/4), 8)}")
    ok &= chk("the_miss_splits_as_deformation_plus_flavour",
              abs((w - thr) - (deform + flav_lead/4)) < TOL, True,
              note="Lean: weight_miss")
    ok &= chk("and_the_miss_is_the_flat_half_not_the_derived_flavour_split",
              deform/(flav_lead/4) > 100, True,
              note=f"ratio {mp.nstr(deform/(flav_lead/4), 8)}. The ONE derived "
                   "ingredient in w is 151x too small to matter; the entire "
                   "miss is an undeformed average sitting in a deformed algebra")

    print()
    print("=" * 78)
    print("8. WHICH MEANS CAN WORK: EXACTLY THOSE BELOW THE GEOMETRIC")
    print("=" * 78)
    two_q2 = Q0**2 + Q0**-2

    def power_mean(pp):
        pp = mp.mpf(pp)
        return mp.sqrt(B_PP*B_NN) if pp == 0 else ((B_PP**pp + B_NN**pp)/2)**(1/pp)

    print(f"    {'p':>6}{'M_p':>20}{'delta':>20}   sign")
    pm = []
    for pp in (3, 2, 1, mp.mpf("0.5"), 0, mp.mpf("-0.5"), -1, -2, -3):
        m = power_mean(pp)
        d_ = -mp.log(m) + (mp.log(B_PP) + mp.log(B_NN))/2
        pm.append({"p": str(pp), "M_p": mp.nstr(m, 14), "delta": mp.nstr(d_, 14)})
        print(f"    {str(pp):>6}{mp.nstr(m, 16):>20}{mp.nstr(d_, 16):>20}   "
              f"{'SEMF' if d_ > 0 else ('zero' if d_ == 0 else 'wrong')}")

    def d_of(m):
        return -mp.log(m) + (mp.log(B_PP) + mp.log(B_NN))/2

    odd = all(abs(d_of(power_mean(pp)) + d_of(power_mean(-pp))) < TOL
              for pp in (mp.mpf("0.5"), 1, 2, 3))
    ok &= chk("power_mean_delta_is_odd_under_p_to_minus_p", odd, True,
              note="M_p . M_-p = b_pp.b_nn = GM^2 for every p, so delta(-p) = "
                   "-delta(p). The convention sits at p = +1; its exact mirror "
                   "is the harmonic mean. Lean: harmonic_mul_arithmetic and "
                   "delta_harmonic_eq_neg_delta_arithmetic for p = +/-1")
    ok &= chk("the_sign_is_right_exactly_when_p_is_negative",
              all((mp.mpf(r["delta"]) > 0) == (mp.mpf(r["p"]) < 0)
                  for r in pm if mp.mpf(r["p"]) != 0), True,
              note="M_p is increasing in p and M_0 is the geometric mean, so "
                   "the SEMF sign needs a mean STRICTLY BELOW geometric -- "
                   "where no average with p >= 0 can go")

    AM_, GM_, HM_ = (B_PP + B_NN)/2, mp.sqrt(B_PP*B_NN), 2*B_PP*B_NN/(B_PP + B_NN)
    print()
    print(f"    AM = [2]_q^2/(2[2]_q)      = {mp.nstr(two_q2/(2*TWO_Q), 16)}")
    print(f"    GM = 1/[2]_q               = {mp.nstr(1/TWO_Q, 16)}")
    print(f"    HM = 2/([2]_q [2]_q^2)     = {mp.nstr(2/(TWO_Q*two_q2), 16)}")
    ok &= chk("the_three_classical_means_have_closed_two_q_forms",
              bool(abs(AM_ - two_q2/(2*TWO_Q)) < TOL and abs(GM_ - 1/TWO_Q) < TOL
                   and abs(HM_ - 2/(TWO_Q*two_q2)) < TOL), True,
              note="with [2]_x = x + 1/x. Lean: arithmetic_pinned, "
                   "harmonic_pinned; AM.HM = GM^2 closes the triple")

    print()
    print("    ⚠ AND A PATTERN THAT IS NOT ONE:")
    print("      w(AM) = 1/2, w(GM) = q^-1/[2]_q, w(HM) = q^-2/[2]_q^2 look like")
    print("      a ladder q^-k/[2]_{q^k}. Tested off the classical points:")
    ladder = []
    for pp in (2, mp.mpf("0.5"), -2, -3):
        k = 1 - mp.mpf(pp)
        pred = Q0**(-k)/(Q0**k + Q0**-k)
        act = (power_mean(pp) - B_NN)/(B_PP - B_NN)
        ladder.append({"p": str(pp), "actual": mp.nstr(act, 12),
                       "ladder_prediction": mp.nstr(pred, 12)})
        print(f"        p={str(pp):>5}  actual {mp.nstr(act, 10):>14}   "
              f"ladder says {mp.nstr(pred, 10):>14}")
    ok &= chk("the_weight_ladder_is_a_coincidence_of_the_three_classical_means",
              all(abs(mp.mpf(r["actual"]) - mp.mpf(r["ladder_prediction"]))
                  > mp.mpf("1e-6") for r in ladder), True,
              note="it fails at every non-classical p tested -- 0.55089 vs "
                   "0.55198 at p=2. Recorded so nobody re-derives it as "
                   "structure; the near-pattern is exactly what the anti-fit "
                   "discipline is for")

    print()
    print("=" * 78)
    print("9. WHAT IS CLOSED")
    print("=" * 78)
    print("  The synthesis audit called the symmetry energy 'a named gap with NO")
    print("  available route'. There IS a route -- the p-n interface count -- and")
    print("  it is SIGN-LOCKED: a log-additive law compares against a geometric")
    print("  mean, the construction supplies an arithmetic one, and AM > GM")
    print("  whenever q > 1. Stronger than 'no route found', and it names the")
    print("  single quantity a repair must change: the convex weight w, which")
    print("  must fall below 1/(q^2+1) = 0.448018.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-symmetry-sign-is-am-gm-locked",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "b_pp": mp.nstr(B_PP, 20), "b_pn": mp.nstr(B_PN, 20),
                       "b_nn": mp.nstr(B_NN, 20),
                       "lean": "QOU/Hecke/SymmetrySignAmGm.lean",
                       "convexity_input": "pn-bond-cannot-be-extremal.md "
                                          "(merged 2026-09-04) -- verified "
                                          "numerically here, not re-derived"},
        "data": {"geometric_mean": mp.nstr(gm, 20),
                 "arithmetic_mean": mp.nstr(am, 20),
                 "am_minus_gm": mp.nstr(am - gm, 20),
                 "h_squared_over_two_two_q": mp.nstr(H**2/(2*TWO_Q), 20),
                 "recovered_convex_weight": mp.nstr(w, 20),
                 "threshold_one_over_q2_plus_1": mp.nstr(thr, 20),
                 "weight_over_threshold": mp.nstr(w/thr, 12),
                 "delta_at_corpus_weight": mp.nstr(delta_of(w), 20),
                 "delta_sweep_in_w": sweep,
                 "threshold_sweep_in_q": qsweep,
                 "f_pn_from_convention": mp.nstr(f_pn_conv, 20),
                 "miss_deformation_part": mp.nstr(deform, 20),
                 "miss_flavour_part": mp.nstr(flav_lead/4, 20),
                 "miss_ratio": mp.nstr(deform/(flav_lead/4), 12),
                 "power_mean_sweep": pm,
                 "failed_weight_ladder": ladder},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_symmetry_sign_is_am_gm_locked_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-symmetry-sign-is-am-gm-locked.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
