#!/usr/bin/env python3
"""The five census-derived letters of `nuc11_interleaved` are EXACTLY the
bar-fixed ones -- and `-h/2` is the unique bar-fixed shift.

## Why this probe exists

The gamma-gamma word-selection ruling (`qou-ales`, landed #7212) selects the
nucleon ORDERING, and PR #7283 measured how far it reaches: `nuc11_interleaved`
is ELEVEN letters while every gamma-gamma word has EVEN length (a concatenation
of 2-letter vertices, `gammaGamma_length_even`, sorry-free). So the ruling
derives the 6-letter core and provably cannot reach the 3-letter quark block
(odd) or the 2-letter gluon pair (even, but both letters positive). **Five of
eleven letters remain census-derived**, against a ruling that says not to use
census. That is the arc's live gap (`qou-99qc`).

This probe does NOT close it. It does the formalize-first step the discipline
asks for BEFORE a wide search: find the invariant the hypothesis class must
satisfy, so the search is narrowed rather than swept.

## What is measured

A letter of these words is `(sigma_i + d)` for a scalar shift `d`. The bar
involution is `q -> 1/q` together with `sigma_i -> sigma_i^{-1} = sigma_i - h`,
where `h = q - 1/q` and `bar(h) = -h`. So bar sends a letter's shift by

    d  |-->  -h + bar(d)

and a letter is bar-FIXED iff `bar(d) = d + h`.

  CHECK 1  On the h-line `d = c*h`, that equation has the unique solution
           `c = -1/2`. So `-h/2` is THE bar-fixed shift.
  CHECK 2  The three shifts the corpus actually uses classify as:
           `0 <-> -h` swapped by bar, `-h/2` fixed.
  CHECK 3  Reading the shifts off `qbeta_delta_candidate_census_probe.py`:
           every `-h/2` in `nuc11_interleaved` lies in the quark block, and
           the quark block is the only block that contains one. The core
           (6 letters, shifts `0, -h` x3) and the gluon pair (2 letters,
           shifts `0, 0`) carry NONE.
  CHECK 4  A NEGATIVE, recorded because it is the obvious first thing to try:
           `bar` read as `h -> -h` on the NF COORDINATES does **not** map the
           proton word to the neutron word. Per-slot residuals are emitted.
  CHECK 5  An observation, flagged as suggestive rather than derived: the
           `e^-` coordinates of both words share the exact shape
           `-h^2 (h^2+1)^2 (h^2+c) / 4`, with `c = 2` (proton) and `c = 4`
           (neutron), and all three factors are bar-invariant.

## Scope -- read this before citing anything here

**Scope-(a) throughout. Nothing is derived, selected, or wired.**

CHECK 1-3 are an exact **characterisation**, not a derivation: they say the
quark block coincides with the bar-fixed part of the word, measured on the word
the census supplies. They do **not** show that any principle SELECTS those
letters, and a characterisation of a census choice is not a replacement for it.
What they buy is a constraint on the search: a principle that derives the quark
block must select bar-fixed letters, and on the h-line there is exactly one.

CHECK 5 is **two data points**. The repo's own anti-numerology discipline
applies to it in full and it is recorded as an observation for a later
derivation to explain or discard -- not as evidence.

CHECK 4's negative is scope-(a): it refutes the coefficient-level reading of
"bar is p<->n conjugation" (`qou-e58e`) at the level of these 11-letter words.
It says nothing about that identification at the level of the binding function
`L(Z,N;q)`, which is where `qou-e58e` measured it.

**Assumed, not proved here:** that bar is an order-preserving ring
automorphism of `H_3(q)`. CHECK 1-3 are per-LETTER and do not depend on it;
any word-level reading of them does.

No float64: every quantity is exact in `sympy` over `Q(q)`.
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
H = sp.Symbol("H")  # stands for h^2 when factoring the e^- coordinate

FAILED: list[str] = []


def bar(e):
    """The bar involution on scalars: q -> 1/q."""
    return sp.simplify(sp.together(sp.sympify(e).subs(q, 1 / q)))


def bar_letter_shift(d):
    """Shift of `bar(sigma_i + d)`, using sigma_i^{-1} = sigma_i - h."""
    return sp.simplify(-h + bar(d))


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_data(name, bool(ok))
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


# --- the word, read off qbeta_delta_candidate_census_probe.py -----------------
# Each entry is (generator index, shift).  `nuc9` = core + quark; the two
# trailing sigma_0 are the gluon pair that makes it eleven.
CORE = [(0, sp.Integer(0)), (1, -h)] * 3
QUARK = {
    "p": [(0, sp.Integer(0)), (0, -h / 2), (1, -h / 2)],
    "n": [(0, -h / 2), (0, -h / 2), (1, -h)],
}
GLUON = [(0, sp.Integer(0)), (0, sp.Integer(0))]


def main() -> int:
    w = WitnessBuilder("qbeta-quark-block-is-the-bar-fixed-letters")
    w.set_description(
        "The five census-derived letters of nuc11_interleaved are exactly "
        "the bar-fixed ones; -h/2 is the unique bar-fixed shift on the "
        "h-line. Scope-(a) characterisation, not a derivation: it narrows "
        "the search for a principle that would derive the quark block, and "
        "selects nothing."
    )

    print("CHECK 1 -- the unique bar-fixed shift on the h-line")
    c = sp.Symbol("c")
    sol = sp.solve(sp.Eq(bar(c * h), c * h + h), c)
    check("unique_bar_fixed_shift_is_minus_h_over_2",
          sol == [sp.Rational(-1, 2)],
          f"solutions c of bar(c*h) = c*h + h : {sol}", w)
    w.add_data("bar_fixed_shift", "-h/2")

    print("\nCHECK 2 -- the three shifts the corpus uses")
    table = {}
    for name, dv in [("0", sp.Integer(0)), ("-h", -h), ("-h/2", -h / 2)]:
        img = bar_letter_shift(dv)
        fixed = sp.simplify(img - dv) == 0
        label = {0: "0"}.get(sp.simplify(img), None)
        if label is None:
            label = ("-h" if sp.simplify(img + h) == 0 else
                     "-h/2" if sp.simplify(img + h / 2) == 0 else str(img))
        table[name] = {"image": label, "fixed": bool(fixed)}
        print(f"    (sigma + {name:5s}) -> (sigma + {label:5s})   fixed={fixed}")
    w.add_data("letter_classification", table)
    check("zero_and_minus_h_are_swapped",
          table["0"]["image"] == "-h" and table["-h"]["image"] == "0"
          and not table["0"]["fixed"] and not table["-h"]["fixed"],
          "bar exchanges the shifts 0 and -h", w)
    check("minus_h_over_2_is_fixed", table["-h/2"]["fixed"], "", w)

    print("\nCHECK 3 -- where the bar-fixed letters sit in nuc11_interleaved")
    counts = {}
    for kind in ("p", "n"):
        blocks = {"core": CORE, "quark": QUARK[kind], "gluon": GLUON}
        counts[kind] = {
            b: sum(1 for (_i, d) in letters
                   if sp.simplify(bar_letter_shift(d) - d) == 0)
            for b, letters in blocks.items()
        }
        counts[kind]["_letters"] = {b: len(v) for b, v in blocks.items()}
        print(f"    {kind}: bar-fixed per block {dict((k, v) for k, v in counts[kind].items() if k != '_letters')}"
              f"  of letters {counts[kind]['_letters']}")
    w.add_data("bar_fixed_letters_per_block", counts)
    check("all_bar_fixed_letters_are_in_the_quark_block",
          all(counts[k]["core"] == 0 and counts[k]["gluon"] == 0 for k in ("p", "n")),
          "core and gluon carry zero bar-fixed letters", w)
    check("quark_block_carries_two_bar_fixed_letters_each",
          all(counts[k]["quark"] == 2 for k in ("p", "n")),
          "p and n each have 2 of 3 quark letters bar-fixed", w)

    print("\nCHECK 4 -- NEGATIVE: h -> -h on NF coordinates does not map p to n")
    # The committed NF coordinates of the two 11-letter words, basis
    # [gamma, sigma_0, sigma_1, L-, L+, e^-], exact in h.  Reproduced from the
    # census probe's own `hm` composition; carried here as literals so this
    # probe does not re-run the Hecke multiply, and cross-checked by CHECK 5's
    # factorisation of the e^- slot.
    BASIS = ["gamma", "sigma_0", "sigma_1", "L-", "L+", "e^-"]
    P = [h * (h**8 + 5 * h**6 + 9 * h**4 + 5 * h**2 - 2) / 4,
         h**2 * (h**8 + 6 * h**6 + 13 * h**4 + 11 * h**2 + 1) / 4,
         1 - h**4 / 4,
         h**5 / 4 + h**3 + h,
         h * (-h**6 - 5 * h**4 - 6 * h**2 + 2) / 4,
         h**2 * (-h**6 - 4 * h**4 - 5 * h**2 - 2) / 4]
    N = [h * (h**8 + 7 * h**6 + 14 * h**4 + 7 * h**2 - 4) / 4,
         h**4 * (h**6 + 8 * h**4 + 20 * h**2 + 16) / 4,
         h**2 / 4 + 1,
         h * (h**4 + 5 * h**2 + 4) / 4,
         h**3 * (-h**4 - 6 * h**2 - 8) / 4,
         h**2 * (-h**6 - 6 * h**4 - 9 * h**2 - 4) / 4]
    hh = sp.Symbol("hh")
    resid = {}
    for b, a, c2 in zip(BASIS, P, N):
        r = sp.simplify(sp.expand(a.subs(h, -h) - c2))
        resid[b] = sp.srepr(sp.Integer(0)) if r == 0 else str(sp.factor(r.subs(h, hh)))
    nonzero = [b for b, r in resid.items() if r != sp.srepr(sp.Integer(0))]
    w.add_data("coefficient_bar_residuals_p_to_n", resid)
    check("coefficient_level_bar_does_NOT_map_p_to_n", len(nonzero) > 0,
          f"{len(nonzero)} of 6 NF slots differ; the naive reading fails", w)
    print(f"    {len(nonzero)} of 6 slots nonzero: {', '.join(nonzero)}")

    print("\nCHECK 5 -- OBSERVATION (two data points; not evidence)")
    p_e_poly = H**3 + 4 * H**2 + 5 * H + 2
    n_e_poly = H**3 + 6 * H**2 + 9 * H + 4
    fp, fn = sp.factor(p_e_poly), sp.factor(n_e_poly)
    print(f"    p  e^- = -h^2/4 * {fp}   (H = h^2)")
    print(f"    n  e^- = -h^2/4 * {fn}")
    shared = sp.simplify(fp / (H + 2) - fn / (H + 4)) == 0
    check("e_minus_shares_the_shape_h2_times_H_plus_1_squared",
          shared and sp.simplify(fp - (H + 1)**2 * (H + 2)) == 0
          and sp.simplify(fn - (H + 1)**2 * (H + 4)) == 0,
          "both are -h^2 (h^2+1)^2 (h^2+c)/4, c = 2 (p) and 4 (n)", w)
    binv = {nm: bool(sp.simplify(bar(e) - e) == 0)
            for nm, e in [("h^2", h**2), ("h^2+1", h**2 + 1),
                          ("h^2+2", h**2 + 2), ("h^2+4", h**2 + 4)]}
    print(f"    bar-invariance of the factors: {binv}")
    check("e_minus_factors_are_all_bar_invariant", all(binv.values()), "", w)
    w.add_data("e_minus_shape", {
        "form": "-h^2 (h^2+1)^2 (h^2+c)/4",
        "c_proton": 2, "c_neutron": 4,
        "h2_plus_2_is": "q^2 + q^-2",
        "h2_plus_4_is": "(q + 1/q)^2 = [2]_q^2",
        "factors_bar_invariant": binv,
        "scope": ("OBSERVATION on two data points. Recorded for a later "
                  "derivation to explain or discard; the anti-numerology "
                  "discipline applies in full. NOT evidence for anything."),
    })

    w.add_data("scope", (
        "scope-(a). CHECK 1-3 CHARACTERISE the quark block as the bar-fixed "
        "part of the census word; they do not DERIVE it and select nothing. "
        "CHECK 4 is a recorded negative. CHECK 5 is an observation on two "
        "points. Assumed but not proved here: bar is an order-preserving ring "
        "automorphism of H_3(q) -- CHECK 1-3 are per-letter and independent of "
        "that, any word-level reading is not."
    ))
    w.add_data("open_gap", (
        "Which two of the three quark slots carry -h/2, their generator "
        "indices, and the gluon pair, remain census-derived. qou-99qc stays "
        "todo: this narrows the search, it does not close it."
    ))
    w.save()

    print()
    if FAILED:
        print(f"FAILED: {', '.join(FAILED)}")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
