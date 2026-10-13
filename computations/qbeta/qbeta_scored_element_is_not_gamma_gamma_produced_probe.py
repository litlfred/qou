#!/usr/bin/env python3
"""The scored `Q_beta` element is NOT gamma-gamma-produced — element-level, by
the alternating character, not by parity.

## Why this probe exists

PR #7283 measured that the gamma-gamma word-selection ruling (`qou-ales`)
reaches 6 of `nuc11_interleaved`'s 11 letters and provably not the other 5:
every gamma-gamma word has EVEN length (`gammaGamma_length_even`, sorry-free)
and 11 is odd. **That argument is WORD-level**, so it is defeated by re-padding
a candidate to even length, and it says nothing about the algebra ELEMENT.

`GammaGammaWordSelection.lean` supplies a stronger invariant it already proves:

    altChar_eq_one -- the alternating character `sigma_i |-> -q^{-1}` of every
    gamma-gamma-produced word is exactly 1 (each vertex `sigma_i sigma_{i+1}^{-1}`
    contributes `(-q^{-1})(-q) = 1`).

That is a **character** — a one-dimensional representation, hence an algebra
homomorphism — so its value is a property of the ELEMENT, not of the word
presenting it. Two words presenting the same element have the same alternating
character. This probe evaluates it on the scored element.

## What is measured

  CHECK 1  `sigma_i |-> -1/q` really is a 1-dim rep of `H_n(q)`: it satisfies
           the Hecke relation `s^2 = h s + 1` with `h = q - 1/q`. (Without this
           the whole argument is void, so it is checked, not assumed.)
  CHECK 2  Per-letter values. A letter is `(sigma_i + d)`, so its character is
           `-1/q + d`:  shift `0 -> -1/q`,  `-h -> -q`,  `-h/2 -> -[2]_q/2`.
           The gamma-gamma vertex `(0)(-h)` gives `1`, reproducing the Lean
           lemma from this probe's own letter reading.
  CHECK 3  Per-block, on `nuc11_interleaved`:
               core  (6 letters)  = 1        <- IS gamma-gamma (`borromean_gammaGamma`)
               gluon (2 letters)  = 1/q^2    <- NOT 1
               quark (3 letters)  < 0        <- NOT 1
  CHECK 4  Whole element:
               altChar(B_p) = -(q^2+1)^2 / (4 q^5)
               altChar(B_n) = -(q^2+1)^2 / (4 q^3)
           Both are **strictly negative for every q > 0**, since the numerator
           is `-(q^2+1)^2 < 0`. A gamma-gamma element has character `1 > 0`, so
           the exclusion holds by SIGN alone — no anchor, no pin, no tolerance.
  CHECK 5  CALIBRATION, and it is what makes the rest trustworthy. The same
           two characters are computed a second, independent way: by pairing
           the committed NF coordinate vectors against the characters of the
           six `H_3` basis words `[1, s0, s1, s1s0, s0s1, s0s1s0]`. The two
           routes agree exactly, which validates the letter reading AND the
           coordinate vectors simultaneously.
  CHECK 6  `sigma_i - h/2` is not a braid letter at all. Writing
           `sigma^k = a_k sigma + b_k` (`a_{k+1} = a_k h + b_k`, `b_{k+1} = a_k`),
           `a_k = 1` only at `k = +-1`; for `|k| >= 2`, `deg a_k = |k| - 1 >= 1`,
           so it is never the constant 1. Hence the only shifts realised by an
           integer power are `0` (k=+1) and `-h` (k=-1).

## Scope

**CHECK 4 is a scope-(b) STRUCTURAL EXCLUSION**, and the invariant is named:
the alternating character, fixed at 1 for every gamma-gamma word by
`QOU.Mass.GammaGammaWordSelection.altChar_eq_one` (sorry-free). Because a
character is an algebra hom, this excludes the ELEMENT, not merely the word as
written — it survives any rewriting, re-padding or reordering.

**What this does NOT say, and the distinction is the whole point.**

* It does **not** say the gamma-gamma route is dead. The 6-letter core IS
  gamma-gamma-produced and its character is 1 — that is CHECK 3, and it is a
  positive result for the ruling. What is excluded is *this* element.
* It does **not** contradict the owner ruling. `qou-ales` used a
  gamma-gamma-derived criterion to DISCRIMINATE BETWEEN two census candidates
  (interleaved vs gen-grouped); it did not certify either as gamma-gamma-
  produced. This probe shows neither is. So the ruling stands and its reach is
  what PR #7283 measured — what fails is reading the witness field
  `element_is_ruled: true` as "the scored element is gamma-gamma-produced".
* It does **not** identify the right element, or say one exists.

No float64: exact in `sympy` over `Q(q)` throughout.
"""

from __future__ import annotations

import os
import sys
import warnings

warnings.filterwarnings("ignore")

import sympy as sp  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

from witness_base import WitnessBuilder  # noqa: E402

q = sp.Symbol("q", positive=True)
h = q - 1 / q
S = -1 / q  # the alternating character's value on every generator

FAILED: list[str] = []

# The word, read off qbeta_delta_candidate_census_probe.py. A letter is
# (sigma_i + d); `hm(nf, ONE, d, i)` right-multiplies by it.
CORE = [(0, sp.Integer(0)), (1, -h)] * 3
QUARK = {
    "p": [(0, sp.Integer(0)), (0, -h / 2), (1, -h / 2)],
    "n": [(0, -h / 2), (0, -h / 2), (1, -h)],
}
GLUON = [(0, sp.Integer(0)), (0, sp.Integer(0))]

# Committed NF coordinates of the two 11-letter words, basis
# [gamma, sigma_0, sigma_1, L-, L+, e^-]; used only for the CHECK 5 calibration.
NF = {
    "p": [h * (h**8 + 5 * h**6 + 9 * h**4 + 5 * h**2 - 2) / 4,
          h**2 * (h**8 + 6 * h**6 + 13 * h**4 + 11 * h**2 + 1) / 4,
          1 - h**4 / 4,
          h**5 / 4 + h**3 + h,
          h * (-h**6 - 5 * h**4 - 6 * h**2 + 2) / 4,
          h**2 * (-h**6 - 4 * h**4 - 5 * h**2 - 2) / 4],
    "n": [h * (h**8 + 7 * h**6 + 14 * h**4 + 7 * h**2 - 4) / 4,
          h**4 * (h**6 + 8 * h**4 + 20 * h**2 + 16) / 4,
          h**2 / 4 + 1,
          h * (h**4 + 5 * h**2 + 4) / 4,
          h**3 * (-h**4 - 6 * h**2 - 8) / 4,
          h**2 * (-h**6 - 6 * h**4 - 9 * h**2 - 4) / 4],
}
#: characters of the six H_3 basis words [1, s0, s1, s1s0, s0s1, s0s1s0]
BASIS_CHAR = [sp.Integer(1), S, S, S**2, S**2, S**3]


def ac(d):
    """Alternating character of the letter (sigma_i + d)."""
    return sp.simplify(sp.together(S + d))


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_data(name, bool(ok))
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def main() -> int:
    w = WitnessBuilder("qbeta-scored-element-is-not-gamma-gamma-produced")
    w.set_description(
        "Scope-(b) structural exclusion: neither nuc11_interleaved proton nor "
        "neutron word is a gamma-gamma-produced ELEMENT. Invariant: the "
        "alternating character, fixed at 1 for every gamma-gamma word by "
        "GammaGammaWordSelection.altChar_eq_one (sorry-free). Both are "
        "strictly negative for every q>0, so the exclusion holds by sign. "
        "Element-level, unlike the word-level parity argument. Excludes THIS "
        "element only -- the 6-letter core IS gamma-gamma-produced."
    )

    print("CHECK 1 -- altChar is a genuine 1-dim rep of H_n(q)")
    check("alt_char_satisfies_hecke_relation",
          sp.simplify(S**2 - (h * S + 1)) == 0,
          "s = -1/q satisfies s^2 = h*s + 1, so it is an algebra hom", w)

    print("\nCHECK 2 -- per-letter characters")
    letters = {}
    for nm, d in [("0", sp.Integer(0)), ("-h", -h), ("-h/2", -h / 2)]:
        v = sp.factor(ac(d))
        letters[nm] = str(v)
        print(f"    altChar(sigma + {nm:5s}) = {v}")
    w.add_data("letter_characters", letters)
    check("minus_h_over_2_letter_is_minus_half_q_bracket_two",
          sp.simplify(ac(-h / 2) + (q + 1 / q) / 2) == 0,
          "altChar(sigma - h/2) = -[2]_q/2", w)
    check("gamma_gamma_vertex_character_is_one",
          sp.simplify(ac(sp.Integer(0)) * ac(-h) - 1) == 0,
          "(0)(-h) vertex -> (-1/q)(-q) = 1, reproducing Lean altChar_eq_one", w)

    print("\nCHECK 3/4 -- per block and whole element")
    # 🛑 Keep the sympy EXPRESSIONS. Round-tripping through str() and
    # sp.sympify() mints a fresh Symbol('q') WITHOUT `positive=True`, which is a
    # different symbol, so the differences never cancel and every comparison
    # below reads False while printing identical values. Caught by CHECK 5,
    # which is exactly what a calibration is for.
    block_e, total_e = {}, {}
    for kind in ("p", "n"):
        blocks = {"core": CORE, "quark": QUARK[kind], "gluon": GLUON}
        vals = {b: sp.factor(sp.simplify(sp.prod([ac(d) for _i, d in L])))
                for b, L in blocks.items()}
        block_e[kind] = vals
        total_e[kind] = sp.factor(sp.simplify(sp.prod(list(vals.values()))))
        print(f"    {kind}: core={vals['core']}  gluon={vals['gluon']}")
        print(f"       quark={vals['quark']}")
        print(f"       altChar(B_{kind}) = {total_e[kind]}")
    w.add_data("block_characters",
               {k: {b: str(v) for b, v in vals.items()} for k, vals in block_e.items()})
    w.add_data("element_characters", {k: str(v) for k, v in total_e.items()})

    check("core_is_gamma_gamma_character_one",
          all(sp.simplify(block_e[k]["core"] - 1) == 0 for k in ("p", "n")),
          "the 6-letter core has altChar 1 -- it IS gamma-gamma (borromean_gammaGamma)", w)
    check("gluon_pair_character_is_not_one",
          all(sp.simplify(block_e[k]["gluon"] - 1) != 0 for k in ("p", "n")),
          "gluon pair -> 1/q^2; even length does NOT make it gamma-gamma", w)

    # the exclusion, by sign -- numerator -(q^2+1)^2 < 0, denominator 4q^k > 0
    neg = {}
    for kind in ("p", "n"):
        num, den = sp.fraction(sp.together(total_e[kind]))
        neg[kind] = bool(sp.simplify(sp.expand(-num) - sp.expand((q**2 + 1)**2)) == 0
                         and sp.simplify(den - 4 * q**(5 if kind == "p" else 3)) == 0)
    check("scored_element_is_NOT_gamma_gamma_produced",
          all(sp.simplify(total_e[k] - 1) != 0 for k in ("p", "n")),
          "altChar != 1 for both; gamma-gamma requires exactly 1", w)
    check("exclusion_holds_by_sign_for_every_q_positive", all(neg.values()),
          "altChar = -(q^2+1)^2/(4q^k) < 0 identically, while gamma-gamma gives +1", w)

    print("\nCHECK 5 -- CALIBRATION: same characters from the NF coordinates")
    agree = {}
    for kind in ("p", "n"):
        from_nf = sp.factor(sp.simplify(sum(a * c for a, c in zip(NF[kind], BASIS_CHAR))))
        agree[kind] = bool(sp.simplify(from_nf - total_e[kind]) == 0)
        print(f"    {kind}: NF-pairing {from_nf}   letters {total_e[kind]}"
              f"   agree={agree[kind]}")
    check("two_independent_routes_agree",
          all(agree.values()),
          "letter product == NF-coordinate pairing; validates both inputs", w)

    print("\nCHECK 6 -- sigma_i - h/2 is not any integer power of sigma_i")
    hs = sp.Symbol("hs")
    A = {1: sp.Integer(1)}
    B = {1: sp.Integer(0)}
    for k in range(1, 9):
        A[k + 1] = sp.expand(A[k] * hs + B[k])
        B[k + 1] = A[k]
    for k in range(1, -9, -1):
        A[k - 1] = B[k]
        B[k - 1] = sp.expand(A[k] - B[k] * hs)
    unit_lead = sorted(k for k in A if sp.simplify(A[k] - 1) == 0)
    shifts = {k: str(sp.simplify(B[k])) for k in unit_lead}
    print(f"    integer powers with leading coefficient 1: {unit_lead}, shifts {shifts}")
    check("only_plus_and_minus_one_have_unit_leading_coefficient",
          unit_lead == [-1, 1],
          "so the only braid-letter shifts are 0 (k=+1) and -h (k=-1)", w)
    w.add_data("unit_leading_coefficient_powers", {"k": unit_lead, "shifts": shifts})
    w.add_data("degree_argument", (
        "deg a_k = |k| - 1 for |k| >= 1, so a_k is the constant 1 only at "
        "k = +-1; the finite scan -8..8 corroborates the degree argument, it "
        "does not stand in for it."
    ))

    w.add_data("scope", (
        "CHECK 4 is scope-(b): a STRUCTURAL EXCLUSION of the scored element "
        "from the gamma-gamma class, with the invariant named -- the "
        "alternating character, fixed at 1 by "
        "QOU.Mass.GammaGammaWordSelection.altChar_eq_one (sorry-free). A "
        "character is an algebra hom, so this is ELEMENT-level and survives "
        "any rewriting of the word, unlike the word-level parity argument "
        "(gammaGamma_length_even) which re-padding to even length defeats."
    ))
    w.add_data("what_this_does_not_say", (
        "(1) The gamma-gamma ROUTE is not excluded: the 6-letter core IS "
        "gamma-gamma-produced, altChar 1 (CHECK 3). Only THIS element is "
        "excluded. (2) No contradiction with the owner ruling qou-ales, which "
        "used a gamma-gamma criterion to DISCRIMINATE BETWEEN two census "
        "candidates and did not certify either as gamma-gamma-produced; what "
        "fails is reading the witness field element_is_ruled: true as 'the "
        "scored element is gamma-gamma-produced'. (3) It identifies no "
        "replacement element and does not claim one exists."
    ))
    w.save({"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})

    print()
    if FAILED:
        print(f"FAILED: {', '.join(FAILED)}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
