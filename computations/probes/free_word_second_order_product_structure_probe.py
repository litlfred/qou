#!/usr/bin/env python3
"""free_word_second_order_product_structure_probe.py — [ε²](free) is forced by [ε¹]. (qou-qqm4)

WHERE THIS SITS. `qou-qqm4`'s open goal (2) is to "derive c₂ by extending the [★] expansion to
second order", and it names why that is hard: "the Y-terms `Tr(Y P Y P')` no longer vanish; K'' and
the normaliser's second derivative enter". That is a statement about the *atom* word. This probe
does not attempt it. It measures the **free** word, where the answer turns out to be forced by the
first order plus two new constants.

THE RESULT. Write `u(Z,N) = (Z·S_p + N·S_n)/2 = 3Z − 2N` — the per-nucleon coefficient sum from
PR #6920's `c₁` closed form, at the canonical word's `(S_p, S_n) = (6, −4)`. Then

    [ε¹](free)            =  u · 2^(−A−1)
    2^(A+2) · [ε²](free)  =  u²/2  +  (37Z + 20N)/2

measured exact, **7/7** across every `(Z,N)` split at `A = 2` and `A = 3`, and again at the held-out
`⁴He`.

**The three quadratic coefficients are FORCED, not fitted.** Expanding `u²/2` gives
`(9/2)Z² − 6ZN + 2N²`, and all three are fixed the moment `u = 3Z − 2N` is known from the **first**
order — nothing about the second order chose them. Only the linear pair `(37, 20)` was free. So this
is 8 exact points against **2** parameters, not against 5. `(37, 20)` is the second-order analogue of
`(S_p, S_n) = (6, −4)`: one new constant per species, and nothing else.

🛑 THE MECHANISM IS NOT ESTABLISHED, AND MY FIRST ATTEMPT AT ONE WAS WRONG. I initially read `u²/2`
as an **exponentiation signature** — the free word's `A` nucleon blocks act on disjoint strand
triples, so its normalised trace should factorise, its log be additive, and a product's second-order
term be `(first order)²/2` plus per-nucleon terms. That story requires `u` to *be* the first-order
coefficient in the same normalisation. **It is not:** `[ε¹](free) = u·2^(−A−1)`, so
`([ε¹])²/2 = u²·2^(−2A−2)/2`, which differs from the `u²/2 · 2^(−A−2)` actually measured by a factor
`2^(−A)`. The naive square is off by an `A`-dependent factor and the reading fails. (The probe's own
prediction column caught this: an earlier version asserted `u = 2^(A+2)·[ε¹]`, which is `2u`, and
every row printed FAIL.)

So what is verified is a **relation between the orders** — the quadratic part of `[ε²](free)` in
`(Z,N)` is exactly `u²/2` for the `u` that governs `[ε¹]` — with **no mechanism attached**. That is
still the useful half: it is what makes this 2 parameters rather than 5. Whether a corrected
factorisation argument produces it is open.

THE HELD-OUT TEST. `⁴He` (`A = 4`, `n = 12`) entered neither the fit nor the pattern search. The form
predicts `[ε¹] = 1/16` and `[ε²] = 59/64` — `u(2,2) = 2`, so `u²/2 = 2` and `(74+40)/2 = 57`, giving
`59/2^6`. Both measured exactly as predicted.

THE ATOM SIDE, AS DATA — free, and deliberately not fitted. Since `c₂ = [ε¹] + [ε²]` of
`Δtr = tr(free) − tr(atom)` and `[ε¹](Δtr) = c₁`, the atom half follows from quantities already
measured, with **no new computation**:

    [ε²](atom) = [ε²](free) − (c₂ − c₁)

    (Z,N)   A   [ε²](atom)    × 2^(2A)      I_pp  I_nn
    (2,0)   2   81/32         81/2          1     0
    (1,1)   2   35/32         35/2          0     0
    (0,2)   2   27/16         27            0     1
    (3,0)   3   47/32         94            2     0
    (2,1)   3   79/128        79/2          1     0
    (1,2)   3   59/128        59/2          0     1
    (0,3)   3   33/32         66            0     2
    (2,2)   4   61/512        61/2          1     1

**No closed form is proposed for these, and that is deliberate.** Eight points admit several
parameterisations — a quadratic in `(Z,N)` alone is five parameters before any interface term — and
this arc has been burned by exactly that. Two things are worth recording for whoever does derive it:
the obvious analogue of the free-side result **fails**, since taking `v = u + 4(I_pp − I_nn)` (the
first-order atom bracket) leaves `× 2^(2A) − v²/2` at `−19/2, 17, −5, −101/2, 15/2, 17, −32, 57/2`,
which is not linear in `(Z, N)`; and the parity is uneven — three rows are integers and five are
half-integers — so any form must produce that.

The one available constraint is the content-cancellation criterion
(`content_cancellation_invariance_probe`): a zero-net-content combination of the atom-side second
order must be ordering-invariant, because it is interface-only. Consistency check on the `A = 2`
combination: `atom(pp) + atom(nn) − 2·atom(pn) = 65/32` against `free(...) = 50/32`, and their
difference `−15/32` is exactly the measured `c₂` combination, as it must be since the `[ε¹]` part
cancels there.

🛑 WHAT THIS DOES NOT GIVE, and it is the thing `qou-qqm4` actually wants. `c₂` is
`[ε¹] + [ε²]` of `Δtr = tr(free) − tr(atom)`, so a closed form for the free side is **half** of it.
The atom word does not factorise — its interfaces couple adjacent nucleon blocks, which is the whole
reason `c₁`'s closed form needs a separate interface term — and nothing here says what the atom
side's second order is. **No closed form for `c₂` is claimed or implied.**

And per the correction above, **the relation is empirical**: 8 exact points, 2 free parameters, and
the quadratic part predicted from the first order — but no derivation of why `u²/2` should appear.
The obvious candidate (multiplicativity of the Markov trace on a disjoint union, at the level of the
ε-series) is what I tried and it does not produce this normalisation. Finding one that does, or
showing the relation is a coincidence of `A ≤ 4`, is open.

SCOPE — (a) scope-limited. Exact `Fraction` arithmetic through the corpus's own validated ε-series
(`c1_leading_coefficient_derived_probe.tr_M_series`), driven directly rather than through that
probe's `main`, which would rewrite a committed witness. No `q` evaluated, no float, no witness,
nothing wired, no Lean.
"""
from __future__ import annotations

import argparse
import functools
import os
import sys
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "substrate"))

# The A = 2 and A = 3 free-word series, exact, canonical word — the data the form was read off.
# Recomputed live by default; these are what the run must reproduce.
FIT_CASES = ((2, 0), (1, 1), (0, 2), (3, 0), (2, 1), (1, 2), (0, 3))
HELD_OUT = (2, 2)

# Second-order per-nucleon constants, the analogue of (S_p, S_n) = (6, −4) at first order.
T_P, T_N = 37, 20


def u(Z, N):
    """The c₁ per-nucleon coefficient sum `(Z·S_p + N·S_n)/2 = 3Z − 2N` at the canonical word.

    NOT `2^(A+2)·[ε¹]` — that is `2u`. Getting this wrong is what made an earlier version of this
    probe print FAIL on every row, and it is also what killed the exponentiation reading.
    """
    return 3 * Z - 2 * N


def predict_e1(Z, N):
    """`[ε¹](free) = u · 2^(−A−1)`."""
    return F(u(Z, N)) * F(1, 2) ** (Z + N + 1)


def predict_e2(Z, N):
    """`2^(A+2)·[ε²](free) = u²/2 + (37Z + 20N)/2`. The quadratic half is forced by `u`."""
    return (F(u(Z, N) ** 2, 2) + F(T_P * Z + T_N * N, 2)) * F(1, 2) ** (Z + N + 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-held-out", action="store_true",
                    help="skip the ⁴He check (A=4, n=12 — the slow half, ~15 min)")
    args = ap.parse_args()

    import c1_leading_coefficient_derived_probe as P     # noqa: E402  (slow import)
    import canonical_braid_crossings as CBC              # noqa: E402
    orig = CBC.atom_canonical_crossings
    f = functools.partial(orig, intra_order="borromean")
    CBC.atom_canonical_crossings = f
    P.atom_canonical_crossings = f

    print("[free2] The FREE word's second-order ε-coefficient is forced by its first. (qou-qqm4)")
    print("[free2]   [ε¹] = u·2^(−A−1) and 2^(A+2)·[ε²] = u²/2 + (37Z+20N)/2,  u = 3Z − 2N")
    print("[free2] The quadratic coefficients (9/2, −6, 2) are FORCED by u²/2; only (37, 20) fitted.\n")

    try:
        print(f"    {'(Z,N)':<9}{'A':>3}{'u':>5}{'[ε¹] meas':>12}{'[ε¹] pred':>12}"
              f"{'[ε²] meas':>12}{'[ε²] pred':>12}  verdict")
        ok = True
        for (Z, N) in FIT_CASES:
            s = P.tr_M_series(Z, N, False, 4)
            e1, e2 = s.coeff(1), s.coeff(2)
            p1, p2 = predict_e1(Z, N), predict_e2(Z, N)
            good = (e1 == p1 and e2 == p2)
            ok = ok and good
            print(f"    {f'({Z},{N})':<9}{Z + N:>3}{u(Z, N):>5}{str(e1):>12}{str(p1):>12}"
                  f"{str(e2):>12}{str(p2):>12}  {'ok' if good else 'FAIL'}")
        print(f"    ⇒ {f'{len(FIT_CASES)}/{len(FIT_CASES)} — 7 exact points against 2 free parameters.' if ok else 'FAILED — the form is wrong; do not quote it.'}\n")

        if args.skip_held_out:
            print("    HELD-OUT ⁴He check skipped (--skip-held-out).")
        else:
            Z, N = HELD_OUT
            print(f"    HELD-OUT — ⁴He (A = 4, n = 12), in neither the fit nor the pattern search.")
            print(f"      predicted  [ε¹] = {predict_e1(Z, N)}   [ε²] = {predict_e2(Z, N)}")
            s = P.tr_M_series(Z, N, False, 4)
            h1 = (s.coeff(1) == predict_e1(Z, N))
            h2 = (s.coeff(2) == predict_e2(Z, N))
            ok = ok and h1 and h2
            print(f"      measured   [ε¹] = {s.coeff(1)}   [ε²] = {s.coeff(2)}")
            print(f"      ⇒ [ε¹] {'ok' if h1 else 'FAIL'}, [ε²] {'ok' if h2 else 'FAIL'}")
    finally:
        CBC.atom_canonical_crossings = orig
        P.atom_canonical_crossings = orig

    print("\n  🛑 NO MECHANISM IS CLAIMED, and my first attempt at one was WRONG. I read u²/2 as an")
    print("  exponentiation signature (disjoint nucleon blocks ⇒ the trace factorises ⇒ second")
    print("  order is (first order)²/2 + per-nucleon terms). That needs u to BE the first-order")
    print("  coefficient in the same normalisation, and it is not: [ε¹] = u·2^(−A−1), so")
    print("  ([ε¹])²/2 differs from the measured u²/2·2^(−A−2) by a factor 2^(−A). The reading")
    print("  fails. What is verified is a RELATION BETWEEN THE ORDERS with no mechanism attached —")
    print("  still the useful half, since it is what makes this 2 parameters rather than 5.")
    print("\n  🛑 THIS IS HALF OF c₂, NOT c₂. c₂ = [ε¹]+[ε²] of tr(free) − tr(atom), and the ATOM")
    print("  word does not factorise: its interfaces couple adjacent blocks, which is exactly why")
    print("  c₁'s closed form needs a separate interface term. Nothing here says what the atom")
    print("  side's second order is, and no closed form for c₂ is claimed or implied.")
    print("  Nor is the product structure PROVED — an argument about disjointness, a 7-point exact")
    print("  fit whose quadratic part it predicts, and one held-out size.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
