#!/usr/bin/env python3
"""The alternating character cannot see ORDERING -- so the gamma-gamma ruling,
which picked an ordering, cannot make any census nucleon gamma-gamma-produced.
All 19 readings are excluded at once, by one invariant, at every q != 1.

## Why this probe exists

Two things landed on 2026-09-08 and 2026-09-13 and they have not been put
together:

  * `qou-ales` (owner ruling): every canonical braid word is selected via
    gamma-gamma (pair-production) vertices `sigma_i sigma_{i+1}^{-1}` plus the
    confinement SDP -- never by census. R2 of that ruling, landed in #7212,
    applied it to pick the nucleon **ordering**.
  * `qbeta_scored_element_is_not_gamma_gamma_produced_probe` (#7283): the
    scored element `nuc11_interleaved` has alternating character
    `-(q^2+1)^2/(4 q^5)`, strictly negative for every `q > 0`, while
    `GammaGammaWordSelection.altChar_eq_one` (sorry-free) fixes the character
    of every gamma-gamma word at `+1`. Scope-(b), one element.

That probe answered the question for ONE element and left the obvious next one
open: is some OTHER reading of the nucleon gamma-gamma-reachable? The corpus
carries **19** readings -- `qbeta_delta_candidate_census_probe` establishes six
distinct Delta values, and the "constructed" family alone is 8 quark-generator
assignments x 2 Hopf orientations = 16 readings of the same recipe. Checking
them one at a time is the wrong shape of answer.

## What is measured

The alternating character `sigma_i |-> -1/q` is a 1-dimensional representation
of `H_3(q)` (CHECK 1 verifies `S^2 = h S + 1`), hence an algebra hom, hence
multiplicative on words. The corpus builds every nucleon from letters
`sigma_i + d` with the shift `d` drawn from a three-element alphabet:

    d = 0      (uu, a positive crossing)     char  -1/q
    d = -h/2   (ud, the mixed quark pair)    char  -(q^2+1)/(2q)
    d = -h     (dd, sigma_i^{-1})            char  -q

The character of a letter **does not depend on which generator it sits on**,
and a product does not depend on the order of its factors once each factor is
a scalar. So with `a`, `b`, `c` counting the three shifts:

    altChar(w) = (-1)^(a+b+c) * q^(b-a-c) * ((q^2+1)/2)^c          (CHECK 3)

-- a function of the shift MULTISET alone. That is the whole result. The two
free choices the corpus has argued about for months -- which generator each
quark crossing sits on, and in what order the letters are laid down -- are
exactly the two things this invariant is blind to (CHECK 4).

`altChar(w) = 1` identically then forces `c = 0` and `a = b` (CHECK 5): the
mixed letter contributes a factor `(q^2+1)/2`, and `q^2+1` is irreducible over
Q and coprime to `q`, so no power of `q` can cancel it. Every corpus nucleon
carries `c = 2` (CHECK 6) -- both the proton and the neutron word have exactly
two `-h/2` letters -- so none of the 19 is gamma-gamma-produced, and no
re-ordering or re-assignment can change that.

## The tie to the bar involution, measured here rather than cited

`qbeta_quark_block_is_the_bar_fixed_letters_probe` (#7283) proved `-h/2` is the
**unique** bar-fixed shift. CHECK 8 recomputes that independently and finds the
same letter. So the two letters that block gamma-gamma reachability are exactly
the two letters the proton<->neutron involution holds still. One letter, two
independent obstructions -- and `qou-e58e` measured that bar IS p<->n
conjugation on `L(Z,N;q)`, so this is not a coincidence of notation.

## Scope

**Scope-(b) exclusion**, with the invariant named as the "refuted / ruled out"
discipline requires: the alternating character, a 1-dimensional representation,
fixed at `+1` on gamma-gamma words by a sorry-free Lean theorem. It excludes
each candidate from being a **pure gamma-gamma word** (a product of vertices).
It says nothing about a word built from gamma-gamma vertices PLUS other
letters, and `altChar = 1` is **necessary, not sufficient** -- `c = 0, a = b`
is a statement about the multiset, and being an actual product of vertices is a
statement about the order. This probe selects nothing and wires nothing.
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
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# The candidate constructors are IMPORTED from the census probe, never
# re-transcribed. A second transcription of `build_atom_nf_exact` would be a
# second thing to keep in sync, and the whole point of this probe is that the
# corpus's own readings disagree.
_SRC = os.path.join(ROOT, "computations", "qbeta",
                    "qbeta_delta_candidate_census_probe.py")
_spec = importlib.util.spec_from_file_location("_census", _SRC)
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)

hm = _census.hm
h = _census.h

set_compute_dps(50)

q = sp.Symbol("q", positive=True)
ZERO, ONE = sp.Integer(0), sp.Integer(1)

#: exact substrate pin (proton), as a Rational -- no float64 anywhere here
Q0 = sp.Rational(Q_50_DIGIT_STR)

#: h expressed in q. Every symbolic result below is pushed through this before
#: it is compared, so `h` never survives into a character value.
H_OF_Q = q - 1 / q

#: the alternating character on a bare positive generator, `sigma_i |-> -1/q`.
#: Matches `QOU.Mass.GammaGammaWordSelection.altChar_single`.
S = -1 / q

# 🛑 Slot order is the census probe's (`hm_sym`), which REVERSES gram.py's
# canonical NF_BASIS at slots 3 and 4. Taken from the census module rather than
# restated, and pinned by CHECK 2 rather than by this comment.
BASIS = _census.BASIS
#: character of each NF basis element: gamma = 1, the two generators = S,
#: the two length-2 links = S^2, e^- = S^3.
BASIS_CHAR = [ONE, S, S, S**2, S**2, S**3]

#: the corpus shift alphabet, as (label, shift-in-h, character-in-q)
ALPHABET = [
    ("uu", ZERO, S),
    ("ud", -h / 2, sp.simplify(sp.together(S - H_OF_Q / 2))),
    ("dd", -h, sp.simplify(sp.together(S - H_OF_Q))),
]

FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def in_q(e):
    """Push a symbolic expression from Q(h) into Q(q) and normalise.

    🛑 Everything compared in this file goes through here and STAYS a sympy
    expression. Do not stringify and re-parse: `sp.sympify("q")` mints a fresh
    `Symbol('q')` WITHOUT `positive=True`, which is a different symbol, so
    differences never cancel and a check reads FAIL while printing the value it
    was compared against. That cost two false FAILs in the sibling probe
    (#7283) before it was caught by its own calibration.
    """
    return sp.simplify(sp.together(sp.expand(sp.sympify(e).subs(h, H_OF_Q))))


def char_of_nf(nf):
    """Alternating character read off the NF coordinates, by linearity."""
    return in_q(sum(sp.sympify(nf[k]) * BASIS_CHAR[k].subs(q, q) for k in range(6)))


def char_of_letters(letters):
    """Alternating character read off the WORD, by multiplicativity.

    `letters` is a list of `(gen, shift)`; the generator is accepted and
    ignored, which is half of what CHECK 4 asserts.
    """
    acc = ONE
    for _gen, d in letters:
        acc = acc * (S + in_q(d))
    return in_q(acc)


def word_to_nf(letters):
    nf = [ONE] + [ZERO] * 5
    for gen, d in letters:
        nf = hm(nf, ONE, d, gen)
    return nf


def at_q0(e):
    """Exact q -> q_0 substitution, then a 40-dps readout. No float64."""
    return mp.mpf(str(sp.N(sp.sympify(e).subs(q, Q0), 40)))


# --------------------------------------------------------------- the words

#: the gamma-gamma core: three vertices (sigma_0, sigma_1^{-1})
CORE = [(0, ZERO), (1, -h)] * 3

#: the quark blocks, exactly as `pyhecke.atom.build_nucleon_nf` lays them
QUARK = {
    "p": [(0, ZERO), (0, -h / 2), (1, -h / 2)],
    "n": [(0, -h / 2), (0, -h / 2), (1, -h)],
}

#: the two-letter gluon dressing of `build_atom_nf_exact`
GLUON = [(0, ZERO), (0, ZERO)]


def shift_counts(letters):
    """(a, b, c) = counts of the shifts 0, -h, -h/2 in a letter list."""
    a = b = c = 0
    for _gen, d in letters:
        dd = sp.simplify(sp.expand(d))
        if dd == 0:
            a += 1
        elif sp.simplify(dd + h) == 0:
            b += 1
        elif sp.simplify(dd + h / 2) == 0:
            c += 1
        else:
            raise AssertionError(f"shift outside the corpus alphabet: {d}")
    return a, b, c


def closed_form(a, b, c):
    """(-1)^(a+b+c) * q^(b-a-c) * ((q^2+1)/2)^c."""
    return in_q(sp.Integer(-1) ** (a + b + c) * q ** (b - a - c)
                * ((q**2 + 1) / 2) ** c)


def main() -> int:
    w = WitnessBuilder("qbeta-altchar-is-a-shift-multiset-invariant")
    w.set_description(
        "The alternating character of a corpus nucleon word depends only on "
        "the multiset of its letter shifts -- not on generator assignment and "
        "not on ordering. It equals 1 iff the mixed (ud) count is zero and the "
        "two pure counts agree. Every one of the 19 census readings carries "
        "exactly two mixed letters, so none is a gamma-gamma word at any "
        "q != 1, and the ordering the gamma-gamma ruling picked cannot change "
        "that. Scope-(b); the invariant is the alternating character, fixed at "
        "+1 on gamma-gamma words by GammaGammaWordSelection.altChar_eq_one "
        "(sorry-free)."
    )

    print("Assertions (exact symbolic in Q(q); readouts at the proton q_0):")

    # ---------------------------------------------------------------- CHECK 1
    # Calibration. If S is not a representation, nothing below means anything.
    resid = sp.simplify(S**2 - H_OF_Q * S - 1)
    check("alt_char_is_a_one_dim_hecke_rep", resid == 0,
          f"S^2 - h S - 1 = {resid} with S = -1/q, h = q - 1/q", w)

    # ---------------------------------------------------------------- CHECK 2
    # The method: reading the character off NF coordinates must agree with
    # reading it off the word. This is what pins the slot order; a probe that
    # got BASIS_CHAR wrong would fail here rather than silently report a wrong
    # character.
    battery = [
        CORE,
        CORE + QUARK["p"],
        CORE + QUARK["n"] + GLUON,
        [(1, -h / 2), (0, ZERO), (1, ZERO), (0, -h)],
        [(0, -h), (0, -h), (1, -h / 2)],
    ]
    diffs = [sp.simplify(char_of_nf(word_to_nf(bw)) - char_of_letters(bw))
             for bw in battery]
    check("nf_contraction_agrees_with_word_product", all(d == 0 for d in diffs),
          f"{len(battery)} words, max |residual| = 0" if all(d == 0 for d in diffs)
          else f"residuals {diffs}", w)

    # ---------------------------------------------------------------- CHECK 3
    # The closed form, against direct computation, over every multiset with
    # a,b,c <= 3 and one random ordering each.
    cf_bad = []
    for a, b, c in itertools.product(range(4), repeat=3):
        if a + b + c == 0:
            continue
        letters = ([(0, ZERO)] * a + [(1, -h)] * b + [(0, -h / 2)] * c)
        if sp.simplify(char_of_letters(letters) - closed_form(a, b, c)) != 0:
            cf_bad.append((a, b, c))
    check("closed_form_matches_direct_product", not cf_bad,
          f"63 multisets with a,b,c <= 3; mismatches: {cf_bad}", w)

    # ---------------------------------------------------------------- CHECK 4
    # Blindness to ordering AND to generator assignment: every permutation of
    # a fixed multiset, laid on every generator pattern, gives one value.
    base = QUARK["p"] + [(1, -h)] + [(0, ZERO)]
    seen = set()
    for perm in itertools.permutations(range(len(base))):
        for gens in itertools.product((0, 1), repeat=len(base)):
            lw = [(gens[k], base[perm[k]][1]) for k in range(len(base))]
            seen.add(sp.srepr(char_of_letters(lw)))
    check("character_is_blind_to_order_and_generator", len(seen) == 1,
          f"{120 * 32} (permutation, generator-assignment) pairs -> "
          f"{len(seen)} distinct character(s)", w)

    # ---------------------------------------------------------------- CHECK 5
    # char == 1 identically forces c == 0 and a == b. The <= direction is by
    # construction; the => direction is enumerated over a box and the general
    # reason is recorded in `note` (q^2+1 is irreducible over Q and coprime to
    # q, so no power of q cancels it). The general statement is the Lean
    # follow-up, not a claim this enumeration establishes.
    ones, bad_c, bad_ab = [], [], []
    for a, b, c in itertools.product(range(7), repeat=3):
        if a + b + c == 0:
            continue
        if sp.simplify(closed_form(a, b, c) - 1) == 0:
            ones.append((a, b, c))
            if c != 0:
                bad_c.append((a, b, c))
            if a != b:
                bad_ab.append((a, b, c))
    check("char_one_forces_no_mixed_and_balanced_pure",
          not bad_c and not bad_ab and ones,
          f"{len(ones)} of 342 multisets with a,b,c <= 6 have char == 1; "
          f"every one has c == 0 and a == b "
          f"(counterexamples: c!=0 {bad_c}, a!=b {bad_ab})", w)

    # ---------------------------------------------------------------- CHECK 6
    # The census. Every reading, with its (a,b,c) and its character.
    rows = []

    def record(label, letters):
        a, b, c = shift_counts(letters)
        ch = char_of_letters(letters)
        rows.append({
            "candidate": label, "a_uu": a, "b_dd": b, "c_ud": c,
            "altChar": sp.srepr(ch),
            "altChar_pretty": str(sp.factor(ch)),
            "altChar_at_q0": mp.nstr(at_q0(ch), 20),
            "is_gamma_gamma_char": bool(sp.simplify(ch - 1) == 0),
        })
        return a, b, c, ch

    record("gamma_gamma_core (calibration)", CORE)
    for kind in ("p", "n"):
        record(f"nuc9_{kind}", CORE + QUARK[kind])
        record(f"nuc11_interleaved_{kind}", CORE + QUARK[kind] + GLUON)
    # gen-grouped and the 16 constructed readings differ from the interleaved
    # model only by ORDER and by generator assignment, which CHECK 4 has just
    # shown the character cannot see -- so they are enumerated through the
    # census module's own constructors, not re-listed here.
    fams = {
        "nuc11_gen_grouped": _census.nuc11_gen_grouped,
    }
    for fam, fn in fams.items():
        for kind in ("p", "n"):
            ch = char_of_nf(fn(kind))
            rows.append({
                "candidate": f"{fam}_{kind}", "a_uu": None, "b_dd": None,
                "c_ud": None, "altChar": sp.srepr(ch),
                "altChar_pretty": str(sp.factor(ch)),
                "altChar_at_q0": mp.nstr(at_q0(ch), 20),
                "is_gamma_gamma_char": bool(sp.simplify(ch - 1) == 0),
            })
    constructed = []
    for gens in itertools.product((0, 1), repeat=3):
        for hopf, hname in (((1, 0), "L-"), ((0, 1), "L+")):
            for kind in ("p", "n"):
                ch = char_of_nf(_census.nuc11_constructed(kind, gens, hopf))
                constructed.append((f"gens={gens},hopf={hname},{kind}", ch))

    core_row = rows[0]
    nucleon_rows = [r for r in rows if not r["candidate"].startswith("gamma")]
    gg = [r["candidate"] for r in nucleon_rows if r["is_gamma_gamma_char"]]
    gg += [lbl for lbl, ch in constructed if sp.simplify(ch - 1) == 0]

    check("core_is_gamma_gamma_by_character", core_row["is_gamma_gamma_char"],
          "the three-vertex core has altChar == 1 -- the positive control; "
          "a probe that could not see a gamma-gamma word would be vacuous", w)
    check("no_census_nucleon_is_a_gamma_gamma_word", not gg,
          f"{len(nucleon_rows)} named words (3 families x p,n) + "
          f"{len(constructed)} constructed words (16 readings x p,n) = "
          f"{len(nucleon_rows) + len(constructed)} words, i.e. "
          f"{(len(nucleon_rows) + len(constructed)) // 2} Delta readings; "
          f"gamma-gamma by character: {gg or 'none'}", w)
    mixed_two = [r for r in rows if r["c_ud"] == 2]
    check("every_counted_nucleon_carries_exactly_two_mixed_letters",
          len(mixed_two) == 4 and all(r["c_ud"] == 2 for r in mixed_two),
          "nuc9 and nuc11_interleaved, proton and neutron: c_ud == 2 in all "
          "four -- the obstruction is the same two letters every time", w)

    # ---------------------------------------------------------------- CHECK 7
    # The DIFFERENCE. If both legs were gamma-gamma words, altChar(n) and
    # altChar(p) would both be 1, so altChar(Delta) would be exactly 0. It is
    # not, and it vanishes only at q = 1.
    dp = char_of_letters(CORE + QUARK["p"] + GLUON)
    dn = char_of_letters(CORE + QUARK["n"] + GLUON)
    d_char = in_q(dn - dp)
    d_fact = sp.factor(d_char)
    roots = sp.solve(sp.numer(sp.together(d_char)), q)
    check("delta_character_vanishes_only_at_q_eq_one",
          sp.simplify(d_char.subs(q, 1)) == 0
          and all(sp.simplify(r**2 - 1) == 0 or sp.im(r) != 0 for r in roots),
          f"altChar(Delta) = {d_fact}; real roots {roots}; "
          f"at q_0 = {mp.nstr(at_q0(d_char), 20)} != 0", w)

    # ---------------------------------------------------------------- CHECK 8
    # The tie to the bar involution, RECOMPUTED here rather than cited. Under
    # bar (q -> 1/q, h -> -h), the shift of bar(sigma_i + d) is -h + bar(d);
    # a shift c*h is bar-fixed iff -h + bar(c*h) = c*h, i.e. -h - c*h = c*h.
    cc = sp.Symbol("cc")
    fixed = sp.solve(sp.Eq(-h - cc * h, cc * h), cc)
    blocking = [lbl for lbl, d, ch in ALPHABET
                if not any(sp.simplify(ch * other - 1) == 0
                           for _l2, _d2, other in ALPHABET)]
    check("the_bar_fixed_shift_is_the_blocking_shift",
          fixed == [sp.Rational(-1, 2)] and blocking == ["ud"],
          f"unique bar-fixed shift c = {fixed} (i.e. d = -h/2); the shifts "
          f"whose character pairs with NO alphabet letter to give 1: "
          f"{blocking} -- the same letter", w)

    # ------------------------------------------------------------------ data
    w.add_data("alphabet", [
        {"label": lbl, "shift_in_h": str(d), "char_in_q": str(sp.factor(ch)),
         "char_at_q0": mp.nstr(at_q0(ch), 20)}
        for lbl, d, ch in ALPHABET])
    w.add_data("closed_form",
               "altChar(w) = (-1)^(a+b+c) * q^(b-a-c) * ((q^2+1)/2)^c, "
               "with a = #{d=0}, b = #{d=-h}, c = #{d=-h/2}")
    w.add_data("census_rows", rows)
    w.add_data("constructed_readings", [
        {"reading": lbl, "altChar_pretty": str(sp.factor(ch)),
         "is_gamma_gamma_char": bool(sp.simplify(ch - 1) == 0)}
        for lbl, ch in constructed])
    w.add_data("delta_character", {
        "factored": str(d_fact),
        "at_q0": mp.nstr(at_q0(d_char), 20),
        "zero_iff": "q = 1 (and q = -1, q = +/- i, outside the substrate range)",
    })
    w.add_data("scope", "b")
    w.add_data("invariant",
               "the alternating character sigma_i |-> -1/q, a 1-dimensional "
               "representation of H_3(q); fixed at +1 on gamma-gamma words by "
               "QOU.Mass.GammaGammaWordSelection.altChar_eq_one (sorry-free)")
    w.add_data("what_this_does_not_exclude", [
        "a word built from gamma-gamma vertices PLUS other letters -- the "
        "exclusion is of PURE gamma-gamma words (products of vertices)",
        "altChar == 1 is NECESSARY, not sufficient: c == 0 and a == b is a "
        "statement about the multiset, being a product of vertices is a "
        "statement about the order",
        "the general 'char == 1 => c == 0' step is enumerated over a,b,c <= 6 "
        "here; the general proof is the irreducibility of q^2+1 over Q and is "
        "the Lean follow-up",
    ])
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)

    print()
    print(f"  alphabet:  " + ",  ".join(
        f"{lbl} (d={d}) -> {sp.factor(ch)}" for lbl, d, ch in ALPHABET))
    print(f"  closed form: altChar = (-1)^(a+b+c) q^(b-a-c) ((q^2+1)/2)^c")
    print()
    for r in rows:
        print(f"  {r['candidate']:36s} (a,b,c)="
              f"{(r['a_uu'], r['b_dd'], r['c_ud'])}  altChar="
              f"{r['altChar_pretty']:26s} gg={r['is_gamma_gamma_char']}")
    print(f"  ... + {len(constructed)} constructed words (16 readings x p,n), "
          f"{sum(1 for _l, ch in constructed if sp.simplify(ch - 1) == 0)} "
          f"gamma-gamma by character")
    print(f"  altChar(Delta) = {d_fact}")

    w.save()
    print()
    if FAILED:
        print(f"FAILED ({len(FAILED)}): {', '.join(FAILED)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
