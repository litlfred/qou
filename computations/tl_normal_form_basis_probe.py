#!/usr/bin/env python3
"""Jones normal forms for TL_n(δ): are they the diagram basis, and does the
reduction a Lean proof would need actually terminate?

Bean `qou-cds1`. The Lean arc (PRs #6986, #7001) has now reached the planar
diagram basis from four directions -- spanning sets, lower bounds, Wedderburn
decompositions, and semisimplicity all stop at it. Before committing to a large
Lean build this probe settles, computationally and exactly, three questions the
build's DESIGN depends on.

**Formalize-first, applied to a Lean build.** §"Formalize-first probe
discipline" says to find the invariant before running a wide search. The wide
search here is the Lean development itself; this probe is the cheap prune that
tells you which shape it must take.

## What is checked

1. **The family is Catalan.** The Jones normal forms

       (e_{i1} e_{i1-1} ... e_{j1}) (e_{i2} ... e_{j2}) ... (e_{ik} ... e_{jk})
       with  1 <= i1 < ... < ik <= n-1,  1 <= j1 < ... < jk <= n-1,  j_m <= i_m

   number exactly `catalan n`, and are distinct as words.

2. **They ARE the diagram basis.** Mapping each normal form to its planar
   diagram (a non-crossing perfect matching on 2n points, composed with loop
   counting) is a BIJECTION onto all such diagrams. Every normal form is
   loop-free, so no normal form carries a hidden power of δ.

3. **Left multiplication closes, and how.** For every generator `e_k` and every
   normal form `w`, the diagram of `e_k · w` is again a normal form's, times
   `δ^loops`. The probe records the loop counts and the word-length changes.

4. **The route to a general-`m` cardinality proof.** A normal form for
   `TL_{m+1}` is a pair `(I, J)` of equal-size subsets of the `m` generators
   with `J` dominating `I`; equivalently a word of length `m` over four letters
   -- `I`-only, `J`-only, *both*, *neither* -- whose every prefix has
   `#(I-only) <= #(J-only)`, with equality overall. Those are the **bicoloured
   Motzkin words**: two step letters and two neutral ones, with a ballot
   condition. This check confirms, against `catalan(m+1)`, both that count and
   its closed form

       catalan(m+1)  =  sum_k  C(m, 2k) * catalan(k) * 2^(m-2k)

   so the general theorem is a bicoloured-Motzkin-to-Catalan bijection, NOT a
   Dyck-path one -- the two neutral letters are exactly the difference. Recorded
   because "bijection to Dyck paths" was this agent's first guess and it is
   wrong.

## The finding that changes the Lean design

Closure holds -- and it is **NOT length-monotone**. The word length changes by
`+1`, `0`, or a NEGATIVE ODD amount reaching `-5` by `n = 7`. So a Lean proof
cannot induct on word length with a "rewrite until shorter" termination
measure; it must carry the `(i₁<...<i_k, j₁<...<j_k)` index data and prove the
multiplication rule on THAT. Recording this because the length measure is the
first thing an agent reaches for, and it does not work.

Loop counts are always 0 or 1 -- never higher -- so the δ-bookkeeping in such a
proof is a single factor per generator, not a power.

## Arithmetic

Exact integers and set operations only. No floating point appears anywhere in
this file (nothing to carry as `mpmath.mpf`, since nothing is real-valued), so
the NO-FLOAT64 family is satisfied by construction rather than by care.

## What this does NOT establish

It is a check at `n <= 7`, not a proof at any `n`. It says the family is the
right one to formalise and names the measure that will not work; it does not
prove the closure lemma. Nothing here wires to production.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

WITNESS = Path(__file__).with_name("tl-normal-form-basis.witness.json")

MAX_N_COUNT = 8      # normal-form count vs catalan
MAX_N_BIJ = 6        # bijection onto planar diagrams (enumeration is catalan-sized)
MAX_N_CLOSURE = 7    # left-multiplication closure table
MAX_M_MOTZKIN = 10   # bicoloured-Motzkin route to the general count


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


# --------------------------------------------------------------------------
# Jones normal forms
# --------------------------------------------------------------------------

def normal_forms(n: int) -> list[tuple[int, ...]]:
    """Every Jones normal form for TL_n, as a word in generator indices."""
    gens = range(1, n)
    out: list[tuple[int, ...]] = []
    for k in range(0, n):
        for I in combinations(gens, k):
            for J in combinations(gens, k):
                if all(J[m] <= I[m] for m in range(k)):
                    w: list[int] = []
                    for m in range(k):
                        w.extend(range(I[m], J[m] - 1, -1))
                    out.append(tuple(w))
    return out


# --------------------------------------------------------------------------
# Planar diagrams: points 0..n-1 are the top row, n..2n-1 the bottom row.
# A diagram is a tuple m with m[i] the partner of point i.
# --------------------------------------------------------------------------

def ident(n: int) -> tuple[int, ...]:
    m = [0] * (2 * n)
    for i in range(n):
        m[i] = n + i
        m[n + i] = i
    return tuple(m)


def gen(n: int, k: int) -> tuple[int, ...]:
    """`e_k`, 1-indexed: joins strands k and k+1 on both rows."""
    m = [0] * (2 * n)
    a, b = k - 1, k
    m[a], m[b] = b, a
    m[n + a], m[n + b] = n + b, n + a
    for i in range(n):
        if i not in (a, b):
            m[i] = n + i
            m[n + i] = i
    return tuple(m)


def mul(n: int, x: tuple[int, ...], y: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    """`x * y` with x stacked above y. Returns (diagram, closed-loop count)."""
    par: dict[tuple[str, int], tuple[str, int]] = {}

    def find(u):
        while par[u] != u:
            par[u] = par[par[u]]
            u = par[u]
        return u

    def uni(u, v):
        ru, rv = find(u), find(v)
        if ru != rv:
            par[ru] = rv

    for lab in ("t", "m", "b"):
        for i in range(n):
            par[(lab, i)] = (lab, i)

    def node_x(i):
        return ("t", i) if i < n else ("m", i - n)

    def node_y(i):
        return ("m", i) if i < n else ("b", i - n)

    for i in range(2 * n):
        if i < x[i]:
            uni(node_x(i), node_x(x[i]))
    for i in range(2 * n):
        if i < y[i]:
            uni(node_y(i), node_y(y[i]))

    comp: dict = {}
    for lab, rng in (("t", range(n)), ("b", range(n))):
        for i in rng:
            comp.setdefault(find((lab, i)), []).append((lab, i))

    m = [0] * (2 * n)
    for mem in comp.values():
        assert len(mem) == 2, f"boundary component of size {len(mem)}"
        (l1, i1), (l2, i2) = mem
        p1 = i1 if l1 == "t" else n + i1
        p2 = i2 if l2 == "t" else n + i2
        m[p1], m[p2] = p2, p1

    boundary_roots = set(comp)
    loops, seen = 0, set()
    for i in range(n):
        r = find(("m", i))
        if r not in boundary_roots and r not in seen:
            seen.add(r)
            loops += 1
    return tuple(m), loops


def word_diagram(n: int, w: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    d, tot = ident(n), 0
    for k in w:
        d, l = mul(n, d, gen(n, k))
        tot += l
    return d, tot


def _planar(pts: list[int]) -> list[list[tuple[int, int]]]:
    """Non-crossing perfect matchings of `pts` in the given cyclic order."""
    if not pts:
        return [[]]
    res = []
    first = pts[0]
    for idx in range(1, len(pts), 2):
        inside, outside = pts[1:idx], pts[idx + 1:]
        for a in _planar(inside):
            for b in _planar(outside):
                res.append([(first, pts[idx])] + a + b)
    return res


def planar_diagrams(n: int) -> set[tuple[int, ...]]:
    order = [i for i in range(n)] + [2 * n - 1 - i for i in range(n)]
    out = set()
    for M in _planar(order):
        m = [0] * (2 * n)
        for a, b in M:
            m[a], m[b] = b, a
        out.add(tuple(m))
    return out


# --------------------------------------------------------------------------
# The general-count route
# --------------------------------------------------------------------------

def bicoloured_motzkin(m: int) -> int:
    """Words of length m over {a, b, x, y} with every prefix `#a <= #b` and
    `#a == #b` overall.  `a`/`b` are the `I`-only and `J`-only letters; `x`/`y`
    are *both* and *neither*, both neutral."""
    from itertools import product as _product
    tot = 0
    for w in _product("abxy", repeat=m):
        bal, ok = 0, True
        for ch in w:
            if ch == "a":
                bal += 1
            elif ch == "b":
                bal -= 1
            if bal > 0:
                ok = False
                break
        if ok and bal == 0:
            tot += 1
    return tot


def closed_sum(m: int) -> int:
    """sum_k C(m, 2k) * catalan(k) * 2^(m-2k)."""
    return sum(comb(m, 2 * k) * catalan(k) * 2 ** (m - 2 * k)
               for k in range(m // 2 + 1))


# --------------------------------------------------------------------------

def main() -> int:
    checks: list[dict] = []
    ok = True

    # 1. the family is Catalan, and its words are distinct
    counts = []
    for n in range(1, MAX_N_COUNT + 1):
        nf = normal_forms(n)
        distinct = len(nf) == len(set(nf))
        match = len(nf) == catalan(n)
        ok &= distinct and match
        counts.append({"n": n, "normal_forms": len(nf), "catalan": catalan(n),
                       "distinct_words": distinct, "match": match})
        print(f"n={n}: normal forms {len(nf):5d}  catalan {catalan(n):5d}  "
              f"{'MATCH' if match else '*** MISMATCH ***'}", flush=True)
    checks.append({"check": "normal_form_count_is_catalan",
                   "range": f"n=1..{MAX_N_COUNT}", "rows": counts,
                   "pass": all(r["match"] and r["distinct_words"] for r in counts)})

    # 2. bijection onto planar diagrams; every normal form is loop-free
    print(flush=True)
    bij_rows = []
    for n in range(1, MAX_N_BIJ + 1):
        nf = normal_forms(n)
        d2w: dict = {}
        loopfree = True
        for w in nf:
            d, l = word_diagram(n, w)
            if l != 0:
                loopfree = False
            d2w.setdefault(d, []).append(w)
        P = planar_diagrams(n)
        bij = (len(d2w) == len(nf) == len(P) == catalan(n)) and set(d2w) == P
        ok &= bij and loopfree
        bij_rows.append({"n": n, "normal_forms": len(nf), "distinct_diagrams": len(d2w),
                         "planar_diagrams": len(P), "catalan": catalan(n),
                         "bijection": bij, "all_loop_free": loopfree})
        print(f"n={n}: NF {len(nf):4d}  distinct diagrams {len(d2w):4d}  "
              f"planar {len(P):4d}  bijection={'YES' if bij else 'NO'}", flush=True)
    checks.append({"check": "normal_forms_are_the_diagram_basis",
                   "range": f"n=1..{MAX_N_BIJ}", "rows": bij_rows,
                   "pass": all(r["bijection"] and r["all_loop_free"] for r in bij_rows)})

    # 3. left multiplication closes; record loops and length change
    print(flush=True)
    clo_rows = []
    for n in range(2, MAX_N_CLOSURE + 1):
        nf = normal_forms(n)
        d2w = {}
        for w in nf:
            d, _ = word_diagram(n, w)
            d2w[d] = w
        loops, dlen, closed = Counter(), Counter(), True
        for k in range(1, n):
            ek = gen(n, k)
            for w in nf:
                dw, _ = word_diagram(n, w)
                d, l = mul(n, ek, dw)
                if d not in d2w:
                    closed = False
                    continue
                loops[l] += 1
                dlen[len(d2w[d]) - len(w)] += 1
        ok &= closed
        clo_rows.append({
            "n": n, "products": (n - 1) * len(nf), "closed_in_normal_forms": closed,
            "loop_counts": {str(a): b for a, b in sorted(loops.items())},
            "word_length_change": {str(a): b for a, b in sorted(dlen.items())},
        })
        print(f"n={n}: {(n-1)*len(nf):5d} products e_k·w  closed={closed}  "
              f"loops {dict(sorted(loops.items()))}  "
              f"Δ|word| {dict(sorted(dlen.items()))}", flush=True)
    max_loop = max(int(a) for r in clo_rows for a in r["loop_counts"])
    min_dlen = min(int(a) for r in clo_rows for a in r["word_length_change"])
    checks.append({
        "check": "left_multiplication_closes_in_normal_forms",
        "range": f"n=2..{MAX_N_CLOSURE}", "rows": clo_rows,
        "max_loops_per_product": max_loop,
        "min_word_length_change": min_dlen,
        "length_monotone": min_dlen >= 0,
        "pass": all(r["closed_in_normal_forms"] for r in clo_rows),
    })

    # 4. the route to the general count
    print(flush=True)
    motz_rows = []
    for m in range(0, MAX_M_MOTZKIN + 1):
        bm, cs, ct = bicoloured_motzkin(m), closed_sum(m), catalan(m + 1)
        agree = bm == cs == ct
        ok &= agree
        motz_rows.append({"m": m, "bicoloured_motzkin": bm, "closed_sum": cs,
                          "catalan_m_plus_1": ct, "agree": agree})
        print(f"m={m:2d}: bicoloured Motzkin {bm:7d}  closed sum {cs:7d}  "
              f"catalan({m+1}) {ct:7d}  {'agree' if agree else '*** DISAGREE ***'}",
              flush=True)
    checks.append({
        "check": "general_count_route_is_bicoloured_motzkin_not_dyck",
        "range": f"m=0..{MAX_M_MOTZKIN}", "rows": motz_rows,
        "note": ("a normal form is a 4-letter word (I-only / J-only / both / "
                 "neither) with a ballot condition on the first two: a bicoloured "
                 "Motzkin word. The two neutral letters are why it is Motzkin and "
                 "not Dyck."),
        "pass": all(r["agree"] for r in motz_rows),
    })

    print(flush=True)
    print(f"max loops per product = {max_loop} (so a single δ, never a power)", flush=True)
    print(f"min word-length change = {min_dlen} — length is NOT a termination "
          f"measure for the reduction", flush=True)

    payload = {
        "description": (
            "Jones normal forms for TL_n(δ) are exactly the planar diagram basis "
            "(n<=6, bijectively) and number catalan n (n<=8); left multiplication by "
            "a generator closes in them (n<=7) with at most one loop per product. "
            "The reduction is NOT word-length monotone (Δ reaches -5 by n=7), so a "
            "Lean proof must index by the (I,J) normal-form data rather than induct "
            "on length. The general-m count is a bicoloured-Motzkin-to-Catalan "
            "bijection, not a Dyck-path one (m<=10)."
        ),
        "bean": "qou-cds1",
        "arithmetic": "exact integers only; no floating point anywhere in this producer",
        "scope": (
            "checked at finite n, not proved at general n; establishes which family to "
            "formalise and which termination measure fails. Wires to nothing."
        ),
        "checks": checks,
        "all_pass": ok,
    }
    payload.setdefault("scriptFile", os.path.basename(__file__))
    try:
        from qou_substrate.witness import WitnessBuilder as _WB
        _WB.stamp_staleness_metadata(payload, script_path=__file__, engine=None,
                                     q0_anchor=None)
    except Exception as exc:  # provenance is best-effort; the result is not
        payload["provenance_note"] = f"stamp unavailable: {exc!r}"
    WITNESS.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"\nWROTE {WITNESS.name} — all_pass={ok}", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
