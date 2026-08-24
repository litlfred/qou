#!/usr/bin/env python3
"""
d_frame_prefactor_localisation_probe.py — the uniform 6 in the D-frame
prefactor lives entirely in the single inter-nucleon interface crossing.

WHAT THIS SETTLES.  Bean `qou-cxon` adjudicated `qou-iayk` and left one
sub-question explicitly open:

    "The 2^(2A+1) prefactor is derived by crossing-counting, which is
     convention-FREE — yet it moves 32 -> 192.  So crossing-counting alone
     does not determine it.  That needs a real derivation, not a re-count."

This probe does not derive the value 6.  It *localises* it, which turns an
unexplained global constant into a statement about one identified crossing,
and it does so by a falsification test rather than by pattern-matching.

## The measurement

`tr_M_atomic(Z, N)` is an integer-coefficient rational function of q.  Take
the integer content of its denominator — the "prefactor" — and compare it
against the convention-C law's `2^(2A+1)`
(`d_u_closed_form_proof.py`, derived by counting averaged crossings: each
averaged crossing contributes (sigma + sigma^-1)/2, giving 2A halvings for the
nucleons plus 1 for the single mixed (p,n) interface of canonical pppnnn
ordering).

    atom      A   inter=ON   ratio    inter=OFF   ratio    ON/OFF
    proton    1          4     1/2            4     1/2         1
    neutron   1          4     1/2            4     1/2         1
    D         2        192       6           16     1/2        12
    T         3        768       6           64     1/2        12
    3He       3        768       6           64     1/2        12
    4He       4       3072       6          256     1/2        12

## What it shows

1. **With the interface off, the D prefactor is exactly `2^(2A)` in every
   case** — ratio 1/2 against the C law's `2^(2A+1)`, uniformly.  So the
   *intra-nucleon* half of the crossing-count derivation transfers to
   convention D unchanged; only the "+1" does not.

2. **A = 1 has no inter-nucleon crossing at all** (structurally — there is no
   second nucleon), and it already sits at ratio 1/2 with the interface
   nominally on.  That is an independent confirmation that does not rely on
   the `include_inter` switch behaving as advertised.

3. **Switching the interface on multiplies the prefactor by exactly 12**, for
   every A >= 2, independent of A, Z and N.  The C law gives that same
   crossing a factor 2 (one halving).  `12 / 2 = 6` — the whole of the
   uniform 6, attached to one crossing.

## Why crossing-counting could not have found it

`12 = 2^2 * 3`, and the 3 is not a count of anything.  Under the canonical
`bring_color_weighted` p/n convention the inter-nucleon crossing carries the
colour weight

    delta(q) = (q - 1)^2 * (1 - q^-4) / 3

(`markov_peel.py:100`, the symbolic mirror of
`_li_2_q_util.flavor_split_leading`).  Its rational coefficient has a 3 in the
denominator.  A crossing count sees a crossing; it cannot see the coefficient
that crossing carries.  So the C proof's `2^(2A+1)` is not *wrong* about the
crossings — it is silent about the colour weight, and the colour weight is
where the discrepancy lives.

This does not close the sub-question.  It relocates it, from "why does a
convention-free count move?" to "derive the interface factor 12 from
delta(q)", which is a much smaller and better-posed target.  Stating the
localisation is not a derivation of 12 and must not be cited as one.

## Scope (per AGENTS.md refuted/ruled-out discipline)

Every claim here is scope-(a): a measurement of these six configurations under
the canonical `bring_color_weighted` convention at convention D.  Nothing here
excludes any ingredient from any closure.

Exact rationals throughout — sympy over Q(q), no float anywhere, no anchor
enters (`tr_M_atomic` is symbolic in q).

Output: `d-frame-prefactor-localisation.witness.json`.
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

q = sp.Symbol("q")

# (label, Z, N).  A=1 first: it is the no-interface control and costs ~0.2 s.
ATOMS = [("proton", 1, 0), ("neutron", 0, 1), ("D", 1, 1),
         ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


def denominator_content(Z: int, N: int, *, include_inter: bool) -> sp.Integer:
    """Integer content of the denominator of tr_M_atomic(Z, N).

    Exact: `tr_M_atomic` returns an integer-coefficient rational function of
    the symbolic q, so `factor_list` on the cancelled denominator gives the
    content as an exact Integer.  No float is formed at any point.
    """
    import markov_peel as mkp
    tr = sp.cancel(sp.together(sp.sympify(
        mkp.tr_M_atomic(Z, N, include_inter=include_inter))))
    _num, den = sp.fraction(tr)
    content, _factors = sp.factor_list(sp.expand(den))
    return sp.Integer(content)


def main() -> int:
    rows = []
    print(f"{'atom':8s} {'Z':>2s} {'N':>2s} {'A':>2s} | {'inter=ON':>9s} "
          f"{'ratio':>6s} | {'inter=OFF':>9s} {'ratio':>6s} | {'ON/OFF':>6s}")
    for label, Z, N in ATOMS:
        t0 = time.time()
        A = Z + N
        on = denominator_content(Z, N, include_inter=True)
        off = denominator_content(Z, N, include_inter=False)
        ref_c = sp.Integer(2) ** (2 * A + 1)
        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A,
            "prefactor_inter_on": str(on),
            "prefactor_inter_off": str(off),
            "c_law_2_pow_2A_plus_1": str(ref_c),
            "ratio_on_over_c": str(sp.Rational(on, ref_c)),
            "ratio_off_over_c": str(sp.Rational(off, ref_c)),
            "interface_factor_on_over_off": str(sp.Rational(on, off)),
            "off_equals_2_pow_2A": bool(off == sp.Integer(2) ** (2 * A)),
            "elapsed_sec": f"{time.time() - t0:.2f}",
        })
        print(f"{label:8s} {Z:2d} {N:2d} {A:2d} | {str(on):>9s} "
              f"{str(sp.Rational(on, ref_c)):>6s} | {str(off):>9s} "
              f"{str(sp.Rational(off, ref_c)):>6s} | "
              f"{str(sp.Rational(on, off)):>6s}   "
              f"[{time.time() - t0:.1f}s]", flush=True)

    multi = [r for r in rows if r["A"] >= 2]
    single = [r for r in rows if r["A"] == 1]

    assertions = [
        {"name": "inter_off_prefactor_is_two_pow_2A",
         "passed": all(r["off_equals_2_pow_2A"] for r in rows),
         "note": "the intra-nucleon half of the C crossing-count derivation "
                 "transfers to convention D unchanged; only the '+1' does not"},
        {"name": "inter_off_ratio_to_c_law_is_one_half",
         "passed": all(r["ratio_off_over_c"] == "1/2" for r in rows),
         "note": "uniform across A, Z and N"},
        {"name": "single_nucleon_already_at_one_half_with_inter_on",
         "passed": all(r["ratio_on_over_c"] == "1/2" for r in single),
         "note": "A=1 has no second nucleon, so no interface exists to "
                 "switch off -- an independent check that does not rely on "
                 "the include_inter flag"},
        {"name": "interface_factor_is_uniformly_twelve",
         "passed": all(r["interface_factor_on_over_off"] == "12"
                       for r in multi),
         "note": "independent of A, Z, N -- so it is one object, not a "
                 "per-nucleon or per-strand contribution"},
        {"name": "uniform_six_equals_interface_twelve_over_c_two",
         "passed": all(r["ratio_on_over_c"] == "6" for r in multi),
         "note": "12 / 2 = 6: the C law gives this crossing a single "
                 "halving; convention D with bring_color_weighted gives it 12"},
    ]

    witness = {
        "computation": "d-frame-prefactor-localisation",
        "description": (
            "Localises the uniform factor 6 in the convention-D atomic Markov "
            "prefactor (qou-cxon Q1) to the single inter-nucleon interface "
            "crossing. With include_inter off the D prefactor is exactly "
            "2^(2A) for all six configurations (ratio 1/2 against the "
            "convention-C law 2^(2A+1)); switching the interface on "
            "multiplies by exactly 12 for every A>=2, independent of A, Z, N. "
            "A=1, which structurally has no interface, already sits at 1/2. "
            "The C law assigns that crossing a factor 2 (one averaged "
            "crossing), so 12/2 = 6 accounts for the whole discrepancy. "
            "12 = 2^2 * 3 and the 3 is not a count: the bring_color_weighted "
            "interface carries delta(q) = (q-1)^2 (1 - q^-4) / 3, which a "
            "crossing count cannot see. This LOCALISES the 6; it does NOT "
            "derive it, and must not be cited as a derivation. Scope-(a) "
            "measurement of these six configurations only."
        ),
        "convention": {
            "markov_z": "q**3/(q**2 + 1)   (convention D, canonical per the "
                        "2026-08-15 owner ruling R1)",
            "pn_convention": "bring_color_weighted (canonical per R3)",
            "anchor": (
                "NONE enters the computation: tr_M_atomic is an "
                "integer-coefficient rational function of symbolic q, and "
                "every number here is the integer content of a denominator. "
                "The top-level q0Anchor/q0Value fields are the AMBIENT stamp "
                "applied by WitnessBuilder to every witness -- they record "
                "which pin this process ran under, not an input to any value "
                "below. Do not read them as an anchor for these prefactors."
            ),
        },
        "reference_blocks": [
            "def:markov-trace",
            "prop:atomic-braid-decomposition",
        ],
        "atoms": rows,
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    out = REPO / "computations" / "d-frame-prefactor-localisation.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  allPassed = {witness['allPassed']}   "
          f"-> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
