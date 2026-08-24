#!/usr/bin/env python3
"""
d_frame_interface_twelve_derivation_probe.py — the interface factor 12 IS the
denominator of `1/2 - delta/4`, and the prefactor is the product of per-crossing
denominator contents.

WHAT THIS SETTLES.  `qou-cxon` Q1, which the prior probe LOCALISED but did not
derive:

    "This localises the 6; it does not derive 12. The open question moves to
     'derive 12 from delta(q)': one crossing, one known coefficient."

Derived here.  The colour-weighted inter-nucleon crossing is
`sigma - h*(1/2 - delta/4)*1` with `delta = flavor_split_leading(q) =
(q-1)^2 (1 - q^-4) / 3`.  Its exact coefficient is

    d_iface = (q-1)(q+1)(q^6 - 2q^5 - 5q^4 - q^2 + 2q - 1) / (12 q^5)

    denominator integer content = 12
    numerator   integer content = 1     <- nothing cancels

**The 12 is `4 * 3`**: the colour-averaging quarter in `delta/4`, times
`delta`'s own third.  `1/2 - X/(3*4) = (6 - X)/12`.

## The model, and it is falsifiable

The prefactor (the integer content of the trace denominator) is the PRODUCT of
the per-crossing denominator integer contents:

    prefactor = 2^(#averaged intra crossings) * den_content(d_iface)

    atom      A | #avg  2^#avg x iface = predicted | measured
    proton    1 |    2       4 x     1 =         4 |        4
    neutron   1 |    2       4 x     1 =         4 |        4
    D         2 |    4      16 x    12 =       192 |      192
    T         3 |    6      64 x    12 =       768 |      768
    3He       3 |    6      64 x    12 =       768 |      768
    4He       4 |    8     256 x    12 =      3072 |     3072

6/6.  `A = 1` has no interface and the model predicts `2^(2A)` with no 12 --
which is the same statement the `include_inter` switch made, now as an
arithmetic consequence rather than a measurement.

## Why this derives the uniform 6

The convention-C law gives that same crossing the colour-BLIND coefficient
`-h/2`, whose denominator content is **2**.  So the two conventions differ on
that one crossing by `12 / 2 = 6` -- the whole of the uniform 6, now with a
reason: **it is the ratio of the two conventions' interface denominators**,
`(4*3)` against `2`.

## A measurement trap, recorded because it cost a wrong reading

`atom_braid_word_3A(..., q=q)` labels the interface crossing with a FLOAT --
`0.41666666666666666666666666666666666666666666666666666666667` (= 5/12 at
~60 dps, mpmath rather than float64).  Reading denominator content off the
WORD therefore gives 1 for that crossing, and the product model appears to
fail: it returns 16 for both `include_inter=True` and `False`, against
measured 192 and 16.  The float is only a template LABEL -- `crossing_from_cd`
recognises it and substitutes the exact symbolic form, which is what the trace
actually uses.  Take the coefficient from `d_for_ctype(..., delta=
flavor_split_leading(q))`, never from the word's numeric field.

An earlier attempt at this derivation tried to vary `delta`'s denominator `k`
by patching `markov_peel._COLOR_DELTA` and checking the prefactor tracked
`den_content(-h*(1/2 - delta_k/4))`.  The patch did not take -- the measured
prefactor stayed 192 for every `k`, including k where the prediction was 16,
20, 24, 48.  That run was INCONCLUSIVE, not confirming, and its `k=3` "pass"
was only the unpatched value agreeing with itself.  It is not the evidence
here; the six-atom table above is.

Exact rationals throughout; no float is formed in any measured quantity.

Output: `d-frame-interface-twelve-derivation.witness.json`.
"""
from __future__ import annotations

import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import sympy as sp  # noqa: E402
import hecke_symbolic as hs  # noqa: E402

q = hs.q
H = q - 1 / q

ATOMS = [("proton", 1, 0), ("neutron", 0, 1), ("D", 1, 1), ("T", 1, 2),
         ("3He", 2, 1), ("4He", 2, 2)]


def _content(e):
    """Integer content of the denominator of `e` as an exact rational fn."""
    e = sp.sympify(e)
    if e == 0:
        return sp.Integer(1)
    return sp.factor_list(
        sp.expand(sp.fraction(sp.cancel(sp.together(e)))[1]))[0]


def _num_content(e):
    return sp.factor_list(
        sp.expand(sp.fraction(sp.cancel(sp.together(sp.sympify(e))))[0]))[0]


def main() -> int:
    from mass_at_3A_proper import atom_braid_word_3A
    from canonical_braid_crossings import d_for_ctype
    from _li_2_q_util import flavor_split_leading
    import markov_peel as mkp

    delta = flavor_split_leading(q)
    d_iface = d_for_ctype("averaged_weighted", H, delta=delta)
    d_blind = d_for_ctype("averaged", H)

    iface_den = _content(d_iface)
    iface_num = _num_content(d_iface)
    blind_den = _content(d_blind)

    print("delta(q)      =", sp.factor(sp.cancel(sp.together(delta))))
    print("d_iface       =", sp.factor(sp.cancel(sp.together(d_iface))))
    print(f"  den content = {iface_den}   num content = {iface_num}")
    print(f"d_blind den   = {blind_den}   ratio = {sp.nsimplify(iface_den/blind_den)}")
    print()

    rows = []
    print(f"{'atom':8s} {'A':>2s} | {'#avg':>4s} {'2^#avg':>7s} x {'iface':>5s} "
          f"= {'predicted':>9s} | {'measured':>8s}  ok")
    for label, Z, N in ATOMS:
        t0 = time.time()
        A = Z + N
        word = atom_braid_word_3A(Z, N, include_inter=True, q=q)
        navg = sum(1 for _, d, _ in word if _content(d) == 2)
        iface = iface_den if A >= 2 else sp.Integer(1)
        pred = sp.Integer(2) ** navg * iface
        meas = _content(sp.sympify(mkp.tr_M_atomic(Z, N, use_fast=False)))
        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A,
            "averaged_crossings": int(navg),
            "two_pow_averaged": int(2 ** navg),
            "interface_den_content": int(iface),
            "predicted_prefactor": int(pred),
            "measured_prefactor": int(meas),
            "model_holds": bool(pred == meas),
            "elapsed_sec": f"{time.time() - t0:.2f}",
        })
        print(f"{label:8s} {A:2d} | {navg:4d} {2**navg:7d} x {str(iface):>5s} "
              f"= {str(pred):>9s} | {str(meas):>8s}  "
              f"{'YES' if pred == meas else 'no'}", flush=True)

    assertions = [
        {"name": "interface_denominator_is_twelve",
         "passed": bool(iface_den == 12),
         "note": "12 = 4*3, the colour-averaging quarter in delta/4 times "
                 "delta's own third: 1/2 - X/(3*4) = (6 - X)/12"},
        {"name": "interface_numerator_content_is_one",
         "passed": bool(abs(iface_num) == 1),
         "note": "nothing cancels the 12 -- this is what makes the "
                 "denominator survive into the prefactor"},
        {"name": "colour_blind_denominator_is_two",
         "passed": bool(blind_den == 2)},
        {"name": "uniform_six_is_the_denominator_ratio",
         "passed": bool(sp.nsimplify(iface_den / blind_den) == 6),
         "note": "12/2 = 6: the uniform 6 is the ratio of the two "
                 "conventions' interface denominators"},
        {"name": "product_model_holds_on_all_six",
         "passed": all(r["model_holds"] for r in rows),
         "note": "prefactor = 2^(#averaged) * den_content(d_iface); A=1 has "
                 "no interface and gets 2^(2A) with no 12, as an arithmetic "
                 "consequence rather than a measurement"},
    ]

    witness = {
        "computation": "d-frame-interface-twelve-derivation",
        "description": (
            "DERIVES the convention-D interface factor 12 that the prior "
            "probe only localised. The colour-weighted inter-nucleon crossing "
            "sigma - h*(1/2 - delta/4) has exact coefficient with denominator "
            "integer content 12 and numerator content 1, so nothing cancels; "
            "12 = 4*3 is the colour-averaging quarter times delta's own "
            "third. The prefactor is the PRODUCT of per-crossing denominator "
            "contents, 2^(#averaged) * 12, verified on all six atoms. The "
            "colour-blind coefficient -h/2 has denominator 2, so the uniform "
            "6 is exactly 12/2 -- the ratio of the two conventions' interface "
            "denominators. TRAP: atom_braid_word_3A labels that crossing with "
            "a ~60-dps FLOAT (5/12), so denominator content read off the WORD "
            "is 1 and the model appears to fail; the float is a template "
            "label and crossing_from_cd substitutes the exact form. Take the "
            "coefficient from d_for_ctype, never from the word. Scope-(a): "
            "these six configurations under bring_color_weighted."
        ),
        "convention": {
            "markov_z": "q**3/(q**2 + 1)   (convention D, canonical per R1)",
            "pn_convention": "bring_color_weighted (canonical per R3)",
            "delta": "flavor_split_leading(q) = (q-1)^2 (1 - q^-4) / 3",
            "anchor": (
                "NONE enters: every measured number is an integer content of "
                "an exact rational function of symbolic q. Top-level "
                "q0Anchor/q0Value are the ambient WitnessBuilder stamp."
            ),
        },
        "interface_coefficient": {
            "exact": str(sp.factor(sp.cancel(sp.together(d_iface)))),
            "denominator_content": int(iface_den),
            "numerator_content": int(iface_num),
            "colour_blind_denominator_content": int(blind_den),
            "ratio": int(sp.nsimplify(iface_den / blind_den)),
        },
        "reference_blocks": ["def:markov-trace",
                             "prop:flavor-split-substrate",
                             "prop:atomic-braid-decomposition"],
        "atoms": rows,
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = str(
        pathlib.Path(__file__).resolve().relative_to(REPO / "computations"))
    out = (REPO / "computations"
           / "d-frame-interface-twelve-derivation.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  allPassed = {witness['allPassed']}   "
          f"-> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
