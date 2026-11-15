#!/usr/bin/env python3
"""Bar symmetry does NOT pin the averaging weight -- it admits a whole family.

The p-n interface is `f_pn = w.b_pp + (1-w).b_nn` and the corpus takes
`w = 1/2 + d/4`, justified by bar invariance (`sigma_avg = (sigma+sigma^-1)/2`,
prop:averaging-resonance-rule). `qbeta_symmetry_sign_is_am_gm_locked_probe.py`
showed that choice is what makes the symmetry energy come out wrong-signed.
This probe shows bar invariance does not force it. Bean `qou-79wa`; the open half
of `qou-i01a`. Instantiates `QOU/Hecke/BarWeightFamily.lean`.

*** THE INVARIANCE CONDITION, DERIVED ***

Under `q -> 1/q` the bracket `[2]_q` is FIXED while `b_pp = q^2/[2]_q` and
`b_nn = q^-2/[2]_q` SWAP. So

    f_pn(1/q) = wbar . b_nn + (1-wbar) . b_pp
    f_pn(q)   = w    . b_pp + (1-w)    . b_nn

and `f_pn(1/q) = f_pn(q)` reduces to `(1 - wbar - w)(b_pp - b_nn) = 0`, i.e.

    wbar = 1 - w                for q != 1

**One equation, not a determination.**

*** THE FAMILY THAT SATISFIES IT ***

    w_k = q^-k / [2]_{q^k}          [2]_x = x + 1/x

has `wbar_k = q^k/[2]_{q^k} = 1 - w_k` for EVERY k. The corpus's `1/2` is the
`k = 0` member, and what actually pins `k = 0` is the unstated extra assumption
that `w` carries no `q` -- an undeformed bracket inside a deformed algebra,
which is the same defect the AM-GM result found, now in the premise.

*** WHERE THE SIGN LIVES ON IT ***

    k       w_k          delta        sign
    0       0.500000     -0.021618    wrong   <- the corpus
    0.5     0.473938     -0.010838    wrong
    1       0.448018      0           the geometric mean, neutral
    1.5     0.422377     +0.010838    SEMF
    2       0.397148     +0.021618    SEMF
    3       0.348408     +0.042778    SEMF

`delta(w_k)` vanishes at exactly `k = 1` and is ODD about it.

*** WHAT IS DERIVED, AND WHAT IS NOT ***

Derived: the condition `wbar = 1 - w`; that the family meets it for all `k`;
monotonicity of `w_k`; hence the BOUND `delta > 0 <=> k > 1`.

**NOT derived: `k`.** `k = 2` gives the SEMF sign and is deliberately NOT adopted
on that basis -- a target to check a derivation AGAINST, never a criterion to
search ON. The one member with an independent argument is `k = 1`: it uses the
framework's own bracket `[2]_q` and returns the loop value `1/[2]_q` exactly.
It gives ZERO symmetry term, not the SEMF one. Reported, not skipped past.
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
KS = (mp.mpf(0), mp.mpf("0.5"), mp.mpf(1), mp.mpf("1.5"),
      mp.mpf(2), mp.mpf(3), mp.mpf(4), mp.mpf(6))


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def bracket(x):
    return x + 1/x


def w_of(k, q=Q0):
    return q**(-k)/bracket(q**k)


def wbar_of(k, q=Q0):
    """`w_k` evaluated at `1/q` -- the bar image."""
    return w_of(k, 1/q)


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
    print("=" * 78)
    print("1. THE BAR INVOLUTION FIXES [2]_q AND SWAPS THE LIKE-SPECIES BONDS")
    print("=" * 78)
    print(f"    [2]_q  = {mp.nstr(TWO_Q, 16)}     [2]_(1/q) = "
          f"{mp.nstr(bracket(1/Q0), 16)}")
    print(f"    b_pp(q) = {mp.nstr(B_PP, 16)}     b_pp(1/q) = "
          f"{mp.nstr((1/Q0)**2/bracket(1/Q0), 16)}")
    print(f"    b_nn(q) = {mp.nstr(B_NN, 16)}")
    ok &= chk("bar_fixes_the_bracket_and_swaps_the_bonds",
              bool(abs(bracket(1/Q0) - TWO_Q) < TOL
                   and abs((1/Q0)**2/bracket(1/Q0) - B_NN) < TOL), True,
              note="so invariance of w.b_pp + (1-w).b_nn reduces to "
                   "(1 - wbar - w)(b_pp - b_nn) = 0, i.e. wbar = 1 - w for "
                   "q != 1. ONE equation, not a determination")

    print()
    print("=" * 78)
    print("2. THE WHOLE FAMILY w_k = q^-k/[2]_{q^k} SATISFIES IT")
    print("=" * 78)
    print(f"    {'k':>6}{'w_k':>20}{'wbar_k':>20}{'1 - w_k':>20}{'inv':>6}")
    fam, bad = [], []
    for k in KS:
        wk, wb = w_of(k), wbar_of(k)
        inv = abs(wb - (1 - wk)) < TOL
        if not inv:
            bad.append(mp.nstr(k, 4))
        fam.append({"k": mp.nstr(k, 6), "w_k": mp.nstr(wk, 20),
                    "wbar_k": mp.nstr(wb, 20),
                    "delta": mp.nstr(delta_of(wk), 20)})
        print(f"    {mp.nstr(k, 4):>6}{mp.nstr(wk, 16):>20}{mp.nstr(wb, 16):>20}"
              f"{mp.nstr(1 - wk, 16):>20}{'YES' if inv else 'NO':>6}")
    ok &= chk("every_member_is_bar_invariant", bad, [],
              note="wbar_k = q^k/[2]_{q^k} = 1 - w_k identically. Lean: "
                   "bar_weight_bar_eq_one_sub, proved for all real k")
    ok &= chk("the_corpus_rule_is_the_k_equals_zero_member",
              abs(w_of(mp.mpf(0)) - mp.mpf(1)/2) < TOL, True,
              note="w_0 = 1/2. Nothing selects it except the unstated extra "
                   "assumption that w carries no q -- an undeformed bracket "
                   "inside a deformed algebra")
    ok &= chk("and_w_one_is_the_crossing_weight",
              abs(w_of(mp.mpf(1)) - 1/(Q0**2 + 1)) < TOL, True,
              note="w_1 = q^-1/[2]_q = 1/(q^2+1), which lands exactly on the "
                   "geometric mean 1/[2]_q. Lean: weight_one plus "
                   "SymmetrySignAmGm.crossing_weight")

    print()
    print("=" * 78)
    print("3. WHERE THE SIGN LIVES ON THE FAMILY")
    print("=" * 78)
    print(f"    {'k':>6}{'w_k':>18}{'delta':>20}   sign")
    for k in KS:
        d = delta_of(w_of(k))
        print(f"    {mp.nstr(k, 4):>6}{mp.nstr(w_of(k), 14):>18}"
              f"{mp.nstr(d, 16):>20}   "
              f"{'zero' if abs(d) < TOL else ('SEMF' if d > 0 else 'wrong')}")
    ok &= chk("the_sign_is_wrong_below_k_one_and_SEMF_above_it",
              all((delta_of(w_of(k)) > TOL) == (k > 1) for k in KS if k != 1), True,
              note="w_k is strictly decreasing in k (Lean: weight_strictAnti) "
                   "and w_1 is the geometric mean, so k > 1 is exactly the "
                   "region below it. This is the DERIVED bound; k itself is not")
    ok &= chk("delta_vanishes_exactly_at_k_one",
              abs(delta_of(w_of(mp.mpf(1)))) < TOL, True)
    odd = all(abs(delta_of(w_of(1 - t)) + delta_of(w_of(1 + t))) < TOL
              for t in (mp.mpf("0.5"), mp.mpf(1)))
    ok &= chk("and_delta_is_odd_about_k_one", odd, True,
              note="delta(w_(1-t)) = -delta(w_(1+t)). The corpus at k = 0 has "
                   "k = 2 as its exact mirror, -0.021618 against +0.021618 -- "
                   "the same reflection the power means show about the "
                   "geometric mean")

    print()
    print("=" * 78)
    print("4. WHAT IS DERIVED, AND WHAT IS NOT")
    print("=" * 78)
    print("  DERIVED: the condition wbar = 1 - w; that the family meets it for")
    print("  all k; monotonicity of w_k; hence the BOUND delta > 0 <=> k > 1.")
    print()
    print("  NOT DERIVED: k. The corpus's k = 0 rests on an unstated assumption")
    print("  (w carries no q), and k = 2 -- which gives the SEMF sign -- is NOT")
    print("  adopted on that basis. It is a target to check a derivation")
    print("  AGAINST, never a criterion to search ON.")
    print()
    print("  The one member with an independent argument is k = 1: it uses the")
    print("  framework's own bracket [2]_q and returns the loop value 1/[2]_q")
    print("  exactly. It gives ZERO symmetry term, not the SEMF one.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-bar-weight-family",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "family": "w_k = q^-k/[2]_{q^k}",
                       "lean": "QOU/Hecke/BarWeightFamily.lean",
                       "note": "k is NOT derived here and nothing is wired to "
                               "production; the derived content is the bound "
                               "delta > 0 <=> k > 1"},
        "data": {"bracket": mp.nstr(TWO_Q, 20), "b_pp": mp.nstr(B_PP, 20),
                 "b_nn": mp.nstr(B_NN, 20), "family": fam,
                 "crossing_w1": mp.nstr(w_of(mp.mpf(1)), 20)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_bar_weight_family_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-bar-weight-family.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
