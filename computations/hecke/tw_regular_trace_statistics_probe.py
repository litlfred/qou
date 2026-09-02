#!/usr/bin/env python3
"""What determines tr(L_{T_u}) in H_n(q)?  Three natural answers, all refuted.

Bean `qou-0y6h`.  The Gram entries of `QOU.Hecke.TwBasis.twGram` are
`tr(L_{T_v T_w})`, and the single thing blocking the determinant at rank >= 2 is
the diagonal structure constant `[T_u T_w : T_w]` for a general `u` --
equivalently `tr(L_{T_u}) = sum_w [T_u T_w : T_w]`, since left multiplication by
`T_u` is what the Gram reads.  The generator case is proved in Lean
(`trace_lmul_sigma`: only descents contribute, `2 tr = (q-1)(n+1)!`).

Before formalising a closed form one should know whether a *simple* one exists.
This probe asks whether `tr(L_{T_u})` is determined by any of the three obvious
combinatorial statistics of `u`.  It is not:

    determined by length(u) alone        -- NO  (fails from S_4 on)
    determined by cycle type(u) alone    -- NO  (fails from S_4 on)
    determined by (length, cycle type)   -- NO  (holds in S_4, FAILS in S_5)

**The third line is the one that matters, and the S_4 / S_5 split is the trap.**
`(length, cycle type)` determines the trace for every element of `S_4`.  It is a
coincidence of that group: in `S_5` it fails at four (length, type) pairs.  Two
elements of `S_5` of the SAME length 4 and the SAME cycle type (2,2,1):

    u = (0,3,4,1,2)   tr(L_{T_u}) =  5 (q-1)^2 (q^2 + 4q + 1)
    u = (1,0,4,3,2)   tr(L_{T_u}) = 10 (q-1)^2 (q^2 +  q + 1)

Not proportional, not even the same irreducible factors.

## What this does and does not establish

It **refutes** three specific hypotheses, by exact finite computation, with
witnesses -- not a numerical near-miss.  It does **not** establish that no
closed form exists: `tr(L_{T_u})` is `sum_lambda d_lambda chi_lambda(T_u)`, and
Hecke characters are governed by Geck-Pfeiffer's theory of minimal-length
representatives of conjugacy classes.  The pattern here is that theory's
signature -- the trace at a class's minimal length differs from the trace at
higher length in the same class, which is exactly why cycle type alone cannot
determine it.  So the honest reading is: the closed form, if wanted, IS
Geck-Pfeiffer, which is a book-length development rather than a lemma.

Practical consequence for `qou-0y6h`: do not spend a session looking for a
combinatorial formula in `length` / `cycle type` / descent set.  Closing
`det(twGram)` at rank >= 2 in Lean means formalising character theory for
`H_n(q)`, and should be scoped as Mathlib-scale.

## Precision

Exact arithmetic only -- sympy expressions in `q`, or Python ints at integer
`q`.  No float anywhere and none admissible: the output is an argument about
what to attempt next, and that is the expensive kind of thing to get wrong.

## Conventions (identical to QOU/Hecke/TwMul.lean)

`sigma_i . T_v = T_{v s_i}` if `v(i) < v(i+1)`, else `(q-1) T_v + q T_{v s_i}`.

**Handedness -- the trap that makes this file's numbers wrong if ignored.**
Applying a reduced word of `u` to `T_1` lands on `T_{u^{-1}}`, because left
multiplication by a generator multiplies the INDEX on the right.  That
mislabelling is invisible in a determinant (it permutes rows and columns by the
same involution) and is NOT invisible in a trace, which is what this file
computes.  `T_u` is therefore reached by the reduced word of `u^{-1}`.

Usage:  python3 -u computations/hecke/tw_regular_trace_statistics_probe.py
"""
from __future__ import annotations

import itertools
from collections import defaultdict
from typing import Dict, List, Tuple

Perm = Tuple[int, ...]


def perms(m: int) -> List[Perm]:
    return list(itertools.permutations(range(m)))


def inverse(w: Perm) -> Perm:
    out = [0] * len(w)
    for i, v in enumerate(w):
        out[v] = i
    return tuple(out)


def length(w: Perm) -> int:
    """Coxeter length = number of inversions."""
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])


def cycle_type(w: Perm) -> Tuple[int, ...]:
    seen: set = set()
    parts = []
    for i in range(len(w)):
        if i in seen:
            continue
        c, j = 0, i
        while j not in seen:
            seen.add(j)
            j = w[j]
            c += 1
        parts.append(c)
    return tuple(sorted(parts, reverse=True))


def right_swap(v: Perm, i: int) -> Perm:
    lst = list(v)
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return tuple(lst)


def make_sigma_act(q):
    def sigma_act(i: int, vec: Dict[Perm, object]) -> Dict[Perm, object]:
        out: Dict[Perm, object] = {}
        for v, c in vec.items():
            if c == 0:
                continue
            vs = right_swap(v, i)
            if v[i] < v[i + 1]:
                out[vs] = out.get(vs, 0) + c
            else:
                out[v] = out.get(v, 0) + (q - 1) * c
                out[vs] = out.get(vs, 0) + q * c
        return {k: val for k, val in out.items() if val != 0}

    return sigma_act


def reduced_word(w: Perm) -> List[int]:
    lst = list(w)
    word: List[int] = []
    changed = True
    while changed:
        changed = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                word.append(i)
                changed = True
    return list(reversed(word))


def regular_traces(m: int, q) -> Dict[Perm, object]:
    """`tr(L_{T_u})` for every `u` in `S_m`, exactly.

    `tr(L_{T_u}) = sum_w [T_u T_w : T_w]` -- the diagonal of left multiplication
    read in the `T_w` basis."""
    sigma_act = make_sigma_act(q)
    P = perms(m)
    one = 1 if not hasattr(q, "free_symbols") else q ** 0

    def act_word(u: Perm, vec):
        for i in reversed(reduced_word(u)):
            vec = sigma_act(i, vec)
        return vec

    out = {}
    for u in P:
        ui = inverse(u)  # see the handedness note in the module docstring
        total = 0
        for w in P:
            total += act_word(ui, {w: one}).get(w, 0)
        out[u] = total
    return out


def determined_by(traces: Dict[Perm, object], stat) -> Tuple[bool, List]:
    """Does `stat(u)` determine `traces[u]`?  Returns (verdict, failing keys)."""
    groups = defaultdict(set)
    for u, t in traces.items():
        groups[stat(u)].add(str(t))
    bad = sorted(k for k, vals in groups.items() if len(vals) > 1)
    return (not bad), bad


def main() -> None:
    import sympy as sp

    q = sp.symbols("q")

    print("What determines tr(L_{T_u}) in H_n(q)?\n")

    stats = [
        ("length alone", lambda u: length(u)),
        ("cycle type alone", lambda u: cycle_type(u)),
        ("(length, cycle type)", lambda u: (length(u), cycle_type(u))),
    ]

    verdicts = {}
    for m in (2, 3, 4, 5):
        # S_5 symbolically is slow; integer q at several points separates the
        # classes just as well and the S_4 answers are cross-checked symbolically.
        if m <= 4:
            traces = regular_traces(m, q)
            traces = {u: sp.factor(sp.expand(t)) for u, t in traces.items()}
        else:
            tabs = [regular_traces(m, x) for x in (2, 3, 5, 7, 11)]
            traces = {u: tuple(t[u] for t in tabs) for u in perms(m)}
        print(f"S_{m}  ({len(perms(m))} elements)")
        for name, stat in stats:
            ok, bad = determined_by(traces, stat)
            note = "" if ok else f"   fails at {bad[:4]}{' …' if len(bad) > 4 else ''}"
            print(f"    determined by {name:22s}: {'YES' if ok else 'NO '}{note}")
            verdicts[(m, name)] = ok
        print()

    # The S_4 / S_5 split on the joint statistic is the whole point.
    assert verdicts[(4, "(length, cycle type)")], "S_4 was expected to satisfy it"
    assert not verdicts[(5, "(length, cycle type)")], "S_5 was expected to refute it"
    for m in (4, 5):
        assert not verdicts[(m, "length alone")]
        assert not verdicts[(m, "cycle type alone")]

    # The witness pair, stated explicitly so a reader can check it by hand.
    tr5 = regular_traces(5, q)
    a, b = (0, 3, 4, 1, 2), (1, 0, 4, 3, 2)
    ta, tb = sp.factor(sp.expand(tr5[a])), sp.factor(sp.expand(tr5[b]))
    assert length(a) == length(b) == 4
    assert cycle_type(a) == cycle_type(b) == (2, 2, 1)
    assert sp.simplify(ta - tb) != 0
    print("Witness — same length 4, same cycle type (2,2,1), different traces:")
    print(f"    u = {a}   tr = {ta}")
    print(f"    u = {b}   tr = {tb}")
    print()
    print("(length, cycle type) determines the trace in S_4 and NOT in S_5.")
    print("Do not generalise the rank-3 answer; this probe exists because I did.")


if __name__ == "__main__":
    main()
