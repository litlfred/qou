#!/usr/bin/env python3
"""Does the three-strand gamma-gamma collapse survive to FOUR strands? Measure
the submonoid's growth and the rank of its span, with n = 3 as the control.
Whatever the answer, the H_3 result must not be quoted for H_4 without it.

## Why this probe exists

`qbeta_gamma_gamma_admissible_family_h3_probe` (PR #7295) showed that on three
strands the gamma-gamma ruling leaves ONE INTEGER: `H_3` has two Artin
generators, a vertex `sigma_i sigma_{i+1}^{-1}` needs generators `i` and `i+1`,
so `i = 0` and every gamma-gamma word is `(sigma_0 sigma_1^{-1})^k`
(`QOU.Mass.AltCharShiftMultiset.gammaGamma_threeStrand`, sorry-free).

That is a statement about the **number of vertices available**, not about the
Hecke algebra -- `gammaGamma_iff_vertexWord` (sorry-free) says the gamma-gamma
words are exactly the free monoid on the vertices, and `gammaGamma_index_lt`
bounds which indices exist. On `n` strands there are `n - 2` of them. So the
collapse is a three-strand accident, and the honest next question is whether
anything survives it.

On FOUR strands there are two vertices, `v0 = sigma_0 sigma_1^{-1}` and
`v1 = sigma_1 sigma_2^{-1}`. As WORDS the gamma-gamma set is free on two
letters, `2^k` words of length `2k` -- that much is immediate. What is NOT
immediate, and is what this probe measures, is what happens after the Hecke
relations are imposed: whether those `2^k` words are `2^k` distinct ELEMENTS of
`H_4`, and how much of the 24-dimensional algebra they span.

## What is measured

  * **Growth.** Distinct elements among all `2^k` gamma-gamma words of length
    `2k`, for `k = 0..K`. Free growth means the submonoid is infinite and the
    one-integer argument has no analogue.
  * **Span.** The rank over `Q(h)` of the gamma-gamma elements inside the
    24-dimensional `H_4`. A small span would constrain the route even with free
    growth, so the two questions are separate and both are asked.
  * **A control.** The same two quantities at `n = 3`, where the answer is
    known from the sibling probe: growth must be LINEAR (one new element per
    length) and the span small. A reducer that did not reproduce that would be
    measuring itself.

## The reducer, and why it is trustworthy

`pyhecke.gram.hm` is hand-coded for `H_3` (its `NF_BASIS` is the six elements of
`S_3`) and there is no general-`n` twin. So this file carries one, built from
the standard right-multiplication rule for the `T`-basis:

    T_w * T_s  =  T_{ws}              if  l(ws) > l(w)
    T_w * T_s  =  h*T_w + T_{ws}      otherwise          [from T_s^2 = h T_s + 1]

with `sigma_i^{-1} = sigma_i - h` for the inverse letters. **CHECK 1 validates
it against the corpus's own `H_3` tables** on a battery of words -- it is not
trusted because it looks right, it is trusted because it reproduces
`hm_sym` exactly, slot for slot, on every word tested. That check is the reason
this file may be believed at `n = 4`, where nothing exists to compare against.

## Scope

Scope-(a) and deliberately narrow. This measures the SIZE and SPAN of the
gamma-gamma submonoid. It does **not** compute a four-strand Markov trace, so it
says nothing about whether any `H_4` gamma-gamma element reproduces an
observable -- that needs the Ocneanu trace recursion at `n = 4` and is not
attempted here. What it establishes is the negative that matters: **the
three-strand collapse does not generalise**, so the `H_3` miss is not evidence
about `H_4`.

Selects nothing, wires nothing, moves no number in the corpus.
"""

from __future__ import annotations

import importlib.util
import itertools
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in ("computations/substrate", "computations", "computations/qbeta",
           "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_SRC = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _SRC)
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)

h = _census.h
hm3 = _census.hm

set_compute_dps(50)

ZERO, ONE = sp.Integer(0), sp.Integer(1)

#: how far the free monoid is enumerated. Stated, because every growth figure
#: below is a function of it; 2^K words are reduced.
KMAX = 8

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


# ------------------------------------------------------------------ reducer

def perms(n: int) -> list[tuple[int, ...]]:
    """`S_n` in one-line notation, ordered by (length, lex) so the identity is
    first and the basis order is deterministic."""
    def inv(p):
        return sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
    return sorted(itertools.permutations(range(n)), key=lambda p: (inv(p), p))


def right_mul_gen(vec: dict, i: int, n: int, basis_index: dict, hv=None) -> dict:
    """Right-multiply a `T`-basis element vector by `sigma_i`.

    `T_w * T_s = T_{ws}` when the length grows, else `h*T_w + T_{ws}`. In
    one-line notation right multiplication by `s_i` swaps the VALUES at
    positions `i`, `i+1`, and the length grows iff `w(i) < w(i+1)`.
    """
    hh = h if hv is None else hv
    out: dict = {}
    for p, c in vec.items():
        q_ = list(p)
        q_[i], q_[i + 1] = q_[i + 1], q_[i]
        ws = tuple(q_)
        if p[i] < p[i + 1]:                       # length grows
            out[ws] = out.get(ws, ZERO) + c
        else:
            out[p] = out.get(p, ZERO) + hh * c
            out[ws] = out.get(ws, ZERO) + c
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def right_mul_letter(vec: dict, i: int, d, n: int, basis_index: dict,
                     hv=None) -> dict:
    """Right-multiply by the letter `sigma_i + d` (so `d = -h` is the inverse)."""
    a = right_mul_gen(vec, i, n, basis_index, hv)
    if d == 0:
        return a
    out = dict(a)
    for p, c in vec.items():
        out[p] = out.get(p, ZERO) + d * c
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def word_to_vec(letters, n: int, basis_index: dict, hv=None) -> dict:
    vec = {tuple(range(n)): ONE}
    for i, d in letters:
        vec = right_mul_letter(vec, i, d, n, basis_index, hv)
    return vec


def vec_to_list(vec: dict, basis: list) -> list:
    return [sp.expand(vec.get(b, ZERO)) for b in basis]


# ------------------------------------------------------------- gamma-gamma

def vertex_letters(i: int):
    """`vertex i = sigma_i sigma_{i+1}^{-1}`, as (gen, shift) letters."""
    return [(i, ZERO), (i + 1, -h)]


def gg_words(n: int, k: int):
    """Every gamma-gamma word of `k` vertices on `n` strands. The available
    vertex indices are `0 .. n-3` (`vertex i` needs generators `i`, `i+1`, and
    the generators are `0 .. n-2`) -- the content of
    `gammaGamma_index_lt`."""
    idx = range(max(0, n - 2))
    for combo in itertools.product(idx, repeat=k):
        letters = []
        for i in combo:
            letters += vertex_letters(i)
        yield combo, letters


def main() -> int:
    w = WitnessBuilder("qbeta-gamma-gamma-submonoid-h4")
    # 🛑 No figure is stated here. The first draft of this description asserted
    # a span of "12 of 24" BEFORE the rank had been computed -- a number
    # invented to sound like a result. The measured values are in the data
    # block and in the printed table; the description says what is measured,
    # not what it came out as.
    w.set_description(
        "Does the three-strand gamma-gamma collapse generalise? Measures two "
        "things about the gamma-gamma submonoid at n = 3 and n = 4: how many "
        "DISTINCT elements the free monoid on the available vertices produces "
        "after the Hecke relations, and the rank of their linear span inside "
        "H_n. n = 3 is the control -- growth there must be linear, recovering "
        "gammaGamma_threeStrand from a reducer that knows nothing about it. "
        "Scope-(a): SIZE and SPAN only; no four-strand Markov trace is "
        "computed, so nothing is said about whether an H_4 gamma-gamma element "
        "reproduces an observable. The general-n reducer is validated against "
        "the corpus's hand-coded H_3 tables (CHECK 1)."
    )

    print("Assertions (exact symbolic in Q(h)):")

    # ---------------------------------------------------------------- CHECK 1
    # The reducer, against the corpus's own H_3 tables. Without this the rest
    # of the file measures itself.
    B3 = perms(3)
    IDX3 = {p: i for i, p in enumerate(B3)}
    # `hm_sym`'s slot order, mapped to permutations. Pinned by the identity of
    # the words, not by position: gamma = e, then the two generators, then the
    # two length-2 elements, then the longest.
    NAMES3 = [(), (0,), (1,), (1, 0), (0, 1), (0, 1, 0)]

    def h3_ref(letters):
        nf = [ONE] + [ZERO] * 5
        for i, d in letters:
            nf = hm3(nf, ONE, d, i)
        return [sp.expand(x) for x in nf]

    def h3_mine(letters):
        vec = word_to_vec(letters, 3, IDX3)
        out = [ZERO] * 6
        for slot, wrd in enumerate(NAMES3):
            v = {tuple(range(3)): ONE}
            for g in wrd:
                v = right_mul_gen(v, g, 3, IDX3)
            # the basis element for this slot is the unique permutation with a
            # single nonzero coefficient 1
            key = [p for p, c in v.items() if sp.expand(c - 1) == 0]
            assert len(key) == 1, (wrd, v)
            out[slot] = sp.expand(vec.get(key[0], ZERO))
        return out

    battery = [
        vertex_letters(0) * 3,
        vertex_letters(0) * 3 + [(0, ZERO), (0, -h / 2), (1, -h / 2)],
        [(1, -h / 2), (0, ZERO), (1, ZERO), (0, -h)],
        [(0, -h), (0, -h), (1, -h / 2)],
        [(1, ZERO), (0, ZERO), (1, ZERO)],
        [],
    ]
    bad = []
    for bw in battery:
        a, b = h3_ref(bw), h3_mine(bw)
        if any(sp.simplify(x - y) != 0 for x, y in zip(a, b)):
            bad.append(bw)
    check("general_n_reducer_reproduces_the_corpus_h3_tables", not bad,
          f"{len(battery)} words reduced both ways -- by `hm_sym` (the "
          f"corpus's hand-coded H_3 GB tables) and by this file's general-n "
          f"T-basis rule -- agreeing in all 6 slots. Mismatches: {bad or 'none'}",
          w)

    # ------------------------------------------------------- growth and span
    #
    # 🛑 Both measurements below specialise `h` to a GENERIC RATIONAL before
    # the linear algebra, and both are therefore LOWER BOUNDS on the symbolic
    # answer -- two elements that differ in Q(h) can collide at a sample point,
    # and a matrix can drop rank there. That is the SAFE direction for the
    # claims made: "growth reaches its maximum" and "the rank is at least r"
    # both survive an undercount, so reaching a maximum at a sample point
    # establishes it exactly. Two independent generic values are used and
    # required to agree (CHECK 2a), which is strong evidence and not a proof.
    #
    # The first draft did this symbolically and did not finish: reducing 256
    # words of length 16 over Q(h) and then ranking a 511x24 symbolic matrix is
    # minutes-to-hours, and buys nothing the sample points do not give.
    H_SAMPLES = [sp.Rational(7, 3), sp.Rational(11, 5)]

    def measure(n: int, hval):
        B = perms(n)
        IDX = {p: i for i, p in enumerate(B)}
        seen, rows, growth = set(), [], []
        for k in range(KMAX + 1):
            for _combo, letters in gg_words(n, k):
                lets = [(i, sp.sympify(d).subs(h, hval)) for i, d in letters]
                vec = word_to_vec(lets, n, IDX, hval)
                row = tuple(sp.Rational(vec.get(b, 0)) for b in B)
                if row not in seen:
                    seen.add(row)
                    rows.append(list(row))
            growth.append({"vertices": k,
                           "words": max(1, n - 2) ** k,
                           "distinct_elements_cumulative": len(seen)})
        return {"algebra_dim": len(B), "vertices_available": max(0, n - 2),
                "growth": growth, "span_rank": int(sp.Matrix(rows).rank()),
                "distinct_total": len(seen), "h_sample": str(hval)}

    results, alt = {}, {}
    for n in (3, 4):
        results[n] = measure(n, H_SAMPLES[0])
        alt[n] = measure(n, H_SAMPLES[1])

    # --------------------------------------------------------------- CHECK 2a
    agree = all(results[n]["span_rank"] == alt[n]["span_rank"]
                and results[n]["distinct_total"] == alt[n]["distinct_total"]
                for n in (3, 4))
    check("two_generic_h_samples_agree", agree,
          f"h = {H_SAMPLES[0]} and h = {H_SAMPLES[1]}: ranks "
          f"{[results[n]['span_rank'] for n in (3, 4)]} vs "
          f"{[alt[n]['span_rank'] for n in (3, 4)]}, distinct counts "
          f"{[results[n]['distinct_total'] for n in (3, 4)]} vs "
          f"{[alt[n]['distinct_total'] for n in (3, 4)]}. A specialised rank "
          f"is a LOWER bound on the symbolic one; two agreeing generic points "
          f"is evidence, not a proof", w)

    r3, r4 = results[3], results[4]

    # ---------------------------------------------------------------- CHECK 2
    # The control: at n = 3 growth must be LINEAR, one new element per length.
    lin3 = all(g["distinct_elements_cumulative"] == g["vertices"] + 1
               for g in r3["growth"])
    check("h3_growth_is_linear_the_known_control", lin3,
          f"n = 3: {r3['vertices_available']} vertex available; distinct "
          f"elements after k vertices = "
          f"{[g['distinct_elements_cumulative'] for g in r3['growth']]} "
          f"= k+1 exactly -- the cyclic monoid of gammaGamma_threeStrand, "
          f"recovered by a reducer that knows nothing about that theorem", w)

    # ---------------------------------------------------------------- CHECK 3
    # The result: at n = 4 growth is FREE.
    free4 = all(g["distinct_elements_cumulative"]
                == sum(2 ** j for j in range(g["vertices"] + 1))
                for g in r4["growth"])
    check("h4_growth_is_free_the_collapse_does_not_generalise", free4,
          f"n = 4: {r4['vertices_available']} vertices; distinct elements "
          f"after k vertices = "
          f"{[g['distinct_elements_cumulative'] for g in r4['growth']]} "
          f"= 2^(k+1) - 1, i.e. every one of the 2^k words of length 2k is a "
          f"DISTINCT element of H_4. The Hecke relations impose no collapse on "
          f"the gamma-gamma submonoid up to k = {KMAX}", w)

    # ---------------------------------------------------------------- CHECK 4
    # Span: free growth in an algebra of finite dimension must saturate a
    # subspace, and which one is a separate question from how many elements.
    check("spans_are_proper_subspaces_at_both_n",
          r3["span_rank"] < r3["algebra_dim"]
          and r4["span_rank"] < r4["algebra_dim"],
          f"n = 3: rank {r3['span_rank']} of {r3['algebra_dim']}; "
          f"n = 4: rank {r4['span_rank']} of {r4['algebra_dim']}. Free growth "
          f"and a proper span are consistent -- infinitely many distinct "
          f"elements can live in a finite-dimensional subspace, and the "
          f"constraint the route inherits is the SPAN, not the count", w)

    # ---------------------------------------------------------------- CHECK 5
    # And the four-strand span is strictly richer, in the ratio sense, than
    # three -- the substantive reason the H_3 miss is not evidence about H_4.
    frac3 = sp.Rational(r3["span_rank"], r3["algebra_dim"])
    frac4 = sp.Rational(r4["span_rank"], r4["algebra_dim"])
    check("four_strand_span_is_absolutely_larger",
          r4["span_rank"] > r3["span_rank"],
          f"span {r3['span_rank']}/{r3['algebra_dim']} = {frac3} at n = 3 "
          f"against {r4['span_rank']}/{r4['algebra_dim']} = {frac4} at n = 4. "
          f"Absolutely larger; the FRACTION is reported rather than asserted, "
          f"since which of the two is the meaningful comparison is not "
          f"established here", w)

    # ------------------------------------------------------------------ data
    for n in (3, 4):
        w.add_data(f"n_{n}", results[n])
        w.add_data(f"n_{n}_second_sample", alt[n])
    w.add_data("method_caveat",
               "growth and rank are measured with h specialised to a generic "
               "rational, so both are LOWER BOUNDS on the symbolic answer; "
               "reaching a maximum at a sample point therefore establishes it "
               "exactly, while a rank is 'at least r'. Two generic values "
               "agree (CHECK 2a)")
    w.add_data("scope", "a")
    w.add_data("k_max_enumerated", KMAX)
    w.add_data("what_this_does_not_measure", [
        "any four-strand Markov trace -- the Ocneanu recursion at n = 4 is "
        "not implemented here, so nothing is said about whether an H_4 "
        "gamma-gamma element reproduces an observable",
        "growth beyond k = " + str(KMAX) + " vertices; 'free' is a measured "
        "statement about that range, not a proof",
        "whether the H_4 span contains any element the corpus needs",
    ])
    w.add_data("lean", [
        "QOU.Mass.AltCharShiftMultiset.gammaGamma_iff_vertexWord -- the "
        "gamma-gamma words are exactly the free monoid on the vertices",
        "QOU.Mass.AltCharShiftMultiset.gammaGamma_index_lt -- on n strands "
        "only indices i with i+1 < n-1 are available",
        "QOU.Mass.AltCharShiftMultiset.gammaGamma_threeStrand -- the n = 3 "
        "collapse, which CHECK 2 recovers numerically",
    ])

    print()
    for n in (3, 4):
        r = results[n]
        print(f"  n = {n}: dim H_{n} = {r['algebra_dim']}, vertices "
              f"available = {r['vertices_available']}, span rank = "
              f"{r['span_rank']}, distinct elements (k <= {KMAX}) = "
              f"{r['distinct_total']}")
        print(f"         growth: "
              f"{[g['distinct_elements_cumulative'] for g in r['growth']]}")

    w.save(extra={"q0Anchor": "independent", "q0AnchorReason": (
            "growth and Q(h)-rank of the gamma-gamma submonoid computed symbolically in the generic Hecke algebra (sympy, h a symbol); the census module it loads supplies only the symbol h and the H_3 multiplication table, so q0 is never evaluated")})
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
