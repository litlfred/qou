#!/usr/bin/env python3
"""free_word_second_order_product_structure_probe.py — the free word is a PRODUCT. (qou-qqm4)

🛑 **THIS FILE PREVIOUSLY RETRACTED THE MECHANISM IT NOW ESTABLISHES. The retraction was wrong, and
it was mine.** Read the correction below before quoting anything from this arc.

## The result

The free word's `A` nucleon blocks act on disjoint strand triples, so the normalised Markov trace
**factorises over nucleons**:

    tr(free; Z, N)  =  tr(p)^Z · tr(n)^N

where `tr(p)`, `tr(n)` are the single-nucleon normalised traces. Writing each single-nucleon series
as `a·(1 + r·ε + q·ε² + …)`, the two are measured (independently, at `n = 3`) to be

    a_p = a_n = 1/2        r_p = 3/2,  r_n = −1        q_p = 23/4,  q_n = 3

and every order-2 quantity of the multi-nucleon free word follows with **no free parameter at all**:

    [ε⁰](free)  =  a_p^Z a_n^N                       =  2^(−A)
    [ε¹](free)  =  (Z r_p + N r_n) · [ε⁰]            =  u · 2^(−A−1)
    [ε²](free)  =  [Z q_p + N q_n + (σ₁² − σ₂)/2] · [ε⁰],   σ₁ = Σ r_i,  σ₂ = Σ r_i²

**7/7 exact** on `pp, pn, nn, 3p, T, ³He, 3n`, and the same factorisation reproduces the
letter-pair classes of `c2_pair_class_decomposition_probe` term by term:

    intra(free)  =  (Z·intra_p + N·intra_n) · [ε⁰],        intra_p = 2,  intra_n = −2
    cross(free)  =  [C(Z,2) r_p² + Z·N r_p r_n + C(N,2) r_n²] · [ε⁰]
    n-if, if-if  =  0                                      (the free word has no interfaces)

## Two constants that were called "new data" are now derived

- **`(S_p, S_n) = (6, −4)` — `c₁`'s only ordering-dependent input (PR #6920, `qou-pdg9`) — is
  `4·(r_p, r_n) = 4·(3/2, −1)`.** So `u = 3Z − 2N = 2(Z r_p + N r_n)`, and `[ε¹] = u·2^(−A−1)` is not
  a fitted shape: it is the first-order term of a product, with the per-nucleon deletion sums
  identified as four times the single-nucleon trace ratios.
- **`(37, 20)`** — which this file used to call "the genuinely new data, the second-order analogue of
  `(S_p, S_n)`, the only fitted pair" — falls out of `q_p, q_n`. The identity

      4·[Z q_p + N q_n + (σ₁² − σ₂)/2]  =  u²/2 + (37Z + 20N)/2

  is verified exactly on all 8 `(Z,N)` at `A = 2, 3, 4`. So the measured form is **8 points against
  ZERO free parameters**, not against two: its inputs are two single-nucleon series computed on
  their own, never fitted to multi-nucleon data.

## 🛑 The correction, in full — what I asserted, what is true, and what else it reached

**What this file used to say.** That the exponentiation/factorisation reading *fails*, on the
grounds that it "requires `u` to *be* the first-order coefficient in the same normalisation, and it
is not — `[ε¹] = u·2^(−A−1)`, so `([ε¹])²/2` differs from the measured `u²/2·2^(−A−2)` by a factor
`2^(−A)`." It concluded there was "a relation between the orders with **no mechanism attached**".

**What is true.** Multiplicativity holds, and it never predicted `([ε¹])²/2`. Two errors in that
comparison:

1. **The normaliser was squared.** `[ε¹]` already carries `[ε⁰] = 2^(−A)`. A product's second-order
   cross term is `Σ_{i<j} r_i r_j · [ε⁰]` — the `[ε⁰]` appears **once**. Squaring `[ε¹]` squares it,
   which is precisely the stray `2^(−A)` I then read as the refutation.
2. **The self terms were not subtracted.** `Σ_{i<j} r_i r_j = (σ₁² − σ₂)/2`, not `σ₁²/2`. Part of
   the linear `(37Z + 20N)` comes from `−σ₂/2`, so no version of "(first order)²/2" can be right.

I tested my instinct against an expression the mechanism does not produce and concluded the
mechanism was wrong. The probe's own prediction column then agreed with me, because it had been
written to the same wrong expression.

**How the correction was measured.** `trace_expansion(1,0)` and `trace_expansion(0,1)` give the two
single-nucleon series exactly; the products are checked against `trace_expansion(Z,N)` and against
`s2_by_pair_class(Z,N)` on 7 words, `Fraction ==`; and the `(37, 20)` identity is checked
symbolically on 8 `(Z,N)`. Nothing is fitted at any step.

**What else the wrong retraction reached.** The 🛑 box in this file (now replaced), finding 5 of PR
#6920's body, and the copy of it in bean `qou-qqm4` — all three said the mechanism was not
established. All three are corrected. The *measured relation* was right throughout and is unchanged;
only its status moves from "empirical, 2 free parameters" to "derived, 0".

## What this still does NOT give

**`c₂` is `[ε¹]+[ε²]` of `tr(free) − tr(atom)`, and only the free half is derived here.** The atom
word does **not** factorise — its interface letters couple adjacent blocks — so nothing above says
what the atom side's second order is. Concretely, in the pair-class decomposition the `n-if` and
`if-if` columns of `Δtr` are **pure atom-side data** (the free word contributes zero to both), and
`cross` and `intra` each have a free half that is now known and an atom half that is not.

Nor is factorisation *proved* here. Disjoint strand triples is an argument; the 7-word exact
agreement across three orders and four pair classes is evidence. A Lean statement of
`tr(free; Z,N) = tr(p)^Z tr(n)^N` would settle it and does not exist.

SCOPE — (a) scope-limited. Exact `Fraction` arithmetic through the corpus's own `[◇]` expansion,
driven directly rather than through any `main` that would rewrite a committed witness. No `q`
evaluated, no float, no witness, nothing wired, no Lean.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from fractions import Fraction as F
from math import comb
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

_spec2 = importlib.util.spec_from_file_location(
    "dec", _HERE / "c2_pair_class_decomposition_probe.py")
_DEC = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(_DEC)

CASES = (("pp", 2, 0), ("pn", 1, 1), ("nn", 0, 2),
         ("3p", 3, 0), ("T", 1, 2), ("3He", 2, 1), ("3n", 0, 3))
# (Z,N) for the symbolic (37, 20) identity — the seven above plus the held-out ⁴He.
IDENTITY_CASES = ((2, 0), (1, 1), (0, 2), (3, 0), (1, 2), (2, 1), (0, 3), (2, 2))


def single_nucleon():
    """The two single-nucleon series `(a, r, q, intra)`, measured at `n = 3`, never fitted."""
    out = {}
    for key, Z, N in (("p", 1, 0), ("n", 0, 1)):
        c, cls = _D.trace_expansion(Z, N, False, 2)
        out[key] = {"a": c[0], "r": c[1] / c[0], "q": c[2] / c[0],
                    "intra": cls[2][2] / c[0]}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-classes", action="store_true",
                    help="skip the per-pair-class checks (the slower half)")
    args = ap.parse_args()
    t0 = time.time()

    print("=" * 92)
    print("  The FREE word factorises over nucleons — every order-2 quantity, zero free parameters")
    print("=" * 92)

    S = single_nucleon()
    p, nn_ = S["p"], S["n"]
    print(f"  single nucleon (n = 3, measured independently):")
    print(f"    proton   a = {p['a']}   r = {p['r']}   q = {p['q']}   intra = {p['intra']}")
    print(f"    neutron  a = {nn_['a']}   r = {nn_['r']}   q = {nn_['q']}   intra = {nn_['intra']}")
    print(f"    ⇒ (S_p, S_n) = 4·(r_p, r_n) = ({4 * p['r']}, {4 * nn_['r']})"
          f"   — c₁'s only ordering-dependent input, DERIVED\n")

    hdr = (f"    {'case':<6}{'[ε⁰]':>9}{'pred':>9}{'[ε¹]':>9}{'pred':>9}"
           f"{'[ε²]':>11}{'pred':>11}")
    if not args.skip_classes:
        hdr += f"{'intra':>9}{'pred':>9}{'cross':>11}{'pred':>11}"
    print(hdr)
    ok = True
    for name, Z, N in CASES:
        A = Z + N
        e0p = p["a"] ** Z * nn_["a"] ** N
        s1 = Z * p["r"] + N * nn_["r"]
        s2 = Z * p["r"] ** 2 + N * nn_["r"] ** 2
        e1p = s1 * e0p
        e2p = (Z * p["q"] + N * nn_["q"] + (s1 ** 2 - s2) / 2) * e0p
        full, _ = _D.trace_expansion(Z, N, False, 2)
        good = (full[0] == e0p and full[1] == e1p and full[2] == e2p)
        line = (f"    {name:<6}{str(full[0]):>9}{str(e0p):>9}{str(full[1]):>9}{str(e1p):>9}"
                f"{str(full[2]):>11}{str(e2p):>11}")
        if not args.skip_classes:
            dec = _DEC.s2_by_pair_class(Z, N, False)
            ip = (Z * p["intra"] + N * nn_["intra"]) * e0p
            cp = (F(comb(Z, 2)) * p["r"] ** 2 + F(Z * N) * p["r"] * nn_["r"]
                  + F(comb(N, 2)) * nn_["r"] ** 2) * e0p
            good = good and dec["intra"][2] == ip and dec["cross"][2] == cp
            # the free word has no interface letters, so these two must be identically zero
            good = good and dec["n-if"][2] == 0 and dec["if-if"][2] == 0
            line += (f"{str(dec['intra'][2]):>9}{str(ip):>9}"
                     f"{str(dec['cross'][2]):>11}{str(cp):>11}")
        ok = ok and good
        print(line + f"  {'ok' if good else 'FAIL'}   [{time.time()-t0:5.1f}s]")
    print(f"    ⇒ {f'{len(CASES)}/{len(CASES)} — the product reproduces every order and every pair class.' if ok else 'FAIL — factorisation does NOT hold; do not quote this file.'}")

    # The (37, 20) identity: what this file used to call the only fitted pair.
    print("\n  ── (37, 20) is DERIVED, not fitted ──")
    idok = True
    for (Z, N) in IDENTITY_CASES:
        u = 3 * Z - 2 * N
        s1 = Z * p["r"] + N * nn_["r"]
        s2 = Z * p["r"] ** 2 + N * nn_["r"] ** 2
        lhs = 4 * (Z * p["q"] + N * nn_["q"] + (s1 ** 2 - s2) / 2)
        rhs = F(u ** 2, 2) + F(37 * Z + 20 * N, 2)
        idok = idok and lhs == rhs
    print(f"    4·[Z q_p + N q_n + (σ₁² − σ₂)/2]  ==  u²/2 + (37Z + 20N)/2"
          f"   on {len(IDENTITY_CASES)}/{len(IDENTITY_CASES)} (Z,N) incl. ⁴He:"
          f"   {'HOLDS' if idok else 'FAILS'}")
    print("    So the measured form is 8 points against ZERO free parameters, not two: its inputs")
    print("    are q_p = 23/4 and q_n = 3, measured on single nucleons, never fitted to the")
    print("    multi-nucleon data they predict.")

    print("\n  🛑 THIS FILE USED TO RETRACT THIS MECHANISM, AND THE RETRACTION WAS WRONG.")
    print("  It compared the measurement against ([ε¹])²/2, which multiplicativity never predicts:")
    print("  the cross term is Σ_{i<j} r_i r_j · [ε⁰], so [ε⁰] appears ONCE (squaring [ε¹] squares")
    print("  it — that was the stray 2^(−A) I read as a refutation) and the self terms are")
    print("  SUBTRACTED, (σ₁² − σ₂)/2 not σ₁²/2. The relation was right throughout; only its")
    print("  status moves, from 'empirical, 2 free parameters' to 'derived, 0'.")
    print("\n  🛑 STILL ONLY HALF OF c₂. c₂ is [ε¹]+[ε²] of tr(free) − tr(atom), and the ATOM word")
    print("  does NOT factorise — its interfaces couple adjacent blocks. In the pair-class")
    print("  decomposition the n-if and if-if columns of Δtr are PURE atom-side data (verified")
    print("  above: the free word contributes exactly 0 to both), and intra and cross each have a")
    print("  free half now known and an atom half that is not.")
    print("\n  Nor is factorisation PROVED here: disjoint strand triples is an argument, and 7 words")
    print("  across three orders and four pair classes is evidence. A Lean statement of")
    print("  tr(free; Z,N) = tr(p)^Z tr(n)^N would settle it and does not exist.")
    print(f"\n  ({time.time()-t0:.1f}s)")
    return 0 if (ok and idok) else 1


if __name__ == "__main__":
    sys.exit(main())
