#!/usr/bin/env python3
"""Derive k: only k = 0 and k = 1 have arguments, and neither gives the SEMF sign.

`qbeta_bar_weight_family_probe.py` reduced the averaging rule to one scalar: bar
invariance admits the whole family `w_k`, and the corpus's `1/2` is the `k = 0`
member. This probe asks what selects `k`. Bean `qou-yf02`; instantiates the
second half of `QOU/Hecke/BarWeightFamily.lean`.

*** 1. THE FAMILY IS SIMPLER THAN ITS DEFINITION ***

    w_k = q^-k/[2]_{q^k} = 1/(q^{2k}+1) = 1/(1 + (b_pp/b_nn)^(k/2))

since `b_pp/b_nn = q^4`. So **`k/2` is literally the power of the bond ratio the
average is weighted by**: `k = 0` weights by ratio^0 (flat), `k = 1` by its
square root, `k = 2` by the ratio itself. And the interface closes as

    f_pn(k) = [2]_{q^(2-k)} / ([2]_q . [2]_{q^k})

one expression covering the arithmetic mean (k=0), the geometric (k=1) and the
harmonic (k=2).

*** 2. THE REFLECTION IS ONE LINE FROM IT ***

    f_pn(k) . f_pn(2-k) = 1/[2]_q^2 = GM^2

so `k -> 2-k` INVERTS the interface about the loop value, `delta` is odd about
`k = 1`, and `k = 1` is the only fixed point.

*** 3. WHICH MEMBERS HAVE AN ARGUMENT — the enumeration is the result ***

  k = 0   the UNDEFORMED limit. `w_0 = 1/2` is what "flat average" MEANS, so it
          is derived -- from an assumption the deformation contradicts.  WRONG SIGN.
  k = 1   the unique member whose interface IS the loop value `1/[2]_q`, and the
          unique fixed point of the reflection. Two independent characterisations
          of one point.  ZERO.

**Nothing in the SEMF-signed region `k > 1` has an argument.**

*** 4. THE TWO READINGS OF k = 2 I CONSIDERED, AND WHY NEITHER IS A PRINCIPLE ***

  (A) `w_2 = b_nn/(b_pp + b_nn)` -- weight each branch by the OTHER's bond
      factor. A cross-weighting with no stated motivation anywhere in the corpus.
  (B) `k = 2` is the harmonic mean, which is what one averages when averaging
      RATES (parallel resistances, inverse times). But the bond factors are
      trace amplitudes, and nothing identifies them with a reciprocal quantity.

Both are stories. Written down so a successor attacks them rather than
rediscovering them. **`k = 2` gives the SEMF sign and is NOT adopted for that
reason** -- a target to check a derivation AGAINST, never a criterion to search ON.

*** 5. SO THE DERIVABLE PREDICTION IS k = 1, delta = 0 ***

The p-n interface contributes NO symmetry energy, and the SEMF term comes from
outside this channel. Falsifiable, and the honest close. What would overturn it
is a principle producing `k` from the ALGEBRA -- a strand count, a colour count,
a Casimir -- rather than from a choice of mean.
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
B_PP = Q0**2/TWO_Q
B_NN = Q0**-2/TWO_Q
TOL = mp.mpf(10)**(-30)


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def bq(x):
    return x + 1/x


def w_def(k):
    """The definitional form."""
    return Q0**(-k)/bq(Q0**k)


def w_simple(k):
    return 1/(Q0**(2*k) + 1)


def w_ratio(k):
    return 1/(1 + (B_PP/B_NN)**(k/2))


def f_pn(k):
    """Interface closed form."""
    return bq(Q0**(2 - k))/(TWO_Q*bq(Q0**k))


def delta_of(w):
    return -mp.log(w*B_PP + (1 - w)*B_NN) + (mp.log(B_PP) + mp.log(B_NN))/2


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
    KS = (mp.mpf(0), mp.mpf("0.5"), mp.mpf(1), mp.mpf("1.5"), mp.mpf(2), mp.mpf(3))

    print("=" * 78)
    print("1. THREE FORMS OF THE SAME WEIGHT, AND k/2 IS THE BOND-RATIO POWER")
    print("=" * 78)
    print(f"    b_pp/b_nn = q^4 = {mp.nstr(B_PP/B_NN, 16)}")
    print(f"    {'k':>6}{'q^-k/[2]_{q^k}':>22}{'1/(q^2k+1)':>22}{'1/(1+r^(k/2))':>22}")
    for k in KS:
        print(f"    {mp.nstr(k, 4):>6}{mp.nstr(w_def(k), 18):>22}"
              f"{mp.nstr(w_simple(k), 18):>22}{mp.nstr(w_ratio(k), 18):>22}")
    ok &= chk("the_three_forms_agree",
              all(abs(w_def(k) - w_simple(k)) < TOL and abs(w_def(k) - w_ratio(k)) < TOL
                  for k in KS), True,
              note="w_k = 1/(q^2k+1) = 1/(1 + (b_pp/b_nn)^(k/2)). So k/2 is "
                   "LITERALLY the power of the bond ratio the average is "
                   "weighted by. Lean: weight_eq_inv_rpow")

    print()
    print("=" * 78)
    print("2. THE INTERFACE CLOSED FORM AND ITS REFLECTION")
    print("=" * 78)
    print(f"    f_pn(k) = [2]_(q^(2-k)) / ([2]_q [2]_(q^k))")
    print(f"    {'k':>6}{'direct':>22}{'closed form':>22}{'named mean':>14}")
    names = {mp.mpf(0): "arithmetic", mp.mpf(1): "geometric", mp.mpf(2): "harmonic"}
    fam = []
    for k in KS:
        direct = w_def(k)*B_PP + (1 - w_def(k))*B_NN
        fam.append({"k": mp.nstr(k, 6), "w_k": mp.nstr(w_def(k), 20),
                    "f_pn": mp.nstr(f_pn(k), 20),
                    "delta": mp.nstr(delta_of(w_def(k)), 20)})
        print(f"    {mp.nstr(k, 4):>6}{mp.nstr(direct, 18):>22}"
              f"{mp.nstr(f_pn(k), 18):>22}{names.get(k, ''):>14}")
    ok &= chk("the_interface_closed_form_is_exact",
              all(abs(w_def(k)*B_PP + (1 - w_def(k))*B_NN - f_pn(k)) < TOL
                  for k in KS), True,
              note="one expression covering AM (k=0), GM (k=1) and HM (k=2). "
                   "Lean: interface_closed_form")
    ok &= chk("k_maps_to_two_minus_k_inverts_about_the_loop_value",
              all(abs(f_pn(k)*f_pn(2 - k) - 1/TWO_Q**2) < TOL for k in KS), True,
              note=f"f(k).f(2-k) = 1/[2]_q^2 = {mp.nstr(1/TWO_Q**2, 16)} for every "
                   "k. That is WHY delta is odd about k = 1, and why k = 1 -- the "
                   "only fixed point -- is where it vanishes. Lean: "
                   "interface_reflection")
    ok &= chk("and_k_one_is_exactly_the_loop_value",
              abs(f_pn(mp.mpf(1)) - 1/TWO_Q) < TOL, True,
              note=f"f_pn(1) = 1/[2]_q = {mp.nstr(1/TWO_Q, 18)}. Lean: "
                   "interface_one_eq_loop_value")

    print()
    print("=" * 78)
    print("3. WHERE THE CORPUS ACTUALLY SITS — AND IT IS NEGATIVE")
    print("=" * 78)
    flav = ((Q0 - 1)**2*(1 - Q0**-4)/3)
    w_corpus = mp.mpf(1)/2 + flav/4
    k_corpus = mp.log((1 - w_corpus)/w_corpus)/(2*mp.log(Q0))
    print(f"    corpus weight  w = 1/2 + d/4 = {mp.nstr(w_corpus, 18)}")
    print(f"    solving w = 1/(q^2k+1)  ->  k = {mp.nstr(k_corpus, 14)}")
    ok &= chk("the_flavour_split_pushes_k_negative_away_from_the_SEMF_region",
              bool(k_corpus < 0), True,
              note=f"k_corpus = {mp.nstr(k_corpus, 10)}. The corpus's ONE "
                   "bar-breaking ingredient moves it further from k > 1, not "
                   "toward it -- and by 1/151 of what the sign needs anyway")

    print()
    print("=" * 78)
    print("4. WHICH MEMBERS HAVE AN ARGUMENT")
    print("=" * 78)
    print(f"    {'k':>6}{'w_k':>18}{'delta':>20}{'argument':>34}")
    cand = [
        (mp.mpf(0), "undeformed limit: 'flat average'"),
        (mp.mpf(1), "interface IS the loop value 1/[2]_q"),
        (mp.mpf(2), "-- none (see the two readings)"),
    ]
    for k, arg in cand:
        d = delta_of(w_def(k))
        sgn = "zero" if abs(d) < TOL else ("SEMF" if d > 0 else "wrong")
        print(f"    {mp.nstr(k, 4):>6}{mp.nstr(w_def(k), 14):>18}"
              f"{mp.nstr(d, 16):>20}{arg:>34}   {sgn}")
    ok &= chk("no_member_of_the_SEMF_region_has_an_argument",
              bool(delta_of(w_def(mp.mpf(0))) < 0
                   and abs(delta_of(w_def(mp.mpf(1)))) < TOL
                   and delta_of(w_def(mp.mpf(2))) > 0), True,
              note="k = 0 (derived, wrong sign) and k = 1 (derived, zero) are "
                   "the only members with arguments. k = 2 gives the SEMF sign "
                   "and has none -- NOT adopted on that basis")

    print()
    print("=" * 78)
    print("5. THE DERIVABLE PREDICTION")
    print("=" * 78)
    print("  k = 1: the p-n interface carries the loop value, delta = 0, and the")
    print("  p-n channel contributes NO symmetry energy. The SEMF symmetry term")
    print("  comes from outside this channel.")
    print()
    print("  Two readings of k = 2 were considered and neither is a principle:")
    print("   (A) w_2 = b_nn/(b_pp+b_nn) -- weight each branch by the OTHER's")
    print("       bond factor. A cross-weighting with no corpus motivation.")
    print("   (B) the harmonic mean is what one averages when averaging RATES.")
    print("       But the bond factors are trace amplitudes, and nothing")
    print("       identifies them with a reciprocal quantity.")
    print()
    print("  What would overturn this: a principle producing k from the ALGEBRA")
    print("  -- a strand count, a colour count, a Casimir -- rather than from a")
    print("  choice of mean.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-averaging-index-k",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "family": "w_k = 1/(q^{2k}+1) = 1/(1+(b_pp/b_nn)^(k/2))",
                       "interface": "f_pn(k) = [2]_{q^(2-k)}/([2]_q [2]_{q^k})",
                       "lean": "QOU/Hecke/BarWeightFamily.lean",
                       "note": "k is NOT derived; the result is the ENUMERATION "
                               "-- only k = 0 and k = 1 have arguments and "
                               "neither gives the SEMF sign. Nothing wired."},
        "data": {"bond_ratio_q4": mp.nstr(B_PP/B_NN, 20),
                 "loop_value": mp.nstr(1/TWO_Q, 20),
                 "reflection_product": mp.nstr(1/TWO_Q**2, 20),
                 "family": fam,
                 "corpus_weight": mp.nstr(w_corpus, 20),
                 "corpus_k": mp.nstr(k_corpus, 16)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_averaging_index_k_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-averaging-index-k.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
