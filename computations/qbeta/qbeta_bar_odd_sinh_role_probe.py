#!/usr/bin/env python3
"""Element-level symmetry tests on the Q_beta nucleon words: does any composite of
{bar, word reversal, generator swap} (plus the eigenline swap chi) map n <-> p, or
Delta = n - p to +/-Delta?

Bean `qou-hlx8`, scoped to the element-level symmetry tests only. The trace/bar
intertwining, the g = f/h decomposition and the f_odd value are stream 12's (draft
PR #7860, `qbeta_bar_parity_split_gap_probe.py`, `QOU/Mass/BarParitySplitGap.lean`)
and are NOT recomputed here. This also answers stream 12's gap bean `qou-z08b`: which
letters or positions break the symmetry.

ANALYSIS ONLY: writes NO witness, computes NO Q_beta value, touches no dashboard.

Symmetries (all exact, sympy, on the census letters c*sigma_g + d(h)):

    bar   : sigma -> sigma^-1 = sigma - h, scalars h -> -h   (KL bar involution)
    rev   : reverse the word (the anti-involution sigma_i -> sigma_i)
    swap  : sigma_0 <-> sigma_1 (the diagram flip)
    chi   : sigma -> -sigma^-1 = h - sigma (eigenline swap at the same q, qou-hlx6)
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, _p))

_spec = importlib.util.spec_from_file_location(
    "_census", os.path.join(HERE, "qbeta_delta_candidate_census_probe.py"))
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
hm, h = _census.hm, _census.h

RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


ONE, ZERO = sp.Integer(1), sp.Integer(0)
U = lambda g: (ONE, ZERO, g)
D = lambda g: (ONE, -h, g)
UD = lambda g: (ONE, -h / 2, g)
CORE = [U(0), D(1)] * 3
GLUON = [U(0), U(0)]
P_TAIL = [U(0), UD(0), UD(1)]
N_TAIL = [UD(0), UD(0), D(1)]
N_WORD = CORE + N_TAIL + GLUON
P_WORD = CORE + P_TAIL + GLUON
SEGMENT = ["core"] * 6 + ["tail"] * 3 + ["gluon"] * 2


def nf(letters):
    v = [ONE] + [ZERO] * 5
    for c, d, g in letters:
        v = hm(v, c, d, g)
    return [sp.expand(x) for x in v]


def s_bar(ls):
    # bar(c s + d(h)) = c (s - h) + d(-h); census c are constants
    return [(c, sp.expand(-h * c + sp.sympify(d).subs(h, -h)), g) for c, d, g in ls]


def s_rev(ls):
    return list(reversed(ls))


def s_swap(ls):
    return [(c, d, 1 - g) for c, d, g in ls]


def s_chi(ls):
    return [(-c, sp.expand(h * c + d), g) for c, d, g in ls]


OPS = {"bar": s_bar, "rev": s_rev, "swap": s_swap, "chi": s_chi}


def apply(names, ls):
    for nm in names:
        ls = OPS[nm](ls)
    return ls


def is_zero(vec):
    return all(sp.simplify(x) == 0 for x in vec)


def name(L):
    c, d, g = L
    d = sp.simplify(sp.sympify(d) / c) if c != 0 else d
    tag = {0: "u", -h: "d", -h / 2: "ud"}.get(sp.simplify(d), f"[{d}]")
    sign = "-" if c == -1 else ""
    return f"{sign}{tag}{g}"


def main() -> int:
    nfp, nfn = nf(P_WORD), nf(N_WORD)
    dd = [a - b for a, b in zip(nfn, nfp)]
    print("n word:", " ".join(name(L) for L in N_WORD))
    print("p word:", " ".join(name(L) for L in P_WORD))
    print("\nELEMENT LEVEL (NF, exact): every composite of length <= 4")
    rows = []
    for r in range(0, 5):
        for names in itertools.permutations(OPS, r):
            sn, sp_ = nf(apply(names, N_WORD)), nf(apply(names, P_WORD))
            row = dict(
                lab="+".join(names) or "id",
                n_to_p=is_zero([a - b for a, b in zip(sn, nfp)]),
                n_to_mp=is_zero([a + b for a, b in zip(sn, nfp)]),
                D_odd=is_zero([(a - b) + c for a, b, c in zip(sn, sp_, dd)]),
                D_even=is_zero([(a - b) - c for a, b, c in zip(sn, sp_, dd)]),
                n_to_mn=is_zero([a + b for a, b in zip(sn, nfn)]),
            )
            rows.append(row)
            print(f"    {row['lab']:16s} S(n)=p:{row['n_to_p']!s:5} S(n)=-p:{row['n_to_mp']!s:5}"
                  f" S(D)=-D:{row['D_odd']!s:5} S(D)=D:{row['D_even']!s:5}"
                  f" S(n)=-n:{row['n_to_mn']!s:5}")
    nontriv = [r for r in rows if r["lab"] != "id"]
    check("no_composite_maps_n_to_plus_or_minus_p",
          not any(r["n_to_p"] or r["n_to_mp"] for r in nontriv))
    odd = [r for r in nontriv if r["D_odd"]]
    check("Delta_odd_only_via_length_parity",
          bool(odd) and all(r["n_to_mn"] for r in odd),
          f"{[r['lab'] for r in odd]}: sigma -> -sigma, h -> -h (q -> -q); every census "
          "letter is odd, so S(n) = -n and S(p) = -p")
    even = [r["lab"] for r in nontriv if r["D_even"]]
    print(f"    composites with S(Delta) = +Delta: {even}")
    bar_set = [r for r in nontriv if set(r["lab"].split("+")) <= {"bar", "rev", "swap"}]
    check("within_bar_rev_swap_no_n_p_map_and_no_Delta_sign",
          not any(r["n_to_p"] or r["n_to_mp"] or r["D_odd"] for r in bar_set))

    print("\nWHERE IT BREAKS: letters of S(n) vs p, position by position")
    print("    (positions 0-5 core, 6-8 quark tail, 9-10 gluon)")
    for names in [("bar",), ("rev",), ("swap",), ("bar", "rev"), ("bar", "swap"),
                  ("rev", "swap"), ("bar", "rev", "swap")]:
        sn = apply(names, N_WORD)
        mism = [i for i in range(len(sn))
                if not (sp.simplify(sn[i][0] - P_WORD[i][0]) == 0
                        and sp.simplify(sp.sympify(sn[i][1]) - P_WORD[i][1]) == 0
                        and sn[i][2] == P_WORD[i][2])]
        segs = sorted({SEGMENT[i] for i in mism})
        print(f"    S={'+'.join(names):14s} S(n) = {' '.join(name(L) for L in sn)}")
        print(f"    {'':16s}mismatch at {mism} -> segments {segs}")

    print("\nSEGMENT bar-images (letter level)")
    for lab, seg in (("core (s0 s1^-1)^3", CORE), ("gluon s0 s0", GLUON),
                     ("p tail", P_TAIL), ("n tail", N_TAIL)):
        b = s_bar(seg)
        same = all(sp.simplify(sp.sympify(x[1]) - y[1]) == 0 for x, y in zip(b, seg))
        print(f"    bar({lab:18s}) = {' '.join(name(L) for L in b):24s} fixed: {same}")
    check("bar_fixes_no_segment",
          not any(all(sp.simplify(sp.sympify(x[1]) - y[1]) == 0 for x, y in zip(s_bar(seg), seg))
                  for seg in (CORE, GLUON, P_TAIL, N_TAIL)))
    check("bar_swaps_u_d_fixes_ud",
          s_bar([U(0)])[0][1] == -h and s_bar([D(0)])[0][1] == 0
          and sp.expand(s_bar([UD(0)])[0][1] + h / 2) == 0)

    ok = all(r[1] for r in RESULTS)
    print(f"\n{sum(r[1] for r in RESULTS)}/{len(RESULTS)} checks pass")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
